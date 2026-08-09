---
name: stress-test-downside-and-leverage
description: Test whether a business, transaction, or portfolio can survive adverse operating, financing, liquidity, correlation, and reputation scenarios without forced action or permanent impairment. Use before leveraged commitments, acquisitions, concentrated exposures, cyclical investments, refinancing, or any decision where average-case returns hide a ruin path.
---

# Stress Test Downside and Leverage

## Operating stance

Risk is the path to permanent loss or forced behavior, not merely price volatility. Include the effect of financial pressure on decision freedom: a sound asset can become a bad outcome when financing terms force action.

## Inputs

Require current:

- Debt, leases, guarantees, derivatives, pensions, supplier/customer financing, and contingent claims.
- Maturity schedule, interest basis, collateral, covenants, and cross-defaults.
- Cash, committed facilities, working-capital needs, and restricted liquidity.
- Fixed/variable cost structure, cycle history, customer/supplier concentration.
- Portfolio correlations, margin rules, redemption terms, and exit liquidity where relevant.

## Method

### 1. Map all leverage

Include:

- Balance-sheet borrowing.
- Operating leverage and fixed commitments.
- Hidden/contingent leverage from guarantees, derivatives, leases, litigation, pensions, or take-or-pay contracts.
- Behavioral leverage from short deadlines, margin calls, redemption promises, or reputation dependence.

### 2. Define survival resources

Count only liquidity available under stress. Haircut marketable assets, exclude cash trapped by regulation or subsidiaries, and verify whether credit facilities remain drawable after covenant deterioration.

### 3. Build causal stress scenarios

At minimum:

- Revenue/volume decline.
- Margin/input shock.
- Working-capital reversal.
- Refinancing cost or market closure.
- Counterparty/customer loss.
- Correlated multi-shock.

Use historical and structural evidence; avoid arbitrary “minus 10% everywhere.”

### 4. Trace the path, not only the endpoint

For each month/quarter where material, show cash generation, obligations, covenant headroom, collateral calls, management actions, and when choices disappear.

### 5. Test permanent impairment

Ask whether stress causes:

- Dilution at a bad price.
- Asset sale below value.
- Loss of license, customers, key staff, or supplier trust.
- Underinvestment that weakens the moat.
- Default, restructuring, or reputational damage.

### 6. Test management responses

Separate reversible actions (pause growth capex, reduce optional spend) from actions that harm future economics (cut maintenance, fire critical capacity, sell crown assets).

### 7. Find the first break

Name the earliest binding constraint and its lead indicator. Survival analysis is only useful when it identifies what to monitor and how much time remains.

### 8. Add buffers and decision rules

Recommend liquidity, maturity, covenant, collateral, concentration, or commitment buffers. Specify actions before—not after—the first break.

### 9. Reach a verdict

- `Resilient`: survives severe plausible stress with choices intact.
- `Conditional`: survives only if named early actions occur.
- `Fragile`: plausible stress forces value-destructive action.
- `Ruin path`: low-probability scenario can create unrecoverable loss.
- `Unknown`: obligations or correlations are incomplete.

## Output contract

Produce a `Downside and Leverage Map`:

1. Full leverage inventory.
2. Available stress liquidity.
3. Scenario assumptions and evidence.
4. Path-by-path cash/covenant headroom.
5. First break and lead indicator.
6. Permanent-impairment mechanism.
7. Pre-commitment actions and buffers.
8. Verdict, confidence, and missing claims.

## Stop and escalate

Stop if derivative, covenant, guarantee, pension, insurance, regulatory capital, or legal obligations cannot be interpreted. Escalate solvency/legal conclusions. Do not assume facilities remain available because they exist today.

## Failure modes

- Treating volatility as risk while ignoring forced action.
- Stressing one variable at a time when shocks correlate.
- Counting restricted or mark-to-market assets at face value.
- Ignoring maturity timing and covenant path.
- Assuming all capex can be cut safely.
- Using average interest rates instead of refinancing terms.
- Calling low probability equivalent to no risk.

## Safety and truthfulness

Use source dates and mark unknown obligations. Do not provide leverage encouragement or personalized position sizing. Never claim a scenario proves safety.

## Self-review

- Did I include operating, contingent, and behavioral leverage?
- Is stress liquidity actually available under the scenario?
- What breaks first, and when?
- Which response preserves vs destroys future economics?
- Did I test correlated shocks and forced actions?
- Are buffers and early triggers explicit?

Evidence basis: `../../research/evidence-ledger.md` S04, S05, S06, B03, I01, I04.
