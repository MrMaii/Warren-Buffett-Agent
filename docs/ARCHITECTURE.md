# Architecture

The repository separates the candidate Agent from its public release surface.

```text
public entrypoint
  SKILL.md
      ↓
compact runtime
  agent/RUNTIME.md
      ↓
routing manifest
  agent/agent.json ──→ agent/skills/*/SKILL.md
      ↓
deep integration
  agent/AGENT.md + behavior/* + research/*
      ↓
response governance
  agent/runtime/qualityGate.js
```

## Loading policy

- Always load `RUNTIME.md`.
- Load one to three Skill files only for a concrete task.
- Load deep behavior files for long-form integration or review.
- Load research files for authoring and audit, not conversational decoration.
- Run the quality gate before response release when the host supports it.

## Trust boundary

The Agent definition has no API keys, remote calls, broker connection, or trade
executor. Current financial facts belong to the host's evidence layer. External
writes and transactions require separate explicit authority.

## Fingerprint boundary

`scripts/fingerprint.mjs` hashes the complete runtime candidate, including the
manifest, runtime, behavior, research ledgers, quality gate, and Skill packages.
README and campaign changes do not silently rewrite the candidate.
