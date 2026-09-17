// Last updated June 9 2026
require('dotenv').config();
const express = require('express');
const cron = require('node-cron');
const Anthropic = require('@anthropic-ai/sdk');

process.on('uncaughtException', (err) => console.error('Uncaught error:', err));
process.on('unhandledRejection', (err) => console.error('Unhandled rejection:', err));

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const { airtable, getStudentByPhone, createStudent, updateStudent, getAllActiveStudents } = require('./airtable');
const { sendWhatsApp, validateWhatsAppToken } = require('./whatsapp');
const { initToken, checkAndRefreshToken } = require('./tokenManager');
const { sendSMS } = require('./sms');
const { createPaymentLink, verifyPayment } = require('./payments');
const { generateQuestion, generateFeedback, generateReexplanation, generateHelpAnswer, generateWeeklySummary, generateMyStats, generateParentReport, generateSaturdayQuiz } = require('./claude');
const { getRankTitle, checkMilestone, getMilestoneMessage } = require('./ranks');
const { enrollmentFlow, PRICING } = require('./enrollment');
const { handleNectaResults } = require('./necta');
const { t } = require('./lang');

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const PLAN_MESSAGE = `⏰ Jaribio lako linaisha! Your 3-day free trial is ending!\n\nChoose your plan to keep learning:\n\n1️⃣ Wiki Pass — 1,500 TZS (7 days)\n   Perfect for exam week! 📅\n\n2️⃣ Mwezi Pack — 5,000 TZS (30 days)\n   Most popular! 🔥\n\n3️⃣ Muhula Pass — 12,000 TZS (1 full term)\n   Best value — save 3,000 TZS! 💰\n\n4️⃣ Mwaka Pack — 30,000 TZS (full year)\n   Ultimate saving — save 30,000 TZS! 🏆\n\nReply 1, 2, 3 or 4 to choose!\nThen send your M-Pesa confirmation number.\n\nAu jibu moja kwa moja — just reply your choice!`;

const PLAN_MAP = {
  '1': { name: 'Wiki Pass',   price: 1500,  days: 7   },
  '2': { name: 'Mwezi Pack',  price: 5000,  days: 30  },
  '3': { name: 'Muhula Pass', price: 12000, days: 90  },
  '4': { name: 'Mwaka Pack',  price: 30000, days: 365 },
};

// ─── Deployment trigger: 2026-05-20 ──────────────────────────────────────────
// ─── Health Check ────────────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({ status: 'JIBU bot is running 🎓', time: new Date().toISOString() });
});

// ─── Privacy Policy ───────────────────────────────────────────────────────────
app.get('/privacy', (req, res) => {
  res.sendFile(__dirname + '/privacy.html');
});

// ─── WhatsApp Webhook Verification (Meta Cloud API) ──────────────────────────
app.get('/webhook/whatsapp', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];
  if (mode === 'subscribe' && token === process.env.WHATSAPP_VERIFY_TOKEN) {
    console.log('✅ WhatsApp webhook verified');
    return res.status(200).send(challenge);
  }
  res.sendStatus(403);
});

