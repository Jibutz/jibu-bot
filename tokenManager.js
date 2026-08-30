/**
 * tokenManager.js
 *
 * Manages the WhatsApp / Meta long-lived access token.
 *
 * Strategy
 * ────────
 *  • On startup  → load the best available token (Airtable > env), immediately
 *                  exchange it for a 60-day long-lived token if it looks short.
 *  • Every day   → check days-remaining via debug_token.
 *  • At ≤ 10 days remaining (i.e. ~day 50 of a 60-day token) → proactive refresh.
 *  • After every refresh → persist to:
 *      1. In-process  : process.env.WHATSAPP_TOKEN
 *      2. Airtable    : Settings table  (Key = whatsapp_access_token / _expiry)
 *      3. Railway     : project env var WHATSAPP_TOKEN  (requires RAILWAY_TOKEN)
 */

'use strict';

const axios = require('axios');
const Airtable = require('airtable');

// ─── Constants ────────────────────────────────────────────────────────────────
const SETTINGS_TABLE  = 'Settings';
const TOKEN_KEY       = 'whatsapp_access_token';
const EXPIRY_KEY      = 'whatsapp_token_expiry';
const REFRESH_THRESHOLD_DAYS = 10;   // refresh when this many days remain (~day 50)
const GRAPH_VERSION   = 'v19.0';

// ─── In-process token state ───────────────────────────────────────────────────
let currentToken = process.env.WHATSAPP_TOKEN || '';
let currentExpiry = null; // epoch seconds, updated whenever the token is loaded/refreshed

// ─── Timestamp helper ─────────────────────────────────────────────────────────
function ts() {
  return new Date().toISOString();
}

// ─── Airtable helpers ─────────────────────────────────────────────────────────
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
    const tokenRecord  = records.find(r => r.fields.Key === TOKEN_KEY);
    const expiryRecord = records.find(r => r.fields.Key === EXPIRY_KEY);
    if (!tokenRecord?.fields.Value) return null;
    return {
      token:  tokenRecord.fields.Value,
      expiry: expiryRecord ? parseInt(expiryRecord.fields.Value, 10) : null,
    };
  } catch (err) {
    if (!err.message?.includes('TABLE_NOT_FOUND') && err.statusCode !== 404) {
      console.warn(`[${ts()}] ⚠️  Token load from Airtable failed:`, err.message);
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
        console.warn(`[${ts()}] ⚠️  Airtable "Settings" table not found — token will not persist across restarts.`);
        console.warn('   Fix: create a Settings table with "Key" (text) and "Value" (long text) fields.');
        return;
      }
      console.warn(`[${ts()}] ⚠️  Could not save ${key} to Airtable:`, err.message);
    }
  }
  console.log(`[${ts()}] ✅ Token saved to Airtable Settings table.`);
}

// ─── Railway API helper ───────────────────────────────────────────────────────
/**
 * Upserts WHATSAPP_TOKEN in the Railway project environment so the value
 * survives a redeploy.
 *
 * Required env vars (all provided automatically inside a Railway deployment
 * except RAILWAY_TOKEN which must be added manually):
 *   RAILWAY_TOKEN          — Railway API token (create at railway.app → Account Settings → Tokens)
 *   RAILWAY_PROJECT_ID     — auto-injected by Railway
 *   RAILWAY_SERVICE_ID     — auto-injected by Railway
 *   RAILWAY_ENVIRONMENT_ID — auto-injected by Railway  (usually the "production" env id)
 */
async function saveToRailway(token) {
  const railwayToken = process.env.RAILWAY_TOKEN;
  const projectId    = process.env.RAILWAY_PROJECT_ID;
  const serviceId    = process.env.RAILWAY_SERVICE_ID;
  const environmentId = process.env.RAILWAY_ENVIRONMENT_ID;

  if (!railwayToken) {
    console.warn(`[${ts()}] ⚠️  RAILWAY_TOKEN not set — skipping Railway env-var update.`);
    console.warn('   Add RAILWAY_TOKEN in Railway → project → Variables to enable persistent storage.');
    return false;
  }
  if (!projectId || !serviceId || !environmentId) {
    console.warn(`[${ts()}] ⚠️  Missing Railway IDs (PROJECT_ID/SERVICE_ID/ENVIRONMENT_ID) — skipping Railway update.`);
    return false;
  }

  const mutation = `
    mutation UpsertVariable($input: VariableUpsertInput!) {
      variableUpsert(input: $input)
    }
  `;

  const variables = {
    input: {
      projectId,
      serviceId,
      environmentId,
      name:  'WHATSAPP_TOKEN',
      value: token,
    },
  };

  try {
    const { data } = await axios.post(
      'https://backboard.railway.app/graphql/v2',
      { query: mutation, variables },
      {
        headers: {
          Authorization: `Bearer ${railwayToken}`,
          'Content-Type': 'application/json',
        },
        timeout: 10000,
      }
    );

    if (data.errors?.length) {
      const msg = data.errors.map(e => e.message).join('; ');
      console.error(`[${ts()}] ❌ Railway API error:`, msg);
      return false;
    }

    console.log(`[${ts()}] ✅ WHATSAPP_TOKEN updated in Railway environment variables.`);
    return true;
  } catch (err) {
    console.error(`[${ts()}] ❌ Railway API request failed:`, err.response?.data || err.message);
    return false;
  }
}

