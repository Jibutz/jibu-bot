const axios = require('axios');
const Airtable = require('airtable');

const SETTINGS_TABLE = 'Settings';
const TOKEN_KEY = 'whatsapp_access_token';
const EXPIRY_KEY = 'whatsapp_token_expiry';

let currentToken = process.env.WHATSAPP_TOKEN || '';

function getBase() {
  if (!process.env.AIRTABLE_API_KEY || !process.env.AIRTABLE_BASE_ID) return null;
  return new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(process.env.AIRTABLE_BASE_ID);
}

async function loadFromAirtable() {
  const base = getBase();
  if (!base) return null;
  try {
    const records = await base(SETTINGS_TABLE).select({
      filterByFormula: `OR({Key} = "${TOKEN_KEY}", {Key} = "${EXPIRY_KEY}")`,
      maxRecords: 2,
    }).firstPage();
    if (!records.length) return null;
    const tokenRecord = records.find(r => r.fields.Key === TOKEN_KEY);
    const expiryRecord = records.find(r => r.fields.Key === EXPIRY_KEY);
    if (!tokenRecord?.fields.Value) return null;
    return {
      token: tokenRecord.fields.Value,
      expiry: expiryRecord ? parseInt(expiryRecord.fields.Value, 10) : null,
    };
  } catch (err) {
    if (!err.message?.includes('TABLE_NOT_FOUND') && err.statusCode !== 404) {
      console.warn('⚠️  Token load from Airtable failed:', err.message);
    }
    return null;
  }
}

async function saveToAirtable(token, expiry) {
  const base = getBase();
  if (!base) return;
  for (const [key, value] of [[TOKEN_KEY, token], [EXPIRY_KEY, String(expiry)]]) {
    try {
      const records = await base(SETTINGS_TABLE).select({
        filterByFormula: `{Key} = "${key}"`,
        maxRecords: 1,
      }).firstPage();
      if (records.length > 0) {
        await base(SETTINGS_TABLE).update(records[0].id, { Value: String(value) });
      } else {
        await base(SETTINGS_TABLE).create({ Key: key, Value: String(value) });
      }
    } catch (err) {
      if (err.message?.includes('TABLE_NOT_FOUND') || err.statusCode === 422 || err.statusCode === 404) {
        console.warn('⚠️  Airtable "Settings" table not found — token will not persist across restarts.');
        console.warn('   Fix: create a Settings table with "Key" (text) and "Value" (long text) fields.');
        return;
      }
      console.warn(`⚠️  Could not save ${key} to Airtable:`, err.message);
    }
  }
}

async function checkTokenExpiry(token) {
  const appId = process.env.FACEBOOK_APP_ID;
  const appSecret = process.env.FACEBOOK_APP_SECRET;
  if (!appId || !appSecret) return null;
  try {
    const { data } = await axios.get('https://graph.facebook.com/debug_token', {
      params: { input_token: token, access_token: `${appId}|${appSecret}` },
    });
    const info = data.data;
    if (!info.is_valid) return { valid: false, daysLeft: 0 };
    if (!info.expires_at || info.expires_at === 0) return { valid: true, daysLeft: Infinity };
    const daysLeft = Math.floor((info.expires_at - Date.now() / 1000) / 86400);
    return { valid: true, daysLeft };
  } catch (err) {
    console.warn('⚠️  debug_token check failed:', err.response?.data?.error?.message || err.message);
    return null;
  }
}

async function exchangeToken(token) {
  const appId = process.env.FACEBOOK_APP_ID;
  const appSecret = process.env.FACEBOOK_APP_SECRET;
  if (!appId || !appSecret) {
    console.warn('⚠️  FACEBOOK_APP_ID / FACEBOOK_APP_SECRET not set — cannot refresh token.');
    return null;
  }
  try {
    const { data } = await axios.get('https://graph.facebook.com/oauth/access_token', {
      params: {
        grant_type: 'fb_exchange_token',
        client_id: appId,
        client_secret: appSecret,
        fb_exchange_token: token,
      },
    });
    const expiry = Math.floor(Date.now() / 1000) + (data.expires_in || 5184000);
    return { token: data.access_token, expiry };
  } catch (err) {
    console.error('❌ Token exchange failed:', err.response?.data?.error?.message || err.message);
    return null;
  }
}

async function refreshToken() {
  console.log('🔄 Refreshing WhatsApp access token...');
  const result = await exchangeToken(currentToken);
  if (!result) {
    console.error('❌ Token refresh failed — keeping existing token.');
    return false;
  }
  currentToken = result.token;
  process.env.WHATSAPP_TOKEN = currentToken;
  const daysLeft = Math.floor((result.expiry - Date.now() / 1000) / 86400);
  console.log(`✅ WhatsApp token refreshed. Valid for ~${daysLeft} days.`);
  await saveToAirtable(result.token, result.expiry);
  return true;
}

async function checkAndRefreshToken() {
  console.log('🔍 Checking WhatsApp token status...');
  const status = await checkTokenExpiry(currentToken);
  if (!status) {
    console.log('ℹ️  Token status unknown (set FACEBOOK_APP_ID + FACEBOOK_APP_SECRET for expiry checks).');
    return;
  }
  if (!status.valid) {
    console.error('❌ Token is invalid! Attempting refresh from env...');
    currentToken = process.env.WHATSAPP_TOKEN || currentToken;
    await refreshToken();
    return;
  }
  if (status.daysLeft === Infinity) {
    console.log('✅ Token never expires. No refresh needed.');
    return;
  }
  console.log(`✅ Token valid — ~${status.daysLeft} days remaining.`);
  if (status.daysLeft < 10) {
    console.log('⚠️  Expires soon — refreshing proactively...');
    await refreshToken();
  }
}

async function initToken() {
  console.log('🔑 Initializing WhatsApp token manager...');
  if (!currentToken) {
    console.error('❌ WHATSAPP_TOKEN not set — cannot initialize token manager.');
    return;
  }

  const stored = await loadFromAirtable();
  if (stored?.token && stored.expiry) {
    const daysLeft = Math.floor((stored.expiry - Date.now() / 1000) / 86400);
    if (daysLeft > 5) {
      currentToken = stored.token;
      process.env.WHATSAPP_TOKEN = currentToken;
      console.log(`✅ Loaded persisted token from Airtable — ~${daysLeft} days remaining.`);
      if (daysLeft < 10) await refreshToken();
      return;
    }
    console.log(`⚠️  Persisted token expires in ${daysLeft} days — re-exchanging...`);
  }

  await refreshToken();
}

function getToken() {
  return currentToken;
}

module.exports = { initToken, checkAndRefreshToken, refreshToken, getToken };
