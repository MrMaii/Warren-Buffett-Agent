import assert from 'node:assert/strict';
import { access, readFile, readdir, stat } from 'node:fs/promises';
import test from 'node:test';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = new URL('../', import.meta.url);
const rootPath = fileURLToPath(root);
const diagramPaths = [
  'assets/diagrams/01-method-lens.svg',
  'assets/diagrams/02-evidence-chain.svg',
  'assets/diagrams/03-capability-clusters.svg',
  'assets/diagrams/04-mode-router.svg',
  'assets/diagrams/05-quality-loop.svg',
  'assets/diagrams/06-studio-network.svg',
];

test('publishes a real installable Agent entrypoint', async () => {
  const skill = await readFile(new URL('skills/warren-buffett-agent/SKILL.md', root), 'utf8');
  assert.match(skill, /^name:\s*warren-buffett-agent$/m);
  assert.match(skill, /agent\/RUNTIME\.md/);
  assert.match(skill, /relational/);
  assert.match(skill, /high-stakes/);
  assert.match(skill, /one to three routed Skills/);
});

async function listFiles(directory, relativeDirectory = '') {
  const entries = await readdir(path.join(directory, relativeDirectory), { withFileTypes: true });
  const files = [];
  for (const entry of entries.sort((left, right) => left.name.localeCompare(right.name))) {
    const relativePath = path.join(relativeDirectory, entry.name);
    if (entry.isDirectory()) files.push(...await listFiles(directory, relativePath));
    else if (entry.isFile()) files.push(relativePath.split(path.sep).join('/'));
  }
  return files;
}

test('ships a byte-equivalent full-Agent install distribution', async () => {
  const canonicalRoot = path.join(rootPath, 'agent');
  const distributionRoot = path.join(rootPath, 'skills', 'warren-buffett-agent', 'agent');
  const canonicalFiles = await listFiles(canonicalRoot);
  assert.deepEqual(await listFiles(distributionRoot), canonicalFiles);
  for (const relativePath of canonicalFiles) {
    const canonical = await readFile(path.join(canonicalRoot, relativePath));
    const distribution = await readFile(path.join(distributionRoot, relativePath));
    assert.equal(distribution.equals(canonical), true, `distribution drift: ${relativePath}`);
  }
  await access(path.join(distributionRoot, 'RUNTIME.md'));
  await access(path.join(distributionRoot, 'AGENT.md'));
});

test('packages the complete twelve-Skill candidate', async () => {
  const manifest = JSON.parse(await readFile(new URL('agent/agent.json', root), 'utf8'));
  assert.equal(manifest.personaSlug, 'buffett');
  assert.equal(manifest.skills.length, 12);
  for (const skill of manifest.skills) {
    await access(new URL('agent/' + skill.path, root));
    assert.ok(Array.isArray(skill.outputs) && skill.outputs.length > 0, skill.id + ' output contract');
  }
});

