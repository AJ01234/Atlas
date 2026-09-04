# 27 — Investor Atlas: Deep Company-Level Evidence

**Version:** v2.0 — evidence expansion  
**Date:** 4 September 2026  
**Purpose:** Reverse-engineer how differentiated investors actually select and support companies, using portfolio evidence rather than generic investor branding.

> **Method rule:** This chapter separates **FACT**, **OBSERVATION**, **INFERENCE**, and **TEST**. Portfolio examples demonstrate what a firm has backed; they do not by themselves prove that a stated characteristic caused an outcome.

## 27.1 Executive finding

Across the investors studied, there is no single universal VC selection formula. The strongest repeatable pattern is a layered model: founder quality or founder-problem fit; a structurally important problem or market; and a differentiated source of compounding advantage. Investors differ mainly in the edge they underwrite.

- **Sequoia:** exceptional founder + non-obvious insight + large market.
- **a16z:** technology/category opportunity + platform leverage + operator support.
- **HF0:** repeat-founder execution compression + unusually strong operating velocity.
- **EF:** latent founder capability before company maturity.
- **NFX:** team + market + explicit network-effect compounding.
- **General Catalyst:** founder/problem fit + difficult problem + mission + institutional support.
- **OpenAI ecosystem:** frontier-model-native builders + real-work deployment leverage.
- **NVIDIA:** AI/technical depth + strategic ecosystem fit; Inception is an ecosystem funnel, while NVentures is the curated strategic capital layer.

The portfolio itself is the decisive evidence. A firm's stated thesis explains its intended lens; repeated portfolio behavior is stronger evidence of what it finds investable.

Selection and support must also be modeled separately. Some organizations primarily underwrite companies; others deliberately add talent formation, compute, distribution, technical infrastructure, customer access or founder residency.

---

## 27.2 Investor comparison matrix

| Investor | Primary entry point | Core underwriting object | Distinctive edge | Portfolio evidence signal | Evidence strength |
|---|---|---|---|---|---|
| **YC** | Very early | Founder + problem + velocity of learning | Dense founder network, batch pressure | Broad category exposure; current RFS emphasizes AI moving into the physical world and rebuilding systems | High for public thesis; moderate for hidden weights |
| **Sequoia** | Pre-seed/seed/A | Exceptional founder + insight + market | Long-term company building | Stripe, Airbnb, NVIDIA, SpaceX, Vanta, Retool plus newer AI companies | High |
| **a16z** | Seed through growth | Team + idea + market/category | Large operator/platform layer | Broad sector portfolio; deep current AI infrastructure exposure | High |
| **HF0** | Residency | Repeat founder + execution | Intense in-person environment; 10 teams at a time | Public cohorts show unusually high demo-day revenue | High for program profile; moderate for causal selection |
| **EF** | Individual before company/cofounder | Founder potential | Talent discovery + cofounder/company formation | Investment can precede a fully formed company | High for design; lower for attribution |
| **NFX** | Pre-seed/seed | Team + market + network effects | Network-effects expertise | Explicit network-effect thesis and historical value study | High for thesis; moderate for causal effect |
| **General Catalyst** | Seed through growth | Founder/problem fit + hard problem + differentiation | Thematic and operating support | Strong presence in difficult healthcare, defense, infrastructure and AI problems | High |
| **OpenAI ecosystem** | AI-native startups | Model leverage + deployment | Frontier-model access and ecosystem support | Current frontier-builder examples are deeply model-native | Moderate |
| **NVIDIA Inception / NVentures** | Inception: broad; NVentures: curated | Technical AI depth + strategic fit | Compute, software, expertise, investor and GTM network | Robotics, AI infra, digital biology, applied AI, frontier compute | High |

---

# 27.3 Sequoia Capital

## FACT

Sequoia's own seed-investing description says it seeks exceptional founders with a unique insight focused on a market poised for large growth, and that it is more interested in what might be possible than in a working product or existing customers. It also describes active help with strategy, recruiting and customer introductions. [S1]

Its public company directory includes long-duration winners such as SpaceX, Airbnb, NVIDIA, Reddit, Linear, Snowflake, Stripe, Vanta and Retool, alongside newer AI infrastructure and application companies. [S2]

Sequoia's people pages expose partner-level company histories. David Cahn's page, for example, lists companies including Air, Astrocade and Clay with stage and first-partnered information. [S3]

## OBSERVATION

The portfolio is not narrowly sector-defined. The recurring feature is that a strong founder can plausibly define or reshape a large market.

## INFERENCE

**Sequoia selection model:**

> Exceptional founder × non-obvious insight × large market × willingness to build before proof is obvious.

The critical variable is **insight**, not merely competence. The strongest candidate should know or believe something important that a smart outsider is unlikely to know.

## Testable founder questions

