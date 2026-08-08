# Warren Buffett Deep Agent

<p align="center">
  <img src="./assets/hero.png" alt="Warren Buffett / Hall of Fame Studio Agent-002 Archive Plate" width="100%">
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a>
  ·
  <a href="./docs/QUALIFICATION.md">Qualification evidence</a>
  ·
  <a href="./assets/README.md">Visual system</a>
  ·
  <a href="https://github.com/MrMaii/Hall-of-Fame-Studio">Hall of Fame Studio</a>
</p>

<p align="center">
  <img alt="Status: repository-prequalified" src="https://img.shields.io/badge/status-repository--prequalified-2a2118?style=flat-square">
  <img alt="12 dedicated Skills" src="https://img.shields.io/badge/dedicated_Skills-12-8d6f3e?style=flat-square">
  <img alt="46 registered sources" src="https://img.shields.io/badge/registered_sources-46-6b5a42?style=flat-square">
  <img alt="Apache 2.0 license" src="https://img.shields.io/badge/license-Apache--2.0-302a23?style=flat-square">
</p>

> Not a quote bot. Not a stock picker. Not an oracle.
> An evidence-grounded **Long-Term Owner and Capital Allocation Partner**.

This is the standalone, open-source distribution of the Warren Buffett Agent
created inside [Hall of Fame Studio](https://github.com/MrMaii/Hall-of-Fame-Studio).
The public figure is the historical subject; the product is a decision system
for evidence, owner orientation, opportunity cost, survival, candor, and revision.

The Agent turns haste, social pressure, and undifferentiated fear into a calmer
view of what is known, what can cause permanent damage, what remains reversible,
and what the next-best use of capital, time, or attention would be. It does not
claim to reproduce Warren Buffett, represent him, know his current holdings, or
provide official financial advice.

## At a glance

| Field | Value |
|---|---|
| Agent | Warren Buffett Deep Agent · Agent 002 |
| Product role | Long-Term Owner and Capital Allocation Partner |
| Evidence profile | 46 registered sources · 56 atomic observations · 11 behavior claims |
| Callable surface | 12 dedicated Skills · four interaction modes |
| Qualification | <code>repository-prequalified</code>; Director verdict remains open |
| Visual language | One reviewed 3:2 Archive Plate and one shared frosted-glass diagram system |

The repository includes restrained motion studies for distribution surfaces,
but this README presents the reviewed primary plate once. The artwork preserves
the approved composition; it does not simulate a live model transcript.

## The operating promise

Calm is not passivity. It is a better order of operations:

<p align="center">
  <img src="./assets/diagrams/01-method-lens.svg" alt="Warren Buffett decision lens from pressure to owner judgment" width="100%">
</p>

The Agent separates four questions:

- What do we know, and what is only an estimate or inference?
- What can cause permanent loss?
- What can be made reversible or staged?
- What is the next-best use of capital, time, attention, or reputation?

The output is a durable decision with explicit downside, preserved options, a
named alternative, and a falsifier or review date.

## Evidence and traceability

The method is compiled from evidence rather than borrowed from a reputation:

<p align="center">
  <img src="./assets/diagrams/02-evidence-chain.svg" alt="Warren Buffett evidence chain from sources through observations, claims, runtime rules, tests, and observed behavior" width="100%">
</p>

The trace remains inspectable:

<pre><code>source → atomic observation → behavior claim → runtime rule → test → observed decision behavior</code></pre>

A missing fact stays missing. It never becomes a confident transaction.

## Capability clusters

The person chooses the tools. The tools do not replace owner judgment.

<p align="center">
  <img src="./assets/diagrams/03-capability-clusters.svg" alt="Warren Buffett Agent capability clusters around a long-term owner core" width="100%">
</p>

- **Understand the business** — trace the cash engine, test whether a moat is
  behavioral or rhetorical, and judge management as stewards.
- **Translate economics into value** — rebuild owner earnings, model a range,
  and turn uncertainty into a price or deal-structure buffer.
- **Allocate capital and protect survival** — compare every real use of the next
  dollar, expose hidden correlations, and find leverage or illiquidity breaks.
- **Know the boundary and communicate like an owner** — say what is understood,
  what needs research, and how to deliver bad news without hiding consequences.

## Conversation router

The personality core stays present in every mode. Skill activation changes the
work method, not the human relationship.

<p align="center">
  <img src="./assets/diagrams/04-mode-router.svg" alt="Warren Buffett Agent conversation router for relational, exploratory, task, and high-stakes work" width="100%">
</p>

| Mode | Runtime behavior | Hard Skills |
|---|---|---:|
| relational | Stay with the person and the exact detail; do not force an investment memo | 0 |
| exploratory | Contribute concrete starts, then ask one real question | 0 by default |
| task | Compare the decision and return a named artifact | 1–3 |
| high-stakes | Verify dated evidence, downside, obligations, and human review | only what is necessary |

## Quality and safety

The quality gate catches:

- fabricated memory or current holdings;
- cheap reassurance, guaranteed return, or all-in advice;
- using a competence boundary as a social exit;
- unsupported certainty, language mismatch, incomplete financial mechanics,
  and missing downside or review.

<p align="center">
  <img src="./assets/diagrams/05-quality-loop.svg" alt="Warren Buffett Agent quality loop from draft through a persona-owned gate to release or bounded revision" width="100%">
</p>

Specific securities, large financial commitments, or other high-stakes decisions
require dated primary evidence, downside analysis, and appropriate human review.

## Three-minute start

### 1. Install it as a Codex Skill

PowerShell:

<pre><code>git clone https://github.com/MrMaii/Warren-Buffett-Agent.git "$env:USERPROFILE\.codex\skills\warren-buffett-agent"</code></pre>

macOS or Linux:

<pre><code>git clone https://github.com/MrMaii/Warren-Buffett-Agent.git ~/.codex/skills/warren-buffett-agent</code></pre>

### 2. Start with the decision—not the celebrity

<pre><code>$warren-buffett-agent

We can acquire a smaller competitor, but it would consume most of our cash.
Separate the business case from the pressure to act. Show me the permanent-loss
paths, the reversible alternatives, and the next-best use of the capital.</code></pre>

### 3. Ask for a named artifact when the work is concrete

<pre><code>$warren-buffett-agent

Use $weigh-opportunity-cost. Compare hiring a sales team, rebuilding onboarding,
and keeping the cash. Return an Opportunity Cost Ledger with the winner, the
next-best alternative, assumptions that could reverse the choice, and a review date.</code></pre>

## Skill catalog

### A. Understand the business

| Skill | Use it when | Named output |
|---|---|---|
| [analyze-business-quality](./agent/skills/analyze-business-quality/SKILL.md) | You need the cash engine, incremental returns, resilience, and reinvestment runway | Business Quality Dossier |
| [map-economic-moat](./agent/skills/map-economic-moat/SKILL.md) | A brand, network effect, switching cost, or cost advantage needs an attacker test | Moat Map |
| [evaluate-management-stewardship](./agent/skills/evaluate-management-stewardship/SKILL.md) | Incentives, candor, governance, succession, and capital records need separation | Stewardship Dossier |

### B. Translate economics into value

| Skill | Use it when | Named output |
|---|---|---|
| [normalize-owner-earnings](./agent/skills/normalize-owner-earnings/SKILL.md) | Reported profit, working capital, maintenance investment, and dilution obscure owner cash | Owner Earnings Bridge |
| [estimate-intrinsic-value](./agent/skills/estimate-intrinsic-value/SKILL.md) | You need conservative, base, and favorable value scenarios with a per-share bridge | Intrinsic Value Range |
| [demand-margin-of-safety](./agent/skills/demand-margin-of-safety/SKILL.md) | You must choose act, wait, research, or reject under imperfect knowledge | Margin of Safety Decision |

### C. Allocate capital and protect survival

| Skill | Use it when | Named output |
|---|---|---|
| [allocate-capital](./agent/skills/allocate-capital/SKILL.md) | Reinvestment, acquisition, buyback, dividends, debt, and cash compete | Capital Allocation Board |
| [weigh-opportunity-cost](./agent/skills/weigh-opportunity-cost/SKILL.md) | Several good options compete for money, time, attention, or reputation | Opportunity Cost Ledger |
| [stress-test-downside-and-leverage](./agent/skills/stress-test-downside-and-leverage/SKILL.md) | Debt maturity, covenants, liquidity, and forced-sale paths matter | Downside and Leverage Map |
| [construct-concentrated-portfolio](./agent/skills/construct-concentrated-portfolio/SKILL.md) | A research portfolio needs conviction without hidden common failure modes | Portfolio Architecture Memo |

### D. Know the boundary and communicate like an owner

| Skill | Use it when | Named output |
|---|---|---|
| [assess-circle-of-competence](./agent/skills/assess-circle-of-competence/SKILL.md) | The decision depends on variables the team may not truly understand | Circle of Competence Gate |
| [communicate-with-owner-candor](./agent/skills/communicate-with-owner-candor/SKILL.md) | A board, partner, or owner needs facts, mistakes, responsibility, and correction | Owner Decision Memo / Shareholder Letter / Board Update |

## How to use it well

Good requests name the owner, horizon, alternatives, constraints, evidence,
irreversible loss, and desired artifact.

| Weak request | Better request |
|---|---|
| “Is this stock good?” | “Using the latest primary filings dated today, map business quality, owner earnings, impairment paths, and what evidence would falsify the thesis. Do not issue a trade.” |
| “What would Buffett do?” | “Compare these three uses of cash in one owner unit and return the decision spread.” |
| “Motivate me to be patient.” | “Separate what is merely uncomfortable from what can permanently damage the project, then give one reversible next move.” |
| “Write a shareholder letter.” | “State the bad result first, reconcile the original promise with the outcome, quantify the economic consequence, name responsibility, and set a review date.” |

## Host integration

The runtime package has no third-party dependencies. A host needs four steps:

1. Load [agent/RUNTIME.md](./agent/RUNTIME.md) as the compact constitution.
2. Use [agent/agent.json](./agent/agent.json) to route at most one to three
   Skills for a normal task.
3. Load [agent/AGENT.md](./agent/AGENT.md) and the behavior files only when a
   deeper integration context is justified.
4. Run evaluateBehavior against a draft, revise once when needed, and release
   or return a qualified fallback.

<pre><code>import { evaluateBehavior } from './agent/runtime/qualityGate.js';

const violations = evaluateBehavior(userMessage, draftResponse, conversationContext);
if (violations.length > 0) {
  // Repair the responsible evidence, runtime, or Skill rule before release.
}</code></pre>

Inspect a draft locally:

<pre><code>node scripts/check-response.mjs \
  --user "Should I put all my savings into this popular stock?" \
  --draft "Put it all in; popularity guarantees profit."</code></pre>

## Validate the package

Node.js 20 or later is sufficient for runtime validation. Rebuilding the
release media and diagrams additionally requires Python 3 and Pillow.

<pre><code>npm run validate
npm run fingerprint
npm run media:build
npm run diagrams:build
npm test</code></pre>

Candidate source fingerprint:

<pre><code>sha256:4736e707ef1e4a851cee104822598af6246b9f3a89038a42a261cced898ab448</code></pre>

Static release surfaces preserve the supplied Archive Plate byte-for-byte.
The diagrams are deterministic SVGs generated from the shared frosted-glass
template; the README uses each visual asset only once.

## Qualification status

Status: <strong>repository-prequalified</strong>. This means the repository
floor passed and the candidate is ready for human Director qualification. It
does not mean the historical person was reproduced, that returns are promised,
or that a Director has recorded pass.

Read [the qualification boundary](./docs/QUALIFICATION.md).

## From Agent 002 to Hall of Fame Studio

This repository is one Agent. Hall of Fame Studio is the institution around it.

[Hall of Fame Studio](https://github.com/MrMaii/Hall-of-Fame-Studio) is an
open-source, local-first environment where consequential minds can be recruited
from a Talent Market, tested in Persona Chat, composed into project teams, and
governed through Leader, Reviewer, evidence, revision, Flow Graph, and Proof Map
contracts.

The standalone Agent is useful alone. Inside the Studio it can disagree with a
product leader, review a capital-heavy proposal, hand current facts to a
specialist, and return an owner decision without flattening every Agent into
one generic assistant.

<p align="center">
  <a href="https://github.com/MrMaii/Hall-of-Fame-Studio">
    <img src="./assets/diagrams/06-studio-network.svg" alt="Warren Buffett Agent inside the Hall of Fame Studio network" width="100%">
  </a>
</p>

## Repository map

<pre><code>.
├── SKILL.md                 # installable public entrypoint
├── agent/                   # exact repository-prequalified candidate
│   ├── AGENT.md             # complete integration contract
│   ├── RUNTIME.md           # compact conversation constitution
│   ├── agent.json           # manifest and Skill routing
│   ├── behavior/            # human-core behavior documents
│   ├── research/            # sources → observations → claims
│   ├── runtime/             # Buffett-specific quality gate
│   ├── skills/              # 12 callable hard Skills
│   └── tests/               # focused quality-gate tests
├── assets/                  # Archive Plate, motion studies, and diagrams
├── docs/                    # architecture, qualification, Studio context
├── scripts/                 # validation, fingerprint, media, and diagram tools
└── tests/                   # public-package contracts</code></pre>

## Financial and identity boundary

This software is for analysis, education, and decision support. It is **not
financial advice**, does not execute trades, does not promise returns, and must
not reach a current buy/sell conclusion without relevant dated primary evidence,
the user's actual obligations, and appropriate review.

The project is not affiliated with Warren Buffett or Berkshire Hathaway and is
not authorized or endorsed by them. See [NOTICE.md](./NOTICE.md).

Original software, runtime rules, Skills, tests, documentation, diagrams, and
project-created media are available under [Apache License 2.0](./LICENSE).
Third-party research sources retain their own rights.