// ─── WhatsApp Webhook (Meta Cloud API) ───────────────────────────────────────
app.post('/webhook/whatsapp', async (req, res) => {
  res.sendStatus(200);
  try {
    const body = req.body;
    if (body.object !== 'whatsapp_business_account') return;

    const messages = body.entry?.[0]?.changes?.[0]?.value?.messages;
    if (!messages?.length) return;

    for (const message of messages) {
      if (message.type !== 'text') continue;
      const phone = message.from;
      const rawText = (message.text?.body || '').trim();
      const text = rawText.toUpperCase();
      console.log('Received message:', JSON.stringify(rawText));

      if (text.startsWith('JIBU MATOKEO')) {
        await handleNectaResults(phone, text, 'whatsapp');
        continue;
      }

      const student = await getStudentByPhone(phone);

      if (!student) {
        await enrollmentFlow(phone, text, null, 'whatsapp');
        continue;
      }

      const msg = rawText.trim().toUpperCase();
      const step = parseInt(student.Enrollment_Step) || 0;

      // 1. Commands first — always recognised regardless of enrolment state
      if (msg === 'HELP') {
        await updateStudent(student.id, { Enrollment_Step: 31 });
        await sendWhatsApp(phone,
          `Hey ${student.Student_Name}! 👋 I am here to help!\n\nWhat do you need help with? Just tell me in your own words — for example:\n\n💬 "I don't understand photosynthesis"\n💬 "How do I solve quadratic equations"\n💬 "What topics should I focus on for NECTA"\n💬 "I want to change my subjects"\n💬 "How does JIBU work"\n\nJust type your question and I will help you! 🎓`
        );
        continue;
      }

      if (msg === 'MYSTATS') {
        await handleMyStats(student, phone, 'whatsapp');
        continue;
      }

      if (msg === 'SUBJECTS') {
        await updateStudent(student.id, { Enrollment_Step: 30 });
        await sendWhatsApp(phone,
          `Which subjects do you want to study? Choose from:\n\n📐 Maths\n🔬 Biology\n⚗️ Chemistry\n🧪 Physics\n📖 English\n📚 History\n🌍 Geography\n\nType the subjects you want separated by commas!\nExample: Maths, Biology, Chemistry`
        );
        continue;
      }

      if (msg === 'TEST' || msg === 'TESTQUESTION') {
        await sendDailyQuestion(student);
        continue;
      }

      if (msg === 'WRONG' || msg === 'EXPLAIN') {
        await handleChallenge(student, phone, 'whatsapp');
        continue;
      }

      if (msg === 'SWAHILI' || msg === 'NIAMBIE KWA KISWAHILI') {
        await updateStudent(student.id, { Language_Pref: 'sw' });
        await sendWhatsApp(phone, `Got it! 🇹🇿 Nitaongea nawe kwa Kiswahili zaidi. Send "English" anytime to switch back.`);
        continue;
      }

      if (msg === 'ENGLISH') {
        await updateStudent(student.id, { Language_Pref: 'en' });
        await sendWhatsApp(phone, `Got it! 🇬🇧 Switching to English mode. Send "Swahili" anytime to switch.`);
        continue;
      }

      // 2. PAY command
      if (msg === 'PAY') {
        await updateStudent(student.id, { Enrollment_Step: 40 });
        await sendWhatsApp(phone, PLAN_MESSAGE);
        continue;
      }

      // 3. Saturday quiz answer format (e.g. "1A 2B 3C 4D 5A")
      if (isSaturdayAnswerFormat(msg) && student.Saturday_Answers) {
        await handleSaturdayAnswers(student, msg, phone, 'whatsapp');
        continue;
      }

      // 4. A/B/C/D answer
      if (['A', 'B', 'C', 'D'].includes(msg)) {
        await processAnswer(student, msg, phone, 'whatsapp');
        continue;
      }

      // 5. Pending step handlers
      if (step === 40) {
        await handlePlanSelection(student, msg, phone, 'whatsapp');
        continue;
      }

      if (step === 41) {
        await handlePaymentConfirmation(student, rawText, phone, 'whatsapp');
        continue;
      }

      if (step === 30) {
        await handleSubjectUpdate(student, rawText, phone, 'whatsapp');
        continue;
      }

      if (step === 31) {
        await handleHelpQuestion(student, rawText, phone, 'whatsapp');
        continue;
      }

      // 4. Enrollment in progress (Status-based, not step-range)
      if (student.Status === 'Enrolling') {
        await enrollmentFlow(phone, rawText, student, 'whatsapp');
        continue;
      }

      // 5. Smart help fallback — anything else goes to Claude
      await handleHelpQuestion(student, rawText, phone, 'whatsapp');
    }
  } catch (err) {
    console.error('WhatsApp webhook error:', err);
  }
});

// ─── SMS Webhook (Africa's Talking) ──────────────────────────────────────────
app.post('/webhook/sms', async (req, res) => {
  res.sendStatus(200);
  try {
    const phone = req.body.from;
    const rawText = (req.body.text || '').trim();
    const text = rawText.toUpperCase();
    console.log('Received SMS:', JSON.stringify(rawText));

    if (text.startsWith('JIBU MATOKEO')) {
      await handleNectaResults(phone, text, 'sms');
      return;
    }

    const student = await getStudentByPhone(phone);

    if (!student) {
      await enrollmentFlow(phone, text, null, 'sms');
      return;
    }

    const msg = rawText.trim().toUpperCase();
    const step = parseInt(student.Enrollment_Step) || 0;

    // 1. Commands first
    if (msg === 'HELP') {
      await updateStudent(student.id, { Enrollment_Step: 31 });
      await sendSMS(phone,
        `Hey ${student.Student_Name}! 👋 I am here to help!\n\nWhat do you need help with? Just tell me in your own words — for example:\n\n"I don't understand photosynthesis"\n"How do I solve quadratic equations"\n"What topics should I focus on for NECTA"\n\nJust type your question and I will help you! 🎓`
      );
      return;
    }

    if (msg === 'MYSTATS') {
      await handleMyStats(student, phone, 'sms');
      return;
    }

    if (msg === 'SUBJECTS') {
      await updateStudent(student.id, { Enrollment_Step: 30 });
      await sendSMS(phone,
        `Which subjects do you want to study? Choose from:\n\n📐 Maths\n🔬 Biology\n⚗️ Chemistry\n🧪 Physics\n📖 English\n📚 History\n🌍 Geography\n\nType the subjects you want separated by commas!\nExample: Maths, Biology, Chemistry`
      );
      return;
    }

    if (msg === 'TEST' || msg === 'TESTQUESTION') {
      await sendDailyQuestion(student);
      return;
    }

    if (msg === 'WRONG' || msg === 'EXPLAIN') {
      await handleChallenge(student, phone, 'sms');
      return;
    }

    // 2. PAY command
    if (msg === 'PAY') {
      await updateStudent(student.id, { Enrollment_Step: 40 });
      await sendSMS(phone, PLAN_MESSAGE);
      return;
    }

    // 3. Saturday quiz answer format (e.g. "1A 2B 3C 4D 5A")
    if (isSaturdayAnswerFormat(msg) && student.Saturday_Answers) {
      await handleSaturdayAnswers(student, msg, phone, 'sms');
      return;
    }

    // 4. A/B/C/D answer
    if (['A', 'B', 'C', 'D'].includes(msg)) {
      await processAnswer(student, msg, phone, 'sms');
      return;
    }

    // 5. Pending step handlers
    if (step === 40) {
      await handlePlanSelection(student, msg, phone, 'sms');
      return;
    }

    if (step === 41) {
      await handlePaymentConfirmation(student, rawText, phone, 'sms');
      return;
    }

    if (step === 30) {
      await handleSubjectUpdate(student, rawText, phone, 'sms');
      return;
    }

    if (step === 31) {
      await handleHelpQuestion(student, rawText, phone, 'sms');
      return;
    }

    // 4. Enrollment in progress
    if (student.Status === 'Enrolling') {
      await enrollmentFlow(phone, rawText, student, 'sms');
      return;
    }

    // 5. Smart help fallback
    await handleHelpQuestion(student, rawText, phone, 'sms');
  } catch (err) {
    console.error('SMS webhook error:', err);
  }
});