- Why this founder specifically?
- What non-obvious fact do they understand?
- Why can the market become much larger than current estimates suggest?
- Is the company early because it is weak, or because the opportunity is ahead of the market?

## FALSIFIER

If a broad matched sample of Sequoia early-stage investments shows pre-investment traction predicts later outcomes substantially better than founder insight and market structure, the thesis weakens.

---

# 27.4 Andreessen Horowitz (a16z)

## FACT

a16z's public portfolio is broad and stage-diverse; the firm says the public list includes current and former investments and is updated monthly. [A1]

Its enterprise portfolio spans AI/ML, data, DevOps, infrastructure, security, platform engineering and SaaS. [A2]

Its current infrastructure portfolio is especially revealing: it includes Databricks, dbt Labs, Fivetran, Pinecone, OpenAI, OpenRouter, Mistral AI, Replicate, Resend, Tecton, World Labs and many others. [A3]

## OBSERVATION

The firm's advantage is difficult to reduce to a single sector thesis. The evidence is more consistent with a **category + platform** model: identify important technology categories early, then surround companies with recruiting, marketing, policy/legal, technical and domain capabilities.

## INFERENCE

**a16z model:**

> Team + technology/category opportunity + platform acceleration.

The infrastructure portfolio also suggests preference for companies that can become a technical **control point** rather than merely another end-user feature.

## FALSIFIER

If platform resources do not produce measurable incremental outcomes relative to matched companies, the support-edge hypothesis weakens.

---

# 27.5 HF0

## FACT

HF0 explicitly calls itself “the residency for repeat founders.” [H1]

HF0 states that it backs only 10 teams at a time. Its published facts include: four of ten W25 teams breaking $3M revenue by demo day; three of ten S24 teams breaking $2M ARR by demo day; and earlier cohorts with repeat-unicorn/repeat-decacorn founders. [H2]

## OBSERVATION

This distribution is materially different from a broad idea-stage accelerator. HF0 appears designed for people already capable of unusually fast execution, while the residency removes distractions and increases peer intensity.

## INFERENCE

**HF0 model:**

> Prior founder experience × operating velocity × intense environment.

The environment itself is part of the investment design: selection brings together founders likely to benefit from compressed execution.

## FALSIFIER

Compare first-time versus repeat founders controlling for starting traction, sector and team size. If repeat-founder status does not retain predictive value, the public thesis is overstated.

Public data do not currently support that causal estimate.

---

# 27.6 Entrepreneur First (EF)

## FACT

EF is structurally different because its investment object can be the **person before the company**. Its model is based around talent discovery, cofounder matching and company formation.

## OBSERVATION

EF therefore accepts greater uncertainty in the company variable and attempts to reduce uncertainty in the founder variable.

## INFERENCE

**EF model:**

> Latent founder capability → cofounder formation → company formation → market discovery.

The appropriate unit of analysis is not only the startup. It is the **founder trajectory**.

## Variables Venture Atlas should measure

`learning_rate`, `agency`, `technical_depth`, `resilience`, `recruiting`, `domain_authority`, `ambiguity_tolerance`, `ambition`

## FALSIFIER

If prior company traction predicts EF outcomes better than founder variables measured before company formation, the talent-first thesis is overstated.

A public startup panel cannot run this cleanly.

---

# 27.7 NFX

## FACT

NFX explicitly centers network effects. Its Network Effects Manual describes network effects as a major source of digital defensibility and lays out multiple network-effect types. [N1]

Its historical study examined 336 internet-era companies that reached $1B+ value and estimated that roughly 35% had network effects at the core but accounted for about 68% of total value in its spreadsheet. [N2]

## OBSERVATION

NFX provides a mechanistic theory of defensibility rather than a simple sector label. The core question is:

> What becomes more valuable because more participants use the system?

## INFERENCE

**NFX model:**

> Team × market × compounding network effect.

The network loop must be structural, such as participant → liquidity/data/content/identity → greater value → more participants.

## FALSIFIER

If NFX's strongest outcomes are routinely non-network businesses that win through ordinary execution, network effects are less central than advertised.

---

# 27.8 General Catalyst

## FACT

GC's public portfolio is broad and currently includes companies such as Anduril, Anthropic, Applied Intuition, Commure, Helsing, Hippocratic AI, Legora, Maven, Mercor, Ramp, Re:Build, Stripe and Zepto. [G1]

The live portfolio spans AI, defense, healthcare, enterprise, fintech and infrastructure and contains many operationally difficult businesses. [G1]

## OBSERVATION

A common feature is not one technology but **problem difficulty** plus the possibility of institutional help.

## INFERENCE

**GC model:**

> Founder/problem fit × important pain × differentiation × mission × institutional leverage.

A useful operating question is: **Why them on this problem?**

## FALSIFIER

