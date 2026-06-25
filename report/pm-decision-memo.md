# PM Decision Memo: Rollout Recommendation for Urgency Nudge Experiment

**Date:** June 25, 2026  
**To:** Growth Leadership Team  
**From:** Conversion Rate Optimization Team  
**Subject:** Recommendation: Ship Urency Nudge to Desktop Only; Revisit Mobile UX

---

## 1. Strategic Decision

### Recommendation
**Ship the Urgency Nudge on Desktop (100% rollout)** and **Roll Back (Keep Control) on Mobile (0% rollout).**

### Summary of Findings

#### Desktop
- The nudge drove an absolute lift of **+5.14%** in conversions.
- Conversion rate increased from **11.68%** to **16.82%**.
- Result is **highly statistically significant** (**p < 0.0001**).

#### Mobile
- Conversion lift was only **+0.07%**.
- Result was **not statistically significant** (**p = 0.92**).

#### Guardrail: Returns
- Overall return rate increased from **8.50%** to **11.49%** among buyers.
- Statistical test result: **p = 0.1018** (marginally significant at the 10% level).
- This suggests a potential risk of impulsive purchases and warrants post-launch monitoring.

---

## 2. Financial Projection (Desktop-Only Rollout)

### Assumptions
- Annual Desktop Sessions: **1,000,000**
- Average Order Value (AOV): **$50.00**
- Return Processing Cost: **$10.00 per return**

### Gross Revenue Impact

| Metric | Value |
|----------|----------|
| Baseline Annual Revenue | $5,840,909.09 |
| Baseline Orders | 116,818 |
| Projected Annual Revenue | $8,409,090.91 |
| Projected Orders | 168,182 |
| Gross Revenue Lift | **+$2,568,181.82** |
| Additional Orders | **+51,364** |

### Return & Handling Costs

| Metric | Value |
|----------|----------|
| Baseline Returns | 10,000 items |
| Baseline Return Rate | 8.56% |
| Projected Returns | 22,273 items |
| Projected Return Rate | 13.24% |
| Increase in Returns | +12,273 items |
| Additional Processing Costs | +$122,727.27 |

### Net Bottom-Line Impact

| Metric | Value |
|----------|----------|
| Baseline Net Revenue | $5,240,909.09 |
| Projected Net Revenue | $7,072,727.27 |
| Incremental Net Financial Value | **+$1,831,818.18 per year** |

> Even after accounting for increased return rates, refunds, and return-processing costs, a desktop-only rollout is projected to generate **$1.83 million in additional annual profit**.

---

## 3. Why Mobile Failed & How to Revisit UX

### 1. Limited Viewport Space
On mobile devices, product pages have limited vertical space. Adding a separate urgency banner likely pushed the primary **"Add to Cart"** button below the fold, creating friction that offset any psychological benefit from the scarcity message.

### 2. Task-Driven Behavior
Mobile shoppers often exhibit stronger purchase intent and are more sensitive to disruptive interface elements. The urgency banner may have been perceived as intrusive or manipulative.

### 3. Proposed Mobile UX Pivot
Rather than using a standalone promotional banner, integrate scarcity messaging directly into the inventory status line.

**Example:**

- Current: `In Stock`
- Proposed: `Only 3 left!`

This compact message should appear adjacent to the quantity selector and be evaluated in a future mobile-only experiment.

---

## 4. Launch & Monitoring Plan

### 1. Staged Desktop Launch
- Launch with a **50/50 production split** for the first **7 days**.
- Expand to **100% rollout** once return-rate stability has been confirmed.

### 2. Production Alerts
- Establish a desktop return-rate threshold of **13.0%**.
- If return rates exceed this threshold:
  - Trigger a review by the Growth and CRO teams.
  - Evaluate whether additional checkout verification steps should be introduced.

---