// ─── Graph API helpers ────────────────────────────────────────────────────────

/**
 * Inspect a token via Graph debug_token endpoint.
 * Returns { valid, daysLeft } or null if the check could not be performed.
 */
async function checkTokenExpiry(token) {
  const appId     = process.env.FACEBOOK_APP_ID;
  const appSecret = process.env.FACEBOOK_APP_SECRET;
  if (!appId || !appSecret) return null;
  try {
    const { data } = await axios.get(
      `https://graph.facebook.com/${GRAPH_VERSION}/debug_token`,
      { params: { input_token: token, access_token: `${appId}|${appSecret}` }, timeout: 10000 }
    );
    const info = data.data;
    if (!info.is_valid) return { valid: false, daysLeft: 0 };
    if (!info.expires_at || info.expires_at === 0) return { valid: true, daysLeft: Infinity };
    const daysLeft = Math.floor((info.expires_at - Date.now() / 1000) / 86400);
    return { valid: true, daysLeft };
  } catch (err) {
    console.warn(`[${ts()}] ⚠️  debug_token check failed:`, err.response?.data?.error?.message || err.message);
    return null;
  }
}

/**
 * Exchange a short-lived (or existing) token for a new 60-day long-lived token.
 * Returns { token, expiry } or null on failure.
 */
async function exchangeForLongLivedToken(token) {
  const appId     = process.env.FACEBOOK_APP_ID;
  const appSecret = process.env.FACEBOOK_APP_SECRET;
  if (!appId || !appSecret) {
    console.warn(`[${ts()}] ⚠️  FACEBOOK_APP_ID / FACEBOOK_APP_SECRET not set — cannot exchange token.`);
    return null;
  }
  try {
    const { data } = await axios.get(
      `https://graph.facebook.com/${GRAPH_VERSION}/oauth/access_token`,
      {
        params: {
          grant_type:       'fb_exchange_token',
          client_id:        appId,
          client_secret:    appSecret,
          fb_exchange_token: token,
        },
        timeout: 10000,
      }
    );
    // expires_in is in seconds; default to 60 days if not provided
    const expiresIn = data.expires_in || 60 * 86400;
    const expiry    = Math.floor(Date.now() / 1000) + expiresIn;
    const daysValid = Math.floor(expiresIn / 86400);
    console.log(`[${ts()}] 🔄 Graph API returned a new token valid for ~${daysValid} days.`);
    return { token: data.access_token, expiry };
  } catch (err) {
    const msg = err.response?.data?.error?.message || err.message;
    console.error(`[${ts()}] ❌ Token exchange with Graph API failed: ${msg}`);
    return null;
  }
}

// ─── Core refresh logic ───────────────────────────────────────────────────────

/**
 * Exchange the current token, then persist the new one everywhere.
 */
async function refreshToken() {
  console.log(`[${ts()}] 🔄 ──────────────────────────────────────────────`);
  console.log(`[${ts()}] 🔄 Starting WhatsApp token refresh...`);

  const result = await exchangeForLongLivedToken(currentToken);
  if (!result) {
    console.error(`[${ts()}] ❌ Token refresh aborted — keeping existing token.`);
    console.log(`[${ts()}] 🔄 ──────────────────────────────────────────────`);
    return false;
  }

  // 1. Update in-process memory
  currentToken = result.token;
  currentExpiry = result.expiry;
  process.env.WHATSAPP_TOKEN = currentToken;

  const daysLeft = Math.floor((result.expiry - Date.now() / 1000) / 86400);
  const expiryDate = new Date(result.expiry * 1000).toISOString().split('T')[0];
  console.log(`[${ts()}] ✅ New token obtained — valid for ~${daysLeft} days (expires ~${expiryDate}).`);

  // 2. Persist to Airtable
  await saveToAirtable(result.token, result.expiry);

  // 3. Persist to Railway env var (survives redeploy)
  await saveToRailway(result.token);

  console.log(`[${ts()}] 🔄 Token refresh complete. Next auto-refresh in ~${daysLeft - REFRESH_THRESHOLD_DAYS} days.`);
  console.log(`[${ts()}] 🔄 ──────────────────────────────────────────────`);
  return true;
}

