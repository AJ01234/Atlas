# 39 — Company-Level Panel Validation Runbook

**Research cut-off:** 22 August 2026  
**Status:** pipeline implemented; statistical execution requires a GitHub Actions run or local execution environment.

## What is implemented

`analysis/build_yc_panel.py` downloads the YC OSS public company directory, writes a one-row-per-company CSV panel, constructs transparent proxy variables, and estimates logistic models for H2, H3 and H5. H1 and H4 are explicitly marked untestable from the public YC directory because the required founder-background and acceptance-time traction variables are not present.

`.github/workflows/run-yc-panel.yml` is configured to install dependencies, execute the analysis, and commit generated outputs under `analysis_output/`.

## Why this is not yet the final Chapter 37 test

Chapter 37 requires acceptance-time variables including founder capability, problem leverage, traction, customer experience, workflow cost/frequency/complexity, buyer clarity, automation potential, proprietary-data potential, distribution advantage, capital intensity and regulatory intensity. It also requires funding-round outcomes and time-to-event measures. fileciteturn87file0

The public YC OSS directory exposes company-level descriptive fields such as batch, description, industry, tags, team size, stage, status and top-company flag, but not the complete acceptance-time panel or funding history. citeturn4search0turn4search1

## Tests that can be run honestly from the public panel

### H1 — Founder capability
**Deferred.** Do not substitute current team size or school pedigree for the Chapter 37 founder-capability composite.

### H2 — Problem leverage
Run a logistic regression of a deliberately labeled success proxy on a text-derived workflow/problem proxy, controlling for batch and industry. This is a **proxy stress test**, not a causal acceptance test.

### H3 — AI leverage
Run a logistic regression of the success proxy on an AI-tag indicator, controlling for batch and industry. Again, this tests association with later public-directory outcomes, not YC's acceptance decision.

### H4 — Early-stage judgment
**Deferred.** Using later revenue/users/growth would create label leakage. Acceptance-time traction must be reconstructed from dated evidence.

### H5 — Venture-scale potential
Run a coarse proxy test using public-company status/top-company/team-size outcomes and a transparent scale proxy. This is explicitly not a TAM test.

## External benchmark

The 2025 YC founder-background study used 4,323 YC companies from 2005–2024 and a 2,113-company regression sample. It finds observable founder-background variables explain less than 4% of funding variation and reports a more robust association between larger founding teams and funding, around 21% more capital per additional co-founder. This is an external benchmark, not a substitute for Atlas's acceptance-time model. citeturn0academia34

## Execution integrity rule

Until `analysis_output/hypothesis_results.csv` exists from a completed run, Atlas must not report numerical H2/H3/H5 coefficients or p-values as completed results. The correct status is **pipeline implemented, execution pending**.
