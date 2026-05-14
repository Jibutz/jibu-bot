const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Generate a NECTA-style multiple choice question for one specific subject.
 * Returns { questionBody: string, answer: string }
 * questionBody is just the question text + A/B/C/D options, no header/footer.
 */
async function generateQuestion(subject, formLevel) {
  const prompt = `You are a Tanzania NECTA exam question generator. Generate ONE real multiple choice question for Form ${formLevel} ${subject}.

Rules:
- Real specific question, not generic
- 4 real answer options, not placeholders
- Respond ONLY with valid JSON, nothing else

Example format:
{"questionBody":"What is the chemical formula for water?","optionA":"H2O","optionB":"CO2","optionC":"NaCl","optionD":"O2","answer":"A"}

Now generate a question for Form ${formLevel} ${subject}:`;

  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": process.env.ANTHROPIC_API_KEY,
      "anthropic-version": "2023-06-01",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 300,
      messages: [{ role: "user", content: prompt }]
    })
  });

  const data = await response.json();
  console.log("Claude raw response:", JSON.stringify(data));
  const text = data.content[0].text;
  console.log("Claude text:", text);
  const cleaned = text.replace(/```json/g, '').replace(/```/g, '').trim();
  return JSON.parse(cleaned);
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
