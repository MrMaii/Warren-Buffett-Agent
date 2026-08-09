---
name: normalize-owner-earnings
description: Reconcile reported accounting earnings to a conservative range of sustainable cash earnings available to owners after required operating investment. Use for financial-statement analysis, valuation preparation, acquisition diligence, earnings-quality review, or when depreciation, capital expenditure, working capital, stock compensation, acquisitions, or one-offs obscure economic reality.
---

# Normalize Owner Earnings

## Operating stance

Treat Owner Earnings as an analytical bridge, not a number copied from a data service. The key uncertainty is usually the cash required to maintain competitive position and current unit volume.

## Inputs

Require current and historical:

- Income statements, balance sheets, and cash-flow statements.
- Capital-expenditure disclosures and asset/segment notes.
- Working-capital components and revenue-recognition policies.
- Acquisition, restructuring, impairment, stock-compensation, lease, pension, and tax notes.
- Management's maintenance/growth capital claims, with independent checks where possible.

Use at least a full cycle when the business is cyclical.

## Method

### 1. Establish reported anchors

Record net income, operating income, cash from operations, depreciation/amortization, total capital expenditure, working-capital change, stock compensation, and share-count change. Keep period, currency, and units explicit.

### 2. Remove financing and non-owner noise

Separate operating results from investment gains/losses, unusual tax effects, discontinued operations, and financing events. Do not remove a cost merely because management labels it adjusted.

### 3. Normalize operating earnings

Adjust for genuinely nonrecurring items in both directions. Repeated “one-time” restructuring, litigation, acquisition, or compensation costs are recurring economics until evidence shows otherwise.

### 4. Treat non-cash charges economically

- Add back depreciation/amortization only before subtracting required capital spending.
- Do not add back stock compensation without charging dilution or replacement cash cost.
- Examine credit losses, reserves, pensions, leases, and deferred taxes for eventual cash claims.

### 5. Estimate maintenance capital expenditure

Use a range, triangulating:

- Asset age and replacement cost.
- Capacity/volume changes.
- Segment capital intensity.
- Multi-year depreciation vs capital spending.
- Management disclosure and competitor benchmarks.

Never mechanically set maintenance capex equal to depreciation.

### 6. Normalize working capital

Estimate working capital needed to maintain normalized sales, excluding acquisition effects and temporary timing. Growing businesses may need real incremental owner capital even when reported profit is strong.

### 7. Build the bridge

Use the conceptual structure:

```text
Normalized Owner Earnings
= normalized reported earnings
+ non-cash charges that are not economic costs
- maintenance capital expenditure
- working capital required to maintain normalized volume
- other recurring owner cash claims
```

Where the company structure demands it, reconcile from cash from operations as an independent cross-check.

### 8. Produce low/base/high ranges

The range must be driven by maintenance capital, cycle normalization, working capital, recurring adjustments, and dilution—not arbitrary percentage bands.

### 9. Reconcile per share

Use diluted share count and include buyback/issuance history. Owner earnings can grow while owner earnings per share falls.

## Output contract

Produce an `Owner Earnings Bridge`:

```text
Reported anchor:
+/- normalization items:
+ non-cash items accepted:
- maintenance capex range:
- normalized working-capital need:
- dilution/other owner claims:
= low/base/high owner earnings:
= per-share range:
```

For each line provide source, period, classification (`reported`, `adjusted`, `estimated`), rationale, and sensitivity. Finish with the largest uncertainty and the evidence needed to narrow it.

## Stop and escalate

Stop before a single-number result if maintenance capital cannot be bounded, revenue recognition is unreliable, consolidation hides material liabilities, or a financial institution requires a different economic model. Escalate banks/insurers, resource reserves, pensions, or complex tax structures to a specialist.

## Failure modes

- Calling cash from operations “owner earnings.”
- Setting maintenance capex equal to depreciation by default.
- Adding back stock compensation without dilution.
- Removing recurring “one-time” costs.
- Ignoring working capital during growth.
- Using one good year in a cyclical business.
- Mixing enterprise cash flows with equity cash flows.

## Safety and truthfulness

Never fabricate missing statements or capex splits. Label estimates and ranges prominently. This Skill prepares analysis; it does not produce a personalized buy/sell instruction.

## Self-review

- Can every adjustment be traced to a source?
- Did I charge all economic costs even if non-cash today?
- Is maintenance capital a reasoned range?
- Did I normalize cycle and working capital?
- Does the per-share bridge reflect dilution?

Evidence basis: `../../research/evidence-ledger.md` S01, S03, S08, D08.
