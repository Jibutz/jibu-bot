const AfricasTalking = require('africastalking');

let atClient = null;

function getATClient() {
  if (!atClient) {
    const AT = AfricasTalking({
      apiKey: process.env.AFRICASTALKING_API_KEY,
      username: process.env.AFRICASTALKING_USERNAME,
    });
    atClient = AT.SMS;
  }
  return atClient;
}

/**
 * Split a message into 160-character chunks for SMS
 */
function splitSMS(message) {
  const maxLen = 159; // Leave 1 char buffer
  if (message.length <= maxLen) return [message];

  const chunks = [];
  let remaining = message;
  let part = 1;

  while (remaining.length > 0) {
    // Reserve space for part indicator if needed
    const indicator = chunks.length > 0 || remaining.length > maxLen ? ` (${part})` : '';
    const available = maxLen - indicator.length;

    // Try to break at word boundary
    let chunk = remaining.substring(0, available);
    const lastSpace = chunk.lastIndexOf(' ');
    if (lastSpace > available * 0.7 && remaining.length > available) {
      chunk = chunk.substring(0, lastSpace);
    }

    chunks.push(chunk.trim() + (chunks.length > 0 || remaining.length > maxLen ? ` (${part})` : ''));
    remaining = remaining.substring(chunk.length).trim();
    part++;
  }

  return chunks;
}

/**
 * Send an SMS message (auto-splits if over 160 chars)
 */
async function sendSMS(to, message) {
  const phone = to.startsWith('+') ? to : `+${to}`;
  const sms = getATClient();
  const chunks = splitSMS(message);

  const results = [];
  for (const chunk of chunks) {
    try {
      const result = await sms.send({
        to: [phone],
        message: chunk,
        from: process.env.AFRICASTALKING_SENDER_ID || undefined,
      });
      console.log(`✅ SMS sent to ${phone}: ${chunk.substring(0, 30)}...`);
      results.push(result);

      if (chunks.length > 1) {
        await new Promise(r => setTimeout(r, 500));
      }
    } catch (err) {
      console.error(`❌ SMS send error to ${phone}:`, err.message);
      throw err;
    }
  }

  return results;
}

module.exports = { sendSMS, splitSMS };
