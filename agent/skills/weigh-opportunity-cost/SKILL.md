---
name: weigh-opportunity-cost
description: Compare a proposed use of time, money, attention, or risk with the best realistic alternatives on a common owner-value basis. Use when choices look independently attractive, resources are constrained, sunk cost or organizational habit dominates, or a capital-allocation decision needs an explicit next-best alternative.
---

# Weigh Opportunity Cost

## Operating stance

The correct benchmark is the best realistic foregone choice, not zero, historical cost, a budget category, or an arbitrary hurdle inherited from another decision.

## Inputs

Define:

- The scarce resource and amount.
- Decision owner, horizon, constraints, and reversibility.
- Complete set of feasible alternatives, including wait/do nothing.
- Conservative value, risk, liquidity, capacity, and information value for each.
- Dependencies and whether alternatives can be staged or combined.

## Method

### 1. Remove infeasible options

Document hard constraints: mandate, legal, skills, timing, capital, capacity, or liquidity. Do not compare fantasy opportunities with executable ones.

### 2. Use a common unit

Choose owner value per scarce resource, such as:

- Per-share value created per dollar.
- Normalized owner earnings per unit of capital.
- Decision-quality gain per week of research.
- Downside avoided per unit of liquidity.

Do not compare IRR, NPV, payback, and strategic adjectives without reconciliation.

### 3. Normalize time and risk

Align start date, duration, reinvestment assumptions, probability basis, and terminal value. Include the value of preserving options and the cost of irreversible commitment.

### 4. Identify the next-best alternative

Rank the list and name the runner-up. The opportunity cost of the winner is the value of this runner-up, adjusted for resources not actually consumed.

### 5. Calculate the decision spread

Show the difference between winner and runner-up under conservative/base conditions. A narrow spread with weak evidence calls for staging, more research, or waiting.

### 6. Correct common distortions

- Ignore sunk cost except where it changes future cash.
- Treat existing ownership as irrelevant to forward economics.
- Charge management attention and integration capacity.
- Do not give internally generated cash a zero cost.
- Avoid double counting “strategic value” already present in cash flows.

### 7. Value information

When a small experiment can cheaply change the ranking, compare its expected decision value with delay cost. Use staged learning only when it preserves the main opportunity.

### 8. Decide

Choose `Commit`, `Stage`, `Wait`, or `Reject`, and state the value spread plus the assumptions most likely to reverse the ranking.

## Output contract

Produce an `Opportunity Cost Ledger`:

```text
Scarce resource:
Constraint set:
Alternative | Conservative owner value | Time | Risk | Reversibility
Information value | Capacity | Rank
Winner:
Next-best alternative:
Decision spread:
Reversal assumptions:
Action and review trigger:
```

## Stop and escalate

Stop when alternatives use incompatible cash-flow definitions, hidden constraints make execution unknown, or a legal/strategic dependency cannot be valued. Escalate domain-specific assumptions rather than assigning arbitrary scores.

## Failure modes

- Comparing with zero or sunk cost.
- Omitting wait/do nothing.
- Ranking by highest headline return while ignoring capacity.
- Treating cash already on hand as free.
- Ignoring attention, integration, or liquidity.
- Creating a weighted score whose weights hide the decision.

## Safety and truthfulness

State which alternatives were excluded and why. Do not present invented probabilities as data. This Skill structures decisions; it does not execute financial transactions.

## Self-review

- Is the opportunity set complete and feasible?
- Are alternatives in one common unit and horizon?
- What is the actual runner-up?
- Is the decision spread meaningful relative to uncertainty?
- Did sunk cost, existing ownership, or organizational habit receive hidden weight?
- Could a small experiment change the ranking cheaply?

Evidence basis: `../../research/evidence-ledger.md` S04, S06, D04, I02.
