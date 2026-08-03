# Qualification boundary

## Current public status

`repository-prequalified`

The Hall of Fame Studio Foundry validator reports:

```text
PASS buffett against buffett-plus-v1
Repository prequalified. Director qualification is still required.
```

The candidate contains:

- 46 registered sources;
- 56 atomic observations;
- 11 behavior claims;
- 12 callable hard Skills;
- a 2,582-character runtime constitution;
- a persona-owned neutral quality-gate interface;
- source fingerprint `sha256:4736e707ef1e4a851cee104822598af6246b9f3a89038a42a261cced898ab448`.

## What the status means

Repository prequalification means the package meets the reusable Foundry floor
for evidence, human-core documents, Skills, runtime modes, traceability, safety,
and standalone packaging. It is ready for human testing.

It does not mean:

- Warren Buffett has been reproduced or endorsed the project;
- a human Director has issued `pass`;
- every live model will produce the same behavior;
- the Agent may provide current investment authority or promise returns;
- a standalone repository replaces integration with Hall of Fame Studio.

## Remaining human gates

The Foundry workflow reserves final acceptance for:

1. name-blind distinctiveness against at least two contrast Agents;
2. a continuous real ChatBox conversation with ordinary, vulnerable,
   exploratory, correction, cross-domain, professional, and third-Agent turns;
3. material project-team lead/reviewer/handoff trials;
4. a human Director verdict of `pass`, `rework`, or `reject`.

Automated checks may reject. They may not issue the personality verdict.

## Reproduce repository checks

```bash
npm run validate
npm run fingerprint
npm test
```

Any change under `agent/` creates a new candidate and must publish a new
fingerprint, regression evidence, and qualification status.
