/**
 * Returns enMsg normally (80% English), or swMsg when student
 * has set their preference to 'sw' (50% Swahili mode).
 */
function t(student, enMsg, swMsg) {
  return (student && student.Language_Pref === 'sw') ? swMsg : enMsg;
}

module.exports = { t };
