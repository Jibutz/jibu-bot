// rebuilt 2026-05-12T00:00:00Z
const axios = require('axios');

async function sendWhatsApp(to, message) {
  const phone = to.replace(/^\+/, '').trim();
  const url = 'https://graph.facebook.com/v19.0/1152290557959699/messages';
  console.log('📡 POST ' + url);
  console.log('🔑 TOKEN starts: ' + (process.env.WHATSAPP_TOKEN || '').slice(0, 20));
  try {
    const response = await axios.post(url, {
      messaging_product: 'whatsapp',
      recipient_type: 'individual',
      to: phone,
      type: 'text',
      text: { body: message },
    }, {
      headers: {
        Authorization: 'Bearer ' + process.env.WHATSAPP_TOKEN,
        'Content-Type': 'application/json',
      },
    });
    console.log('✅ sent to ' + phone);
    return response.data;
  } catch (err) {
    console.error('❌ error:', JSON.stringify(err.response?.data, null, 2) || err.message);
    throw err;
  }
}

async function sendWhatsAppTemplate(to, templateName, components = []) {
  const phone = to.replace(/^\+/, '').trim();
  const response = await axios.post(
    'https://graph.facebook.com/v19.0/1152290557959699/messages',
    { messaging_product: 'whatsapp', recipient_type: 'individual', to: phone, type: 'template', template: { name: templateName, language: { code: 'sw' }, components } },
    { headers: { Authorization: 'Bearer ' + process.env.WHATSAPP_TOKEN, 'Content-Type': 'application/json' } }
  );
  return response.data;
}

module.exports = { sendWhatsApp, sendWhatsAppTemplate };
