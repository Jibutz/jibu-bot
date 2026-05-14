const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Generate a NECTA-style multiple choice question for one specific subject.
 * Returns { questionBody: string, answer: string }
 * questionBody is just the question text + A/B/C/D options, no header/footer.
 */
async function generateQuestion(student, subject) {
  const formLevel = student.Form_level || '4';
  const weakTopics = student.Weak_Topics || '';

  const userPrompt = `Generate one real multiple choice exam question for a Tanzania Form ${formLevel} student studying ${subject}.${weakTopics ? ` Focus on this weak topic: ${weakTopics}.` : ''} The question must be specific, factual, and exam-ready like a real NECTA past paper question. Give 4 real answer options A, B, C, D — not placeholders like Statement A. Return as JSON: {"questionBody": "...", "optionA": "...", "optionB": "...", "optionC": "...", "optionD": "...", "answer": "A"}`;

  try {
    const response = await client.messages.create({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 400,
      messages: [{ role: 'user', content: userPrompt }],
    });

    const text = (response.content[0] && response.content[0].text) ? response.content[0].text.trim() : '';
    console.log(`📝 Claude raw for ${subject}:\n${text}`);

    if (!text) throw new Error('Empty response from Claude API');

    // Extract JSON — handle markdown code fences if present
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) throw new Error('No JSON found in response');

    const parsed = JSON.parse(jsonMatch[0]);
    const { questionBody, optionA, optionB, optionC, optionD, answer } = parsed;

    if (!questionBody || !optionA) throw new Error('Incomplete JSON fields');

    const body = `${questionBody}\nA) ${optionA}\nB) ${optionB}\nC) ${optionC}\nD) ${optionD}`;
    const ans = (answer || 'A').toUpperCase().charAt(0);

    console.log(`✅ ${subject} — answer: ${ans}, q: "${questionBody.slice(0, 60)}"`);
    return { questionBody: body, answer: ans };
  } catch (err) {
    console.error(`Claude generateQuestion error (${subject}):`, err.message);
    return {
      questionBody: `Which of the following best describes a key concept in ${subject}?\nA) First option\nB) Second option\nC) Third option\nD) Fourth option`,
      answer: 'A',
    };
  }
}

/**
 * Generate personalised feedback after a student answers a question.
 */
async function generateFeedback(studentName, isCorrect, studentAnswer, correctAnswer, subject, formLevel) {
  const systemPrompt = `You are JIBU, a warm Tanzanian AI tutor. A Form ${formLevel} student just answered a ${subject} question.
${isCorrect
    ? `They got it RIGHT (answered ${studentAnswer}). Write a short enthusiastic English congratulation, mention one Swahili celebration phrase, and explain in 1 sentence WHY that answer is correct.`
    : `They answered ${studentAnswer} but the correct answer was ${correctAnswer}. Write a kind English encouragement, mention one Swahili phrase, and explain the correct answer in 1 sentence.`}
Start with the student's name: ${studentName}. Keep total under 220 characters.`;

  try {
    const response = await client.messages.create({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 220,
      messages: [{ role: 'user', content: 'Generate feedback now.' }],
      system: systemPrompt,
    });
    return response.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateFeedback error:', err.message);
    return isCorrect
      ? `✅ Vizuri sana ${studentName}! Correct — the answer is ${correctAnswer}. Hongera! 🌟`
      : `💪 Pole ${studentName}. The correct answer was ${correctAnswer}. Jaribu tena kesho!`;
  }
}

/**
 * Generate weekly parent report.
 */
async function generateParentReport(student) {
  const systemPrompt = `You are JIBU, a Tanzanian AI education platform. Write a brief warm weekly progress report for a parent.

Child: ${student.Student_Name}, Form ${student.Form_level}
Subjects: ${student.Subjects}
Streak: ${student.Current_Streak || 0} days | Longest: ${student.Longest_Streak || 0} days
Points: ${student.Total_Points || 0} | Rank: ${student.Rank_Title || 'Mwanafunzi'}
Strong: ${student.Strong_Topics || 'Still being assessed'}
Weak: ${student.Weak_Topics || 'Still being assessed'}

Write in English. Open with a warm Swahili greeting. 3-4 sentences, encouraging and specific. End with a Swahili motivational phrase. Under 300 characters total.`;

  try {
    const response = await client.messages.create({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 300,
      messages: [{ role: 'user', content: 'Generate parent report.' }],
      system: systemPrompt,
    });
    return response.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateParentReport error:', err.message);
    return `Habari za familia! 📊 ${student.Student_Name} — Streak: ${student.Current_Streak || 0} days, Points: ${student.Total_Points || 0}, Rank: ${student.Rank_Title || 'Mwanafunzi'}. Mungu awabariki! 🙏`;
  }
}

module.exports = { generateQuestion, generateFeedback, generateParentReport };
