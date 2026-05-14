require('dotenv').config();
const express = require('express');
const cron = require('node-cron');
const Anthropic = require('@anthropic-ai/sdk');

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const { airtable, getStudentByPhone, createStudent, updateStudent, getAllActiveStudents } = require('./airtable');
const { sendWhatsApp } = require('./whatsapp');
const { sendSMS } = require('./sms');
const { createPaymentLink, verifyPayment } = require('./payments');
const { generateQuestion, generateFeedback, generateParentReport } = require('./claude');
const { getRankTitle, checkMilestone, getMilestoneMessage } = require('./ranks');
const { enrollmentFlow } = require('./enrollment');
const { handleNectaResults } = require('./necta');
const { t } = require('./lang');

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

// ─── Health Check ────────────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({ status: 'JIBU bot is running 🎓', time: new Date().toISOString() });
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
      const text = (message.text?.body || '').trim().toUpperCase();

      if (text.startsWith('JIBU MATOKEO')) {
        await handleNectaResults(phone, text, 'whatsapp');
        continue;
      }

      const student = await getStudentByPhone(phone);

      if (!student) {
        await enrollmentFlow(phone, text, null, 'whatsapp');
        continue;
      }

      // Language preference toggle
      if (text === 'SWAHILI' || text === 'NIAMBIE KWA KISWAHILI') {
        await updateStudent(student.id, { Language_Pref: 'sw' });
        await sendWhatsApp(phone, `Got it! 🇹🇿 Nitaongea nawe kwa Kiswahili zaidi from now on. Send "English" anytime to switch back.`);
        continue;
      }
      if (text === 'ENGLISH') {
        await updateStudent(student.id, { Language_Pref: 'en' });
        await sendWhatsApp(phone, `Got it! 🇬🇧 Switching to English mode. Send "Swahili" anytime to switch.`);
        continue;
      }

      if (text === 'TEST' || text === 'TESTQUESTION') {
        await sendDailyQuestion(student);
        continue;
      }

      if (['A', 'B', 'C', 'D'].includes(text)) {
        await processAnswer(student, text, phone, 'whatsapp');
        continue;
      }

      if (student.Status === 'Enrolling') {
        await enrollmentFlow(phone, text, student, 'whatsapp');
        continue;
      }

      await sendWhatsApp(phone, t(student,
        `Hey! 👋 Reply A, B, C or D after you get your daily question. Need help? Send HELP!`,
        `Habari! 👋 Jibu kwa A, B, C au D ukipata swali lako la leo. Msaada? Tuma HELP!`
      ));
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
    const text = (req.body.text || '').trim().toUpperCase();

    if (text.startsWith('JIBU MATOKEO')) {
      await handleNectaResults(phone, text, 'sms');
      return;
    }

    const student = await getStudentByPhone(phone);

    if (!student) {
      await enrollmentFlow(phone, text, null, 'sms');
      return;
    }

    if (text === 'TEST' || text === 'TESTQUESTION') {
      await sendDailyQuestion(student);
      return;
    }

    if (['A', 'B', 'C', 'D'].includes(text)) {
      await processAnswer(student, text, phone, 'sms');
      return;
    }

    if (student.Status === 'Enrolling') {
      await enrollmentFlow(phone, text, student, 'sms');
      return;
    }
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
    const nextPayment = new Date(now);
    nextPayment.setMonth(nextPayment.getMonth() + 1);

    await updateStudent(student.id, {
      Status: 'Active',
      Trial_Status: 'Paid',
      Subscription_Starts: now.toISOString().split('T')[0],
      Next_Payment_Date: nextPayment.toISOString().split('T')[0],
      Payment_Amount: 5000,
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

  await updateStudent(student.id, {
    Current_Streak: newStreak,
    Total_Points: newPoints,
    Last_Answer_Date: today,
    Longest_Streak: longestStreak,
    Rank_Title: newRank,
    Weak_Topics: weakTopics,
    Strong_Topics: strongTopics,
    Todays_Correct_Answer: remaining.length ? JSON.stringify(queue) : '',
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

// ─── CRON: Daily Questions at 16:00 EAT (13:00 UTC) ─────────────────────────
cron.schedule('0 13 * * *', async () => {
  console.log('📤 Sending daily questions...');
  try {
    const students = await getAllActiveStudents();
    for (const student of students) {
      await sendDailyQuestion(student);
      await sleep(500);
    }
  } catch (err) {
    console.error('Daily questions cron error:', err);
  }
}, { timezone: 'UTC' });

async function sendDailyQuestion(student) {
  try {
    const subjects = (student.Subjects || '').split(',').map(s => s.trim()).filter(Boolean);
    if (!subjects.length) return;

    const queue = [];
    for (const subject of subjects) {
      const parsed = await generateQuestion(subject, student.Form_level || '4');
      const questionBody = `${parsed.questionBody}\nA) ${parsed.optionA}\nB) ${parsed.optionB}\nC) ${parsed.optionC}\nD) ${parsed.optionD}`;
      const answer = (parsed.answer || 'A').toUpperCase().charAt(0);
      console.log(`📚 Question for ${subject}: answer="${answer}", q="${parsed.questionBody?.slice(0,60)}"`);
      queue.push({ subject, questionBody, answer, done: false });
      await sleep(200);
    }

    await updateStudent(student.id, { Todays_Correct_Answer: JSON.stringify(queue) });

    const streak = student.Current_Streak || 0;
    const rank = student.Rank_Title || getRankTitle(streak);
    const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;

    const header = t(student,
      `🔥 Day ${streak} | ${rank} | ${student.Student_Name}\n\n`,
      `🔥 Siku ${streak} | ${rank} | ${student.Student_Name}\n\n`
    );
    const first = queue[0];
    const qNum = `📚 ${first.subject} — Question 1 of ${subjects.length}\n\n`;
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

// ─── CRON: Trial Expiry Check Daily 09:00 EAT (06:00 UTC) ────────────────────
cron.schedule('0 6 * * *', async () => {
  console.log('💳 Checking trial/payment status...');
  try {
    const students = await getAllActiveStudents(['Trial', 'Active']);
    const today = new Date().toISOString().split('T')[0];

    for (const student of students) {
      const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;

      if (student.Status === 'Trial' && student.Trial_End_Date === today) {
        const payLink = await createPaymentLink(student.Student_Phone, 5000, `JIBU subscription - ${student.Student_Name}`);
        await send(student.Student_Phone, t(student,
          `⏰ ${student.Student_Name}, your 7-day free trial ends today! Your streak is at ${student.Current_Streak} days — don't lose it!\n\nContinue for just TZS 5,000/month:\n${payLink}\n\nPay today to keep your streak alive! 🔥`,
          `⏰ ${student.Student_Name}, siku 7 za JIBU zimekwisha! Streak yako ni siku ${student.Current_Streak} — usiipoteze!\n\nEndelea kwa TZS 5,000 tu kwa mwezi:\n${payLink}\n\nLipa leo streak yako iendelee! 🔥`
        ));
      }

      if (student.Status === 'Trial' && student.Trial_Status !== 'Paid') {
        const trialEnd = new Date(student.Trial_End_Date);
        const graceEnd = new Date(trialEnd);
        graceEnd.setDate(graceEnd.getDate() + 2);
        if (new Date() > graceEnd) {
          await updateStudent(student.id, { Status: 'Paused', Trial_Status: 'Trial_Expired' });
          await send(student.Student_Phone, t(student,
            `😔 ${student.Student_Name}, JIBU is paused — payment overdue. Pay TZS 5,000 to get back in. Your ${student.Current_Streak}-day streak is waiting! 💪`,
            `😔 ${student.Student_Name}, JIBU imesimamishwa kwa sababu ya malipo. Lipa TZS 5,000 kuendelea. Streak yako ya siku ${student.Current_Streak} inakusubiri! 💪`
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

// ─── Helpers ──────────────────────────────────────────────────────────────────
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ─── Start Server ─────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🎓 JIBU bot running on port ${PORT}`);
});

module.exports = app;
