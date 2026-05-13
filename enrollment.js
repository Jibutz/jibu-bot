const { getStudentByPhone, createStudent, updateStudent } = require('./airtable');
const { sendWhatsApp } = require('./whatsapp');
const { sendSMS } = require('./sms');

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
      `🔥 Sasa sasa! Karibu JIBU — tutor wa AI wa Tanzania!\n\nKabla hatujaanza, niambie — wewe ni nani? 👇\n\n1️⃣ - Mwanafunzi (Student)\n2️⃣ - Mzazi (Parent)\n\nJibu kwa 1 au 2 tu!`
    );
    return;
  }

  if (!student.id) {
    await send(phone, `Ai samahani! Kuna hitilafu kidogo. Tuma ujumbe tena tuanze upya. 🙏`);
    return;
  }

  const step = parseInt(student.Enrollment_Step) || 0;

  switch (step) {

    // ── Step 0: student or parent? ──────────────────────────────────────────
    case 0: {
      if (msg === '1') {
        await updateStudent(student.id, { Enrollment_Step: 1 });
        await send(phone,
          `Poa sana! 🎓 Mwanafunzi wenyewe!\n\nJina lako kamili ni nani? Niambie nikuandikishe vizuri! ✍️`
        );
      } else if (msg === '2') {
        await updateStudent(student.id, { Enrollment_Step: 11 });
        await send(phone,
          `Asante mzazi! 🙌 Tunashukuru sana unayefanya kwa mtoto wako!\n\nJina kamili la mtoto ni nani? ✍️`
        );
      } else {
        await send(phone,
          `Jibu kwa 1 au 2 tu bro! 😄\n\n1️⃣ - Mwanafunzi\n2️⃣ - Mzazi`
        );
      }
      break;
    }

    // ── Step 1: student entered their own name ──────────────────────────────
    case 1: {
      const name = capitalizeWords(msg);
      await updateStudent(student.id, { Student_Name: name, Enrollment_Step: 2 });
      await send(phone,
        `Nice to meet you ${name}! 🤝🔥\n\nSasa — uko kidato gani? Jibu kwa namba tu:\n\n1 · 2 · 3 · 4 · 5 · 6`
      );
      break;
    }

    // ── Step 11: parent entered child's name ────────────────────────────────
    case 11: {
      const name = capitalizeWords(msg);
      await updateStudent(student.id, { Student_Name: name, Enrollment_Step: 2 });
      await send(phone,
        `Bomba! ${name} — jina zuri kabisa! 💪\n\n${name} yuko kidato gani sasa hivi? Jibu kwa namba:\n\n1 · 2 · 3 · 4 · 5 · 6`
      );
      break;
    }

    // ── Step 2: form level ──────────────────────────────────────────────────
    case 2: {
      const form = msg;
      if (!VALID_FORMS.includes(form)) {
        await send(phone,
          `Ebu jibu kwa namba 1 hadi 6 tu! 😅\n\n${student.Student_Name} yuko kidato gani? (1, 2, 3, 4, 5 au 6)`
        );
        return;
      }
      await updateStudent(student.id, { Form_level: form, Enrollment_Step: 3 });
      await send(phone,
        `Sawa kabisa! Kidato cha ${form} 📚🔥\n\nSasa — ${student.Student_Name} anasoma masomo gani?\n\nChagua kutoka hapa:\nMaths · Biology · Chemistry · Physics · English · Geography · History\n\nMfano tuma: Maths, Biology, Chemistry`
      );
      break;
    }

    // ── Step 3: subjects ────────────────────────────────────────────────────
    case 3: {
      const parsedSubjects = parseSubjects(msg);
      if (!parsedSubjects.length) {
        await send(phone,
          `Sijapata masomo! Tuma majina kama yalivyo hapa 👇\n\nMaths · Biology · Chemistry · Physics · English · Geography · History\n\nMfano: Maths, Biology`
        );
        return;
      }
      await updateStudent(student.id, { Subjects: parsedSubjects.join(', '), Enrollment_Step: 4 });
      await send(phone,
        `Sawa fiti! ✅ ${parsedSubjects.join(', ')}\n\nMoja ya mwisho — nambari ya M-Pesa ya mzazi kwa malipo baadaye:\n\nMfano: 0712345678`
      );
      break;
    }

    // ── Step 4: parent M-Pesa number ───────────────────────────────────────
    case 4: {
      const parentPhone = formatTanzanianPhone(msg);
      if (!parentPhone) {
        await send(phone,
          `Nambari hiyo haifanyi kazi! 😬 Tuma nambari ya Tanzania tu:\n\nMfano: 0712345678 au 255712345678`
        );
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
      await send(phone,
        `🎉🎉 IMEFANIKIWA! Karibu JIBU, ${student.Student_Name}!\n\n📅 Maswali ya kwanza yanakuja SAA 10 JIONI (4:00 PM) leo!\n💸 Hakuna malipo kwa siku 7 — bure kabisa!\n🏆 Jibu vizuri, pata pointi, panda rank!\n\nTrial inaisha: ${formatDate(trialEndDate)}\n\nSawa, tunaanza safari! Fuzu NECTA, tupo pamoja! 📚🇹🇿🔥`
      );
      break;
    }

    default:
      await send(phone, `Karibu tena JIBU! 📚 Subiri swali la leo saa 10 jioni. 🔥`);
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
