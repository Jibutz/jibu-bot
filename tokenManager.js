/**
 * tokenManager.js
 *
 * Manages the WhatsApp / Meta access token.
 *
 * Strategy
 * ────────
 *  The bot uses a Meta System User access token (created in Meta Business
 *  Settings), which does not expire and cannot be auto-refreshed via the
 *  Graph API the way a temporary token can. There is therefore no refresh
 *  logic here — only visibility:
 *
 *   • On startup  → ping the Graph API with the current token and log
 *                   clearly whether it is valid or expired.
 *   • Every day   → repeat that ping via cron (see index.js) and log
 *                   "TOKEN HEALTHY" or "TOKEN EXPIRED — ACTION NEEDED" so a
 *                   dead token is visible in the Railway logs immediately
 *                   instead of surfacing only as failed message sends.
 *
 *  If the ping ever reports expired, generate a new System User token in
 *  Meta Business Settings and set it as WHATSAPP_TOKEN in Railway.
 */

'use strict';

const axios = require('axios');

// ─── Constants ────────────────────────────────────────────────────────────────
const GRAPH_VERSION    = 'v19.0';
const PHONE_NUMBER_ID  = process.env.WHATSAPP_PHONE_NUMBER_ID;

// ─── In-process token state ───────────────────────────────────────────────────
const currentToken = process.env.WHATSAPP_TOKEN || '';

// ─── Timestamp helper ─────────────────────────────────────────────────────────
function ts() {
  return new Date().toISOString();
}

// ─── Graph API ping ───────────────────────────────────────────────────────────
/**
 * Makes a minimal, side-effect-free Graph API call using the current token
 * to confirm Meta still accepts it.
 * Returns { ok: true } or { ok: false, status, message }.
 */
async function pingGraphApi(token) {
  if (!token) {
    return { ok: false, status: null, message: 'WHATSAPP_TOKEN is not set' };
  }
  if (!PHONE_NUMBER_ID) {
    return { ok: false, status: null, message: 'WHATSAPP_PHONE_NUMBER_ID is not set' };
  }
  try {
    await axios.get(`https://graph.facebook.com/${GRAPH_VERSION}/${PHONE_NUMBER_ID}`, {
      params: { access_token: token, fields: 'display_phone_number' },
      timeout: 10000,
    });
    return { ok: true };
  } catch (err) {
    return {
      ok: false,
      status: err.response?.status ?? null,
      message: err.response?.data?.error?.message || err.message,
    };
  }
}

// ─── Startup check ────────────────────────────────────────────────────────────
/**
 * Called once at bot startup. Logs plainly whether the configured token is
 * currently accepted by Meta, so a dead token shows up in the Railway logs
 * right away instead of surfacing only when a message fails to send.
 */
async function initToken() {
  console.log(`[${ts()}] 🔑 ──────────────────────────────────────────────`);
  console.log(`[${ts()}] 🔑 Checking WhatsApp System User token...`);

  const result = await pingGraphApi(currentToken);
  if (result.ok) {
    console.log(`[${ts()}] ✅ TOKEN VALID — Meta accepted the current WHATSAPP_TOKEN.`);
  } else {
    console.error(`[${ts()}] ❌ TOKEN EXPIRED — ACTION NEEDED (status ${result.status}): ${result.message}`);
    console.error(`[${ts()}] ❌ Generate a new permanent System User token in Meta Business Settings and set it as WHATSAPP_TOKEN in Railway.`);
  }
  console.log(`[${ts()}] 🔑 ──────────────────────────────────────────────`);
}

// ─── Daily health check (called by cron in index.js) ─────────────────────────
/**
 * Sends a test ping to Meta's API and logs the token's health, once per day.
 */
async function checkAndRefreshToken() {
  console.log(`[${ts()}] 🔍 Daily token health check...`);

  const result = await pingGraphApi(currentToken);
  if (result.ok) {
    console.log(`[${ts()}] ✅ TOKEN HEALTHY`);
  } else {
    console.error(`[${ts()}] ❌ TOKEN EXPIRED — ACTION NEEDED (status ${result.status}): ${result.message}`);
    console.error(`[${ts()}] ❌ Generate a new permanent System User token in Meta Business Settings and set it as WHATSAPP_TOKEN in Railway.`);
  }
}

// ─── Accessor ─────────────────────────────────────────────────────────────────
function getToken() {
  return currentToken;
}

module.exports = { initToken, checkAndRefreshToken, getToken };
