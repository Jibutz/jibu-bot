const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Generate a NECTA-style multiple choice question for one specific subject.
 * Returns { questionBody: string, answer: string }
 * questionBody is just the question text + A/B/C/D options, no header/footer.
 */
async function generateQuestion(subject, formLevel) {
  const systemPrompt = `You are a Tanzania NECTA exam expert following the Tanzania Institute of Education TIE curriculum strictly.

For O-Level (Form 1-4) follow these guidelines:
- Maths: algebra, geometry, statistics, trigonometry, arithmetic
- Biology: cell biology, ecology, human biology, genetics, evolution
- Chemistry: atomic structure, chemical reactions, organic chemistry, acids and bases
- Physics: mechanics, electricity, waves, thermal physics, light
- English: grammar, comprehension, composition, literature
- History: Tanzania history, East African history, World history
- Geography: physical and human geography of Tanzania and East Africa
- Kiswahili: sarufi, ufahamu, insha, fasihi

For A-Level (Form 5-6) follow combinations:
- PCM (Physics, Chemistry, Maths): advanced mechanics, calculus, organic chemistry, thermodynamics
- PCB (Physics, Chemistry, Biology): biochemistry, advanced cell biology, chemical equilibrium
- CBG (Chemistry, Biology, Geography): environmental chemistry, ecology, biogeography
- HGL (History, Geography, Literature): African history, postcolonial literature, regional geography
- HGE (History, Geography, Economics): economic history, development economics, East Africa
- HGK (History, Geography, Kiswahili): Kiswahili fasihi, historia ya Afrika, jiografia
- ECA (Economics, Commerce, Accountancy): microeconomics, business finance, double entry
- EGM (Economics, Geography, Maths): statistics, economic geography, calculus
- HKL (History, Kiswahili, Literature): comparative literature, oral tradition, African history

Always match difficulty strictly to the Form level:
- Form 1-2: basic foundational questions
- Form 3-4: CSEE exam level difficulty
- Form 5-6: ACSEE exam level difficulty

Generate questions that feel like real NECTA past paper questions — specific, factual, no vague options.`;

  const userPrompt = `Generate ONE multiple choice question for Form ${formLevel} ${subject}.

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
      system: systemPrompt,
      messages: [{ role: "user", content: userPrompt }]
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
 * Generate a one-sentence explanation for a question answer.
 */
async function generateFeedback(questionBody, correctAnswer, studentAnswer, formLevel) {
  const correctOption = correctAnswer.toUpperCase();
  const prompt = `In one sentence, explain why ${correctOption} is the correct answer to this question: ${questionBody}. Keep it simple for a Form ${formLevel} student.`;

  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "claude-haiku-4-5-20251001",
        max_tokens: 120,
        messages: [{ role: "user", content: prompt }]
      })
    });
    const data = await response.json();
    return data.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateFeedback error:', err.message);
    return `Option ${correctAnswer} is correct for this ${formLevel}-level question.`;
  }
}

/**
 * Re-explain a question answer using a completely different approach.
 */
async function generateReexplanation(lastQuestion) {
  const { questionBody, answer, subject, formLevel } = lastQuestion;
  const subjectLower = (subject || '').toLowerCase();
  const isMaths = subjectLower.includes('maths') || subjectLower.includes('math');
  const isScience = ['biology', 'chemistry', 'physics'].some(s => subjectLower.includes(s));

  const approach = isMaths
    ? 'Show the full step-by-step working to prove why this answer is correct. Use numbered steps.'
    : isScience
    ? 'Use a real-life example or analogy that a student would relate to in Tanzania.'
    : 'Explain using a completely different angle or method than a textbook would use.';

  const prompt = `A Form ${formLevel} student challenged this answer. Re-explain it using a DIFFERENT approach than before.

Question: ${questionBody}
Correct answer: ${answer}
Subject: ${subject}

${approach}

Start by politely acknowledging their challenge (1 short sentence). Then give the re-explanation. End with a kind, confident closing. Keep total response under 320 characters.`;

  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "claude-haiku-4-5-20251001",
        max_tokens: 350,
        messages: [{ role: "user", content: prompt }]
      })
    });
    const data = await response.json();
    return data.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateReexplanation error:', err.message);
    return `Great question to challenge! 💪 The correct answer is still ${answer}. Try re-reading the question carefully and you'll see why. You've got this!`;
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

/**
 * Answer a student's free-text help question.
 */
async function generateHelpAnswer(question, subjects, formLevel) {
  const prompt = `You are JIBU, a friendly Tanzania NECTA exam tutor. A Form ${formLevel} student studying ${subjects} needs help with: ${question}. Give a clear helpful answer in simple English with a Swahili word or two for warmth. Keep it under 5 sentences.`;
  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": process.env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "Content-Type": "application/json" },
      body: JSON.stringify({ model: "claude-haiku-4-5-20251001", max_tokens: 300, messages: [{ role: "user", content: prompt }] })
    });
    const data = await response.json();
    return data.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateHelpAnswer error:', err.message);
    return `Great question! For ${subjects} at Form ${formLevel}, I recommend reviewing your textbook notes and practising past paper questions. Jaribu tena — keep trying! 💪`;
  }
}

/**
 * Generate a weekly learning summary for the student.
 */
async function generateWeeklySummary(student) {
  const prompt = `Write a warm encouraging weekly learning summary for a Tanzania Form ${student.Form_level || '4'} student named ${student.Student_Name} who studied ${student.Subjects || 'their subjects'} this week. Reference what topics these subjects typically cover at this form level. Mention their streak of ${student.Current_Streak || 0} days and ${student.Total_Points || 0} points. Give one specific study tip for their weakest subject (${student.Weak_Topics || 'general study skills'}). Keep it under 150 words. Use simple English with occasional Swahili for warmth.`;
  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": process.env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "Content-Type": "application/json" },
      body: JSON.stringify({ model: "claude-haiku-4-5-20251001", max_tokens: 350, messages: [{ role: "user", content: prompt }] })
    });
    const data = await response.json();
    return data.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateWeeklySummary error:', err.message);
    return `Habari ${student.Student_Name}! 🎓 Great week of studying! Your streak is at ${student.Current_Streak || 0} days and you have ${student.Total_Points || 0} points. Keep practising daily — consistency is the key to NECTA success! Endelea! 💪`;
  }
}

/**
 * Generate a personalised stats summary for MYSTATS command.
 */
async function generateMyStats(student) {
  const prompt = `Write a motivating personal stats summary for a Tanzania student named ${student.Student_Name} studying ${student.Subjects || 'their subjects'} at Form ${student.Form_level || '4'}. Their stats are: streak ${student.Current_Streak || 0} days, total points ${student.Total_Points || 0}, rank title ${student.Rank_Title || 'Mwanafunzi'}. Give one specific encouragement and one study tip. Keep it under 100 words. Use simple English with occasional Swahili.`;
  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": process.env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "Content-Type": "application/json" },
      body: JSON.stringify({ model: "claude-haiku-4-5-20251001", max_tokens: 250, messages: [{ role: "user", content: prompt }] })
    });
    const data = await response.json();
    return data.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateMyStats error:', err.message);
    return `You are doing great ${student.Student_Name}! Keep answering daily to build your streak and climb the rankings. Jitahidi — every question makes you stronger! 💪`;
  }
}

module.exports = { generateQuestion, generateFeedback, generateReexplanation, generateHelpAnswer, generateWeeklySummary, generateMyStats, generateParentReport };
