const Airtable = require('airtable');

const base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(process.env.AIRTABLE_BASE_ID);
const TABLE = 'Students';

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
    console.error('Airtable getStudentByPhone error:', err);
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
      Current_Streak: 0,
      Longest_Streak: 0,
      Total_Points: 0,
      Rank_Title: 'Mwanafunzi',
      Freeze_Credits: 0,
      Weak_Topics: '',
      Strong_Topics: '',
      Todays_Correct_Answer: '',
      Status: 'Trial',
      Trial_Status: 'Active',
      Trial_End_Date: data.trialEndDate || '',
      Channel: data.channel || 'whatsapp',
      School_Name: data.school || '',
      Enrollment_Step: data.enrollmentStep || 1,
      ...data.extra,
    });
    return { id: record.id, ...record.fields };
  } catch (err) {
    console.error('Airtable createStudent error:', err);
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
    console.error('Airtable updateStudent error:', err);
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
    console.error('Airtable getAllActiveStudents error:', err);
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
    console.error('Airtable getStudentByIndexNumber error:', err);
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
