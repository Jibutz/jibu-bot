const axios = require('axios');

const META_VERSION = 'v19.0';
const HARDCODED_PHONE_ID = '1152290557959699';

function getPhoneId() {
  const fromEnv = process.env.WHATSAPP_PHONE_NUMBER_ID;
  return (fromEnv && fromEnv !== 'undefined') ? fromEnv : HARDCODED_PHONE_ID;
}

function getMetaBase() {
  return `https://graph.facebook.com/${META_VERSION}/${getPhoneId()}`;
}

async function sendWhatsApp(to, message) {
  const phone = to.replace(/^\+/, '').trim();
  const url = `${getMetaBase()}/messages`;
  console.log(`📡 POST ${url}`);
  console.log(`🔑 WHATSAPP_TOKEN starts with: ${(process.env.WHATSAPP_TOKEN || '').slice(0, 20)}`);
  try {
    const response = await axios.post(
      url,
      {
        messaging_product: 'whatsapp',
        recipient_type: 'individual',
        to: phone,
        type: 'text',
        text: { preview_url: false, body: message },
      },
      {
        headers: {
          Authorization: `Bearer ${process.env.WHATSAPP_TOKEN}`,
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

async function sendWhatsAppTemplate(to, templateName, components = []) {
  const phone = to.replace(/^\+/, '').trim();
  try {
    const response = await axios.post(
      `${getMetaBase()}/messages`,
      {
        messaging_product: 'whatsapp',
        recipient_type: 'individual',
        to: phone,
        type: 'template',
        template: {
          name: templateName,
          language: { code: 'sw' },
          components,
        },
      },
      {
        headers: {
          Authorization: `Bearer ${process.env.WHATSAPP_TOKEN}`,
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
