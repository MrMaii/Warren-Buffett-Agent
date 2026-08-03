---
name: assess-circle-of-competence
description: Determine whether a business, investment, or capital-allocation question is understandable and falsifiable enough for an honest decision. Use before valuation, when a thesis depends on unfamiliar technology or regulation, when key economics cannot be explained simply, or when the correct output may be research, handoff, or abstention rather than a forced answer.
---

# Assess Circle of Competence

## Operating stance

Treat boundary recognition as a capability. Do not confuse familiarity with understanding, and do not use a larger discount rate to repair a business whose economics cannot be described or tested.

## Inputs

Collect:

- The exact decision, owner, time horizon, and irreversible action.
- A plain description of the product, customer, payment, cost, capital, and cash cycle.
- Available primary sources and their dates.
- Variables that drive value and variables that can destroy it.
- The team's relevant domain expertise and missing reviewers.

If the task concerns a live company, require current filings and a current price only after the understanding gate passes.

## Method

### 1. Rewrite the decision

Convert a vague request into one decision sentence:

```text
Should [owner] commit [capital/action] for [horizon] given [constraints], compared with [alternatives]?
```

### 2. Build the explain-back chain

Explain without jargon:

1. Why does the customer pay?
2. Why does revenue become cash?
3. What resources must be continually reinvested?
4. What prevents competitors or substitutes from taking the economics?
5. What single change could make the model fail?

Mark any answer that merely repeats management language as `claim`, not `understood`.

### 3. Test causal understanding

For every major value driver, require:

- A causal mechanism.
- One observable metric.
- One disconfirming observation.
- A source capable of verifying it.

An input is outside the current circle if the team cannot name how it would know it is wrong.

### 4. Draw the boundary map

Classify each component:

- `Known`: understood and supported by current evidence.
- `Learnable`: important but answerable with named research or a specialist.
- `Structurally uncertain`: dependent on unknowable timing, binary outcomes, or reflexive behavior.
- `Irrelevant`: interesting but not decision-changing.

Do not average these categories. A structurally uncertain variable that dominates value can block the whole decision.

### 5. Apply the dependency test

Estimate how much of the conclusion depends on each unknown:

- Low dependency: conclusion survives a wide range.
- Medium dependency: changes price or timing but not business identity.
- High dependency: reverses the decision or creates permanent-loss risk.

### 6. Choose the gate result

- `Inside`: causal model, evidence, and failure conditions are clear.
- `Edge`: model is mostly clear; named research/specialist can close material gaps.
- `Outside`: core value depends on a mechanism the team cannot explain or test.
- `Forbidden`: request requires insider information, deception, personalized trade execution, or fabricated certainty.

### 7. Route the next action

- Inside → invoke business-quality/owner-earnings/value Skills.
- Edge → issue a bounded evidence request and assign a reviewer.
- Outside → abstain from value judgment; offer only a research map or handoff.
- Forbidden → refuse the prohibited action and offer a lawful analytical alternative.

## Output contract

Produce a `Circle of Competence Gate`:

```markdown
Decision:
Gate: Inside | Edge | Outside | Forbidden
Confidence:
What we can explain:
What remains unknown:
Why the unknown matters:
Disconfirming evidence:
Minimum research/reviewer needed:
Allowed next step:
What we will not conclude:
```

## Stop and escalate

Stop valuation when:

- Core revenue or cost causality cannot be explained.
- A binary regulatory, legal, clinical, technical, or resource event dominates value.
- Disclosures are inconsistent and no primary evidence resolves them.
- The user asks the Agent to infer nonpublic facts.

Escalate to a domain specialist with a specific question, not “please review everything.”

## Failure modes

- Rejecting all new technology merely because it is new.
- Declaring something understood because the brand is familiar.
- Treating an expert opinion as a causal model.
- Continuing to valuation because data is abundant, even though the mechanism is unclear.
- Using “outside my circle” to avoid learnable work.

## Safety and truthfulness

Never imply that a gate result is investment advice. Do not give a buy/sell conclusion when the gate is Edge or Outside. Distinguish unavailable data from structural unknowability.

## Self-review

- Could another analyst reproduce the boundary map?
- Did I name a falsifier for every important claim?
- Did I separate learnable gaps from structural uncertainty?
- Would one unknown reverse the decision?
- Did I route or abstain instead of filling gaps with personality?

Evidence basis: `../../research/evidence-ledger.md` S02, B02, I02, I04.
