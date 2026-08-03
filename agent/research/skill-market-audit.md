# Hard-Skill Market Audit

Audit date: 2026-07-22.

## Audit method

For each desired capability, compare:

1. existing Studio and installed skills;
2. OpenAI curated skill catalog available in this workspace;
3. public agent/persona-building workflows;
4. authoritative professional methods and primary source material;
5. the cost of adapting a generic method versus building a Buffett-specific one.

The decision is `reuse`, `adapt`, or `build`. Every Skill remains independently
callable, but it may not alter the human core outside `task` or `high-stakes`
conversation modes.

## Persona-building workflow comparator

A public one-click persona-generation workflow was reviewed as a comparator.
Its useful disciplines include multiple research lanes, a 40+ primary-source
target, verification, mental models, heuristics, expression DNA, boundary
honesty, and iterative refinement.

Decision: **adapt the evidence discipline, do not use the one-click output as
the Agent source**. This project adds relationship modeling, conversation-mode
composition, same-source Studio/ChatBox compilation, long multi-turn testing,
and private transcript qualification. A generator may accelerate collection;
it cannot replace claim adjudication or live dialogue revision.

## Capability decisions

| Capability | Market finding | Decision | Local Skill |
|---|---|---|---|
| Competence assessment | Generic research/safety gates exist; none model economic understandability and evidence closure together. | Build, and restrict to professional valuation. | `assess-circle-of-competence` |
| Business quality | Generic business analysis is broad and often stops at business-model canvases or ratios. | Build Buffett-specific cash-engine and incremental-return method. | `analyze-business-quality` |
| Economic moat | Competitor-analysis skills map alternatives but rarely prove durability through customer and attacker evidence. | Adapt competitive research principles into a moat-specific method. | `map-economic-moat` |
| Owner Earnings | Accounting/DCF tools calculate free cash flow but do not consistently separate maintenance capital and owner dilution. | Build. | `normalize-owner-earnings` |
| Intrinsic value range | DCF templates exist; they often imply point precision and weak reinvestment logic. | Adapt valuation primitives into range-first owner economics. | `estimate-intrinsic-value` |
| Margin of safety | Risk templates exist; few distinguish risks fixable by price from structural unknowability or fraud. | Build. | `demand-margin-of-safety` |
| Capital allocation | Corporate-finance methods exist but are usually separated by transaction type. | Build one comparable opportunity set across all uses of a dollar. | `allocate-capital` |
| Management stewardship | Governance audits exist; generic leadership rubrics overweight presentation and underweight capital behavior. | Build behavior-led ledger. | `evaluate-management-stewardship` |
| Opportunity cost | Decision matrices are common but often compare scores instead of next-best economic alternatives. | Adapt decision analysis into owner units and reversibility. | `weigh-opportunity-cost` |
| Downside and leverage | Risk-review skills exist; they often report ratios without tracing the first forced-action path. | Adapt stress-testing into path and permanent-loss analysis. | `stress-test-downside-and-leverage` |
| Concentrated portfolio | Portfolio optimizers exist; most optimize volatility and historical covariance. | Build research portfolio focused on understanding, look-through exposure, liquidity, and survival. | `construct-concentrated-portfolio` |
| Owner candor | Copywriting skills exist; they optimize persuasion rather than truth ledger, mistake ownership, and corrective action. | Build. | `communicate-with-owner-candor` |

## Cross-Skill dependency map

```text
business understanding
├─ business quality
├─ moat durability
└─ management stewardship
       ↓
normalized Owner Earnings
       ↓
intrinsic value range
       ↓
margin of safety
       ↓
capital allocation + opportunity cost
       ↓
downside/leverage + portfolio survival
       ↓
owner-candor communication
```

Dependencies do not mean every task runs the whole chain. The router selects
only 1–3 Skills whose prerequisites are already satisfied.

## Market audit result

All twelve capabilities are kept as dedicated in-package Skills because their
value lies in their shared owner-economics semantics and evidence contract.
Generic professional skills remain available for team interoperability, but
they are not automatically injected into casual or exploratory conversation.
