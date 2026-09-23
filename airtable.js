const Airtable = require('airtable');

const TABLE = 'Students';
const QUESTIONS_TABLE = 'CSEE_Questions';
const ACSEE_QUESTIONS_TABLE = 'ACSEE_Questions';

// Lazily construct the Airtable base on first use instead of at require-time,
// so the process can boot (e.g. to serve the health-check route) even when
// AIRTABLE_API_KEY / AIRTABLE_BASE_ID aren't set locally.
let _base = null;
function base(table) {
  if (!_base) {
    if (!process.env.AIRTABLE_API_KEY || !process.env.AIRTABLE_BASE_ID) {
      throw new Error('Airtable is not configured — set AIRTABLE_API_KEY and AIRTABLE_BASE_ID.');
    }
    try {
      _base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(process.env.AIRTABLE_BASE_ID);
    } catch (err) {
      console.error('Airtable base() construction error:', err.message || err);
      throw err;
    }
  }
  return _base(table);
}

/**
 * Log an Airtable error with as much detail as the SDK gives us
 * (HTTP status, Airtable error type, and which call failed).
 */
function logAirtableError(context, err) {
  console.error(
    `Airtable ${context} error: status=${err.statusCode ?? 'n/a'} type=${err.error ?? 'n/a'} message=${err.message ?? err}`
  );
}

/**
 * Normalize a phone number to a consistent format (no + prefix)
 */
function normalizePhone(phone) {
  return phone.replace(/^\+/, '').trim();
}

/**
 * Get a student record by phone number
 */
async function getStudentByPhone(phone) {
  const normalized = normalizePhone(phone);
  try {
    const records = await base(TABLE).select({
      filterByFormula: `OR(SUBSTITUTE({Student_Phone}, "+", "") = "${normalized}", {Student_Phone} = "+${normalized}", {Student_Phone} = "${normalized}")`,
      maxRecords: 1,
    }).firstPage();

    if (!records.length) return null;
    return { id: records[0].id, ...records[0].fields };
  } catch (err) {
    logAirtableError(`getStudentByPhone(phone=${normalized})`, err);
    return null;
  }
}

/**
 * Create a new student record
 */
async function createStudent(data) {
  try {
    const record = await base(TABLE).create({
      Student_Name: data.name || '',
      Student_Phone: normalizePhone(data.phone || ''),
      Parent_Phone: data.parentPhone || '',
      Form_level: data.form || '',
      Subjects: data.subjects || '',
      Current_Streak: Number(0),
      Longest_Streak: Number(0),
      Total_Points: Number(0),
      Rank_Title: 'Mwanafunzi',
      Freeze_Credits: Number(0),
      Weak_Topics: '',
      Strong_Topics: '',
      Todays_Correct_Answer: '',
      Status: 'Trial',
      Trial_Status: 'Active',
      Trial_End_Date: data.trialEndDate || null,
      Channel: data.channel || 'whatsapp',
      School_Name: data.school || '',
      Enrollment_Step: data.enrollmentStep || 1,
      ...data.extra,
    });
    return { id: record.id, ...record.fields };
  } catch (err) {
    logAirtableError(`createStudent(phone=${data.phone})`, err);
    throw err;
  }
}

/**
 * Update a student record by Airtable record ID
 */
async function updateStudent(recordId, fields) {
  try {
    const record = await base(TABLE).update(recordId, fields);
    return { id: record.id, ...record.fields };
  } catch (err) {
    logAirtableError(`updateStudent(recordId=${recordId})`, err);
    throw err;
  }
}

/**
 * Get all active students (Status = Active or Trial)
 * Optionally filter by specific statuses
 */
async function getAllActiveStudents(statuses = ['Active', 'Trial']) {
  try {
    const filterParts = statuses.map(s => `{Status} = "${s}"`);
    const formula = filterParts.length > 1 ? `OR(${filterParts.join(',')})` : filterParts[0];

    const records = await base(TABLE).select({
      filterByFormula: formula,
    }).all();

    return records.map(r => ({ id: r.id, ...r.fields }));
  } catch (err) {
    logAirtableError(`getAllActiveStudents(statuses=${statuses.join(',')})`, err);
    return [];
  }
}

/**
 * Find students by NECTA index number
 */
async function getStudentByIndexNumber(indexNumber) {
  try {
    const records = await base(TABLE).select({
      filterByFormula: `{Index_Number} = "${indexNumber}"`,
      maxRecords: 1,
    }).firstPage();
    if (!records.length) return null;
    return { id: records[0].id, ...records[0].fields };
  } catch (err) {
    logAirtableError(`getStudentByIndexNumber(indexNumber=${indexNumber})`, err);
    return null;
  }
}

/**
 * Fetch every Question record for a subject + form level.
 * Form_Level in the CSEE_Questions table is stored as "Form 4", "Form 3", etc.,
 * while callers pass the bare Students.Form_level value ("4") - normalize here.
 */
async function getQuestionsForSubject(subject, formLevel) {
  const formLabel = /^form/i.test(String(formLevel).trim())
    ? String(formLevel).trim()
    : `Form ${formLevel}`;
  try {
    const records = await base(QUESTIONS_TABLE).select({
      filterByFormula: `AND({Subject} = "${subject}", {Form_Level} = "${formLabel}")`,
    }).all();
    return records.map(r => ({ id: r.id, ...r.fields }));
  } catch (err) {
    logAirtableError(`getQuestionsForSubject(subject=${subject}, formLevel=${formLevel})`, err);
    return [];
  }
}