test('README delivers the launch story and the unified Archive Plate media', async () => {
  const readme = await readFile(new URL('README.md', root), 'utf8');
  const chinese = await readFile(new URL('README.zh-CN.md', root), 'utf8');

  for (const [label, source] of [['English', readme], ['Chinese', chinese]]) {
    assert.match(source, /Archive Plate/);
    assert.match(source, /3:2/);
    assert.match(source, /assets\/hero\.png/);
    assert.match(source, /assets\/README\.md/);
    assert.match(source, /diagrams:build/);
    assert.match(source, /repository-prequalified/);
    assert.match(source, /https:\/\/github\.com\/MrMaii\/Hall-of-Fame-Studio/);
    const images = [...source.matchAll(/<img src="([^"]+)"/g)].map((match) => match[1]);
    const diagrams = images.filter((image) => image.includes('./assets/diagrams/'));
    assert.equal(images.filter((image) => image === './assets/install.gif').length, 1, label + ' README must show the install motion once');
    assert.equal(images.filter((image) => image === './assets/hero.png').length, 1, label + ' README must show the primary plate once');
    assert.equal(images.filter((image) => /poster|social-card|demo|teaser/.test(image)).length, 0, label + ' README must not repeat plate variants');
    assert.equal(new Set(images).size, images.length, label + ' README must not repeat a visual element');
    assert.deepEqual([...diagrams].sort(), diagramPaths.map((path) => './' + path).sort(), label + ' README must contain the shared six diagrams');
    const pasteHeading = label === 'English' ? '## Paste into your Agent' : '## 粘贴到你的 Agent';
    const analysisHeading = label === 'English' ? '## What this Agent is' : '## 这是什么';
    assert.ok(source.indexOf('./assets/install.gif') < source.indexOf(pasteHeading), label + ' install motion must precede the paste instruction');
    assert.ok(source.indexOf(pasteHeading) < source.indexOf(analysisHeading), label + ' user path must precede professional analysis');
    assert.match(source, /Install MrMaii\/Warren-Buffett-Agent as a user-level Agent Skill for this agent\./);
    assert.match(source, /gh skill preview MrMaii\/Warren-Buffett-Agent warren-buffett-agent/);
    assert.match(source, /gh skill install MrMaii\/Warren-Buffett-Agent warren-buffett-agent/);
    assert.doesNotMatch(source, /Install it as a Codex Skill|安装为 Codex Skill/);
    for (const diagram of diagrams) {
      await readFile(new URL(diagram.replace(/^\.\//, ''), root), 'utf8');
    }
    assert.match(
      source,
      /<a href="https:\/\/github\.com\/MrMaii\/Hall-of-Fame-Studio">\s*<img src="\.\/assets\/diagrams\/06-studio-network\.svg"/,
      label + ' Hall of Fame network view must link to the main project',
    );
  }

  const requiredAssets = [
    'assets/source/hero-master.png',
    'assets/source/poster-master.png',
    'assets/hero.png',
    'assets/poster.png',
    'assets/social-card.png',
    'assets/demo.gif',
    'assets/teaser.gif',
    'assets/install.gif',
    'assets/README.md',
    ...diagramPaths,
  ];
  for (const relativePath of requiredAssets) {
    const info = await stat(new URL(relativePath, root));
    assert.ok(info.size > 500, relativePath + ' must be a real asset');
  }

  const sourceMaster = await readFile(new URL('assets/source/hero-master.png', root));
  const compatibilityMaster = await readFile(new URL('assets/source/poster-master.png', root));
  assert.equal(sourceMaster.equals(compatibilityMaster), true, 'source masters must be identical Archive Plates');
  for (const relativePath of ['assets/hero.png', 'assets/poster.png', 'assets/social-card.png']) {
    const output = await readFile(new URL(relativePath, root));
    assert.equal(output.equals(sourceMaster), true, relativePath + ' must preserve the supplied Archive Plate');
  }
});

test('publishes a deterministic looping universal-Agent install motion', async () => {
  const config = JSON.parse(await readFile(new URL('assets/install-motion.json', root), 'utf8'));
  assert.equal(config.repository, 'MrMaii/Warren-Buffett-Agent');
  assert.equal(config.skill_name, 'warren-buffett-agent');
  assert.equal(config.output, 'assets/install.gif');
  const builder = await readFile(new URL('scripts/build-install-gif.py', root), 'utf8');
  assert.match(builder, /Agent Skills compatible/);
  assert.match(builder, /PASTE INTO YOUR AGENT/);
  const gif = await readFile(new URL('assets/install.gif', root));
  assert.equal(gif.subarray(0, 6).toString('ascii'), 'GIF89a');
  assert.equal(gif.readUInt16LE(6), 960);
  assert.equal(gif.readUInt16LE(8), 640);
  assert.ok(gif.includes(Buffer.from('NETSCAPE2.0')), 'GIF must contain the infinite-loop extension');
  assert.ok(gif.length > 100_000, 'install motion must be a real animation');
});

test('states product, status, financial, and identity boundaries', async () => {
  const readme = await readFile(new URL('README.md', root), 'utf8');
  const notice = await readFile(new URL('NOTICE.md', root), 'utf8');
  assert.match(readme, /not\s+(?:official\s+)?financial advice/i);
  assert.match(readme, /does not promise returns/i);
  assert.match(readme, /Hall of Fame Studio/);
  assert.match(notice, /not\s+affiliated with[\s\S]*Warren Buffett/i);
  assert.match(notice, /Berkshire Hathaway/);
});

test('uses the canonical Hall of Fame Studio name everywhere in release text', async () => {
  const files = [
    'README.md',
    'README.zh-CN.md',
    'skills/warren-buffett-agent/SKILL.md',
    'docs/QUALIFICATION.md',
    'docs/HALL-OF-FAME-STUDIO.md',
    'assets/README.md',
    'assets/diagrams/06-studio-network.svg',
    'scripts/build-media.py',
  ];
  const text = (await Promise.all(files.map((relativePath) => readFile(new URL(relativePath, root), 'utf8')))).join('\n');
  const forbiddenBrand = new RegExp([['Holo', 'Fame'].join(''), ['Holo', ' ', 'Fame'].join('')].join('|'), 'i');
  assert.doesNotMatch(text, forbiddenBrand);
  assert.match(text, /Hall of Fame Studio/);
});

test('contains no stale Steve Jobs packaging copy', async () => {
  const surfaces = [
    await readFile(new URL('skills/warren-buffett-agent/SKILL.md', root), 'utf8'),
    await readFile(new URL('package.json', root), 'utf8'),
    await readFile(new URL('NOTICE.md', root), 'utf8'),
  ].join('\n');
  assert.doesNotMatch(surfaces, /Steve Jobs|Apple Inc\.|Pixar/);
});

test('uses the shared frosted-glass diagram language without stale blue styling', async () => {
  for (const relativePath of diagramPaths) {
    const diagram = await readFile(new URL(relativePath, root), 'utf8');
    assert.match(diagram, /url\(#glass\)/, relativePath + ' must use the shared frosted-glass surface');
    assert.match(diagram, /#c5a875/, relativePath + ' must use the shared bronze palette');
    assert.doesNotMatch(diagram, /#7dd3fc|#a5b4fc|#818cf8|#c084fc|#38bdf8/, relativePath + ' contains stale blue AI styling');
  }
});
