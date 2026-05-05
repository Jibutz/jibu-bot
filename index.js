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

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

// ─── Health Check ────────────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({ status: 'JIBU bot is running 🎓', time: new Date().toISOString() });
});
// — WhatsApp Webhook Verification
app.get('/webhook/whatsapp', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];
  if (mode === 'subscribe' && token === process.env.WEBHOOK_VERIFY_TOKEN) {
    res.status(200).send(challenge);
  } else {
    res.sendStatus(403);
  }
// —— WhatsApp Webhook (Meta Cloud API)
app.post('/webhook/whatsapp', async (req, res) => {
  res.sendStatus(200);
  try {
    const body = req.body;
    const entry = body?.entry?.[0];
    const changes = entry?.changes?.[0];
    const value = changes?.value;
    const messages = value?.messages;

    if (!messages?.length) return;

    for (const message of messages) {
      const phone = message.from;
      const text = (message.text?.body || '').trim().toUpperCase();

      if (text.startsWith('JIBU MATOKEO')) {
        await handleNectaResults(phone, text, 'whatsapp');
        continue;
      }

      const student = await getStudentByPhone(phone);

      if (!student) {
        await enrollmentFlow(phone, text, 'whatsapp');
        continue;
      }

      const validAnswers = ['A', 'B', 'C', 'D'];
      if (validAnswers.includes(text) && student.Todays_Correct_Answer) {
        const isCorrect = text === student.Todays_Correct_Answer;
        const feedback = await generateFeedback(student, text, isCorrect);
        const newStreak = isCorrect ? (student.Current_Streak || 0) + 1 : (student.Current_Streak || 0);
        const newPoints = isCorrect ? (student.Total_Points || 0) + 10 : (student.Total_Points || 0);
        const rankTitle = getRankTitle(newStreak);
        await updateStudent(student.id, {
          Current_Streak: newStreak,
          Longest_Streak: Math.max(newStreak, student.Longest_Streak || 0),
          Total_Points: newPoints,
          Last_Answer_Date: new Date().toISOString().split('T')[0],
          Rank_Title: rankTitle
        });
        await sendWhatsApp(phone, feedback);
      } else {
        const question = await generateQuestion(student);
        await sendWhatsApp(phone, question);
      }
    }
  } catch (error) {
    console.error('Webhook error:', error);
  }
});
      const student = await getStudentByPhone(phone);

      if (!student) {
        await enrollmentFlow(phone, text, null, 'whatsapp');
        continue;
      }

      // Answer processing (A, B, C, D)
      if (['A', 'B', 'C', 'D'].includes(text)) {
        await processAnswer(student, text, phone, 'whatsapp');
        continue;
      }

      // Enrollment continuation
      if (student.Status === 'Enrolling') {
        await enrollmentFlow(phone, text, student, 'whatsapp');
        continue;
      }

      // Default fallback
      await sendWhatsApp(phone, `Karibu JIBU! 📚 Jibu kwa A, B, C au D baada ya kupata swali. Kwa msaada tuma "HELP".`);
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
    await send(student.Student_Phone,
      `✅ Asante ${student.Student_Name}! Malipo yako yamefanikiwa. JIBU itaendelea kukutumia maswali kila siku. Streak yako iko salama! 🔥`
    );
  } catch (err) {
    console.error('Payment webhook error:', err);
  }
});

// ─── Answer Processing ────────────────────────────────────────────────────────
async function processAnswer(student, answer, phone, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const correct = (student.Todays_Correct_Answer || '').toUpperCase();

  if (!correct) {
    await send(phone, `Hakuna swali la leo bado. Subiri hadi saa 10 jioni. ⏰`);
    return;
  }

  const isCorrect = answer === correct;
  const today = new Date().toISOString().split('T')[0];

  let newStreak = parseInt(student.Current_Streak) || 0;
  let newPoints = parseInt(student.Total_Points) || 0;
  let weakTopics = student.Weak_Topics || '';
  let strongTopics = student.Strong_Topics || '';

  if (isCorrect) {
    newStreak += 1;
    newPoints += 10;
  } else {
    // Add subject to weak topics
    const subject = student.Subject || student.Subjects?.split(',')[0] || 'General';
    if (!weakTopics.includes(subject)) {
      weakTopics = weakTopics ? `${weakTopics}, ${subject}` : subject;
    }
  }

  const longestStreak = Math.max(parseInt(student.Longest_Streak) || 0, newStreak);
  const newRank = getRankTitle(newStreak);

  await updateStudent(student.id, {
    Current_Streak: newStreak,
    Total_Points: newPoints,
    Last_Answer_Date: today,
    Longest_Streak: longestStreak,
    Rank_Title: newRank,
    Weak_Topics: weakTopics,
    Strong_Topics: strongTopics,
    Todays_Correct_Answer: '',
  });

  // Generate personalised feedback via Claude
  const feedback = await generateFeedback(
    student.Student_Name,
    isCorrect,
    answer,
    correct,
    student.Subjects,
    student.Form_level
  );

  const suffix = `\n\n📊 Streak: ${newStreak} | Points: ${newPoints} | ${newRank}`;
  await send(phone, feedback + suffix);

  // Milestone check
  const milestone = checkMilestone(newStreak);
  if (milestone) {
    const milestoneMsg = getMilestoneMessage(student.Student_Name, newStreak, newRank);
    await send(phone, milestoneMsg);
    await updateStudent(student.id, { Rank_Title: newRank });
  }
}

