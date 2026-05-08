const { getStudentByPhone, createStudent, updateStudent } = require('./airtable');
const { sendWhatsApp } = require('./whatsapp');
const { sendSMS } = require('./sms');

/**
 * Multi-step enrollment flow for new students
 * Steps:
 * 1 → Ask for child's name
 * 2 → Ask for Form level (1-6)
 * 3 → Ask for subjects
 * 4 → Ask for parent's M-Pesa number
 * 5 → Confirm and activate trial
 */

const SUBJECTS = ['Maths', 'Biology', 'Chemistry', 'Physics', 'English', 'Geography', 'History'];
const VALID_FORMS = ['1', '2', '3', '4', '5', '6'];

async function enrollmentFlow(phone, message, student, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const normalizedPhone = phone.replace(/^\+/, '');

  // No student record — brand new user, send welcome
  if (!student) {
    await createStudent({
      phone: normalizedPhone,
      name: '',
      enrollmentStep: 1,
      channel,
      extra: { Status: 'Enrolling' },
    });

    await send(phone,
      `🌟 Karibu JIBU — Tanzania's AI tutor!\nWelcome to JIBU — Tanzania's AI tutor.\n\nNina swali moja. / I have one question.\nJina la mtoto wako ni nani? / What is your child's name?`
    );
    return;
  }

  const step = parseInt(student.Enrollment_Step) || 1;

<<<<<<< HEAD
=======
  if (!student.id) {
    await send(phone, `Samahani, kuna tatizo. Tuma ujumbe tena. / Sorry, please text again.`);
    return;
  }

>>>>>>> 19be898bc5861f922a57882ba0af3f25d0f0787f
  switch (step) {
    case 1: {
      // Received: child's name
      const name = capitalizeWords(message.trim());
      await updateStudent(student.id, {
        Student_Name: name,
        Enrollment_Step: 2,
      });
      await send(phone,
        `Vizuri! / Great! ${name} yuko katika Kidato gani? / Which Form is ${name} in?\n\nJibu: 1, 2, 3, 4, 5 au 6`
      );
      break;
    }

    case 2: {
      // Received: form level
      const form = message.trim();
      if (!VALID_FORMS.includes(form)) {
        await send(phone, `Tafadhali jibu kwa namba 1-6. / Please reply with a number 1-6.\n\n${student.Student_Name} yuko kidato gani? (1, 2, 3, 4, 5 au 6)`);
        return;
      }
      await updateStudent(student.id, {
        Form_level: form,
        Enrollment_Step: 3,
      });
      await send(phone,
        `Vizuri! Kidato cha ${form}. 📚\n\n${student.Student_Name} anasoma masomo gani? / Which subjects?\n\nChagua: Maths, Biology, Chemistry, Physics, English, Geography, History\n\nMfano: Maths, Biology, Chemistry`
      );
      break;
    }

    case 3: {
      // Received: subjects
      const rawSubjects = message.trim();
      const parsedSubjects = parseSubjects(rawSubjects);

      if (!parsedSubjects.length) {
        await send(phone,
          `Masomo hayakueleweka. Tafadhali chagua kutoka: Maths, Biology, Chemistry, Physics, English, Geography, History\n\nMfano tuma: Maths, Biology`
        );
        return;
      }

      await updateStudent(student.id, {
        Subjects: parsedSubjects.join(', '),
        Subject: parsedSubjects[0],
        Enrollment_Step: 4,
      });
      await send(phone,
        `Masomo: ${parsedSubjects.join(', ')} ✅\n\nNambari ya M-Pesa ya mzazi / Parent's M-Pesa number?\n\nMfano: 0712345678`
      );
      break;
    }

    case 4: {
      // Received: parent M-Pesa number
      const parentPhone = formatTanzanianPhone(message.trim());

      if (!parentPhone) {
        await send(phone,
          `Nambari haikueleweka. Tafadhali tuma nambari ya Tanzania (0712345678 au 255712345678)`
        );
        return;
      }

      // Calculate trial end date (today + 7 days)
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
        `🎉 Karibu JIBU ${student.Student_Name}!\n\nMaswali ya kwanza yanakuja leo saa 10 jioni (4:00 PM).\n\nHakuna malipo kwa siku 7! 🆓\n\nTrail inaisha: ${formatDate(trialEndDate)}\n\nJifunze, fanya mazoezi, fuzu NECTA! 📚🇹🇿`
      );
      break;
    }

    default:
      await send(phone, `Karibu JIBU! 📚 Subiri swali la leo saa 10 jioni.`);
  }
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function capitalizeWords(str) {
  return str.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
}

function parseSubjects(input) {
  // Try to match known subjects from the input
  const normalized = input.toLowerCase();
  return SUBJECTS.filter(s => normalized.includes(s.toLowerCase()));
}

function formatTanzanianPhone(phone) {
  // Remove spaces and hyphens
  const cleaned = phone.replace(/[\s\-]/g, '');

  // Already in 255 format
  if (/^255[67]\d{8}$/.test(cleaned)) return cleaned;

  // In 0XX format — convert to 255
  if (/^0[67]\d{8}$/.test(cleaned)) return '255' + cleaned.slice(1);

  // In +255 format
  if (/^\+255[67]\d{8}$/.test(cleaned)) return cleaned.slice(1);

  return null;
}

function formatDate(dateStr) {
  const d = new Date(dateStr);
  return d.toLocaleDateString('sw-TZ', { year: 'numeric', month: 'long', day: 'numeric' });
}

module.exports = { enrollmentFlow };