// ─── Payment Callback (ClickPesa) ─────────────────────────────────────────────
app.post('/webhook/payment', async (req, res) => {
  res.sendStatus(200);
  try {
    const { phone, status, reference } = req.body;
    if (status !== 'SUCCESS') return;

    const student = await getStudentByPhone(phone);
    if (!student) return;

    const now = new Date();
    const planName = student.Payment_Plan || 'Mwezi Pack';
    const planEntry = Object.values(PLAN_MAP).find(p => p.name === planName) || PLAN_MAP['2'];
    const nextPayment = new Date(now);
    nextPayment.setDate(nextPayment.getDate() + planEntry.days);

    await updateStudent(student.id, {
      Status: 'Active',
      Trial_Status: 'Paid',
      Subscription_Starts: now.toISOString().split('T')[0],
      Next_Payment_Date: nextPayment.toISOString().split('T')[0],
      Payment_Amount: planEntry.price,
    });

    const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
    await send(student.Student_Phone, t(student,
      `✅ Payment received, ${student.Student_Name}! You're all set — JIBU will keep sending your daily questions. Streak iko salama! 🔥`,
      `✅ Asante ${student.Student_Name}! Malipo yamefanikiwa — JIBU itaendelea. Streak yako iko salama! 🔥`
    ));
  } catch (err) {
    console.error('Payment webhook error:', err);
  }
});