// ─── CRON: Daily Questions at 16:00 EAT (13:00 UTC) ─────────────────────────
cron.schedule('0 13 * * *', async () => {
  console.log('📤 Sending daily questions...');
  try {
    const students = await getAllActiveStudents();
    for (const student of students) {
      await sendDailyQuestion(student);
      await sleep(500); // Rate limiting
    }
  } catch (err) {
    console.error('Daily questions cron error:', err);
  }
}, { timezone: 'UTC' });

async function sendDailyQuestion(student) {
  try {
    const { question, answer } = await generateQuestion(student);
    await updateStudent(student.id, { Todays_Correct_Answer: answer });

    const streak = student.Current_Streak || 0;
    const rank = student.Rank_Title || getRankTitle(streak);
    const header = `🔥 Siku ${streak} | ${rank} | ${student.Student_Name}\n\n`;
    const footer = `\n\nJibu kwa kutuma A, B, C au D`;
    const fullMessage = header + question + footer;

    const send = student.Channel === 'SMS' ? sendSMS : sendWhatsApp;
    await send(student.Student_Phone, fullMessage);
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
        await send(student.Student_Phone,
          `🛡️ Kinga imetumika ${student.Student_Name}! Streak yako iko salama. Freezes zilizobaki: ${freezes - 1}`
        );
      } else {
        await updateStudent(student.id, {
          Current_Streak: 0,
          Rank_Title: 'Mwanafunzi',
        });
        await send(student.Student_Phone,
          `💔 ${student.Student_Name}, streak yako imevunjika. Streak: 0 | Anza upya leo! Jibu swali la kesho. 💪`
        );
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

      // Trial expiry
      if (student.Status === 'Trial' && student.Trial_End_Date === today) {
        const payLink = await createPaymentLink(student.Student_Phone, 5000, `JIBU subscription - ${student.Student_Name}`);
        await send(student.Student_Phone,
          `⏰ ${student.Student_Name}, siku 7 za JIBU zimekwisha! Streak yako ni siku ${student.Current_Streak}. Endelea kwa TZS 5,000 tu kwa mwezi.\n\nLipa sasa: ${payLink}\n\nUkikosa kulipa leo streak yako itaisha kesho.`
        );
      }

      // Trial grace period expired (2 days after trial end)
      if (student.Status === 'Trial' && student.Trial_Status !== 'Paid') {
        const trialEnd = new Date(student.Trial_End_Date);
        const graceEnd = new Date(trialEnd);
        graceEnd.setDate(graceEnd.getDate() + 2);
        if (new Date() > graceEnd) {
          await updateStudent(student.id, { Status: 'Paused', Trial_Status: 'Trial_Expired' });
          await send(student.Student_Phone,
            `😔 ${student.Student_Name}, JIBU imesimamishwa kwa sababu ya malipo. Lipa TZS 5,000 kuendelea. Streak yako ya siku ${student.Current_Streak} inakusubiri! 💪`
          );
        }
      }

      // Payment renewal reminder (3 days before)
      if (student.Status === 'Active' && student.Next_Payment_Date) {
        const nextPayDate = new Date(student.Next_Payment_Date);
        const reminderDate = new Date(nextPayDate);
        reminderDate.setDate(reminderDate.getDate() - 3);
        if (new Date().toISOString().split('T')[0] === reminderDate.toISOString().split('T')[0]) {
          const payLink = await createPaymentLink(student.Student_Phone, 5000, `JIBU renewal - ${student.Student_Name}`);
          await send(student.Student_Phone,
            `🔔 ${student.Student_Name}, usahau! Usajili wa JIBU unakwisha tarehe ${student.Next_Payment_Date}. Lipa TZS 5,000: ${payLink}`
          );
        }
      }

      // Pause if overdue
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
