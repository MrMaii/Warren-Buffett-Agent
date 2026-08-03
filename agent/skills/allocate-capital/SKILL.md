---
name: allocate-capital
description: Rank competing uses of scarce capital by conservative per-share value creation, durability, reversibility, and survival risk. Use for corporate reinvestment, acquisitions, share repurchases, dividends, debt reduction, cash reserves, portfolio reallocations, or deciding whether a good operating project is still the best available use of funds.
---

# Allocate Capital

## Operating stance

Every retained dollar belongs economically to owners and must compete across the full opportunity set. What is intelligent at one price or funding condition may be destructive at another.

## Inputs

Collect:

- Capital available, source, currency, duration, and restrictions.
- Mandatory maintenance, legal, pension, insurance, and liquidity needs.
- Candidate uses: internal projects, acquisitions, repurchases, debt reduction, dividends, or cash.
- Conservative cash-flow range, incremental return, capacity, and time to realization for each.
- Financing terms, tax, dilution, integration, and exit constraints.
- Current per-share value and realistic alternatives.

## Method

### 1. Protect the base

Reserve capital for maintenance, solvency, contractual obligations, and a stress liquidity buffer before scoring optional uses. Never fund optional upside by making ordinary adversity fatal.

### 2. Define the complete opportunity set

Include “do nothing/hold cash” and return of capital. Exclude categories unavailable in practice, but state why. Do not force capital back into the business or industry that produced it.

### 3. Normalize each candidate

Express each on a common owner basis:

- All-in cash committed and timing.
- Conservative incremental owner earnings.
- Incremental return and duration.
- Per-share value impact, including dilution.
- Reversibility and option value.
- Execution, leverage, and reputation risk.

### 4. Apply category-specific gates

#### Internal reinvestment

Require evidence of attractive incremental returns and runway; historic average returns are insufficient.

#### Acquisition

Include full purchase price, assumed liabilities, integration capital, foregone alternatives, and realistic synergies. Reject deals justified mainly by EPS accretion or size.

#### Share repurchase

Require excess liquidity and purchase below conservatively estimated intrinsic value. Measure continuing-owner per-share impact, not announcement optics.[S04]

#### Debt reduction

Value guaranteed interest savings plus survival/option value. Prioritize when refinancing or covenant risk is material.

#### Dividend

Prefer when owners can likely deploy the marginal dollar better and no higher-value internal use exists.

#### Cash

Charge opportunity cost, but credit liquidity, resilience, and the option to act during dislocation.

### 5. Compare opportunity cost

Rank the best candidate against the next-best, not against zero or the company's historic return. Use `weigh-opportunity-cost` for close choices.

### 6. Check scale and saturation

Distinguish the return on the first dollar from the return on the last dollar. A high-return project may accept only limited capital.

### 7. Stage when uncertainty is reducible

Use milestones, pilots, earn-outs, or staged commitments when they buy information without sacrificing the core opportunity. Do not stage solely to disguise a weak thesis.

### 8. Decide and set review rules

Use `Fund`, `Stage`, `Hold`, `Return`, or `Reject`. Define what evidence releases the next dollar and what stops further capital.

## Output contract

Produce a `Capital Allocation Board`:

```text
Base capital protected:
Candidate | All-in commitment | Conservative return | Capacity/duration
Per-share impact | Reversibility | Key risk | Rank
Selected action:
Next-best alternative and spread:
Milestones / stop conditions:
What will not be funded:
```

## Stop and escalate

Stop if optional capital is not truly available, liabilities/financing terms are incomplete, or candidate returns use incompatible definitions. Escalate tax, solvency, legal, pension, insurance, and complex transaction structures.

## Failure modes

- Automatically reinvesting where cash was generated.
- Judging acquisitions by EPS accretion.
- Treating all repurchases as positive.
- Ignoring dilution or assumed liabilities.
- Comparing candidates with different horizons or risk bases.
- Ranking by headline IRR without capacity or reinvestment duration.
- Calling cash “wasted” without valuing resilience and option value.

## Safety and truthfulness

Use current terms and primary financial data. This Skill supports business decisions and analytical comparisons; it does not authorize real transfers, trades, or personalized portfolio actions.

## Self-review

- Is survival capital protected first?
- Is every candidate on the same owner/per-share basis?
- Is the last dollar's return still attractive?
- Did I include do nothing and return of capital?
- What is the next-best alternative and value spread?
- Are release and stop conditions explicit?

Evidence basis: `../../research/evidence-ledger.md` S04, S06, D04, B03.
