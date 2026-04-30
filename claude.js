const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Generate a NECTA-style multiple choice question for a student
 * Returns { question: string, answer: string }
 */
async function generateQuestion(student) {
  const formLevel = student.Form_level || '4';
  const weakTopics = student.Weak_Topics || '';
  const subjects = student.Subjects || student.Subject || 'Mathematics';

  const systemPrompt = `You are JIBU, a Tanzanian NECTA exam tutor. Generate 1 multiple choice question for a Form ${formLevel} student studying ${subjects}. ${weakTopics ? `Focus on their weak topic: ${weakTopics}.` : 'Choose a topic randomly from their subjects.'} 

Format your response EXACTLY like this:
[Question text here]
A) [option]
B) [option]
C) [option]
D) [option]
ANSWER: [single letter A, B, C, or D]

Style must match real NECTA past papers. Teach in English. Include one short Swahili encouragement phrase at the start (e.g., "Jaribu bidii! -"). Keep the question clear and exam-appropriate.`;

  try {
    const response = await client.messages.create({
      model: 'claude-opus-4-5',
      max_tokens: 400,
      messages: [{ role: 'user', content: 'Generate a question now.' }],
      system: systemPrompt,
    });

    const text = response.content[0].text.trim();
    const lines = text.split('\n');
    const answerLine = lines.find(l => l.startsWith('ANSWER:'));
    const answer = answerLine ? answerLine.replace('ANSWER:', '').trim().toUpperCase().charAt(0) : 'A';
    const questionBlock = lines.filter(l => !l.startsWith('ANSWER:')).join('\n').trim();

    return { question: questionBlock, answer };
  } catch (err) {
    console.error('Claude generateQuestion error:', err);
    // Fallback question
    return {
      question: `Jaribu bidii!\n\nWhich of the following is correct?\nA) Option A\nB) Option B\nC) Option C\nD) Option D`,
      answer: 'A',
    };
  }
}

/**
 * Generate personalised feedback after student answers
 */
async function generateFeedback(studentName, isCorrect, studentAnswer, correctAnswer, subjects, formLevel) {
  const systemPrompt = `You are JIBU, a warm and encouraging Tanzanian AI tutor. The student just answered a ${subjects} question for Form ${formLevel}. 
${isCorrect
  ? `They answered correctly (${studentAnswer}). Give a short, enthusiastic congratulatory message in English. Include one Swahili celebration phrase. Briefly explain WHY the answer is correct in 1-2 sentences. Keep total response under 200 characters.`
  : `They answered ${studentAnswer} but the correct answer was ${correctAnswer}. Give a kind, encouraging message in English. Include one Swahili encouragement phrase. Briefly explain the correct answer in 1-2 sentences. Keep total response under 200 characters.`}
Start with the student's name ${studentName}.`;

  try {
    const response = await client.messages.create({
      model: 'claude-opus-4-5',
      max_tokens: 200,
      messages: [{ role: 'user', content: 'Generate feedback now.' }],
      system: systemPrompt,
    });
    return response.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateFeedback error:', err);
    if (isCorrect) {
      return `✅ Vizuri sana ${studentName}! Jibu sahihi ni ${correctAnswer}. Hongera! Endelea hivyo! 🌟`;
    } else {
      return `💪 Pole ${studentName}. Jibu sahihi lilikuwa ${correctAnswer}. Jaribu tena kesho! Usikate tamaa!`;
    }
  }
}

/**
 * Generate weekly parent report
 */
async function generateParentReport(student) {
  const systemPrompt = `You are JIBU, a Tanzanian AI education platform. Write a brief, warm weekly progress report for a parent about their child. 

Child's name: ${student.Student_Name}
Form: ${student.Form_level}
Subjects: ${student.Subjects || student.Subject}
Current streak: ${student.Current_Streak || 0} days
Longest streak: ${student.Longest_Streak || 0} days
Total points: ${student.Total_Points || 0}
Rank: ${student.Rank_Title || 'Mwanafunzi'}
Strong topics: ${student.Strong_Topics || 'Still being assessed'}
Weak topics: ${student.Weak_Topics || 'Still being assessed'}
Days until NECTA: ${student.Days_Until_Exam || 'Not set'}

Write in English. Start with a warm Swahili greeting (Habari za familia!). Keep it to 3-4 sentences. Be encouraging and specific. End with a Swahili motivational phrase. Keep total under 300 characters.`;

  try {
    const response = await client.messages.create({
      model: 'claude-opus-4-5',
      max_tokens: 300,
      messages: [{ role: 'user', content: 'Generate parent report.' }],
      system: systemPrompt,
    });
    return response.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateParentReport error:', err);
    return `Habari za familia! 📊 Weekly report for ${student.Student_Name}: Current streak ${student.Current_Streak || 0} days, Total points: ${student.Total_Points || 0}. Rank: ${student.Rank_Title || 'Mwanafunzi'}. Mungu awabariki! 🙏`;
  }
}

module.exports = { generateQuestion, generateFeedback, generateParentReport };