// ─── Answer Processing ────────────────────────────────────────────────────────
async function processAnswer(student, answer, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const raw = (student.Todays_Correct_Answer || '').trim();

  if (!raw) {
    await send(phone, t(student,
      `No question yet for today! Come back at 4:00 PM. ⏰`,
      `Bado hakuna swali leo! Rudi saa 10 jioni. ⏰`
    ));
    return;
  }

  // Parse queue (JSON array) or fall back to legacy plain-string answer
  let queue;
  try {
    queue = JSON.parse(raw);
    if (!Array.isArray(queue)) throw new Error('not array');
  } catch {
    // Legacy: single-question mode
    const isCorrect = answer === raw.toUpperCase().charAt(0);
    const feedback = await generateFeedback(student.Student_Name, isCorrect, answer, raw, student.Subjects, student.Form_level);
    await send(phone, feedback);
    await updateStudent(student.id, { Todays_Correct_Answer: '' });
    return;
  }

  // Find first unanswered question
  const idx = queue.findIndex(q => !q.done);
  if (idx === -1) {
    await send(phone, t(student,
      `You've already answered all today's questions! 🎉 See you tomorrow at 4 PM.`,
      `Umekwisha jibu maswali yote leo! 🎉 Tutaonana kesho saa 10 jioni.`
    ));
    return;
  }

  const current = queue[idx];
  const isCorrect = answer === current.answer.toUpperCase();
  const today = new Date().toISOString().split('T')[0];

  // Update streak only once per day (on first question answered)
  const alreadyAnsweredToday = (student.Last_Answer_Date === today);
  let newStreak = parseInt(student.Current_Streak) || 0;
  let newPoints = parseInt(student.Total_Points) || 0;
  let weakTopics = student.Weak_Topics || '';
  let strongTopics = student.Strong_Topics || '';

  if (isCorrect) {
    newPoints += 10;
    if (!alreadyAnsweredToday) newStreak += 1;
    if (!strongTopics.includes(current.subject)) {
      strongTopics = strongTopics ? `${strongTopics}, ${current.subject}` : current.subject;
    }
  } else {
    if (!weakTopics.includes(current.subject)) {
      weakTopics = weakTopics ? `${weakTopics}, ${current.subject}` : current.subject;
    }
  }

  const longestStreak = Math.max(parseInt(student.Longest_Streak) || 0, newStreak);
  const newRank = getRankTitle(newStreak);

  // Mark this question done
  queue[idx].done = true;
  const remaining = queue.filter(q => !q.done);

  // Update topic history and question counts carried inside Last_Question
  // (questionHistory — the exact-wording anti-repeat list — is written by
  // sendDailyQuestion and just needs to be passed through unchanged here)
  let topicHistory = {};
  let questionCounts = {};
  let questionHistory = {};
  try {
    const prevLQ = JSON.parse(student.Last_Question || '{}');
    topicHistory = prevLQ.topicHistory || {};
    questionCounts = prevLQ.questionCounts || {};
    questionHistory = prevLQ.questionHistory || {};
  } catch { /* ignore */ }

  const answeredTopic = current.topic || current.subject;
  if (!topicHistory[current.subject]) topicHistory[current.subject] = [];
  if (!topicHistory[current.subject].includes(answeredTopic)) {
    topicHistory[current.subject].push(answeredTopic);
    // Keep the 20 most recent topics per subject so the prompt stays concise
    if (topicHistory[current.subject].length > 20) {
      topicHistory[current.subject] = topicHistory[current.subject].slice(-20);
    }
  }
  questionCounts[current.subject] = (questionCounts[current.subject] || 0) + 1;

  await updateStudent(student.id, {
    Current_Streak: newStreak,
    Total_Points: newPoints,
    Last_Answer_Date: today,
    Longest_Streak: longestStreak,
    Rank_Title: newRank,
    Weak_Topics: weakTopics,
    Strong_Topics: strongTopics,
    Todays_Correct_Answer: remaining.length ? JSON.stringify(queue) : '',
    Last_Question: JSON.stringify({
      questionBody: current.questionBody,
      answer: current.answer,
      subject: current.subject,
      formLevel: student.Form_level || '4',
      topic: answeredTopic,
      topicHistory,
      questionCounts,
      questionHistory,
    }),
  });

  // Send feedback
  const explanation = await generateFeedback(
    current.questionBody, current.answer, answer, student.Form_level
  );
  const stats = `📊 Streak: ${newStreak} | Points: ${newPoints} | ${newRank}`;
  let feedbackMsg;
  if (isCorrect) {
    feedbackMsg = `✅ Correct! The answer is ${current.answer}. Hongera! ⭐\n\n💡 Why: ${explanation}\n\n${stats}`;
  } else {
    feedbackMsg = `❌ Not quite! The correct answer was ${current.answer}.\n\n💡 Why: ${explanation}\n\nKeep going — you've got this! 💪\n${stats}`;
  }
  await send(phone, feedbackMsg);

  const milestone = checkMilestone(newStreak);
  if (milestone) {
    await send(phone, getMilestoneMessage(student.Student_Name, newStreak, newRank));
  }

  // Send next question or completion message
  if (remaining.length) {
    await sleep(1000);
    const next = remaining[0];
    const nextIdx = queue.findIndex(q => q === next) + 1;
    const total = queue.length;
    const footer = t(student, `\n\nReply A, B, C or D!`, `\n\nJibu kwa A, B, C au D!`);
    await send(phone, `📚 ${next.subject} — Question ${nextIdx} of ${total}\n\n${next.questionBody}${footer}`);
  } else {
    await sleep(500);
    const correctCount = queue.filter(q => q.done && q.answer).length;
    await send(phone, t(student,
      `🏁 Done for today, ${student.Student_Name}! You answered all ${queue.length} questions.\n\n📊 Today: +${newPoints - (parseInt(student.Total_Points) || 0)} pts | Streak: ${newStreak} days\n\nSee you tomorrow at 4 PM! 🌟`,
      `🏁 Umekwisha leo, ${student.Student_Name}! Umejibu maswali yote ${queue.length}.\n\n📊 Leo: +${newPoints - (parseInt(student.Total_Points) || 0)} pts | Streak: siku ${newStreak}\n\nTutaonana kesho saa 10 jioni! 🌟`
    ));
  }
}

