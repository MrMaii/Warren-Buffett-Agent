import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { access, readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { buildSourceFingerprint } from './fingerprint.mjs';

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const agentRoot = path.join(repositoryRoot, 'agent');
const installSkillRoot = path.join(repositoryRoot, 'skills', 'warren-buffett-agent');
const installAgentRoot = path.join(installSkillRoot, 'agent');
const expectedFingerprint = 'sha256:4736e707ef1e4a851cee104822598af6246b9f3a89038a42a261cced898ab448';

async function listFiles(root, relativeDirectory = '') {
  const directory = path.join(root, relativeDirectory);
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries.sort((left, right) => left.name.localeCompare(right.name))) {
    const relativePath = path.join(relativeDirectory, entry.name);
    if (entry.isDirectory()) files.push(...await listFiles(root, relativePath));
    else if (entry.isFile()) files.push(relativePath.split(path.sep).join('/'));
  }
  return files;
}

function sha256(content) {
  return createHash('sha256').update(content).digest('hex');
}

function resolveInsideAgent(relativePath) {
  const resolved = path.resolve(agentRoot, String(relativePath || ''));
  const relative = path.relative(agentRoot, resolved);
  assert.ok(relative && !relative.startsWith('..') && !path.isAbsolute(relative), `Unsafe path: ${relativePath}`);
  return resolved;
}

const manifest = JSON.parse(await readFile(path.join(agentRoot, 'agent.json'), 'utf8'));
assert.equal(manifest.personaSlug, 'buffett');
assert.equal(manifest.skills.length, 12);

const installSkill = await readFile(path.join(installSkillRoot, 'SKILL.md'), 'utf8');
assert.match(installSkill, /^name:\s*warren-buffett-agent$/m);
assert.match(installSkill, /agent\/RUNTIME\.md/);
const canonicalFiles = await listFiles(agentRoot);
const installFiles = await listFiles(installAgentRoot);
assert.deepEqual(installFiles, canonicalFiles, 'Install distribution file set drifted from agent/');
for (const relativePath of canonicalFiles) {
  const canonical = await readFile(path.join(agentRoot, relativePath));
  const installed = await readFile(path.join(installAgentRoot, relativePath));
  assert.equal(sha256(installed), sha256(canonical), `Install distribution drift: ${relativePath}`);
}

for (const relativePath of [
  'assets/source/hero-master.png',
  'assets/source/poster-master.png',
  'assets/hero.png',
  'assets/poster.png',
  'assets/social-card.png',
  'assets/demo.gif',
  'assets/teaser.gif',
  'assets/install.gif',
  'assets/README.md',
]) {
  const info = await stat(path.join(repositoryRoot, relativePath));
  assert.ok(info.size > 500, `${relativePath} must be a real release asset`);
}

const diagramPaths = [
  'assets/diagrams/01-method-lens.svg',
  'assets/diagrams/02-evidence-chain.svg',
  'assets/diagrams/03-capability-clusters.svg',
  'assets/diagrams/04-mode-router.svg',
  'assets/diagrams/05-quality-loop.svg',
  'assets/diagrams/06-studio-network.svg',
];

for (const relativePath of diagramPaths) {
  const info = await stat(path.join(repositoryRoot, relativePath));
  assert.ok(info.size > 500, `${relativePath} must be a real diagram`);
  const diagram = await readFile(path.join(repositoryRoot, relativePath), 'utf8');
  assert.match(diagram, /url\(#glass\)/, `${relativePath} must use the shared frosted-glass surface`);
  assert.match(diagram, /#c5a875/, `${relativePath} must use the shared bronze palette`);
  assert.doesNotMatch(diagram, /#7dd3fc|#a5b4fc|#818cf8|#c084fc|#38bdf8/, `${relativePath} contains stale blue AI styling`);
}

const archivePlate = await readFile(path.join(repositoryRoot, 'assets/source/hero-master.png'));
const compatibilityPlate = await readFile(path.join(repositoryRoot, 'assets/source/poster-master.png'));
assert.equal(archivePlate.equals(compatibilityPlate), true, 'Source masters must be identical Archive Plates');
for (const relativePath of ['assets/hero.png', 'assets/poster.png', 'assets/social-card.png']) {
  const output = await readFile(path.join(repositoryRoot, relativePath));
  assert.equal(output.equals(archivePlate), true, `${relativePath} must preserve the supplied Archive Plate`);
}

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
  const images = [...readme.matchAll(/<img src="([^"]+)"/g)].map((match) => match[1]);
  assert.equal(images.filter((image) => image === './assets/install.gif').length, 1, `${readmeName} must show the install motion once`);
  assert.equal(images.filter((image) => image === './assets/hero.png').length, 1, `${readmeName} must show the primary plate once`);
  assert.equal(images.filter((image) => /poster|social-card|demo|teaser/.test(image)).length, 0, `${readmeName} must not repeat plate variants`);
  assert.equal(images.filter((image) => image.includes('./assets/diagrams/')).length, 6, `${readmeName} must show six unique diagrams`);
  assert.equal(new Set(images).size, images.length, `${readmeName} must not repeat a visual element`);
  const installIndex = readme.indexOf('./assets/install.gif');
  const firstDiagramIndex = readme.indexOf('./assets/diagrams/01-method-lens.svg');
  assert.ok(installIndex >= 0 && installIndex < firstDiagramIndex, `${readmeName} must lead with installation before professional analysis`);
  assert.match(readme, /gh skill install MrMaii\/Warren-Buffett-Agent warren-buffett-agent/);
  assert.doesNotMatch(readme, /Install it as a Codex Skill|安装为 Codex Skill/);
}

const installConfig = JSON.parse(await readFile(path.join(repositoryRoot, 'assets/install-motion.json'), 'utf8'));
assert.equal(installConfig.repository, 'MrMaii/Warren-Buffett-Agent');
assert.equal(installConfig.skill_name, 'warren-buffett-agent');
assert.equal(installConfig.output, 'assets/install.gif');

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
  `Diagrams: ${diagramPaths.length}`,
  `Install bundle files: ${installFiles.length}`,
  `Source fingerprint: ${fingerprint.sourceFingerprint}`,
  '',
].join('\n'));
