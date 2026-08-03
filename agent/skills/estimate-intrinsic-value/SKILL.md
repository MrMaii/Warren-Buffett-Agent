---
name: estimate-intrinsic-value
description: Estimate a conservative range for the present value of owner cash that a business can distribute or reinvest over its remaining life. Use after business quality and normalized owner earnings are understood, for acquisition terms, strategic capital decisions, or price-versus-value analysis; do not use when the circle-of-competence gate fails.
---

# Estimate Intrinsic Value

## Operating stance

Intrinsic value is a range conditional on evidence and assumptions. Prefer a rough range that exposes its drivers over a precise point that hides uncertainty.

## Inputs

Require:

- A passed or Edge-with-closed-gaps circle-of-competence gate.
- Normalized owner earnings and maintenance capital range.
- Business-quality, moat, and management-stewardship findings.
- Net debt, off-balance-sheet claims, dilution, and non-operating assets.
- Current price/terms and date only for a later comparison, not to anchor the estimate.

## Method

### 1. Define the owner claim

State whether valuing operating assets, enterprise value, or common equity. Prevent double counting cash, debt, investments, subsidiaries, leases, pensions, and minority interests.

### 2. Select normalized starting economics

Use through-cycle owner earnings, not the latest peak or trough. Reconcile the starting value to primary statements.

### 3. Model reinvestment explicitly

Separate:

- Cash distributable today.
- Cash reinvested at an estimated incremental return.
- Duration of the reinvestment runway.
- Capital likely returned or misallocated.

Growth without its required reinvestment is not a valid valuation input.

### 4. Build three evidence-based scenarios

- `Conservative`: weaker economics or shorter duration that remains plausible.
- `Base`: most supported path, not the most comfortable path.
- `Favorable`: upside that has a causal mechanism and evidence.

For each, specify revenue/volume, margin, capital needs, incremental return, duration, terminal economics, and probability only if probabilities are defensible.

### 5. Discount for time and risk without double counting

Use a rate consistent with cash-flow definition and currency. Put operating uncertainty primarily in cash-flow scenarios; do not both crush cash flows and add an arbitrary punitive discount rate without explanation.

### 6. Cross-check independently

Use at least two where relevant:

- Discounted owner earnings.
- Normalized earnings-power value.
- Replacement or liquidation value for asset-bound businesses.
- Transaction/market multiples only as a sanity check, never the source of truth.

### 7. Bridge enterprise to equity and per share

Subtract all owner claims senior to common equity, add non-operating assets conservatively, and use fully diluted shares. Show the bridge.

### 8. Identify value-break variables

Name the 2–4 assumptions that drive most of the range. Run sensitivities and state what evidence would narrow them.

### 9. Keep price separate

Finish the value estimate before comparing with price or proposed transaction terms. Pass the range to `demand-margin-of-safety`.

## Output contract

Produce an `Intrinsic Value Range`:

1. Valuation date, unit, currency, and owner claim.
2. Normalized starting owner earnings.
3. Conservative/base/favorable assumptions.
4. Valuation by primary method.
5. Independent cross-check.
6. Enterprise-to-equity and per-share bridge.
7. Low/base/high range with no false precision.
8. Value-break variables and confidence.
9. Facts that would invalidate the range.

## Stop and escalate

Stop if the business mechanism, maintenance capital, major liabilities, or share count cannot be bounded. Do not value binary-outcome assets with a conventional steady-state model. Escalate specialized financial, insurance, resource, biotech, or regulated-asset models.

## Failure modes

- Starting from market price or analyst target.
- Forecasting growth without reinvestment.
- Using latest-year earnings as normalized.
- Double counting cash or risk.
- Hiding uncertainty in terminal value.
- Applying one multiple to unlike segments.
- Reporting more precision than source data supports.

## Safety and truthfulness

Use current sourced data and show dates. Label the output analytical, not personalized advice. Never imply a valuation range guarantees a market outcome or timing.

## Self-review

- Did the circle gate pass?
- Is starting owner earnings traceable and normalized?
- Does growth pay for its capital?
- Are scenarios causal rather than percentage decorations?
- Is price absent until the valuation is complete?
- Can the largest sensitivity be understood in one sentence?

Evidence basis: `../../research/evidence-ledger.md` S01, S04, S09, D04, D08.
