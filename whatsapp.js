const axios = require('axios');

const META_BASE = 'https://graph.facebook.com/v19.0';

async function sendWhatsApp(to, message) {
  const phone = to.replace(/^\+/, '').trim();
  try {
    const response = await axios.post(
      `${META_BASE}/${process.env.WHATSAPP_PHONE_ID}/messages`,
      {
        messaging_product: 'whatsapp',
        recipient_type: 'individual',
        to: phone,
        type: 'text',
        text: { body: message },
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.WHATSAPP_TOKEN}`,
          'Content-Type': 'application/json',
        },
      }
    );
    console.log(`✅ WhatsApp sent to ${phone}`);
    return response.data;
  } catch (err) {
    const errorDetail = JSON.stringify(err.response?.data);
    console.error(`❌ WhatsApp error: ${errorDetail}`);
    throw err;
  }
}

async function sendWhatsAppTemplate(to, templateName, components = []) {
  const phone = to.replace(/^\+/, '').trim();
  try {
    const response = await axios.post(
      `${META_BASE}/${process.env.WHATSAPP_PHONE_ID}/messages`,
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
          'Authorization': `Bearer ${process.env.WHATSAPP_TOKEN}`,
          'Content-Type': 'application/json',
        },
      }
    );
    return response.data;
  } catch (err) {
    const errorDetail = JSON.stringify(err.response?.data);
    console.error(`❌ WhatsApp template error: ${errorDetail}`);
    throw err;
  }
}

module.exports = { sendWhatsApp, sendWhatsAppTemplate };
