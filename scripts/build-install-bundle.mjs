import assert from 'node:assert/strict';
import { cp, mkdir, readFile, rm, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const packageManifest = JSON.parse(await readFile(path.join(repositoryRoot, 'package.json'), 'utf8'));
const sourceRoot = path.join(repositoryRoot, 'agent');
const skillRoot = path.join(repositoryRoot, 'skills', packageManifest.name);
const distributionRoot = path.join(skillRoot, 'agent');

function assertSafeTarget(target) {
  const relative = path.relative(repositoryRoot, target);
  assert.ok(relative && !relative.startsWith('..') && !path.isAbsolute(relative), `Unsafe target: ${target}`);
  assert.equal(path.resolve(target), path.resolve(repositoryRoot, 'skills', packageManifest.name, 'agent'));
}

assertSafeTarget(distributionRoot);
assert.ok((await stat(sourceRoot)).isDirectory(), 'agent/ must exist before building the install bundle');
assert.ok((await stat(path.join(skillRoot, 'SKILL.md'))).isFile(), `skills/${packageManifest.name}/SKILL.md must exist`);

await rm(distributionRoot, { recursive: true, force: true });
await mkdir(skillRoot, { recursive: true });
await cp(sourceRoot, distributionRoot, { recursive: true, force: true });

process.stdout.write(`Install bundle synchronized: agent/ -> skills/${packageManifest.name}/agent/\n`);
