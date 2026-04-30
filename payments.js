const axios = require('axios');

const CLICKPESA_BASE = 'https://api.clickpesa.com/third-parties';

let accessToken = null;
let tokenExpiry = null;

/**
 * Authenticate with ClickPesa and get an access token
 */
async function getAccessToken() {
  if (accessToken && tokenExpiry && Date.now() < tokenExpiry) {
    return accessToken;
  }

  try {
    const response = await axios.post(`${CLICKPESA_BASE}/generate-token`, {
      clientId: process.env.CLICKPESA_CONSUMER_KEY,
      clientSecret: process.env.CLICKPESA_CONSUMER_SECRET,
    });

    accessToken = response.data.token || response.data.access_token;
    // Token usually expires in 1 hour; refresh 5 minutes early
    tokenExpiry = Date.now() + (55 * 60 * 1000);
    return accessToken;
  } catch (err) {
    console.error('ClickPesa auth error:', err.response?.data || err.message);
    throw err;
  }
}

/**
 * Create a ClickPesa payment link for M-Pesa collection
 * Returns a payment URL string
 */
async function createPaymentLink(phone, amount, description) {
  try {
    const token = await getAccessToken();

    const response = await axios.post(
      `${CLICKPESA_BASE}/create-order`,
      {
        amount: amount,
        currency: 'TZS',
        description: description,
        customerPhone: phone.startsWith('+') ? phone : `+${phone}`,
        callbackUrl: `${process.env.APP_URL || 'https://jibu-bot.railway.app'}/webhook/payment`,
        reference: `JIBU_${phone}_${Date.now()}`,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );

    return response.data.paymentLink || response.data.checkout_url || `https://pay.clickpesa.com/${response.data.orderId}`;
  } catch (err) {
    console.error('ClickPesa createPaymentLink error:', err.response?.data || err.message);
    // Return a fallback manual payment instruction
    return `Tuma TZS ${amount} kwa Lipa Namba: ${process.env.MPESA_TILL_NUMBER || 'JIBU'}`;
  }
}

/**
 * Verify a payment by reference/order ID
 */
async function verifyPayment(orderId) {
  try {
    const token = await getAccessToken();

    const response = await axios.get(
      `${CLICKPESA_BASE}/orders/${orderId}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    return {
      status: response.data.status,
      amount: response.data.amount,
      phone: response.data.customerPhone,
    };
  } catch (err) {
    console.error('ClickPesa verifyPayment error:', err.response?.data || err.message);
    return { status: 'UNKNOWN' };
  }
}

/**
 * Initiate a USSD push payment (M-Pesa STK push equivalent)
 */
async function initiateUSSDPush(phone, amount, description) {
  try {
    const token = await getAccessToken();

    const response = await axios.post(
      `${CLICKPESA_BASE}/collect-payment`,
      {
        amount,
        currency: 'TZS',
        phone: phone.startsWith('+') ? phone : `+255${phone.replace(/^0/, '')}`,
        description,
        reference: `JIBU_${Date.now()}`,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );

    return response.data;
  } catch (err) {
    console.error('ClickPesa USSD push error:', err.response?.data || err.message);
    throw err;
  }
}

module.exports = { createPaymentLink, verifyPayment, initiateUSSDPush };