/**
 * Pull a random not-yet-seen question for a student from the CSEE_Questions
 * table, tracking what they've seen per subject in Students.Seen_Question_IDs
 * (a JSON blob: { "Biology": ["recXXX", ...], "Chemistry": [...] }).
 *
 * Returns the same shape as claude.generateQuestion() (questionBody, optionA-D,
 * answer, topic, examTip) plus optionE, explanation, and questionId, so a
 * caller can do `parsed = await getRandomQuestion(...) || await generateQuestion(...)`.
 *
 * Returns null when the student has no student record, the CSEE_Questions
 * table has nothing for this subject/form, or every matching question has already
 * been seen - in all of those cases the caller should fall back to AI
 * generation.
 */
async function getRandomQuestion(subject, formLevel, studentPhone) {
  const student = await getStudentByPhone(studentPhone);
  if (!student) {
    console.error(`getRandomQuestion: no student found for phone=${studentPhone}`);
    return null;
  }

  let seen = {};
  try {
    seen = JSON.parse(student.Seen_Question_IDs || '{}');
  } catch {
    seen = {};
  }
  const seenIds = seen[subject] || [];

  const questions = await getQuestionsForSubject(subject, formLevel);
  const available = questions.filter(q => !seenIds.includes(q.id));

  if (!available.length) {
    console.log(`getRandomQuestion: exhausted (${questions.length} total, ${seenIds.length} seen) for subject=${subject} formLevel=${formLevel} phone=${studentPhone}`);
    return null;
  }

  const pick = available[Math.floor(Math.random() * available.length)];

  try {
    seen[subject] = [...seenIds, pick.id];
    await updateStudent(student.id, { Seen_Question_IDs: JSON.stringify(seen) });
  } catch (err) {
    logAirtableError(`getRandomQuestion updateStudent(seen tracking, phone=${studentPhone})`, err);
    // Still return the question - failing to record it as seen just risks a
    // future repeat, which is far less bad than silently dropping the question.
  }

  return {
    questionBody: pick.Question || '',
    optionA: pick.Option_A || '',
    optionB: pick.Option_B || '',
    optionC: pick.Option_C || '',
    optionD: pick.Option_D || '',
    optionE: pick.Option_E || '',
    answer: pick.Correct_Answer || 'A',
    topic: pick.Topic || subject,
    explanation: pick.Explanation || '',
    examTip: '',
    questionId: pick.id,
  };
}

/**
 * Fetch every ACSEE_Questions record for a subject.
 *
 * Unlike getQuestionsForSubject (CSEE), this does NOT filter by Form_Level.
 * ACSEE past papers don't distinguish Form 5 vs Form 6 content - both years
 * of A-Level study toward the same national exam - so Form 5 and Form 6
 * students share one question pool per subject.
 */
async function getACSEEQuestionsForSubject(subject) {
  try {
    const records = await base(ACSEE_QUESTIONS_TABLE).select({
      filterByFormula: `{Subject} = "${subject}"`,
    }).all();
    return records.map(r => ({ id: r.id, ...r.fields }));
  } catch (err) {
    logAirtableError(`getACSEEQuestionsForSubject(subject=${subject})`, err);
    return [];
  }
}

/**
 * Pull a random not-yet-seen ACSEE (Form 5/6) question for a student from
 * ACSEE_Questions.
 *
 * Reuses the same Students.Seen_Question_IDs JSON blob that getRandomQuestion
 * uses (keyed by subject) rather than a separate field - safe to share
 * because Airtable record IDs are globally unique across the whole base,
 * and a student is never simultaneously O-Level and A-Level.
 *
 * Returns { questionBody, answerSummary, explanation, topic, questionId } -
 * deliberately NOT the MCQ shape getRandomQuestion returns (no option
 * letters, no answer field), since ACSEE questions are revealed as a
 * free-text model answer, never graded against a reply.
 *
 * Returns null when there's no student record, nothing in the table for
 * this subject yet, or the student has already seen everything available.
 */
async function getRandomACSEEQuestion(subject, studentPhone) {
  const student = await getStudentByPhone(studentPhone);
  if (!student) {
    console.error(`getRandomACSEEQuestion: no student found for phone=${studentPhone}`);
    return null;
  }

  let seen = {};
  try {
    seen = JSON.parse(student.Seen_Question_IDs || '{}');
  } catch {
    seen = {};
  }
  const seenIds = seen[subject] || [];

  const questions = await getACSEEQuestionsForSubject(subject);
  const available = questions.filter(q => !seenIds.includes(q.id));

  if (!available.length) {
    console.log(`getRandomACSEEQuestion: exhausted (${questions.length} total, ${seenIds.length} seen) for subject=${subject} phone=${studentPhone}`);
    return null;
  }

  const pick = available[Math.floor(Math.random() * available.length)];

  try {
    seen[subject] = [...seenIds, pick.id];
    await updateStudent(student.id, { Seen_Question_IDs: JSON.stringify(seen) });
  } catch (err) {
    logAirtableError(`getRandomACSEEQuestion updateStudent(seen tracking, phone=${studentPhone})`, err);
    // Still return the question - failing to record it as seen just risks a
    // future repeat, which is far less bad than silently dropping the question.
  }

  return {
    questionBody: pick.Question || '',
    answerSummary: pick.Answer_Summary || '',
    explanation: pick.Explanation || '',
    topic: pick.Topic || subject,
    questionId: pick.id,
  };
}

module.exports = {
  base,
  TABLE,
  ACSEE_QUESTIONS_TABLE,
  getStudentByPhone,
  createStudent,
  updateStudent,
  getAllActiveStudents,
  getStudentByIndexNumber,
  getQuestionsForSubject,
  getRandomQuestion,
  getACSEEQuestionsForSubject,
  getRandomACSEEQuestion,
};
