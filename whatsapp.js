const axios = require('axios');
const { getToken } = require('./tokenManager');

const PHONE_NUMBER_ID = process.env.WHATSAPP_PHONE_NUMBER_ID || '1152290557959699';
const API_VERSION = 'v19.0';

// ─── Shared failure logging ───────────────────────────────────────────────────
// Prints the full Meta API error (status, code, type, message, trace id) so
// send failures are never silent in Railway logs.
function logSendFailure(phone, err) {
  const status = err.response?.status;
  const metaError = err.response?.data?.error;

  const summary = metaError
    ? `[HTTP ${status}] code=${metaError.code}${metaError.error_subcode ? `/${metaError.error_subcode}` : ''} type=${metaError.type} — ${metaError.message}${metaError.error_data?.details ? ` (${metaError.error_data.details})` : ''}`
    : (err.message || String(err));

  console.error(`❌ Message send FAILED to ${phone}: ${summary}`);
  console.error(`❌ WA error status: ${status}`);
  console.error(`❌ WA error full response: ${JSON.stringify(err.response?.data, null, 2)}`);
  if (metaError?.fbtrace_id) {
    console.error(`❌ Meta fbtrace_id: ${metaError.fbtrace_id}`);
  }
}

async function sendWhatsApp(to, message) {
  const phone = to.replace(/^\+/, '').trim();
  const url = `https://graph.facebook.com/${API_VERSION}/${PHONE_NUMBER_ID}/messages`;
  const token = getToken();

  const body = {
    messaging_product: 'whatsapp',
    recipient_type: 'individual',
    to: phone,
    type: 'text',
    text: { body: message },
  };

  console.log(`📤 Attempting to send message to ${phone}`);
  console.log(`📡 WA POST ${url}`);
  console.log(`🔑 Token: ${token.slice(0, 20)}... (length ${token.length})`);
  console.log(`📦 Request body: ${JSON.stringify(body)}`);

  try {
    const response = await axios.post(url, body, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });
    console.log(`✅ WA sent to ${phone} — status ${response.status}`);
    console.log(`✅ Message sent successfully`);
    return response.data;
  } catch (err) {
    logSendFailure(phone, err);
    throw err;
  }
}

async function sendWhatsAppTemplate(to, templateName, components = []) {
  const phone = to.replace(/^\+/, '').trim();
  const url = `https://graph.facebook.com/${API_VERSION}/${PHONE_NUMBER_ID}/messages`;
  const token = getToken();

  console.log(`📤 Attempting to send message to ${phone}`);
  console.log(`📡 WA TEMPLATE POST ${url} template=${templateName} to=${phone}`);

  try {
    const response = await axios.post(url, {
      messaging_product: 'whatsapp',
      recipient_type: 'individual',
      to: phone,
      type: 'template',
      template: { name: templateName, language: { code: 'sw' }, components },
    }, {
      headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    });
    console.log(`✅ WA template sent to ${phone} — status ${response.status}`);
    console.log(`✅ Message sent successfully`);
    return response.data;
  } catch (err) {
    logSendFailure(phone, err);
    throw err;
  }
}

async function validateWhatsAppToken() {
  const token = getToken();
  const url = `https://graph.facebook.com/${API_VERSION}/${PHONE_NUMBER_ID}`;

  console.log('🔍 Validating WhatsApp token on startup...');
  console.log(`🆔 Phone Number ID: ${PHONE_NUMBER_ID}`);
  console.log(`🔑 Token first 20 chars: ${token.slice(0, 20)} (total length: ${token.length})`);

  if (!token) {
    console.error('❌ WHATSAPP_TOKEN is not set in environment variables!');
    return;
  }

  try {
    const response = await axios.get(url, {
      params: { access_token: token, fields: 'display_phone_number,verified_name' },
    });
    console.log(`✅ Token valid! Phone: ${response.data.display_phone_number}, Name: ${response.data.verified_name}`);
  } catch (err) {
    console.error(`❌ Token validation FAILED — status: ${err.response?.status}`);
    console.error(`❌ Meta error: ${JSON.stringify(err.response?.data?.error)}`);
  }
}

module.exports = { sendWhatsApp, sendWhatsAppTemplate, validateWhatsAppToken };
