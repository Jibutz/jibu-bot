const Anthropic = require('@anthropic-ai/sdk');

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/**
 * Generate a NECTA-style multiple choice question for one specific subject.
 * Returns { questionBody, optionA-D, answer, examTip, topic }
 * Pass coveredTopics (string[]) to avoid repeating subjects already asked.
 * Pass isRevision=true + revisionTopics to generate a cross-topic revision question.
 */
async function generateQuestion(subject, formLevel, coveredTopics = [], isRevision = false, revisionTopics = []) {
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

Generate questions that feel like real NECTA past paper questions — specific, factual, no vague options.

CRITICAL NECTA PATTERN INTELLIGENCE:
NECTA exams repeat question patterns every 4-6 years. When generating questions follow these rules:

1. PATTERN AWARENESS — after generating a question, add a pattern tip like:
"💡 Exam tip: This type of question appears in NECTA almost every year. Master this pattern and you save 10+ minutes in the exam!"

2. HIGH FREQUENCY TOPICS — always prioritize these topics as they appear most in NECTA:
- Maths: quadratic equations, differentiation, probability, matrices, vectors
- Biology: cell biology, photosynthesis, human digestive system, genetics, ecology
- Chemistry: chemical equations, periodic table, organic chemistry, acids and bases
- Physics: electricity, waves, Newton's laws, energy transformations
- English: comprehension, essay writing, grammar tenses
- History: colonialism, independence movements, Tanzania political history
- Geography: weather, population, agriculture in Tanzania and East Africa

3. DIFFICULTY PATTERN — NECTA Paper 1 is always multiple choice (what we send). Paper 2 is structured. Tell students: "This is a Paper 1 style question — expect similar in your exam!"

4. YEAR PATTERN TIP — occasionally add: "Similar questions appeared in NECTA [year] and [year]. Knowing the pattern = knowing the exam! 🎯"

5. TIME TIPS — add exam technique: "In the real exam, spend max 1.5 minutes on multiple choice questions like this one."

TOPIC ROTATION — rotate systematically through these topic areas and always name the topic in the "topic" JSON field:
- Biology F1-2: cells | nutrition | respiration | transport | excretion | reproduction | ecology
- Biology F3-4: genetics | evolution | biotechnology | disease | human biology advanced
- Maths F1-2: algebra basics | geometry | fractions | decimals | ratios | statistics intro
- Maths F3-4: quadratic equations | trigonometry | matrices | vectors | probability | calculus intro
- Chemistry: atomic structure | bonding | periodic table | reactions | organic | acids bases | electrochemistry
- Physics: mechanics | electricity | magnetism | waves | thermal | light | atomic physics
- History: Tanzania pre-colonial | colonial era | independence | East Africa | World Wars | post-independence
- Geography: Tanzania physical | climate | population | agriculture | industry | East Africa | world geography
- English: comprehension | grammar tenses | essay writing | vocabulary | literature

Generate questions that feel like they came straight from a real NECTA paper — because the patterns tell us they will!

CRITICAL JSON FORMATTING RULES — you must follow these exactly or the response will be rejected:
- All field values must be plain text only — no special characters inside JSON strings
- Do NOT use apostrophes or single quotes inside any field value (write "dont" not "don't", "its" not "it's")
- Do NOT use double quotes inside field values (use alternative phrasing)
- Do NOT use math symbols like ÷, ×, ≠, ≤, ≥, ², ³, √ inside JSON strings (write "squared", "divided by", "square root of" instead)
- Do NOT use backslashes, curly braces, or any character that would break JSON parsing
- Keep all text simple, plain, and JSON-safe`;

  const avoidLine = coveredTopics.length > 0
    ? `\nIMPORTANT — Never repeat topics. Previous topics already asked to this student: ${coveredTopics.slice(-15).join(', ')}. Generate a question on a COMPLETELY DIFFERENT topic from this list.\n`
    : '';

  const revisionLine = isRevision && revisionTopics.length >= 2
    ? `\nREVISION QUESTION — This student has answered 10 questions on ${subject}. Combine knowledge from these two topics: ${revisionTopics.slice(-2).join(' and ')}. Write a question that tests how these topics connect. Label the topic field as "revision: ${revisionTopics.slice(-2).join(' + ')}".\n`
    : '';

  const userPrompt = `Generate ONE multiple choice question for Form ${formLevel} ${subject}.
${avoidLine}${revisionLine}
Rules:
- Real specific question, not generic
- 4 real answer options, not placeholders
- Include a short examTip (1-2 sentences) using the NECTA pattern intelligence above — pattern awareness, year pattern, or time tip
- Include a "topic" field naming the specific topic area from the TOPIC ROTATION list
- Respond ONLY with valid JSON, nothing else

Example format:
{"questionBody":"What is the chemical formula for water?","optionA":"H2O","optionB":"CO2","optionC":"NaCl","optionD":"O2","answer":"A","examTip":"💡 Exam tip: Chemical formulas appear in NECTA almost every year. Similar questions appeared in NECTA 2019 and 2022. Spend max 1.5 minutes on this!","topic":"reactions"}

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
      max_tokens: 400,
      system: systemPrompt,
      messages: [{ role: "user", content: userPrompt }]
    })
  });

  const data = await response.json();
  console.log("Claude raw response:", JSON.stringify(data));
  const text = data.content[0].text;
  console.log("Claude text:", text);
  const cleaned = text.replace(/```json/g, '').replace(/```/g, '').trim();

  // Sanitize the response before parsing: escape unescaped control characters
  // and neutralize smart/curly quotes that break JSON.parse
  const sanitized = cleaned
    .replace(/[‘’]/g, "'")   // curly single quotes -> straight
    .replace(/[“”]/g, '"')   // curly double quotes -> straight
    .replace(/[–—]/g, '-')   // en/em dash -> hyphen
    .replace(/[\x00-\x1F\x7F]/g, ' ') // strip control characters
    // Escape unescaped double quotes inside JSON string values (best-effort)
    .replace(/":\s*"((?:[^"\\]|\\.)*)"/g, (match) => {
      // Already valid — let JSON.parse handle it
      return match;
    });

  try {
    return JSON.parse(sanitized);
  } catch (parseErr) {
    console.error('Claude JSON parse failed:', parseErr.message);
    console.error('Raw text was:', text);
    // Return a safe fallback question so the bot never crashes
    return {
      questionBody: `Which of the following is a key concept in Form ${formLevel} ${subject}?`,
      optionA: "Option A",
      optionB: "Option B",
      optionC: "Option C",
      optionD: "Option D",
      answer: "A",
      examTip: "💡 Exam tip: Review your Form " + formLevel + " " + subject + " notes carefully before the exam.",
      topic: "general"
    };
  }
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
        system: JIBU_SYSTEM,
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
const JIBU_SYSTEM = `You are JIBU, a Tanzania NECTA exam tutor. You are an expert in ALL Tanzania secondary school subjects including: Maths, Biology, Chemistry, Physics, English, Geography, History, Kiswahili, Literature, Economics, Commerce, Accountancy, and all A-Level combinations (PCM, PCB, CBG, HGL, HGE, HGK, ECA, EGM, HKL). You cover both O-Level (Form 1-4) and A-Level (Form 5-6). Never say you do not cover a subject — you cover all Tanzania NECTA subjects.`;

async function generateHelpAnswer(question, subjects, formLevel) {
  const prompt = `A Form ${formLevel} student studying ${subjects} needs help with: ${question}. Give a clear helpful answer in simple English with a Swahili word or two for warmth. Keep it under 5 sentences.`;
  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": process.env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "Content-Type": "application/json" },
      body: JSON.stringify({ model: "claude-haiku-4-5-20251001", max_tokens: 300, system: JIBU_SYSTEM, messages: [{ role: "user", content: prompt }] })
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
      body: JSON.stringify({ model: "claude-haiku-4-5-20251001", max_tokens: 350, system: JIBU_SYSTEM, messages: [{ role: "user", content: prompt }] })
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
      body: JSON.stringify({ model: "claude-haiku-4-5-20251001", max_tokens: 250, system: JIBU_SYSTEM, messages: [{ role: "user", content: prompt }] })
    });
    const data = await response.json();
    return data.content[0].text.trim();
  } catch (err) {
    console.error('Claude generateMyStats error:', err.message);
    return `You are doing great ${student.Student_Name}! Keep answering daily to build your streak and climb the rankings. Jitahidi — every question makes you stronger! 💪`;
  }
}

/**
 * Generate 5 NECTA-style MCQ questions for the Saturday quiz.
 * Returns an array of { questionBody, optionA, optionB, optionC, optionD, answer }.
 */
async function generateSaturdayQuiz(subject, formLevel) {
  const prompt = `Generate 5 quick multiple choice questions for a Tanzania Form ${formLevel} student studying ${subject}. Make them exam-style NECTA questions. Return as JSON array with questionBody, optionA, optionB, optionC, optionD, answer for each.`;
  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'x-api-key': process.env.ANTHROPIC_API_KEY, 'anthropic-version': '2023-06-01', 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: 'claude-haiku-4-5-20251001', max_tokens: 1200, messages: [{ role: 'user', content: prompt }] }),
    });
    const data = await response.json();
    const text = data.content[0].text;
    const cleaned = text.replace(/```json/g, '').replace(/```/g, '').trim();
    return JSON.parse(cleaned);
  } catch (err) {
    console.error('Claude generateSaturdayQuiz error:', err.message);
    return null;
  }
}

module.exports = { generateQuestion, generateFeedback, generateReexplanation, generateHelpAnswer, generateWeeklySummary, generateMyStats, generateParentReport, generateSaturdayQuiz };
