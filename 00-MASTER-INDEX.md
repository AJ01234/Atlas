# Venture Atlas — Master Index

**Version:** v3.2 — Consolidated + Executed Empirical Validation  
**Date:** 22 August 2026  
**Status:** Consolidated research master

> This is the canonical map of Venture Atlas. Existing research files are preserved as modules; this index defines the reading order and prevents duplicate numbering from being mistaken for separate conclusions.

## PART I — FOUNDATION

01 — `01-Executive-Summary.md` — Executive Summary  
02 — `02-RESEARCH_METHODOLOGY.md` — Research Methodology  
03 — `03-YC-HISTORY.md` — YC History  
04 — `04-YC-INVESTMENT_THESIS.md` — YC Investment Thesis  
05 — `05-YC-RFS-ANALYSIS.md` — YC RFS Analysis  
06 — `06-YC-BATCH-ANALYSIS-FRAMEWORK.md` — Batch Analysis Framework  
07 — `07-STARTUP-COMPANY-RESEARCH-FRAMEWORK.md` — Company Research Framework  
08 — `08-FOUNDER-EVALUATION-FRAMEWORK.md` — Founder Evaluation Framework  
09 — `09-MARKET-OPPORTUNITY-FRAMEWORK.md` — Market Opportunity Framework  
10 — `10-WHITE-SPACE-ANALYSIS-FRAMEWORK.md` — White Space Framework  
11 — `11-YC-HISTORY-DEEP-RESEARCH(1).md` — YC History Deep Research  
12 — `12-YC-INVESTMENT-THESIS-DEEP-RESEARCH.md` — YC Investment Thesis Deep Research

## PART II — YC DEEP DIVE

13 — `13-YC-RFS-DEEP-ANALYSIS.md` — YC Requests for Startups  
14 — `14-YC-BATCH-EVOLUTION.md` — Batch Evolution  
15 — `15-YC-APPLICATION-PLAYBOOK.md` — Application Playbook  
16 — `16-YC-DEMO-DAY-AND-FUNDRAISING.md` — Demo Day & Fundraising  
17 — `17-YC-PARTNER-AND-ORG-STRUCTURE.md` — Partner & Organization Structure  
18 — `18-YC-SUCCESS-PATTERNS.md` — Success Patterns  
19 — `19-YC-FAILURE-PATTERNS.md` — Failure Patterns  
20 — `20-YC-AI-SHIFT.md` — AI Shift  
21 — `21-YC-FOUNDER-ARCHETYPES.md` — Founder Archetypes  
22 — `22-YC-SECTOR-MAP.md` — Sector Map  
23 — `23-YC-GLOBAL-GEOGRAPHY.md` — Global Geography  
24 — `24-YC-WHAT-YC-AVOIDS.md` — What YC Appears Less Excited About  
25A — `25-2026-BATCH-ANALYSIS.md` — 2026 Batch Evidence Module  
25B — `25-PART-I-SYNTHESIS.md` — YC Selection Model

**Consolidation rule:** 25A and 25B are two modules of the Chapter 25 evidence/synthesis layer, not two independent chapters.

## PART III — INVESTOR ATLAS

26 — `26-INVESTOR-COMPARISON.md` — Investor Comparison  
27 — `27-INVESTOR-ATLAS.md` — Individual Investor Atlases  
28 — `28-FOUNDER-PATTERNS.md` — Cross-Investor Founder Patterns

## PART IV — MARKET & OPPORTUNITY ATLAS

29 — `29-MARKET-MAPS-2026.md` — 2026 Market Maps  
30 — `30-OPPORTUNITY-MAPS.md` — Opportunity Maps  
31 — `31-WHITE-SPACE.md` — White Space

## PART V — FOUNDER APPLICATION

32 — `32-FOUNDER-PLAYBOOK.md` — Founder Playbook

## PART VI — SYNTHESIS & REFERENCES

33 — `33-FINAL-SYNTHESIS.md` — Final Synthesis  
34 — `34-REFERENCES.md` — References  
35* — `26-YC-COMPANY-PROFILES-2026.md` — 2026 Company Profiles

*35 is a reading-order designation only; the historical filename is preserved to avoid destructive renaming.

## PART VII — EMPIRICAL VALIDATION

36 — `36-EMPIRICAL-VALIDATION-2026.md` — 2026 Empirical Validation  
37 — `37-EMPIRICAL-DATASET-SPEC.md` — Company-Level Dataset Specification  
38 — `38-W26-QUANTITATIVE-VALIDATION.md` — W26 Quantitative Validation  
40 — `40-EMPIRICAL-VALIDATION-RUN.md` — Executed empirical validation run

Supporting data:

- `analysis/ycbench_w26_traction.csv` — reproducible 11-company W26 traction subset used for the executed correlation checks.
- `analysis/build_yc_panel.py` — reproducible public-portfolio panel builder and proxy-test code; its unsupported keyword proxy is not treated as a final H2 test.

## RECOMMENDED READING PATH

**01 → 02 → 11 → 12 → 13–24 → 25A → 25B → 26 → 27 → 28 → 29 → 30 → 31 → 35 → 32 → 33 → 34 → 36 → 37 → 38 → 40**

Research-system path:

**Methodology → Frameworks → Evidence → Selection Model → Investor Comparison → Founder Patterns → Market Maps → Opportunities → Company Profiles → Founder Playbook → Empirical Validation → Dataset → Quantitative Validation → Executed Tests → Backtesting**

## CANONICAL INTELLECTUAL SEQUENCE

```text
Research method
      ↓
YC as first case study
      ↓
Evidence about selection
      ↓
YC Selection Model
      ↓
Cross-investor comparison
      ↓
Common founder signals
      ↓
Market structure
      ↓
Opportunity / white space
      ↓
Founder application
      ↓
Empirical validation
      ↓
Quantitative cohort validation
      ↓
Executed proxy tests
      ↓
Acceptance-time company-level backtesting
      ↓
Updated investor model
```

## CURRENT VALIDATION STATUS

The empirical work has now been **actually executed where public evidence permits**. The Atlas does not convert proxy results into causal claims.

- **H1 Founder capability — not directly testable from the public W26 panel; external YC research provides directional evidence.**
- **H2 Problem leverage — not yet validly tested; the earlier keyword proxy is rejected as insufficient.**
- **H3 AI leverage — strong current portfolio evidence; causal outcome effect remains untested.**
- **H4 Early-stage judgment — partially informed by YC Bench's external forecasting benchmark, but YC selection itself remains untested.**
- **H5 Venture-scale potential — structurally plausible, not causally validated.**

The next milestone is **not another narrative chapter**. It is obtaining/building a sufficiently rich acceptance-time panel, ideally including rejected applicants, and running the preregistered H1–H5 models with temporal holdouts and ablation tests.
