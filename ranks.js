/**
 * Rank titles based on streak days
 */
const RANKS = [
  { days: 180, title: 'Daktari Msomi' },
  { days: 90, title: 'Msomi wa Heshima' },
  { days: 60, title: 'Msomi Mkuu' },
  { days: 30, title: 'Msomi Bora' },
  { days: 14, title: 'Msomi' },
  { days: 7, title: 'Msomi Mdogo' },
  { days: 0, title: 'Mwanafunzi' },
];

const MILESTONES = [7, 14, 30, 60, 90, 180];

/**
 * Get rank title based on current streak
 */
function getRankTitle(streak) {
  const days = parseInt(streak) || 0;
  const rank = RANKS.find(r => days >= r.days);
  return rank ? rank.title : 'Mwanafunzi';
}

/**
 * Check if a streak count is a milestone
 */
function checkMilestone(streak) {
  return MILESTONES.includes(parseInt(streak));
}

/**
 * Get milestone celebration message
 */
function getMilestoneMessage(name, streak, rank) {
  const messages = {
    7: `🏆 HONGERA ${name}! Wiki moja kamili — Msomi Mdogo! 7 days. Most students quit in 3. Cheo chako kipya: Msomi Mdogo. 🌟 Share: "Nimefika siku 7 za JIBU! Jiunge: wa.me/255${process.env.WHATSAPP_NUMBER || '255700000000'}"`,

    14: `🎉 SIKU 14 ${name}! Msomi! Wiki mbili za bidii. Wengine wanaacha siku ya 5 — wewe uko siku 14! Cheo: Msomi. Endelea! 💪`,

    30: `🌟 MWEZI MMOJA ${name}! Msomi Bora. 90% of students give up here. You didn't. Mama/Baba amepata ripoti yako. Hongera sana! 🎊`,

    60: `🔥 SIKU 60 ${name}! Msomi Mkuu! Miezi miwili ya nidhamu. Jua linachomoza kwa wanaodumu. Wewe ni mmoja wao! ⭐`,

    90: `🏅 SIKU 90 ${name}. Msomi wa Heshima. Three months of discipline. Matokeo yatasema yote. Tanzania inajivunia wewe! 🇹🇿`,

    180: `👑 ${name}. Daktari Msomi. 180 days. Every single day. Hakuna zaidi ya kusema. Uko tayari kwa NECTA. Asante kwa bidii yako. 🎓`,
  };

  return messages[parseInt(streak)] || `🎉 HONGERA ${name}! Streak ya siku ${streak}! Cheo chako: ${rank}. Endelea! 💪`;
}

module.exports = { getRankTitle, checkMilestone, getMilestoneMessage, RANKS, MILESTONES };
