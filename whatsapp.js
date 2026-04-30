const axios = require('axios');

const DIALOG360_BASE = 'https://waba.360dialog.io/v1';

/**
 * Send a WhatsApp text message via 360dialog
 */
async function sendWhatsApp(to, message) {
  const phone = to.replace(/^\+/, '').trim();

  try {
    const response = await axios.post(
      `${DIALOG360_BASE}/messages`,
      {
        recipient_type: 'individual',
        to: phone,
        type: 'text',
        text: { body: message },
      },
      {
        headers: {
          'D360-API-KEY': process.env.DIALOG360_API_KEY,
          'Content-Type': 'application/json',
        },
      }
    );
    console.log(`✅ WhatsApp sent to ${phone}`);
    return response.data;
  } catch (err) {
    console.error(`❌ WhatsApp send error to ${phone}:`, err.response?.data || err.message);
    throw err;
  }
}

/**
 * Send a WhatsApp template message (for session-independent messages)
 */
async function sendWhatsAppTemplate(to, templateName, components = []) {
  const phone = to.replace(/^\+/, '').trim();

  try {
    const response = await axios.post(
      `${DIALOG360_BASE}/messages`,
      {
        recipient_type: 'individual',
        to: phone,
        type: 'template',
        template: {
          namespace: process.env.WHATSAPP_NAMESPACE || '',
          name: templateName,
          language: { policy: 'deterministic', code: 'sw' },
          components,
        },
      },
      {
        headers: {
          'D360-API-KEY': process.env.DIALOG360_API_KEY,
          'Content-Type': 'application/json',
        },
      }
    );
    return response.data;
  } catch (err) {
    console.error(`WhatsApp template error to ${phone}:`, err.response?.data || err.message);
    throw err;
  }
}

module.exports = { sendWhatsApp, sendWhatsAppTemplate };
