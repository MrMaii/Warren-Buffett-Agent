import assert from 'node:assert/strict';
import { access, readFile, stat } from 'node:fs/promises';
import test from 'node:test';

const root = new URL('../', import.meta.url);

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
    await access(new URL(`agent/${skill.path}`, root));
    assert.ok(Array.isArray(skill.outputs) && skill.outputs.length > 0, `${skill.id} output contract`);
  }
});

test('README delivers the launch story and all required media', async () => {
  const readme = await readFile(new URL('README.md', root), 'utf8');
  const chinese = await readFile(new URL('README.zh-CN.md', root), 'utf8');

  for (const source of [readme, chinese]) {
    assert.match(source, /assets\/hero\.png/);
    assert.match(source, /assets\/poster\.png/);
    assert.match(source, /assets\/demo\.gif/);
    assert.match(source, /assets\/teaser\.gif/);
    assert.match(source, /repository-prequalified/);
    assert.match(source, /https:\/\/github\.com\/MrMaii\/Hall-of-Fame-Studio/);
  }

  const requiredAssets = [
    'assets/hero.png',
    'assets/poster.png',
    'assets/social-card.png',
    'assets/demo.gif',
    'assets/teaser.gif',
    'assets/diagrams/01-decision-lens.svg',
    'assets/diagrams/02-capability-clusters.svg',
    'assets/diagrams/03-mode-router.svg',
    'assets/diagrams/04-quality-loop.svg',
    'assets/diagrams/05-hall-of-fame-network.svg',
  ];
  for (const path of requiredAssets) {
    const info = await stat(new URL(path, root));
    assert.ok(info.size > 500, `${path} must be a real asset`);
  }
});

test('states product, status, financial, and identity boundaries', async () => {
  const readme = await readFile(new URL('README.md', root), 'utf8');
  const notice = await readFile(new URL('NOTICE.md', root), 'utf8');
  assert.match(readme, /not\s+(?:official\s+)?financial advice/i);
  assert.match(readme, /does not promise returns/i);
  assert.match(readme, /Part of <a href="https:\/\/github\.com\/MrMaii\/Hall-of-Fame-Studio">Hall of Fame Studio<\/a>/);
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
    'assets/diagrams/05-hall-of-fame-network.svg',
    'scripts/build-media.py',
  ];
  const text = (await Promise.all(files.map((path) => readFile(new URL(path, root), 'utf8')))).join('\n');
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
