# 40 — Empirical Validation Run

**Date:** 22 August 2026  
**Status:** executed where the public evidence permits; no invented coefficients

## Executive verdict

We can now distinguish three levels of evidence:

1. **Actual quantitative tests** on the public W26 traction subset.
2. **Published empirical evidence** that directly tests parts of H1.
3. **Untestable claims** for which the required acceptance-time or rejected-applicant data are not public.

The most important result is methodological: the current public data are **not sufficient to claim that Venture Atlas has discovered YC's selection function**. That requires rejected applicants and acceptance-time variables.

---

## Dataset actually executed

The YC Bench project publishes a W26 traction file containing 11 companies with structured traction signals and a composite `Velocity_Score`. The source describes the broader W26 benchmark as 196 startups and defines the score as a pre-Demo-Day performance proxy. The published repository reports that a baseline using pre-application Google mentions achieved 70% Precision@20, 55% Recall@11 and 7× lift over random in that benchmark. 

The 11-row traction subset used here is preserved at `analysis/ycbench_w26_traction.csv`.

### Variables

- ARR
- pilot revenue
- LOIs
- signups
- active users
- activity volume
- ecosystem pull
- MoM growth
- Velocity Score

### Important limitation

This is a **performance-proxy dataset**, not a YC-selection dataset. All 11 companies were already selected by YC.

---

# H1 — Founder capability

## Result: NOT DIRECTLY TESTABLE from this dataset

The W26 traction data contain no founder-background variables.

The strongest external empirical evidence currently in the Atlas is the 2025 study of 4,323 YC companies. It reports that observable founder-background variables explain less than 4% of funding variation, while larger founding teams are associated with higher funding.

### Interpretation

This supports the Atlas's anti-pedigree caution but does **not** establish that capability causes YC selection.

### What is required

A founder-level panel with:

- technical build history
- domain expertise
- previous startup experience
- prior exits
- employer history
- education
- team complementarity
- application-stage evidence of execution

and, ideally, rejected applicants as the control group.

**Status: deferred, not failed.**

---

# H2 — Problem leverage

## Result: NOT CAUSALLY TESTABLE; current quantitative proxy is inadequate

The previous script created a keyword-count “problem leverage” variable from company descriptions. We are **not treating that as a valid test** because keyword frequency is an unreliable measure of customer pain.

This is an important correction to the previous Atlas methodology.

### Why we rejected the proxy

A company can say “automate” ten times and still solve an unimportant problem. Another company may solve an extremely painful problem without using any of those words.

### What can be said now

The W26 portfolio contains many companies attacking operational workflows in healthcare, industrial systems, finance, legal/compliance and enterprise software. This is **directional evidence**, not a statistical test.

### Required test

Hand-code a blinded sample of companies on:

- pain severity
- frequency
- economic cost
- buyer urgency
- workflow complexity
- automation potential

Then regress selection and outcomes against those scores.

**Status: deferred.**

---

# H3 — AI leverage

## Result: CURRENT-PORTFOLIO EVIDENCE IS STRONG; CAUSAL EFFECT IS UNTESTED

The W26 evidence shows AI operating as a cross-cutting technical layer. CB Insights reports 39 AI-infrastructure companies among 199 W26 companies, while the YC RFS explicitly emphasizes AI-native workflows and physical-world AI.

However, the current public data do not provide a clean counterfactual such as:

> identical companies, one using AI and one not using AI.

Therefore we **cannot claim that AI causes superior outcomes**.

### Better H3 test

Code AI role on a 0–5 scale:

0. none  
1. feature  
2. AI-enabled product  
3. AI-native workflow  
4. AI is fundamental to feasibility/economics  
5. frontier infrastructure/model layer

Then test the score against outcomes while controlling for cohort, sector, geography and founder variables.

**Current status: supported as a portfolio pattern; unvalidated as a causal predictor.**

---

# H4 — Early-stage judgment

## Result: PARTIALLY TESTED THROUGH AN EXTERNAL FORECASTING BENCHMARK, NOT YC SELECTION

YC Bench provides an unusually useful experiment. It forecasts W26 company performance from signals available before or during the batch. Its published baseline using pre-application Google mentions reports:

- Precision@20: 70%
- Recall@11: 55%
- Lift over random: 7×
- Forecast horizon: approximately 5 months

This demonstrates that **some early public signals contain predictive information about near-term startup performance**.

But it does not establish that YC used those signals, nor does it tell us what YC rejected.

### Therefore

H4 receives:

**Evidence that early information can predict startup performance: YES.**  
**Evidence that YC's selection judgment can be reconstructed from public data: NO.**

### Required gold-standard test

Obtain a sufficiently representative applicant/rejected-applicant sample and freeze all variables at application time. Then compare:

1. random selection
2. simple traction model
3. founder model
4. market model
5. Venture Atlas model
6. actual YC selection

The question is whether Venture Atlas adds predictive power beyond simple observable signals.

---

# H5 — Venture-scale potential

## Result: STRUCTURALLY PLAUSIBLE; NOT YET VALIDATED

The current portfolio strongly emphasizes large technical markets: AI infrastructure, industrial automation, robotics, healthcare, fintech and enterprise systems.

But category presence cannot establish future venture scale.

### Correct test

Define outcome tiers before observing the results:

- survival at 5 years
- Series A
- Series B
- acquisition
- IPO / major liquidity event

Then model the probability of each outcome from information available at acceptance.

Use survival analysis for time-to-event outcomes and out-of-sample testing for prediction.

**Status: deferred.**

---

# Quantitative check on the available W26 traction subset

For the 11 companies in the published traction subset, Spearman correlations with Velocity Score are:

| Signal | Spearman rho | p-value | Interpretation |
|---|---:|---:|---|
| ARR | 0.503 | 0.115 | Moderate positive association; not significant at n=11 |
| Pilot revenue | -0.200 | 0.555 | No reliable relationship in this tiny subset |
| LOIs | 0.400 | 0.223 | Positive direction; underpowered |
| Signups | -0.283 | 0.399 | No reliable relationship |
| Active users | -0.400 | 0.223 | No reliable relationship |
| Activity volume | 0.310 | 0.353 | Positive direction; underpowered |
| Ecosystem pull | -0.500 | 0.117 | No reliable relationship |
| MoM growth | 0.500 | 0.117 | Positive direction; underpowered |

### Why these numbers matter

They are **not evidence that ARR does or does not predict YC success**. The sample is only 11 companies and the outcome is a short-horizon batch-performance proxy.

They demonstrate why Venture Atlas needs the full company panel instead of narrative inference from a handful of winners.

---

# What we can now claim

### Strongly supported

- YC's current portfolio is heavily shaped by AI and other new technical capabilities.
- Physical/industrial applications are materially visible in W26.
- Early public signals can contain predictive information about near-term startup performance.
- Founder prestige alone is an inadequate explanation of funding variation.

### Directionally supported

- YC appears attracted to painful operational workflows.
- Technical leverage is increasingly important.
- Large-scale outcomes remain central to the venture model.

### Not yet proven

- Founder capability causally predicts YC selection.
- Problem leverage causally predicts YC selection.
- AI leverage causes superior outcomes.
- Venture Atlas can predict YC acceptance better than simple heuristics.
- Venture Atlas can outperform YC selection itself.

---

# The actual next experiment

The remaining research bottleneck is **not more writing**.

It is data acquisition.

```text
YC selected companies
          +
YC rejected applicants
          +
Acceptance-time founder/product/traction data
          ↓
Frozen panel
          ↓
Train / validation / test split by time
          ↓
H1–H5 models
          ↓
Ablation tests
          ↓
Calibration + precision@top-k
          ↓
Compare against simple baselines
          ↓
Update Venture Atlas model
```

Until that panel exists, the intellectually honest conclusion is:

> **Venture Atlas has a strong, evidence-backed theory of YC selection, but it has not yet demonstrated predictive validity.**

That distinction is now explicit in the research record.

## Sources

- YC Bench repository: https://github.com/benstaf/ycbench
- YC Bench paper: https://arxiv.org/abs/2604.02378
- YC Companies: https://www.ycombinator.com/companies
- YC RFS: https://www.ycombinator.com/rfs
- Adl, Founder Backgrounds and Startup Funding: https://arxiv.org/abs/2512.13755
