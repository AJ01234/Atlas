# 37 — Empirical Dataset Specification

## Objective

Build the company-level panel required to turn Venture Atlas from a research synthesis into a tested investor-selection model.

## Unit of analysis

One row = one YC-backed company.

## Required fields

### Identity
- company_id
- company_name
- batch
- batch_year
- founded_year
- headquarters
- founders

### Founder variables
- founder_count
- founder_build_score
- founder_domain_score
- founder_execution_score
- founder_learning_score
- founder_team_complementarity
- prior_startup_experience
- prior_funding_experience
- prior_FAANG_experience
- education_tier

### Company-at-acceptance variables
- product_one_liner
- problem_statement
- customer
- industry
- technology_layer
- ai_role
- robotics_role
- hardware_role
- business_model
- traction_state
- revenue_at_acceptance
- users_at_acceptance
- growth_at_acceptance
- paying_customers_at_acceptance
- founder_customer_experience
- why_now
- market_size_proxy
- workflow_frequency
- workflow_cost
- workflow_complexity
- buyer_clarity
- automation_potential
- proprietary_data_potential
- network_effect_potential
- distribution_advantage
- capital_intensity
- regulatory_intensity

### Outcome variables
- funding_total
- funding_round_count
- follow_on_funding
- time_to_follow_on_funding
- series_a
- time_to_series_a
- series_b
- acquisition
- public
- shutdown
- active_status
- employee_count_latest

## Coding rules

Every subjective variable must have:

1. a 0–5 rubric;
2. written evidence;
3. source URL;
4. date observed;
5. coder confidence.

Do not infer traction from later outcomes. The acceptance-time fields must represent information available at or before acceptance.

## Core hypothesis variables

### Founder capability
Composite of build, domain, execution, learning and complementarity.

### Problem leverage
Composite of workflow cost, frequency, complexity, buyer clarity and automation potential.

### Technical leverage
0 = technology is incidental.  
5 = technical capability makes the product economically or operationally possible in a way that was previously impractical.

### AI role
- 0 = no AI
- 1 = minor feature
- 2 = meaningful feature
- 3 = core product capability
- 4 = AI-native workflow
- 5 = AI is the operating mechanism of the company

### Venture-scale potential
Separate TAM from reachable market and expansion mechanism. Score only after identifying the initial wedge.

## Statistical plan

### Model 1 — Funding
Log funding amount against founder, company and batch variables.

### Model 2 — Series A
Logistic regression for whether a company reaches Series A within a fixed window.

### Model 3 — Time to funding
Survival model for time from YC acceptance to next funding event.

### Model 4 — Survival
Time-to-shutdown analysis.

### Model 5 — Robustness
Tree-based models to identify nonlinear interactions, followed by interpretable feature analysis.

## Required controls

- batch
- sector
- geography
- founding year
- initial traction
- capital intensity
- cohort age at observation

## Avoiding common errors

### Survivorship bias
Do not study only successful companies.

### Label leakage
Do not use post-acceptance information to score acceptance-time selection.

### Sector confounding
AI companies may have different funding environments than biotech or hardware companies.

### Batch effects
Macro funding conditions vary sharply across years.

### Taxonomy drift
YC category labels change. Create a normalized taxonomy and retain the original YC tags separately.

### Founder pedigree overfitting
Do not let school/employer variables dominate capability measures.

## Minimum viable validation dataset

A first meaningful test should cover:

- all available YC companies through the latest frozen directory snapshot;
- at least 10 years of cohorts;
- company-level outcomes;
- founder variables where publicly observable;
- acceptance-time traction where observable.

A smaller hand-coded sample can be used first to validate the coding rubric, but it should not be presented as the final statistical test.

## Current evidence anchor

The 2025 YC founder/funding study provides a useful benchmark: it uses 4,323 YC companies from 2005–2024 and finds observable founder-background variables explain less than 4% of funding variation. citeturn0academia31

The 2026 W26 analysis provides a second benchmark: 199 companies across 15 categories, with 39 AI-infrastructure companies and 35 industrial/defense companies. citeturn3search0

These are benchmarks, not substitutes for the Atlas dataset.
