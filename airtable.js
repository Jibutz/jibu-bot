const Airtable = require('airtable');

const TABLE = 'Students';

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

module.exports = {
  base,
  TABLE,
  getStudentByPhone,
  createStudent,
  updateStudent,
  getAllActiveStudents,
  getStudentByIndexNumber,
};
