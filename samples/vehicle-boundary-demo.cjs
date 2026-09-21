'use strict';
/* Offline helper-boundary demonstration. Synthetic text only: no Telegram,
 * Google Cloud Vision, Google Sheets, database or production credentials.
 * The three helpers below are transcribed without logic changes from:
 * builtbyhuy/xuong-vinfast-phuc-loi, src/utils.js, source blob
 * 25aee5a21f2882934fa1f678aba2851f984a66d3 (reviewed 2026-09-21).
 * This is NOT the repository's full test suite or a live bot recording.
 */
const assert = require('node:assert/strict');
function normalizePlate(raw) {
  if (!raw) return '';
  let plate = raw.toUpperCase().trim();
  plate = plate.replace(/[^A-Z0-9]/g, '');
  const match1 = plate.match(/^(\d{2,3})([A-Z])(\d{3,5})$/);
  const match2 = plate.match(/^(\d{2,3})([A-Z][A-Z0-9])(\d{4,5})$/);
  const match = match1 || match2;
  if (match) { plate = `${match[1]}${match[2]}-${match[3]}`; }
  return plate;
}
function isValidVietnamPlate(plate) {
  if (!plate) return false;
  return /^\d{2,3}[A-Z][A-Z0-9]?-?\d{3,5}$/.test(plate);
}
function parseMessage(text) {
  if (!text) return { action: null, params: '' };
  const normalized = text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toUpperCase().trim();
  const raMatch = normalized.match(/^RA\s+(.+)$/);
  if (raMatch) {
    const plate = normalizePlate(raMatch[1]);
    if (plate) return { action: 'RA_MANUAL', params: plate };
  }
  let action = null;
  if (/^(TONKHO|TON KHO)$/.test(normalized)) { action = 'TONKHO'; }
  else if (/^(HELP|HUONGDAN|HUONG DAN)$/.test(normalized)) { action = 'HELP'; }
  else if (/^(BAOCAO|BAO CAO)$/.test(normalized)) { action = 'BAOCAO'; }
  else if (/^(NANGSUAT|NANG SUAT)$/.test(normalized)) { action = 'NANGSUAT'; }
  return { action, params: '' };
}
const checks = [
 ['normalizes synthetic plate text', () => assert.equal(normalizePlate('30a 123.45'), '30A-12345')],
 ['keeps normalized synthetic plate stable', () => assert.equal(normalizePlate('51F-45678'), '51F-45678')],
 ['handles empty text', () => assert.equal(normalizePlate(''), '')],
 ['rejects clearly invalid plate format', () => assert.equal(isValidVietnamPlate('NONSENSE'), false)],
 ['parses manual exit command', () => assert.deepEqual(parseMessage('ra 30a 123.45'), {action:'RA_MANUAL',params:'30A-12345'})],
 ['parses Vietnamese-accented inventory command', () => assert.equal(parseMessage('TỒN KHO').action, 'TONKHO')],
 ['does not invent a command from unknown text', () => assert.equal(parseMessage('unknown request').action, null)],
 ['documents parser/validator boundary', () => {
   const p=parseMessage('RA nonsense');
   assert.equal(p.action,'RA_MANUAL');
   assert.equal(isValidVietnamPlate(p.params),false);
 }],
];
let failures=0;
console.log('OFFLINE HELPER DEMO — SYNTHETIC INPUTS, NO LIVE SERVICES');
console.log('Runtime: '+process.version);
for(const [label,check] of checks){
 try{check();console.log('PASS: '+label);}catch(error){failures++;console.log('FAIL: '+label+' — '+error.message);}
}
console.log(`Result: ${checks.length-failures}/${checks.length} focused checks passed.`);
console.log('Limit: parsing a manual exit does not itself validate the plate. Downstream validation must be checked separately.');
console.log('Not tested: photo recognition, Telegram delivery, Sheets/Excel writes, full application behavior.');
process.exitCode=failures?1:0;
