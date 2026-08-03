import { readFile } from 'node:fs/promises';

import { evaluateBehavior } from '../agent/runtime/qualityGate.js';

function argument(name) {
  const index = process.argv.indexOf(`--${name}`);
  return index >= 0 ? process.argv[index + 1] : '';
}

async function textValue(name) {
  const file = argument(`${name}-file`);
  if (file) return readFile(file, 'utf8');
  return argument(name);
}

const user = await textValue('user');
const draft = await textValue('draft');
const context = await textValue('context');

if (!user || !draft) {
  process.stderr.write(
    'Usage: node scripts/check-response.mjs --user "..." --draft "..."\n'
    + '       Add --context "..." or use --user-file/--draft-file/--context-file.\n',
  );
  process.exitCode = 2;
} else {
  const violations = evaluateBehavior(user, draft, context);
  if (violations.length === 0) {
    process.stdout.write('PASS: no Warren Buffett quality-gate violations detected.\n');
  } else {
    process.stdout.write(`REWORK: ${violations.length} violation(s)\n`);
    for (const violation of violations) process.stdout.write(`- ${violation}\n`);
    process.exitCode = 1;
  }
}
