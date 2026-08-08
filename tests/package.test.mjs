import assert from 'node:assert/strict';
import { access, readFile, stat } from 'node:fs/promises';
import test from 'node:test';

const root = new URL('../', import.meta.url);
const diagramPaths = [
  'assets/diagrams/01-method-lens.svg',
  'assets/diagrams/02-evidence-chain.svg',
  'assets/diagrams/03-capability-clusters.svg',
  'assets/diagrams/04-mode-router.svg',
  'assets/diagrams/05-quality-loop.svg',
  'assets/diagrams/06-studio-network.svg',
];

test('publishes a real installable Agent entrypoint', async () => {
  const skill = await readFile(new URL('SKILL.md', root), 'utf8');
  assert.match(skill, /^name:\s*warren-buffett-agent$/m);
  assert.match(skill, /agent\/RUNTIME\.md/);
  assert.match(skill, /relational/);
  assert.match(skill, /high-stakes/);
  assert.match(skill, /one to three routed Skills/);
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
    assert.equal(images.filter((image) => image === './assets/hero.png').length, 1, label + ' README must show the primary plate once');
    assert.equal(images.filter((image) => /poster|social-card|demo|teaser/.test(image)).length, 0, label + ' README must not repeat plate variants');
    assert.equal(new Set(images).size, images.length, label + ' README must not repeat a visual element');
    assert.deepEqual([...diagrams].sort(), diagramPaths.map((path) => './' + path).sort(), label + ' README must contain the shared six diagrams');
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
    'SKILL.md',
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
    await readFile(new URL('SKILL.md', root), 'utf8'),
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