// ─── Help Question Handler ────────────────────────────────────────────────────
async function handleHelpQuestion(student, question, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const raw = await generateHelpAnswer(question, student.Subjects || 'their subjects', student.Form_level || '4');
  const cleanHelp = raw.replace(/[#*_]/g, '').trim();
  await updateStudent(student.id, { Enrollment_Step: 5 });
  await send(phone, `🎓 ${cleanHelp}\n\nSend HELP anytime you need me! 💪`);
}

// ─── MYSTATS Handler ──────────────────────────────────────────────────────────
async function handleMyStats(student, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const summary = await generateMyStats(student);
  const streak = student.Current_Streak || 0;
  const points = student.Total_Points || 0;
  const rank = student.Rank_Title || 'Mwanafunzi';
  await send(phone,
    `📊 Your JIBU Stats ${student.Student_Name}!\n\n${summary}\n\n🔥 Streak: ${streak} days\n⭐ Total Points: ${points}\n🏆 Rank: ${rank}\n\nKeep going — NECTA unakimbiza! 💪🇹🇿`
  );
}

// ─── Challenge / Re-explanation Handler ──────────────────────────────────────
const CHALLENGE_WORDS = ['wrong', 'disagree', 'how', 'explain', 'why', 'not right', "sure?", "really?", "i don't understand", "don't understand", "dont understand"];

function isChallengeMessage(raw) {
  const lower = raw.toLowerCase();
  return CHALLENGE_WORDS.some(w => lower.includes(w));
}

async function handleChallenge(student, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const raw = student.Last_Question;
  if (!raw) {
    await send(phone, t(student,
      `No recent question to re-explain! Answer today's question first, then ask me if you disagree. 😊`,
      `Hakuna swali la hivi karibuni! Jibu swali la leo kwanza, kisha niulize. 😊`
    ));
    return;
  }
  let lastQuestion;
  try { lastQuestion = JSON.parse(raw); } catch { return; }
  const reexplanation = await generateReexplanation(lastQuestion);
  await send(phone, reexplanation);
}

// ─── Subject Update Handler ───────────────────────────────────────────────────
const VALID_SUBJECTS = ['Maths', 'Biology', 'Chemistry', 'Physics', 'English', 'History', 'Geography'];

async function handleSubjectUpdate(student, rawText, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const normalized = rawText.toLowerCase();
  const matched = VALID_SUBJECTS.filter(s => normalized.includes(s.toLowerCase()));

  if (!matched.length) {
    await send(phone,
      `I couldn't match any subjects! 🤔 Try again using names from this list:\n\nMaths · Biology · Chemistry · Physics · English · History · Geography\n\nExample: Maths, Biology`
    );
    return;
  }

  await updateStudent(student.id, { Subjects: matched.join(', '), Enrollment_Step: 5 });
  await send(phone,
    `Perfect! 🔥 Your subjects are updated to ${matched.join(', ')}. New questions start tomorrow!`
  );
}

// ─── CRON: Token Health Check — daily at 03:00 UTC ───────────────────────────
// Checks days remaining on the 60-day token and refreshes proactively at
// ≤10 days left (i.e. around day 50), then persists the new token to
// Airtable and the Railway WHATSAPP_TOKEN environment variable.
cron.schedule('0 3 * * *', async () => {
  try {
    await checkAndRefreshToken();
  } catch (err) {
    console.error(`[${new Date().toISOString()}] ❌ Token health-check cron error:`, err.message);
  }
}, { timezone: 'UTC' });

// ─── CRON: Daily Questions at 16:00 EAT (13:00 UTC) ─────────────────────────
cron.schedule('0 13 * * *', async () => {
  console.log('📤 Sending daily questions...');
  try {
    const students = await getAllActiveStudents();
    for (const student of students) {
      await sendDailyQuestion(student);
      await sleep(500);
    }
    // Send 1 teaser question to trial-expired (Paused) students
    const pausedStudents = await getAllActiveStudents(['Paused']);
    for (const student of pausedStudents) {
      if (student.Trial_Status === 'Trial_Expired') {
        await sendTeaserQuestion(student);
        await sleep(500);
      }
    }
  } catch (err) {
    console.error('Daily questions cron error:', err);
  }
}, { timezone: 'UTC' });

const MAX_RECENT_QUESTIONS_PER_SUBJECT = 30;

async function sendDailyQuestion(student) {
  try {
    const subjects = (student.Subjects || '').split(',').map(s => s.trim()).filter(Boolean);
    if (!subjects.length) return;

    // Read topic history, question counts, and the exact-wording question
    // history (last 30 per subject) from Last_Question.
    let lastQuestionData = {};
    try {
      lastQuestionData = JSON.parse(student.Last_Question || '{}');
    } catch { /* first-time student, start fresh */ }
    const topicHistory = lastQuestionData.topicHistory || {};
    const questionCounts = lastQuestionData.questionCounts || {};
    const questionHistory = lastQuestionData.questionHistory || {};

    const queue = [];
    const formLevel = student.Form_level || '4';
    for (const subject of subjects) {
      const countSoFar = questionCounts[subject] || 0;
      // Every 10 answered questions on this subject, make the first one a revision
      const isRevision = countSoFar > 0 && countSoFar % 10 === 0;

      // Local working copies so topics/questions generated earlier in THIS
      // batch also get avoided by later questions in the same batch, not
      // just questions from previous days.
      const localTopics = [...(topicHistory[subject] || [])];
      const localQuestions = [...(questionHistory[subject] || [])];

      for (let i = 0; i < 3; i++) {
        const parsed = await generateQuestion(subject, formLevel, localTopics, isRevision && i === 0, localTopics, localQuestions);
        const tip = parsed.examTip ? `\n\n${parsed.examTip}` : '';
        const questionBody = `${parsed.questionBody}\nA) ${parsed.optionA}\nB) ${parsed.optionB}\nC) ${parsed.optionC}\nD) ${parsed.optionD}${tip}`;
        const answer = (parsed.answer || 'A').toUpperCase().charAt(0);
        const topic = parsed.topic || subject;
        console.log(`📚 ${subject} Q${i+1} [${topic}]: answer="${answer}", q="${parsed.questionBody?.slice(0,60)}"`);
        queue.push({ subject, questionBody, answer, topic, done: false });

        if (topic && !localTopics.includes(topic)) localTopics.push(topic);
        if (parsed.questionBody) localQuestions.push(parsed.questionBody);
        await sleep(300);
      }

      topicHistory[subject] = localTopics.slice(-20);
      questionHistory[subject] = localQuestions.slice(-MAX_RECENT_QUESTIONS_PER_SUBJECT);
    }

    await updateStudent(student.id, {
      Todays_Correct_Answer: JSON.stringify(queue),
      Last_Question: JSON.stringify({
        ...lastQuestionData,
        topicHistory,
        questionCounts,
        questionHistory,
      }),
    });

    const streak = student.Current_Streak || 0;
    const rank = student.Rank_Title || getRankTitle(streak);
    const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;

    const header = t(student,
      `🔥 Day ${streak} | ${rank} | ${student.Student_Name}\n\n`,
      `🔥 Siku ${streak} | ${rank} | ${student.Student_Name}\n\n`
    );
    const first = queue[0];
    const total = queue.length;
    const qNum = `📚 ${first.subject} — Question 1 of ${total}\n\n`;
    const footer = t(student, `\n\nReply A, B, C or D!`, `\n\nJibu kwa A, B, C au D!`);
    await send(student.Student_Phone, header + qNum + first.questionBody + footer);
  } catch (err) {
    console.error(`Error sending question to ${student.Student_Phone}:`, err);
  }
}

// ─── CRON: Streak Check at 23:59 EAT (20:59 UTC) ────────────────────────────
cron.schedule('59 20 * * *', async () => {
  console.log('🔍 Checking streaks...');
  try {
    const students = await getAllActiveStudents();
    const today = new Date().toISOString().split('T')[0];

    for (const student of students) {
      if (student.Last_Answer_Date === today) continue;

      const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
      const freezes = parseInt(student.Freeze_Credits) || 0;

      if (freezes > 0) {
        await updateStudent(student.id, { Freeze_Credits: freezes - 1 });
        await send(student.Student_Phone, t(student,
          `🛡️ Streak Shield used, ${student.Student_Name}! Your streak is safe — ${freezes - 1} shield(s) left. Keep going! 💪`,
          `🛡️ Kinga imetumika ${student.Student_Name}! Streak yako iko salama — Shields zilizobaki: ${freezes - 1}. Endelea! 💪`
        ));
      } else {
        await updateStudent(student.id, { Current_Streak: 0, Rank_Title: 'Mwanafunzi' });
        await send(student.Student_Phone, t(student,
          `💔 ${student.Student_Name}, your streak is gone! Back to 0 — but today is a new day. Answer tomorrow's question and rebuild! 💪`,
          `💔 ${student.Student_Name}, streak yako imevunjika! Streak: 0 — lakini kesho ni siku mpya. Jibu swali la kesho uanze tena! 💪`
        ));
      }
      await sleep(300);
    }
  } catch (err) {
    console.error('Streak check cron error:', err);
  }
}, { timezone: 'UTC' });

// ─── CRON: Weekly Parent Reports Sunday 09:00 EAT (06:00 UTC) ────────────────
cron.schedule('0 6 * * 0', async () => {
  console.log('📋 Sending parent reports...');
  try {
    const students = await getAllActiveStudents();
    for (const student of students) {
      if (!student.Parent_Phone) continue;
      const report = await generateParentReport(student);
      const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
      await send(student.Parent_Phone, report);
      await sleep(500);
    }
  } catch (err) {
    console.error('Parent reports cron error:', err);
  }
}, { timezone: 'UTC' });

// ─── CRON: Weekly Student Summaries Sunday 09:00 EAT (06:00 UTC) ─────────────
cron.schedule('0 6 * * 0', async () => {
  console.log('📊 Sending weekly student summaries...');
  try {
    const students = await getAllActiveStudents();
    for (const student of students) {
      try {
        const summary = await generateWeeklySummary(student);
        const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
        await send(student.Student_Phone, `📚 Your Weekly JIBU Summary!\n\n${summary}\n\n🔥 Streak: ${student.Current_Streak || 0} days | ⭐ Points: ${student.Total_Points || 0}\n\nKaa imara — NECTA inakuja! 💪🇹🇿`);
        await sleep(500);
      } catch (err) {
        console.error(`Weekly summary error for ${student.Student_Phone}:`, err.message);
      }
    }
  } catch (err) {
    console.error('Weekly student summaries cron error:', err);
  }
}, { timezone: 'UTC' });

// ─── CRON: Trial Expiry Check Daily 09:00 EAT (06:00 UTC) ────────────────────
cron.schedule('0 6 * * *', async () => {
  console.log('💳 Checking trial/payment status...');
  try {
    const students = await getAllActiveStudents(['Trial', 'Active']);
    const today = new Date().toISOString().split('T')[0];

    for (const student of students) {
      const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;

      if (student.Status === 'Trial' && student.Trial_End_Date === today) {
        await updateStudent(student.id, { Enrollment_Step: 40 });
        await send(student.Student_Phone, PLAN_MESSAGE);
      }

      if (student.Status === 'Trial' && student.Trial_Status !== 'Paid') {
        const trialEnd = new Date(student.Trial_End_Date);
        const graceEnd = new Date(trialEnd);
        graceEnd.setDate(graceEnd.getDate() + 2);
        if (new Date() > graceEnd) {
          await updateStudent(student.id, { Status: 'Paused', Trial_Status: 'Trial_Expired' });
          await send(student.Student_Phone, t(student,
            `😔 ${student.Student_Name}, JIBU is paused. Reply PAY to choose a plan and keep learning! Your ${student.Current_Streak}-day streak is waiting! 💪`,
            `😔 ${student.Student_Name}, JIBU imesimamishwa. Jibu PAY kuchagua mpango wako uendelee! Streak yako ya siku ${student.Current_Streak} inakusubiri! 💪`
          ));
        }
      }

      if (student.Status === 'Active' && student.Next_Payment_Date) {
        const nextPayDate = new Date(student.Next_Payment_Date);
        const reminderDate = new Date(nextPayDate);
        reminderDate.setDate(reminderDate.getDate() - 3);
        if (new Date().toISOString().split('T')[0] === reminderDate.toISOString().split('T')[0]) {
          const payLink = await createPaymentLink(student.Student_Phone, 5000, `JIBU renewal - ${student.Student_Name}`);
          await send(student.Student_Phone, t(student,
            `🔔 Heads up, ${student.Student_Name}! Your JIBU subscription renews on ${student.Next_Payment_Date}. Stay ahead — pay TZS 5,000 now:\n${payLink}`,
            `🔔 ${student.Student_Name}, usisahau! Usajili wako unakwisha ${student.Next_Payment_Date}. Lipa TZS 5,000 mapema:\n${payLink}`
          ));
        }
      }

      if (student.Status === 'Active' && student.Next_Payment_Date < today) {
        await updateStudent(student.id, { Status: 'Paused' });
      }

      await sleep(200);
    }
  } catch (err) {
    console.error('Trial/payment check error:', err);
  }
}, { timezone: 'UTC' });

// ─── Plan Selection Handler (step 40) ────────────────────────────────────────
async function handlePlanSelection(student, msg, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const plan = PLAN_MAP[msg];
  if (!plan) {
    await send(phone, `Please reply 1, 2, 3 or 4 to choose your plan:\n\n1️⃣ Wiki Pass — 1,500 TZS (7 days)\n2️⃣ Mwezi Pack — 5,000 TZS (30 days)\n3️⃣ Muhula Pass — 12,000 TZS (90 days)\n4️⃣ Mwaka Pack — 30,000 TZS (365 days)`);
    return;
  }
  const expiry = new Date();
  expiry.setDate(expiry.getDate() + plan.days);
  const expiryDate = expiry.toISOString().split('T')[0];
  await updateStudent(student.id, {
    Payment_Plan: plan.name,
    Next_Payment_Date: expiryDate,
    Enrollment_Step: 41,
  });
  await send(phone, `✅ Great choice! ${plan.name} — TZS ${plan.price.toLocaleString()} for ${plan.days} days.\n\nNow send your M-Pesa confirmation number to activate your plan.\n\nExample: AB123C45`);
}

// ─── Payment Confirmation Handler (step 41) ───────────────────────────────────
async function handlePaymentConfirmation(student, rawText, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const ref = rawText.trim();
  await updateStudent(student.id, {
    Status: 'Active',
    Trial_Status: 'Paid',
    Payment_Reference: ref,
    Subscription_Starts: new Date().toISOString().split('T')[0],
    Enrollment_Step: 5,
  });
  await send(phone, t(student,
    `✅ Thank you, ${student.Student_Name}! Reference ${ref} received.\n\nYou're now on ${student.Payment_Plan || 'your plan'}! 🎉\nYour questions continue — streak is safe! 🔥\n\nJibu maswali kila siku! 💪🇹🇿`,
    `✅ Asante ${student.Student_Name}! Namba ${ref} imepokelewa.\n\nUme-activate ${student.Payment_Plan || 'mpango wako'}! 🎉\nMaswali yanaendelea — streak iko salama! 🔥\n\nJibu maswali kila siku! 💪🇹🇿`
  ));
}

// ─── Saturday Quiz Format Detector ───────────────────────────────────────────
function isSaturdayAnswerFormat(msg) {
  return /^(\d[A-D])(\s+\d[A-D]){4}$/i.test(msg.trim());
}

// ─── Saturday Quiz Answer Handler ────────────────────────────────────────────
async function handleSaturdayAnswers(student, msg, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  let quizData;
  try {
    quizData = JSON.parse(student.Saturday_Answers);
  } catch {
    await send(phone, t(student, `No Saturday quiz found! Wait for next Saturday. 📅`, `Hakuna mtihani wa Jumamosi! Subiri Jumamosi ijayo. 📅`));
    return;
  }
  if (quizData.graded) {
    await send(phone, t(student, `You already submitted your Saturday answers! 🎉 Wait for next Saturday.`, `Umetuma majibu tayari! 🎉 Subiri Jumamosi ijayo.`));
    return;
  }

  const parts = msg.trim().toUpperCase().split(/\s+/);
  const studentAnswers = {};
  for (const part of parts) {
    const num = parseInt(part[0]);
    const letter = part[1];
    if (num >= 1 && num <= 5 && 'ABCD'.includes(letter)) {
      studentAnswers[num] = letter;
    }
  }

  const questions = quizData.questions;
  let score = 0;
  let corrections = '';
  for (let i = 0; i < questions.length; i++) {
    const qNum = i + 1;
    const correct = questions[i].answer.toUpperCase().charAt(0);
    const given = studentAnswers[qNum];
    if (given === correct) {
      score++;
    } else {
      corrections += `\n❌ Q${qNum}: Correct answer is ${correct} — ${questions[i].questionBody}`;
    }
  }

  await updateStudent(student.id, {
    Saturday_Answers: JSON.stringify({ ...quizData, studentAnswers, graded: true, score }),
  });

  let reply = `🎯 Saturday Results!\n\nScore: ${score}/5 `;
  if (score === 5) reply += '🏆 Perfect! Umefaulu kabisa!';
  else if (score >= 3) reply += '✅ Good job! Hongera!';
  else reply += '💪 Keep practising! Jaribu tena!';
  if (corrections) reply += `\n\nCorrections:${corrections}`;
  reply += `\n\nSee you next Saturday! 🇹🇿`;

  await send(phone, reply);
}

// ─── Send Saturday Quiz ───────────────────────────────────────────────────────
async function sendSaturdayQuiz(student) {
  try {
    const subjects = (student.Subjects || '').split(',').map(s => s.trim()).filter(Boolean);
    if (!subjects.length) return;
    const subject = subjects[0];
    const formLevel = student.Form_level || '4';

    const questions = await generateSaturdayQuiz(subject, formLevel);
    if (!questions || !questions.length) return;

    await updateStudent(student.id, {
      Saturday_Answers: JSON.stringify({ questions, graded: false }),
    });

    let msg = `🎯 JIBU Saturday Challenge!\nMtihani wa Jumamosi — test yourself!\n\nThis week's bonus quiz for Form ${formLevel} ${subject}:\n\n`;
    questions.forEach((q, i) => {
      msg += `Q${i + 1}: ${q.questionBody}\nA) ${q.optionA}  B) ${q.optionB}  C) ${q.optionC}  D) ${q.optionD}\n\n`;
    });
    msg += `Reply with your 5 answers like this:\nExample: 1A 2B 3C 4D 5A\n\nGood luck! Jitahidi! 💪🇹🇿`;

    const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
    await send(student.Student_Phone, msg);
  } catch (err) {
    console.error(`Saturday quiz error for ${student.Student_Phone}:`, err);
  }
}

// ─── CRON: Saturday Quiz at 09:00 EAT (06:00 UTC) ────────────────────────────
cron.schedule('0 6 * * 6', async () => {
  console.log('🎯 Sending Saturday quiz...');
  try {
    const students = await getAllActiveStudents(['Active', 'Trial']);
    for (const student of students) {
      await sendSaturdayQuiz(student);
      await sleep(1000);
    }
  } catch (err) {
    console.error('Saturday quiz cron error:', err);
  }
}, { timezone: 'UTC' });

// ─── Send Teaser Question (1 free question for expired trial students) ────────
async function sendTeaserQuestion(student) {
  try {
    const subjects = (student.Subjects || '').split(',').map(s => s.trim()).filter(Boolean);
    if (!subjects.length) return;
    const subject = subjects[0];
    const formLevel = student.Form_level || '4';

    let topicHistory = {};
    let questionHistory = {};
    try {
      const lastQ = JSON.parse(student.Last_Question || '{}');
      topicHistory = lastQ.topicHistory || {};
      questionHistory = lastQ.questionHistory || {};
    } catch { /* first-time student, start fresh */ }

    const parsed = await generateQuestion(subject, formLevel, topicHistory[subject] || [], false, [], questionHistory[subject] || []);
    const tip = parsed.examTip ? `\n\n${parsed.examTip}` : '';
    const questionBody = `${parsed.questionBody}\nA) ${parsed.optionA}\nB) ${parsed.optionB}\nC) ${parsed.optionC}\nD) ${parsed.optionD}${tip}`;
    const answer = (parsed.answer || 'A').toUpperCase().charAt(0);

    await updateStudent(student.id, {
      Todays_Correct_Answer: JSON.stringify([{ subject, questionBody, answer, done: false }]),
    });

    const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
    const upgradeMsg = `\n\n🔓 Unataka maswali yote 3 leo?\nUpgrade to Wiki Pass — just 1,500 TZS for 7 days!\nReply PAY to see all plans. 💪`;
    await send(student.Student_Phone, `📚 ${subject} — Today's Free Question\n\n${questionBody}\n\nReply A, B, C or D!${upgradeMsg}`);
  } catch (err) {
    console.error(`Teaser question error for ${student.Student_Phone}:`, err);
  }
}

// ─── Helpers ──────────────────────────────────────────────────────────────────
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ─── Start Server ─────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, async () => {
  console.log(`🎓 JIBU bot running on port ${PORT}`);
  const airtableKey = process.env.AIRTABLE_API_KEY || '';
  console.log(`🔑 AIRTABLE_API_KEY loaded: ${airtableKey ? airtableKey.slice(0, 15) : '(not set)'}...`);
  await initToken();
  validateWhatsAppToken();
});

module.exports = app;