// ─── Scheduled check (called by cron in index.js) ────────────────────────────

/**
 * Check the current token's expiry and refresh if within the threshold.
 * Called once per day by the cron job.
 */
async function checkAndRefreshToken() {
  console.log(`[${ts()}] 🔍 Daily token health check...`);

  const status = await checkTokenExpiry(currentToken);

  if (!status) {
    console.log(`[${ts()}] ℹ️  Token status unknown — set FACEBOOK_APP_ID + FACEBOOK_APP_SECRET to enable checks.`);
    return;
  }

  if (!status.valid) {
    console.error(`[${ts()}] ❌ Token is INVALID. Attempting emergency refresh...`);
    await refreshToken();
    return;
  }

  if (status.daysLeft === Infinity) {
    console.log(`[${ts()}] ✅ Token never expires — no refresh needed.`);
    return;
  }

  console.log(`[${ts()}] ✅ Token is valid — ~${status.daysLeft} day(s) remaining.`);

  if (status.daysLeft <= REFRESH_THRESHOLD_DAYS) {
    console.log(`[${ts()}] ⏰ Refresh threshold reached (≤${REFRESH_THRESHOLD_DAYS} days left) — refreshing now...`);
    await refreshToken();
  } else {
    const daysUntilRefresh = status.daysLeft - REFRESH_THRESHOLD_DAYS;
    console.log(`[${ts()}] 🗓️  Next scheduled refresh in ~${daysUntilRefresh} day(s) (when ${REFRESH_THRESHOLD_DAYS} days remain).`);
  }
}

// ─── Startup initialisation ───────────────────────────────────────────────────

/**
 * Called once at bot startup.
 *  1. Try to load a persisted long-lived token from Airtable.
 *  2. If the stored token is still healthy (> threshold), use it.
 *  3. Otherwise exchange the env-var token for a fresh 60-day token.
 */
async function initToken() {
  console.log(`[${ts()}] 🔑 ──────────────────────────────────────────────`);
  console.log(`[${ts()}] 🔑 Initialising WhatsApp token manager...`);

  if (!currentToken) {
    console.error(`[${ts()}] ❌ WHATSAPP_TOKEN env var is not set — cannot initialise token manager.`);
    console.log(`[${ts()}] 🔑 ──────────────────────────────────────────────`);
    return;
  }

  // Try Airtable first
  const stored = await loadFromAirtable();
  if (stored?.token && stored.expiry) {
    const daysLeft = Math.floor((stored.expiry - Date.now() / 1000) / 86400);
    const expiryDate = new Date(stored.expiry * 1000).toISOString().split('T')[0];
    console.log(`[${ts()}] 📦 Found persisted token in Airtable — ~${daysLeft} days remaining (expires ~${expiryDate}).`);

    if (daysLeft > REFRESH_THRESHOLD_DAYS) {
      currentToken = stored.token;
      currentExpiry = stored.expiry;
      process.env.WHATSAPP_TOKEN = currentToken;
      console.log(`[${ts()}] ✅ Using Airtable token — healthy, no exchange needed.`);
      console.log(`[${ts()}] 🔑 Token expiry: ${expiryDate} (~${daysLeft} days remaining)`);
      console.log(`[${ts()}] 🔑 ──────────────────────────────────────────────`);
      return;
    }
    console.log(`[${ts()}] ⚠️  Stored token expires in ${daysLeft} days — exchanging for fresh 60-day token...`);
  } else {
    console.log(`[${ts()}] ℹ️  No valid token in Airtable — exchanging env-var token for 60-day long-lived token...`);
  }

  // Exchange whatever we have for a fresh long-lived token
  await refreshToken();

  if (currentExpiry) {
    const expiryDate = new Date(currentExpiry * 1000).toISOString().split('T')[0];
    const daysLeft = Math.floor((currentExpiry - Date.now() / 1000) / 86400);
    console.log(`[${ts()}] 🔑 Token expiry: ${expiryDate} (~${daysLeft} days remaining)`);
  } else {
    console.log(`[${ts()}] 🔑 Token expiry: unknown (refresh failed or could not be determined)`);
  }
  console.log(`[${ts()}] 🔑 ──────────────────────────────────────────────`);
}

// ─── Accessor ─────────────────────────────────────────────────────────────────
function getToken() {
  return currentToken;
}

module.exports = { initToken, checkAndRefreshToken, refreshToken, getToken };
