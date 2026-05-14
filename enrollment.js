const { getStudentByPhone, createStudent, updateStudent } = require('./airtable');
const { sendWhatsApp } = require('./whatsapp');
const { sendSMS } = require('./sms');
const { t } = require('./lang');

const SUBJECTS = ['Maths', 'Biology', 'Chemistry', 'Physics', 'English', 'Geography', 'History'];
const VALID_FORMS = ['1', '2', '3', '4', '5', '6'];

async function enrollmentFlow(phone, message, student, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const normalizedPhone = phone.replace(/^\+/, '');
  const msg = message.trim();

  // ── Brand new contact: create record at step 0 and ask role ──────────────
  if (!student) {
    await createStudent({
      phone: normalizedPhone,
      name: '',
      enrollmentStep: 0,
      channel,
      extra: { Status: 'Enrolling' },
    });
    await send(phone,
      `Karibu JIBU! 🎓\n\nMimi ni mwalimu wako wa AI atakayekusaidia kufaulu mitihani ya NECTA! 🇹🇿\n\nHere is what we will do together:\n📚 Every day I send you real exam questions for your subjects\n✅ You answer A, B, C or D\n🏆 You earn points, build streaks and climb the ranks\n📈 The more you practice, the better your NECTA results!\n\n7 days FREE — no payment needed to start!\n\nSo let's go — are you a student or parent?\nReply *1* for Mwanafunzi 👨‍🎓\nReply *2* for Mzazi 👨‍👩‍👧`
    );
    return;
  }

  if (!student.id) {
    await send(phone, t(student,
      `Oops, something went wrong! 😬 Please text again to restart.`,
      `Samahani, kuna hitilafu! Tuma ujumbe tena tuanze upya. 🙏`
    ));
    return;
  }

  const step = parseInt(student.Enrollment_Step) || 0;

  switch (step) {

    // ── Step 0: student or parent? ──────────────────────────────────────────
    case 0: {
      if (msg === '1') {
        await updateStudent(student.id, { Enrollment_Step: 1 });
        await send(phone, t(student,
          `Sawa! 🎓 Student mode — let's go!\n\nWhat's your full name?`,
          `Sawa! 🎓 Mwanafunzi wenyewe!\n\nJina lako kamili ni nani? ✍️`
        ));
      } else if (msg === '2') {
        await updateStudent(student.id, { Enrollment_Step: 11 });
        await send(phone, t(student,
          `Asante, mzazi! 🙌 Amazing that you're investing in your child's future!\n\nWhat's your child's full name? ✍️`,
          `Asante mzazi! 🙌 Tunashukuru sana unayofanya kwa mtoto wako!\n\nJina kamili la mtoto ni nani? ✍️`
        ));
      } else {
        await send(phone, t(student,
          `Just reply 1 (Student) or 2 (Parent) — nothing else! 😄`,
          `Jibu kwa 1 au 2 tu bro! 😄\n\n1️⃣ - Mwanafunzi\n2️⃣ - Mzazi`
        ));
      }
      break;
    }

    // ── Step 1: student entered their own name ──────────────────────────────
    case 1: {
      const name = capitalizeWords(msg);
      await updateStudent(student.id, { Student_Name: name, Enrollment_Step: 2 });
      await send(phone, t(student,
        `Nice to meet you, ${name}! 🤝🔥\n\nWhat Form are you in? Reply with just the number:\n\n1 · 2 · 3 · 4 · 5 · 6`,
        `Karibu sana, ${name}! 🤝🔥\n\nUko kidato gani sasa hivi? Jibu kwa namba tu:\n\n1 · 2 · 3 · 4 · 5 · 6`
      ));
      break;
    }

    // ── Step 11: parent entered child's name ────────────────────────────────
    case 11: {
      const name = capitalizeWords(msg);
      await updateStudent(student.id, { Student_Name: name, Enrollment_Step: 2 });
      await send(phone, t(student,
        `Great name! 💪 ${name} is going to ace NECTA!\n\nWhat Form is ${name} in? Reply with the number:\n\n1 · 2 · 3 · 4 · 5 · 6`,
        `Jina zuri kabisa! 💪 ${name} atafaulu NECTA hakika!\n\n${name} yuko kidato gani? Jibu kwa namba:\n\n1 · 2 · 3 · 4 · 5 · 6`
      ));
      break;
    }

    // ── Step 2: form level ──────────────────────────────────────────────────
    case 2: {
      const form = msg;
      if (!VALID_FORMS.includes(form)) {
        await send(phone, t(student,
          `That's not a valid Form! 😅 Reply with a number between 1 and 6 — which Form is ${student.Student_Name} in?`,
          `Hiyo sio sahihi! 😅 Jibu kwa namba 1 hadi 6 tu — ${student.Student_Name} yuko kidato gani?`
        ));
        return;
      }
      await updateStudent(student.id, { Form_level: form, Enrollment_Step: 3 });
      await send(phone, t(student,
        `Form ${form} — let's go! 📚\n\nWhich subjects does ${student.Student_Name} study? Pick from the list:\n\nMaths · Biology · Chemistry · Physics · English · Geography · History\n\nExample: Maths, Biology, Chemistry`,
        `Kidato cha ${form} — sawa kabisa! 📚\n\n${student.Student_Name} anasoma masomo gani? Chagua hapa:\n\nMaths · Biology · Chemistry · Physics · English · Geography · History\n\nMfano: Maths, Biology, Chemistry`
      ));
      break;
    }

    // ── Step 3: subjects ────────────────────────────────────────────────────
    case 3: {
      const parsedSubjects = parseSubjects(msg);
      if (!parsedSubjects.length) {
        await send(phone, t(student,
          `I couldn't match those subjects! 🤔 Try again using names from this list:\n\nMaths · Biology · Chemistry · Physics · English · Geography · History`,
          `Sijapata masomo hayo! 🤔 Jaribu tena kwa majina haya:\n\nMaths · Biology · Chemistry · Physics · English · Geography · History`
        ));
        return;
      }
      await updateStudent(student.id, { Subjects: parsedSubjects.join(', '), Enrollment_Step: 4 });
      await send(phone, t(student,
        `Poa! ✅ ${parsedSubjects.join(', ')}\n\nAlmost done! What's the parent's M-Pesa number for billing?\n\nExample: 0712345678`,
        `Sawa fiti! ✅ ${parsedSubjects.join(', ')}\n\nKaribu mwisho! Nambari ya M-Pesa ya mzazi kwa malipo:\n\nMfano: 0712345678`
      ));
      break;
    }

    // ── Step 4: parent M-Pesa number ───────────────────────────────────────
    case 4: {
      const parentPhone = formatTanzanianPhone(msg);
      if (!parentPhone) {
        await send(phone, t(student,
          `That number doesn't look right! 😬 Send a valid Tanzania number:\n\nExample: 0712345678 or 255712345678`,
          `Nambari hiyo haifanyi kazi! 😬 Tuma nambari ya Tanzania:\n\nMfano: 0712345678 au 255712345678`
        ));
        return;
      }
      const trialEnd = new Date();
      trialEnd.setDate(trialEnd.getDate() + 7);
      const trialEndDate = trialEnd.toISOString().split('T')[0];
      await updateStudent(student.id, {
        Parent_Phone: parentPhone,
        Trial_End_Date: trialEndDate,
        Trial_Status: 'Active',
        Status: 'Trial',
        Enrollment_Step: 5,
      });
      await send(phone, t(student,
        `🎉 You're officially IN! Welcome to JIBU, ${student.Student_Name}!\n\n📅 First question drops at 4:00 PM today!\n💸 7 days free — bure kabisa!\n🏆 Answer daily → earn points → climb the ranks!\n\nTrial ends: ${formatDate(trialEndDate)}\n\nLet's ace that NECTA! 📚🇹🇿🔥`,
        `🎉 Umefanikiwa! Karibu JIBU, ${student.Student_Name}!\n\n📅 Swali la kwanza linakuja saa 10 jioni leo!\n💸 Siku 7 bure kabisa!\n🏆 Jibu kila siku → pata pointi → panda rank!\n\nTrial inaisha: ${formatDate(trialEndDate)}\n\nTunaenda! Fuzu NECTA! 📚🇹🇿🔥`
      ));
      break;
    }

    default:
      await send(phone, t(student,
        `Welcome back to JIBU! 📚 Your daily question arrives at 4:00 PM. 🔥`,
        `Karibu tena JIBU! 📚 Swali lako linakuja saa 10 jioni. 🔥`
      ));
  }
}

function capitalizeWords(str) {
  return str.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
}

function parseSubjects(input) {
  const normalized = input.toLowerCase();
  return SUBJECTS.filter(s => normalized.includes(s.toLowerCase()));
}

function formatTanzanianPhone(phone) {
  const cleaned = phone.replace(/[\s\-]/g, '');
  if (/^255[67]\d{8}$/.test(cleaned)) return cleaned;
  if (/^0[67]\d{8}$/.test(cleaned)) return '255' + cleaned.slice(1);
  if (/^\+255[67]\d{8}$/.test(cleaned)) return cleaned.slice(1);
  return null;
}

function formatDate(dateStr) {
  const d = new Date(dateStr);
  return d.toLocaleDateString('sw-TZ', { year: 'numeric', month: 'long', day: 'numeric' });
}

module.exports = { enrollmentFlow };