If founder/problem fit fails to distinguish GC-backed winners from comparable non-backed companies in the same markets, sector selection or traction may be more important than the qualitative thesis.

---

# 27.9 OpenAI ecosystem / Startup Fund lineage

## FACT

The historical OpenAI Startup Fund was a dedicated investment effort around AI companies with large impact potential. Current OpenAI startup materials are broader and describe a startup ecosystem that helps founders build, grow and scale through technical education, events, resources and support through eligible VC partners. [O1][O2]

OpenAI now explicitly highlights **frontier builders** creating companies natively on OpenAI models. Current examples include Clay, Valthos, Unify, Vanta and Decagon; OpenAI describes them as using machine intelligence to perform real work across functions including go-to-market, customer experience, compliance and biodefense. [O3]

## OBSERVATION

The modern ecosystem should not be treated as one closed VC portfolio. It is closer to a **deployment ecosystem around frontier models**.

## INFERENCE

**OpenAI ecosystem model:**

> Model-native product insight × real-work automation × deployment leverage.

A strong company becomes more capable as frontier-model performance improves, while retaining product and workflow differentiation.

## FALSIFIER

If model capabilities commoditize and the company's differentiation remains unchanged, model leverage was less central than believed.

---

# 27.10 NVIDIA Inception / NVentures

## FACT

NVIDIA Inception is an ecosystem program, not an equity fund. NVIDIA says it is free, has no application fees or equity requirement, and accepts startups at any funding stage. Benefits include technical training, preferred pricing, cloud credits, partner offers, investor exposure and go-to-market support. [N1V]

NVIDIA's VC Alliance says it provides access to a network with visibility into more than 30,000 high-growth AI startups and includes curated founder/VC interactions. [N1W]

Separately, NVentures is NVIDIA's venture capital arm. NVIDIA says it invests in technology companies solving complex problems, particularly AI infrastructure, robotics, digital biology, applied AI and frontier compute, while offering access to technical teams, platform integration and go-to-market resources. [N2V]

## OBSERVATION

This creates two different filters:

**Inception:** broad ecosystem/top-of-funnel participation.

**NVentures:** narrower strategic capital selection.

Therefore Inception membership is weak evidence of investment conviction because membership does not require equity.

## INFERENCE

**NVIDIA strategic model:**

> Technical AI depth × strategic ecosystem fit × compute/platform leverage.

Strategically attractive companies can strengthen or extend NVIDIA's ecosystem through compute demand, developer adoption, robotics deployment, scientific workloads or applied AI.

## FALSIFIER

If NVentures companies show little strategic relationship to NVIDIA's platform and perform like unrelated financial investments, the strategic-fit thesis weakens.

---

# 27.11 Cross-investor pattern mining

## Pattern A — Founder quality is universal, but the definition changes

- Sequoia → insight.
- HF0 → repeat execution.
- EF → latent capability before company formation.
- GC → founder/problem fit.
- YC → agency and learning velocity.

**Atlas implication:** do not create one founder number. Use a vector:

`insight | speed | technical depth | resilience | recruiting | domain authority | ambition | learning rate`

Different investors assign different weights.

## Pattern B — Market size is not enough

Strong investors care about the **mechanism by which a market expands**:

- new capability creates a new category,
- automation makes expensive labor addressable,
- network effects create compounding economics,
- infrastructure becomes a control point,
- distribution shifts,
- regulation/geopolitics creates a strategically large market.

Therefore Atlas should measure `market_expansion_mechanism`, not just TAM.

## Pattern C — Control points recur across portfolios

High-value portfolio companies often become one of:

1. **Infrastructure control points** — compute, data, tooling, core systems.
2. **Workflow control points** — systems that actually perform the work.
3. **Network control points** — systems connecting participants.
4. **Distribution control points** — routes to customers.
5. **Platform control points** — a substrate others build on.
6. **Strategic control points** — assets important to a larger ecosystem.

This is more useful for opportunity mapping than sector labels alone.

---

# 27.12 Atlas investor-prior scorecards

These are **research priors**, not fitted coefficients.

### Sequoia-like

`0.30 founder insight + 0.25 market transformation + 0.20 founder-market fit + 0.15 ambition + 0.10 early evidence`

### a16z-like

`0.25 technology/category timing + 0.20 team + 0.20 market + 0.15 distribution + 0.10 platform leverage + 0.10 defensibility`

### HF0-like

`0.35 execution velocity + 0.30 founder track record + 0.20 traction quality + 0.15 intensity/environment fit`

### EF-like

`0.30 learning rate + 0.25 agency + 0.20 founder quality + 0.15 recruiting ability + 0.10 ambition`

### NFX-like

`0.30 network-effect strength + 0.25 market + 0.20 team + 0.15 compounding loop + 0.10 distribution`

