import assert from 'node:assert/strict';
import { access, readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { buildSourceFingerprint } from './fingerprint.mjs';

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const agentRoot = path.join(repositoryRoot, 'agent');
const expectedFingerprint = 'sha256:4736e707ef1e4a851cee104822598af6246b9f3a89038a42a261cced898ab448';

function resolveInsideAgent(relativePath) {
  const resolved = path.resolve(agentRoot, String(relativePath || ''));
  const relative = path.relative(agentRoot, resolved);
  assert.ok(relative && !relative.startsWith('..') && !path.isAbsolute(relative), `Unsafe path: ${relativePath}`);
  return resolved;
}

const manifest = JSON.parse(await readFile(path.join(agentRoot, 'agent.json'), 'utf8'));
assert.equal(manifest.personaSlug, 'buffett');
assert.equal(manifest.skills.length, 12);

const references = [
  manifest.projectDocument,
  manifest.runtimeDocument,
  manifest.runtimeQualityModule,
  manifest.identityDocument,
  manifest.voiceDocument,
  manifest.relationshipDocument,
  manifest.charismaDocument,
  manifest.researchDocument,
  manifest.sourceRegister,
  manifest.observationCorpus,
  manifest.claimLedger,
  manifest.skillMarketAudit,
  manifest.integrationDocument,
  ...(manifest.behaviorDocuments || []).map((document) => document.path),
  ...(manifest.skills || []).map((skill) => skill.path),
];

for (const relativePath of references) await access(resolveInsideAgent(relativePath));

for (const readmeName of ['README.md', 'README.zh-CN.md']) {
  const readme = await readFile(path.join(repositoryRoot, readmeName), 'utf8');
  const relativeLinks = new Set([
    ...[...readme.matchAll(/(?:src|href)="(\.\/[^"#?]+)(?:[#?][^"]*)?"/g)].map((match) => match[1]),
    ...[...readme.matchAll(/\]\((\.\/[^)#?]+)(?:[#?][^)]*)?\)/g)].map((match) => match[1]),
  ]);
  for (const relativeLink of relativeLinks) {
    await access(path.resolve(repositoryRoot, relativeLink));
  }
}

const requiredSkillSections = [
  '## Inputs',
  '## Method',
  '## Output contract',
  '## Stop and escalate',
  '## Self-review',
];

for (const skill of manifest.skills) {
  const source = await readFile(resolveInsideAgent(skill.path), 'utf8');
  assert.match(source, new RegExp(`^name:\\s*${skill.id}\\s*$`, 'm'), `${skill.id} frontmatter`);
  for (const section of requiredSkillSections) {
    assert.ok(source.includes(section), `${skill.id} is missing ${section}`);
  }
}

const runtime = await readFile(resolveInsideAgent(manifest.runtimeDocument), 'utf8');
assert.ok(runtime.length <= 7000, `RUNTIME.md exceeds the 7,000-character limit: ${runtime.length}`);

const sourceRegister = JSON.parse(await readFile(resolveInsideAgent(manifest.sourceRegister), 'utf8'));
const claimLedger = JSON.parse(await readFile(resolveInsideAgent(manifest.claimLedger), 'utf8'));
const observations = (await readFile(resolveInsideAgent(manifest.observationCorpus), 'utf8'))
  .split(/\r?\n/)
  .filter(Boolean);

assert.ok(sourceRegister.sources.length >= 40, 'Expected at least 40 registered sources');
assert.ok(observations.length >= 50, 'Expected at least 50 atomic observations');
assert.ok(claimLedger.claims.length >= 10, 'Expected at least 10 behavior claims');

const fingerprint = await buildSourceFingerprint();
assert.equal(fingerprint.sourceFingerprint, expectedFingerprint, 'Candidate source fingerprint changed');

process.stdout.write([
  'Warren Buffett Agent package: valid',
  `Skills: ${manifest.skills.length}`,
  `Sources: ${sourceRegister.sources.length}`,
  `Atomic observations: ${observations.length}`,
  `Behavior claims: ${claimLedger.claims.length}`,
  `Runtime characters: ${runtime.length}/7000`,
  `Source fingerprint: ${fingerprint.sourceFingerprint}`,
  '',
].join('\n'));
