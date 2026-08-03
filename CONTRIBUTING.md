# Contributing

Thank you for helping improve the Warren Buffett Deep Agent.

## Governing rule

A personality change is a behavior change, not a prose preference. Preserve:

```text
source → atomic observation → behavior claim → runtime rule → test → observed behavior
```

Do not add a quotation, anecdote, catchphrase, costume cue, investment slogan,
or generic “wise elder” adjective as a shortcut.

## Change boundaries

- `agent/` is the verified candidate source. Editing it creates a new candidate
  and invalidates the published source fingerprint.
- Distribution-only work belongs in `SKILL.md`, `README*`, `docs/`, `assets/`,
  `scripts/`, or root `tests/`.
- A new Skill needs inputs, method, named output, STOP conditions, self-review,
  and a realistic test.
- A quality-gate change starts with a failing regression.
- Do not weaken current-data, downside, attribution, dignity, specialist-review,
  or no-guarantee boundaries to make an answer sound decisive.

## Before a pull request

```bash
npm run validate
npm run fingerprint
npm test
```

If `agent/` changed, explain the observed failure, responsible upstream file,
evidence and counter-boundary, new regression, real conversation path, and new
source fingerprint.

Automated checks may return `repository-prequalified`. Only a human Director
may record `pass`, `rework`, or `reject`.
