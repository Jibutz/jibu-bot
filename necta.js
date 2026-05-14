const { getStudentByPhone, createStudent, updateStudent, base } = require('./airtable');
const { sendWhatsApp } = require('./whatsapp');
const { sendSMS } = require('./sms');
const { createPaymentLink, initiateUSSDPush } = require('./payments');

// In-memory store for pending NECTA lookups (awaiting phone number)
const pendingLookups = new Map();

/**
 * Handle NECTA results lookup flow
 * 1. User sends: JIBU MATOKEO [index_number]
 * 2. Bot asks for their phone number
 * 3. Charges TZS 500 via ClickPesa
 * 4. Returns result
 * 5. Stores for 3-day follow-up subscription offer
 */
async function handleNectaResults(phone, message, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
  const upperMsg = message.trim().toUpperCase();

  // Step 1: Initial NECTA lookup request
  if (upperMsg.startsWith('JIBU MATOKEO')) {
    const parts = message.trim().split(/\s+/);
    const indexNumber = parts[2] || '';

    if (!indexNumber) {
      await send(phone,
        `Include your index number in the message! Example: JIBU MATOKEO S1234/0001/2024`
      );
      return;
    }

    // Store the pending lookup with index number
    pendingLookups.set(phone, {
      indexNumber,
      step: 'awaiting_phone',
      timestamp: Date.now(),
    });

    await send(phone,
      `🎓 NECTA Results for ${indexNumber}\n\nFee: TZS 500 only.\n\nSend your M-Pesa number to pay and get your results instantly! 📋`
    );
    return;
  }

  // Step 2: Received phone number for payment
  const pending = pendingLookups.get(phone);
  if (pending && pending.step === 'awaiting_phone') {
    const mpesaPhone = formatPhone(message.trim());

    if (!mpesaPhone) {
      await send(phone, `That number doesn't look right! Send your M-Pesa number (example: 0712345678)`);
      return;
    }

    pendingLookups.set(phone, { ...pending, mpesaPhone, step: 'awaiting_payment' });

    try {
      const payLink = await createPaymentLink(
        mpesaPhone,
        500,
        `JIBU Matokeo - ${pending.indexNumber}`
      );

      await send(phone,
        `💳 Pay TZS 500 to get results for ${pending.indexNumber}:\n\n${payLink}\n\nResults will be sent instantly after payment! ✅`
      );

      // Save to Airtable for follow-up
      await saveNectaLookup(phone, pending.indexNumber, mpesaPhone, channel);
    } catch (err) {
      console.error('NECTA payment error:', err);
      await send(phone, `Sorry, there was a payment error! 😬 Please try again in a moment.`);
    }
    return;
  }
}

/**
 * Called when NECTA payment is confirmed — send the actual result
 */
async function deliverNectaResult(phone, indexNumber, channel) {
  const send = channel === 'SMS' ? sendSMS : sendWhatsApp;

  try {
    // In a real implementation, you'd query the NECTA results API/database here
    // For now, send a placeholder and note for the developer to integrate
    const result = await fetchNectaResult(indexNumber);

    await send(phone,
      `📋 NECTA Results for ${indexNumber}:\n\n${result}\n\n---\nWant to keep improving? Study with JIBU for just TZS 5,000/month! Send JIBU to join. 🎓`
    );

    // Schedule 3-day follow-up
    scheduleFollowUp(phone, indexNumber, channel);
  } catch (err) {
    console.error('NECTA result delivery error:', err);
    await send(phone, `Sorry, results for ${indexNumber} aren't available right now. Try again later or contact NECTA directly.`);
  }
}

/**
 * Placeholder for NECTA results API integration
 * Developer should implement actual NECTA API call here
 */
async function fetchNectaResult(indexNumber) {
  // TODO: Integrate with actual NECTA results API
  // Options:
  // 1. NECTA official API (if available)
  // 2. Scrape necta.go.tz (check ToS)
  // 3. Maintain your own database of results
  return `[NECTA Result for ${indexNumber}]\n⚠️ Developer: Connect to NECTA results database in src/necta.js fetchNectaResult()`;
}

/**
 * Save NECTA lookup to Airtable for follow-up
 */
async function saveNectaLookup(phone, indexNumber, mpesaPhone, channel) {
  try {
    const AT = require('airtable');
    const base = new AT({ apiKey: process.env.AIRTABLE_API_KEY }).base(process.env.AIRTABLE_BASE_ID);

    await base('NECTA_Lookups').create({
      Phone: phone,
      Index_Number: indexNumber,
      MPesa_Phone: mpesaPhone,
      Channel: channel,
      Lookup_Date: new Date().toISOString().split('T')[0],
      Follow_Up_Date: getFollowUpDate(3),
      Status: 'Pending',
    });
  } catch (err) {
    // Table might not exist — log but don't crash
    console.log('NECTA lookup save (optional):', err.message);
  }
}

/**
 * Schedule a 3-day follow-up subscription offer
 * In production, use a proper job queue; here we use a simple setTimeout
 */
function scheduleFollowUp(phone, indexNumber, channel) {
  const THREE_DAYS = 3 * 24 * 60 * 60 * 1000;
  setTimeout(async () => {
    try {
      const send = channel === 'SMS' ? sendSMS : sendWhatsApp;
      await send(phone,
        `🎓 Hey! How did ${indexNumber} go? 👀\n\nLevel up with JIBU — answer NECTA questions daily, track your progress, and score higher!\n\n7 days free — bure kabisa! Send JIBU to start. 🔥`
      );
    } catch (err) {
      console.error('NECTA follow-up error:', err);
    }
  }, THREE_DAYS);
}

function getFollowUpDate(days) {
  const d = new Date();
  d.setDate(d.getDate() + days);
  return d.toISOString().split('T')[0];
}

function formatPhone(phone) {
  const cleaned = phone.replace(/[\s\-+]/g, '');
  if (/^255[67]\d{8}$/.test(cleaned)) return cleaned;
  if (/^0[67]\d{8}$/.test(cleaned)) return '255' + cleaned.slice(1);
  return null;
}

module.exports = { handleNectaResults, deliverNectaResult };
