---
name: demand-margin-of-safety
description: Translate uncertainty, fragility, liquidity, incentives, and downside into the buffer required between conservative value and the price or terms paid. Use after an intrinsic-value range exists, for investment entry, acquisitions, contracts, project commitments, or deciding whether to wait despite an attractive story.
---

# Demand Margin of Safety

## Operating stance

Margin of safety is protection against being wrong, not a fixed discount printed on every asset. A lower price cannot repair fraud, ruinous leverage, or a business outside the circle of competence.

## Inputs

Require:

- Conservative/base/favorable intrinsic-value range.
- Current price or transaction terms with timestamp.
- Evidence-quality and circle-of-competence verdict.
- Leverage, liquidity, cyclicality, concentration, governance, and moat findings.
- Decision horizon, reversibility, and realistic alternatives.

## Method

### 1. Start from conservative value

Use the defensible low end or explicitly weighted range, not the most optimistic scenario. Document whether price includes fees, dilution, assumed debt, integration cost, or required follow-on capital.

### 2. Inventory uncertainty

Classify:

- `Estimation`: maintenance capital, normalized margin, useful life.
- `Business`: competition, customer concentration, cyclicality.
- `Balance-sheet`: refinancing, covenants, contingent liabilities.
- `Management`: allocation skill, integrity, incentives.
- `Structural`: regulation, technology, binary outcomes.
- `Execution`: integration, capacity, timeline, operational dependency.

### 3. Separate bufferable from unbufferable risk

- Bufferable: plausible estimation error with survivable outcomes.
- Unbufferable: unknown integrity, uncapped liability, forced-sale path, opaque accounting, or core mechanism not understood.

For unbufferable risk, choose Pass/Research; do not invent a heroic discount.

### 4. Assess fragility

Increase required protection when downside is nonlinear, liquidity is thin, leverage is high, cash claims are near-term, value is concentrated in a terminal assumption, or management can deploy more capital without owner control.

### 5. Assess evidence quality

Increase protection for stale data, unaudited numbers, short histories, inconsistent definitions, weak segment disclosure, and estimates that cannot be cross-checked.

### 6. Compare price and terms

Calculate transparent diagnostics such as:

```text
Discount to conservative value = (conservative value - all-in price) / conservative value
Downside to stress value       = (all-in price - stress value) / all-in price
```

Do not let the formula choose the threshold. Explain why the observed buffer is or is not adequate for the named uncertainties.

### 7. Add opportunity cost

The required margin can be larger when equal-quality alternatives offer a better buffer, liquidity, or reversibility. “Positive expected value” alone is insufficient.

### 8. Decide

- `Adequate`: terms cover plausible errors and survival risk is bounded.
- `Thin`: attractive only under base assumptions; wait or reduce commitment.
- `Absent`: price/terms leave no room for ordinary error.
- `Not applicable`: risk is unbufferable; Pass/Research regardless of discount.

## Output contract

Produce a `Margin of Safety Decision`:

```text
Valuation date and all-in terms:
Conservative/base value:
Stress value:
Observed buffer:
Uncertainty inventory:
Unbufferable risks:
Alternative opportunity:
Verdict: Adequate | Thin | Absent | Not applicable
Action: Act | Wait | Research | Pass
Re-entry/review conditions:
```

## Stop and escalate

Stop when price, liabilities, dilution, financing terms, or conservative value are not current and complete. Escalate legal contingencies, complex securities, tax structures, and solvency questions.

## Failure modes

- Applying a universal 20%/30%/50% rule.
- Using base value as the safety anchor.
- Treating volatility as the only uncertainty.
- Discounting an unknowable or unethical situation.
- Ignoring fees, debt, dilution, and follow-on capital.
- Calling a large discount safe when value is collapsing faster.

## Safety and truthfulness

This Skill evaluates analytical protection, not user suitability or personal position size. Use live prices only with source and timestamp. Never promise loss prevention.

## Self-review

- Did I anchor on conservative, not desired, value?
- Which risks cannot be fixed by price?
- Does leverage create nonlinear loss?
- Are all-in terms complete?
- Is a better alternative available?
- Are wait/pass conditions explicit?

Evidence basis: `../../research/evidence-ledger.md` S02, S04, S05, I01, I04.
