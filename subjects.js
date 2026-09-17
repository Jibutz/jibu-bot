'use strict';

// O-Level (Form 1-4) individual subjects offered at enrollment and via SUBJECTS.
const O_LEVEL_SUBJECTS = ['Maths', 'Biology', 'Chemistry', 'Physics', 'English', 'Geography', 'History', 'Kiswahili'];

// A-Level (Form 5-6) combinations — each maps to the individual subjects a
// student in that combination studies. Downstream code (daily questions,
// topic history, etc.) always works with these individual subject names,
// never the combination code itself. Matches the combination descriptions
// used in claude.js's NECTA system prompt.
const A_LEVEL_COMBINATIONS = {
  PCM: ['Physics', 'Chemistry', 'Maths'],
  PCB: ['Physics', 'Chemistry', 'Biology'],
  CBG: ['Chemistry', 'Biology', 'Geography'],
  HGL: ['History', 'Geography', 'Literature'],
  HGE: ['History', 'Geography', 'Economics'],
  HGK: ['History', 'Geography', 'Kiswahili'],
  ECA: ['Economics', 'Commerce', 'Accountancy'],
  EGM: ['Economics', 'Geography', 'Maths'],
  HKL: ['History', 'Kiswahili', 'Literature'],
};

const A_LEVEL_MENU = Object.entries(A_LEVEL_COMBINATIONS)
  .map(([code, subjects]) => `${code} (${subjects.join(', ')})`)
  .join('\n');

function isALevelForm(form) {
  return form === '5' || form === '6';
}

function parseOLevelSubjects(input) {
  const normalized = (input || '').toLowerCase();
  return O_LEVEL_SUBJECTS.filter(s => normalized.includes(s.toLowerCase()));
}

/**
 * Match an A-Level combination code (e.g. "PCM", case-insensitive, anywhere
 * in the message) and return { code, subjects }, or null if none match.
 */
function parseALevelCombination(input) {
  const normalized = (input || '').toUpperCase();
  const code = Object.keys(A_LEVEL_COMBINATIONS).find(c => normalized.includes(c));
  return code ? { code, subjects: A_LEVEL_COMBINATIONS[code] } : null;
}

module.exports = {
  O_LEVEL_SUBJECTS,
  A_LEVEL_COMBINATIONS,
  A_LEVEL_MENU,
  isALevelForm,
  parseOLevelSubjects,
  parseALevelCombination,
};
