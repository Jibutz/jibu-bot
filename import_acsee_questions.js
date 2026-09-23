'use strict';

// One-off importer: reads an ACSEE Q&A CSV (Subject, Form_Level, Topic,
// Question, Answer_Summary, Explanation - the format compile_acsee_biology.py
// and its future per-subject siblings produce) and creates records in the
// ACSEE_Questions Airtable table.
//
// Usage:
//   node import_acsee_questions.js necta-papers-acsee/biology_qa_final.csv
//
// The ACSEE_Questions table must already exist in Airtable before running
// this (the REST API this script uses can't create tables - only Airtable's
// Metadata API can, which needs a personal access token with schema-write
// scope we can't assume is configured). Create it once, manually, with
// these fields:
//   Subject          Single line text
//   Form_Level       Single line text   (kept for reference only - not
//                                         used for filtering; ACSEE content
//                                         is shared across Form 5 and 6)
//   Topic            Single line text
//   Question         Long text
//   Answer_Summary   Long text
//   Explanation      Long text
//
// Airtable's create() API accepts at most 10 records per call, so rows are
// batched with a short delay between batches to stay well under the rate
// limit.

require('dotenv').config();
const fs = require('fs');
const { base, ACSEE_QUESTIONS_TABLE } = require('./airtable');

const BATCH_SIZE = 10;
const BATCH_DELAY_MS = 250;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Minimal RFC4180 CSV parser - handles quoted fields, embedded commas,
 * escaped double-quotes (""), and embedded newlines within quoted fields.
 * No external dependency needed for a one-off import script.
 */
function parseCSV(text) {
  const rows = [];
  let row = [];
  let field = '';
  let inQuotes = false;
  let i = 0;

  while (i < text.length) {
    const char = text[i];

    if (inQuotes) {
      if (char === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i += 2;
          continue;
        }
        inQuotes = false;
        i++;
        continue;
      }
      field += char;
      i++;
      continue;
    }

    if (char === '"') {
      inQuotes = true;
      i++;
      continue;
    }
    if (char === ',') {
      row.push(field);
      field = '';
      i++;
      continue;
    }
    if (char === '\r') {
      i++;
      continue;
    }
    if (char === '\n') {
      row.push(field);
      rows.push(row);
      row = [];
      field = '';
      i++;
      continue;
    }
    field += char;
    i++;
  }
  // Last field/row - the file may or may not end with a trailing newline.
  if (field.length || row.length) {
    row.push(field);
    rows.push(row);
  }
  return rows;
}

function rowsToRecords(csvRows) {
  const [header, ...dataRows] = csvRows;
  return dataRows
    .filter(r => r.length === header.length && r.some(cell => cell.trim() !== ''))
    .map(r => {
      const fields = {};
      header.forEach((col, idx) => {
        fields[col] = r[idx];
      });
      return fields;
    });
}

async function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node import_acsee_questions.js <path-to-csv>');
    process.exit(1);
  }
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    process.exit(1);
  }

  // Strip a leading UTF-8 BOM if present (compile_acsee_biology.py writes
  // with encoding="utf-8-sig", which prepends one) - otherwise it corrupts
  // the first header cell into "﻿Subject" instead of "Subject".
  let text = fs.readFileSync(filePath, 'utf-8');
  if (text.charCodeAt(0) === 0xFEFF) text = text.slice(1);
  const csvRows = parseCSV(text);
  const records = rowsToRecords(csvRows);

  console.log(`Parsed ${records.length} rows from ${filePath}`);

  const table = base(ACSEE_QUESTIONS_TABLE);
  let created = 0;
  let failed = 0;

  for (let i = 0; i < records.length; i += BATCH_SIZE) {
    const batch = records.slice(i, i + BATCH_SIZE).map(r => ({
      fields: {
        Subject: r.Subject || '',
        Form_Level: r.Form_Level || '',
        Topic: r.Topic || '',
        Question: r.Question || '',
        Answer_Summary: r.Answer_Summary || '',
        Explanation: r.Explanation || '',
      },
    }));

    try {
      await table.create(batch);
      created += batch.length;
      console.log(`Created ${created}/${records.length}...`);
    } catch (err) {
      failed += batch.length;
      console.error(`Batch starting at row ${i} failed: ${err.message || err}`);
      if (err.error === 'NOT_FOUND' || /could not find table|table not found/i.test(err.message || '')) {
        console.error(
          `\nThe "${ACSEE_QUESTIONS_TABLE}" table doesn't exist yet in this Airtable base.\n` +
          `Create it first (see the field list in the comment at the top of this script), then re-run.\n`
        );
        process.exit(1);
      }
    }

    if (i + BATCH_SIZE < records.length) await sleep(BATCH_DELAY_MS);
  }

  console.log(`\nDone. Created ${created}, failed ${failed}, total ${records.length}.`);
  if (failed) process.exitCode = 1;
}

main().catch(err => {
  console.error('Import failed:', err);
  process.exit(1);
});