### GC-like

`0.25 founder/problem fit + 0.20 problem importance + 0.20 differentiation + 0.15 mission/endurance + 0.10 institutional leverage + 0.10 traction`

### OpenAI-like

`0.30 model leverage + 0.25 real-work substitution + 0.20 founder/technical execution + 0.15 deployment advantage + 0.10 ecosystem fit`

### NVIDIA-like

`0.30 technical depth + 0.25 compute/workload leverage + 0.20 strategic ecosystem fit + 0.15 deployment path + 0.10 category growth`

**These weights must be re-estimated through backtesting before being used as investment rules.**

---

# 27.13 Company-level evidence schema

To convert this atlas into an investable research system, every portfolio company should eventually be coded into a common table:

```text
company_id
investor
first_partnered_year
stage_at_first_investment
sector
subsector
business_model
founder_count
founder_prior_startups
founder_domain_expertise
founder_technical_depth
problem_type
pain_intensity
market_expansion_mechanism
technical_leverage
network_effect
workflow_ownership
distribution_advantage
capital_intensity
regulatory_complexity
AI_native
infrastructure_position
strategic_ecosystem_fit
initial_traction
later_outcome
outcome_date
exit_type
survival_status
```

The important transition is from **anecdotal investor stories to a structured investor-company panel**.

---

# 27.14 Biases and evidence caveats

Public portfolio evidence contains at least seven important distortions:

1. **Survivorship bias** — failed or written-off companies are less visible.
2. **Disclosure bias** — private investments may remain undisclosed.
3. **Right-censoring** — young companies have not had enough time to mature.
4. **Investor-stage mixing** — seed behavior and growth behavior are not interchangeable.
5. **Selection-on-selection** — a company may be backed by several investors with different theses.
6. **Post-hoc narrative bias** — successful founders are easier to describe as “visionary” after success.
7. **Support-treatment confounding** — investor support may itself affect outcomes.

Any empirical investor comparison must explicitly model these issues.

---

# 27.15 What this chapter proves vs does not prove

### Supported with strong public evidence

- The investors publicly describe materially different investment philosophies.
- Their current portfolios show recurring structures that are consistent with those philosophies.
- Some investors operate broad ecosystems rather than pure capital vehicles.
- NFX provides a quantitative historical argument for network-effect asymmetry.
- HF0 publicly reports unusually concentrated selection and very high early operating metrics.
- NVIDIA clearly separates broad Inception support from its strategic VC arm.

### Not yet proven

- The hidden coefficients behind any investor's decisions.
- That any single qualitative trait causes startup success.
- That investor support itself causes higher outcomes.
- That the Atlas priors above outperform simple heuristics.
- That rejection or non-selection is unrelated to omitted founder variables.

Those questions belong to the empirical chapters.

---

# 27.16 Bottom line

The deepest cross-investor conclusion is not “pick AI,” “have traction,” or “be technical.”

> **Back a rare founder into a structurally expanding market where the company can own a compounding control point.**

The different investors mainly disagree on which part of that equation they are best at recognizing and which capabilities they can add after investment.

Venture Atlas should therefore become a **multi-investor selection engine** rather than a single universal startup score.

---

# Source registry

**[S1] Sequoia — Sequoia and Seed Investing**  
https://sequoiacap.com/article/sequoia-and-seed-investing

**[S2] Sequoia — Our Companies**  
https://sequoiacap.com/our-companies

**[S3] Sequoia — David Cahn**  
https://sequoiacap.com/people/david-cahn

**[A1] a16z — Portfolio**  
https://a16z.com/portfolio/

**[A2] a16z — Enterprise**  
https://a16z.com/enterprise/

**[A3] a16z — Infra**  
https://a16z.com/infra/

**[H1] HF0**  
https://www.hf0.com/

**[H2] HF0 — Facts**  
https://www.hf0.com/facts

**[N1] NFX — Network Effects Manual**  
https://www.nfx.com/post/network-effects-manual

**[N2] NFX — 70 Percent of Value in Tech is Driven by Network Effects**  
https://www.nfx.com/post/70-percent-value-network-effects

**[G1] General Catalyst — Portfolio**  
https://www.generalcatalyst.com/portfolio

**[O1] OpenAI — OpenAI for Startups**  
https://openai.com/startups

**[O2] OpenAI — Startups**  
https://openai.com/business/why-openai/startups/

**[O3] OpenAI — Frontier Builders**  
https://openai.com/index/frontier-builders/

**[N1V] NVIDIA — Inception**  
https://www.nvidia.com/en-us/startups/

**[N1W] NVIDIA — Venture Capital Alliance**  
https://www.nvidia.com/en-us/startups/venture-capital/

**[N2V] NVIDIA — NVentures**  
https://www.nvidia.com/en-us/startups/nventures/
