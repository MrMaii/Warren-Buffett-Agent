import { createHash } from 'node:crypto';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const agentRoot = path.join(repositoryRoot, 'agent');

function safeAgentPath(relativePath) {
  const resolved = path.resolve(agentRoot, String(relativePath || ''));
  const relative = path.relative(agentRoot, resolved);
  if (!relative || relative.startsWith('..') || path.isAbsolute(relative)) {
    throw new Error(`Agent path escapes or resolves to the package root: ${relativePath}`);
  }
  return resolved;
}

async function walkFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await walkFiles(absolute));
    else if (entry.isFile()) files.push(absolute);
  }
  return files;
}

export async function collectRuntimeSourceFiles() {
  const manifest = JSON.parse(await readFile(path.join(agentRoot, 'agent.json'), 'utf8'));
  const fixedPaths = [
    'persona.json',
    'prompt.md',
    'memory.md',
    'examples.md',
    'regression.json',
    'agent.json',
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
  ];

  const files = new Set(fixedPaths.map(safeAgentPath));
  for (const skill of manifest.skills || []) {
    const skillFile = safeAgentPath(skill.path);
    for (const file of await walkFiles(path.dirname(skillFile))) files.add(file);
  }

  return [...files]
    .map((absolute) => path.relative(agentRoot, absolute).replaceAll('\\', '/'))
    .sort();
}

export async function buildSourceFingerprint() {
  const digest = createHash('sha256');
  const sourceFiles = await collectRuntimeSourceFiles();
  for (const relativePath of sourceFiles) {
    digest.update(relativePath, 'utf8');
    digest.update('\0');
    digest.update(await readFile(path.join(agentRoot, relativePath)));
    digest.update('\0');
  }
  return {
    sourceFiles,
    sourceFingerprint: `sha256:${digest.digest('hex')}`,
  };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const result = await buildSourceFingerprint();
  process.stdout.write(`${result.sourceFingerprint}\n`);
}
