# AI 2027 compute forecast: research workfile

**Research cutoff: 12 November 2026.** This is the working research companion to [the supplied forecast](Compute%20Forecast%20%E2%80%94%20AI%202027.html). Numbers below retain their observation dates; publication in 2026 does not turn a 2025 inventory estimate into a current measurement.

## Reports added 12 November 2026

- [Author-update research correction](research/04-ai-futures-wafer-update.md): newly located AI 2040 compute supplement by Romeo Dean; consult before selecting post-2027 wafer assumptions.

- [Report 3: production news and model implications](research/03-production-news-and-model-implications.md): 14 individual assessments of wafer, HBM, packaging, equipment, materials, and hardware news; importance, production dates, recommended adjustments, and reproducible sensitivities.

The initial calculation below is retained as an **aggregate trend estimate**, not a component-model update. Two separate reports now document the methods:

- [Report 1: initial approach and findings](research/01-initial-trend-approach.md): log-linear Epoch shipment extrapolation; 97.6M operational dense-FP8 H100e at end-2027.
- [Report 2: component-limited production estimate](research/02-component-production-forecast.md): separate logic, packaging and HBM limits, updated hardware specifications, and explicit assumed inputs; central 104.5M, joint scenarios 67–173M operational dense-FP8 H100e at end-2027.

The new model is calibrated to the same shipment baseline. Public data did not establish all factory capacities, yields, or hardware shares; it is a conditional component scenario, not a fully observed manufacturing forecast. Sources, equations, input provenance, and reproducible outputs are linked in Report 2. Neither result measures spare rental availability.

## Initial trend implementation: global operational compute through 2027

**Scope agreed after the initial research:** estimate global installed AI accelerator capacity. The broader nine-step plan below is deferred. This section records the initial result; the separate reports above distinguish it from the new component estimate.

“Available” here means operational hardware capacity, expressed in **dense FP8 H100-equivalents**, before workload utilization. It includes capacity already committed to customers. It does not mean spare capacity for rent, capacity available to one lab, or capacity connected tightly enough for one training run. Those quantities require additional allocation/network data.

**Working estimate: approximately 40 million H100e by end-2026 and 100 million by end-2027.** Precision beyond these rounded figures is not supported by public inventory and commissioning evidence. The table retains extra digits only to make the calculation auditable.

| Quarter end | Central operational capacity | Combined stress range |
|---|---:|---:|
| September 2026 | 31.3M H100e | 23.5–39.6M |
| December 2026 | 39.3M | 29.2–50.6M |
| March 2027 | 49.3M | 35.9–65.0M |
| June 2027 | 61.8M | 44.0–84.0M |
| September 2027 | 77.7M | 53.5–109.0M |
| December 2027 | 97.6M | 64.7–141.9M |

These are our conditional calculations, not measured inventories or probability intervals. September 2026 is a historical estimate; later quarters are forecasts. We do not interpolate an apparently precise November 12 inventory from quarterly data.

### Evidence added in this narrow pass

Epoch explicitly uses a **three-month delivery-to-deployment lag** to estimate data-center coverage. Its September article gives approximately **20.3M H100e delivered at end-2025**. This supports the order of magnitude of our approximate 20M opening stock, but delivered-to-customer and supplier-sold stocks may differ. I retain the existing sold-stock baseline rather than silently substitute the differently defined 20.3M. [Epoch methodology explanation, 16 September 2026](https://epoch.ai/latest/scaling-ai-data-centers-research), accessed 12 November 2026.

The current data-center dashboard estimates **44% coverage**, with a wide **30–78% interval**, and derives coverage partly from the chip-sales denominator. Therefore, scaling up its listed facilities is not an independent validation of the global chip-stock estimate. Site totals are also incomplete. [Epoch data-center coverage FAQ](https://epoch.ai/data/ai-data-centers), accessed 12 November 2026.

The shipment model remains based on the published ten-quarter table [S05]. No new worldwide inventory census or complete, consistently dated raw export was obtained. The main improvement here is explicit quarterly availability accounting and isolated sensitivities, not a claim of newly measured precision.

### Minimal model and assumptions

1. Begin with approximately 20M cumulative sold H100e at end-2025.
2. Add the published Q1 and Q2 2026 shipments. Extend later quarterly shipments from the Q2 level at 2.5× annual growth.
3. Commission each shipment cohort one quarter later. By the displayed forecast dates, the opening stock has cleared the assumed lag.
4. Central case assumes no retirements. Stress-test annual capacity attrition of 5% and 10%; these are selected assumptions, not observed retirement rates.

The low combined case uses 2× shipment growth, two-quarter commissioning lag, and 10% annual attrition. The high case uses 3× growth, immediate commissioning, and no attrition. The original report’s 71–142M range omitted attrition; this expanded stress case gives **65–142M** at end-2027. Neither range includes every possible outcome, a calibrated power cap, or the full uncertainty in shipment estimates.

For retirement stress, the opening stock is decayed from end-2025; subsequent cohorts decay after their modeled commissioning quarter. This is aggregate attrition, not a chip-lifetime survival model. Power constraints are represented only indirectly through commissioning delay; larger disruptions can exceed these scenarios.

### What most affects the answer?

Change one assumption at a time from the central case:

| Change | End-2027 operational capacity |
|---|---:|
| Opening sold stock 18M / 22M | 95.6M / 99.6M |
| Annual shipment growth 2× / 3× | 86.1M / 109.0M |
| Deployment delay zero / two quarters | 122.6M / 77.7M |
| Annual attrition 5% / 10% | 93.6M / 89.6M |

Within these chosen ranges, commissioning delay has the largest effect. This motivates prioritizing actual delivery-to-live dates over finer rounding of the old inventory anchor. Continued shipment growth is the next major driver. These comparisons do not establish which uncertainty is statistically most likely.

### How to use and maintain this result

Use **40M end-2026 and 100M end-2027** as provisional global-capacity assumptions, accompanied by the stress ranges. For model input at intervening dates, use the quarterly CSV. Preserve the distinction between period-end capacity and average capacity used during a period.

Run `python research/calculations/availability.py` to regenerate [quarterly availability](research/calculations/availability.csv) and [one-variable sensitivities](research/calculations/availability_sensitivity.json). The script checks scenario ordering, the effect of deployment delay, and retirement direction. The earlier calculation script independently reproduces the central endpoints.

The smallest useful next refresh is to replace projected Q3/Q4 shipments when published and replace the uniform three-month lag with documented commissioning delays. A single frozen chip-sales export would reconcile the opening stock and shipment vintages. Further capex, capability, model-size, and per-lab research is outside this narrowed task.

---

## Findings and recommended approach

Use the original supplement as a physical-compute accounting framework, with updated shipment and lab estimates. Keep capability and takeoff forecasts in a separate layer. The latest authors’ update found is **10 November 2026**, whereas the interactive AI Futures Model identifies itself as the **August 2026 version**. The newer update conditions and adjusts that model; it is not a new measured global hardware inventory. [S03, S04]

The strongest usable update is Epoch’s quarterly shipment series through Q2 2026. Recalculating its regression gives **2.48× annual growth in new compute shipped**, with a **9.15-month doubling time**. A transparent continuation scenario gives **97.6 million operational H100e at end-2027**, close to the original 100 million target, but it depends on continued growth, deployment delays, and compatible unit definitions. This is our illustration, not a new Epoch or AI Futures Project forecast. [S05; calculations below]

A complete current calibration is not possible from the inspected public evidence: lab allocation, chip installation dates, training utilization, model architectures, and internal inference workloads remain uncertain. The workfile supplies usable anchors and explicitly chosen sensitivity values instead of treating these unknowns as observations.

## 1. Which version is latest?

| Item                                 | Date/version found                                                                          | How to use it                                                                                                                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI 2027 Compute Forecast, Romeo Dean | April 2025; live page still has that date                                                   | Original physical-compute framework and scenario comparison. [S01]                                                                                                                                                   |
| Official changelog                   | Compute corrections on 16 December 2025                                                     | Includes distribution totals and chip-efficiency clarification; earlier April 2025 changes raised power assumptions. [S02]                                                                                           |
| AI Futures Model                     | Website labels August 2026; parameter estimates dated 16 August                             | Successor to timelines/takeoff work, not a drop-in compute spreadsheet revision. [S03]                                                                                                                               |
| Q3.5 update                          | 10 November 2026                                                                            | Latest authors’ findings located. Uses filtered AIFM trajectories and alternative explanations for faster research progress. Authors now expect SAR in 2027 conditional on no substantial deliberate slowdown. [S04] |
| Epoch chip sales                     | Hub updated 21 October; specific regression published 29 October using 19 October estimates | Best inspected global shipment calibration. [S05, S06]                                                                                                                                                               |
| Epoch lab users                      | Published 9 September 2026, mostly end-2025 observations                                    | Historical lab anchors, with intervals. [S07, S09]                                                                                                                                                                   |
| Epoch inference methodology          | Version 1; announced 9 November 2026                                                        | Upgrade inference modeling beyond FLOP/s alone. [S12, S13]                                                                                                                                                           |

The November authors’ update estimates approximately **1.7× AI-attributable acceleration in research progress** from METR evidence. That number is neither a hardware growth factor nor an inference speed factor. Its filtered model is sensitive to conditioning and assumptions; do not insert 1.7 into the chip-production equation. [S04]

The original supplement links a public backend spreadsheet [S20]. Its displayed title includes “shared 2024-10-02”; it contains older hardware assumptions. I inspected the rendered sheet but did not obtain or execute the workbook. No newer standalone compute-supplement workbook was verified.

## 2. Input register: numbers usable now

**Status:** reported = company disclosure; estimated = researcher reconstruction; scenario = assumption selected here; unavailable = no defensible current observation found.

### Global compute production and deployment

| Parameter                            | Value                                  | Period/status                                        | Model treatment                                                                                    |
| ------------------------------------ | -------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Quarterly new compute                | 4,980,154 H100e                        | Q1 2026, estimated                                   | Historical shipment observation. [S05]                                                             |
| Quarterly new compute                | 6,327,416 H100e                        | Q2 2026, estimated                                   | Latest complete global shipment quarter in the inspected series. [S05]                             |
| Annual growth of quarterly shipments | 2.5×; regression 90% interval 2.3–2.7× | Q1 2024–Q2 2026 fit                                  | Central continuation anchor; interval excludes underlying inventory-estimation uncertainty. [S05]  |
| Cumulative sold stock                | Approximately 20M H100e                | End-2025, estimated                                  | Provisional starting stock; older data vintage than October series. [S08]                          |
| Operational stock                    | Approximately 16M or 12M H100e         | End-2025, assumed one- or two-quarter deployment lag | Historical reference cases, not measured installations. [S08]                                      |
| Installation delay                   | 0, 1, 2 quarters                       | Scenario                                             | Central one-quarter lag; vary independently of shipment growth.                                    |
| Retirement                           | Zero in illustration                   | Scenario                                             | Add age-specific retirement before a production forecast; test 0–10% annual retirement separately. |
| Growth sensitivity                   | 2.0×, 2.5×, 3.0× per year              | Scenario                                             | Stress range, not a probability interval.                                                          |

Full ten-quarter observations are in [global_shipments.csv](research/data/global_shipments.csv), manually transcribed from S05. Credit: Isabel Juniewicz and Josh You, Epoch AI, CC BY. The dataset omits some smaller accelerator vendors and is not a census of every computing device. [S05]

Recent non-Nvidia evidence matters: Broadcom fiscal Q3 2026 TPU shipments are estimated at **1,965,979 H100e**, versus **961,591** in Q2, with Q3 interval **1,567,748–2,350,392**. These are revenue-derived estimates, sensitive to whether sales cover chips or racks. Fiscal Q3 spans May–early August: do not add this to calendar Q2 global shipments. [S10]

### Compute available to frontier labs

| Lab                         | End-2025 median H100e |        90% interval |
| --------------------------- | --------------------: | ------------------: |
| OpenAI                      |             1,743,000 | 1,251,000–2,185,000 |
| Google DeepMind             |             1,583,000 | 1,008,000–2,549,000 |
| Anthropic                   |             1,190,000 |   842,000–1,717,000 |
| Meta Superintelligence Labs |               996,000 |   606,000–1,638,000 |
| SpaceXAI                    |               615,000 |     551,000–700,000 |

Source: Josh You, Epoch AI, September 2026 publication [S07], CC BY. Machine-readable transcription: [lab_compute_2025.csv](research/data/lab_compute_2025.csv). These are **historical estimates of use**, including relevant rentals, not ownership inventories. The article’s SpaceXAI figure differs from some subsequently surfaced summaries; retain this explicit published vintage until the downloadable current model is reconciled.

OpenAI directly reported power capacity of **0.2 GW in 2023, 0.6 GW in 2024, approximately 1.9 GW in 2025**. These support historical growth calibration; a uniform GW-to-H100e multiplier would ignore changing chip mix. [S11]

For late-2026 lab stocks, use the end-2025 estimates as priors and update from installed site capacity and rental allocations. A 2027 leading-lab share of **10%, 20%, or 30%** is a sensitivity assumption here. Do not present any of those shares as newly measured.

### Hardware and inference

| Input                              | Current inspected specification                                           | Use                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| H100 SXM dense FP16 / FP8          | Approximately 0.989 / 1.979 PFLOP/s                                       | Baseline conversion; Nvidia’s table advertises sparse values at twice these rates. [S15] |
| H100 SXM memory / bandwidth        | 80 GB / 3.35 TB/s                                                         | Physical device reference. [S15]                                                         |
| Rubin GPU dense FP16 / FP8-FP6     | 4 / 17.5 PFLOP/s                                                          | Separate precision-specific conversions. [S14]                                           |
| Rubin HBM                          | 288 GB / 19.2 TB/s                                                        | Current product page; older July architecture material says 22 TB/s. [S14, S21]          |
| Original bandwidth-equivalent unit | 3.6 TB/s                                                                  | Legacy comparison only; a blended H100 reference. [supplied file]                        |
| Inference workload definition      | 256Ki cached context; four model workloads; separate prefill/decode pools | Recompute capacity for a specified output-speed target using IPI methodology. [S12]      |

**Unit bridge:** AI 2027 defines H100e using TPP, while Epoch uses dense 8-bit operations normalized to H100 (with fallbacks for chips lacking 8-bit support). Store both definitions. The same label does not guarantee equal conversion factors for every accelerator. The aggregate projections below use Epoch-style H100e; comparisons with the original are approximate until converted chip by chip. [S01, S09]

### Financial and power checks

| Company/input                     | Latest inspected number                         | Observation and interpretation                                                                       |
| --------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Amazon                            | About $220B 2026 cash capex                     | Q3 guidance; includes company-wide investment. [S16]                                                 |
| Alphabet                          | $195–205B 2026 capex; Q3 $51.4B                 | October 28 call; Q3 technical infrastructure roughly 65% servers/networking, 35% data centers. [S17] |
| Meta                              | $135–145B 2026 capex                            | Q3 guidance, includes finance-lease principal. [S18]                                                 |
| Microsoft                         | About $170B calendar-2026 capex; Q1 FY27 $45.2B | October 28 call supersedes earlier $190B expectation; deliveries delayed. [S19]                      |
| Nvidia                            | $89B quarterly Data Center revenue              | Q2 FY27, ended July 26, reported August 26; supplier revenue includes more than GPU silicon. [S22]   |
| OpenAI infrastructure commitments | More than initial 10GW goal secured             | April 29 announcement; secured future capacity is not verified powered inventory. [S23]              |

Do not convert total corporate capex or supplier revenue directly into chips. Keep cash capex, finance leases, construction, servers, operating cloud bills, and annualized revenue separate. Never add Nvidia sales to customer capex to estimate total ecosystem investment: that counts the supply chain twice.

## 3. Calculations and implications

Reproduce all numerical examples with:

```bash
python research/calculations/recalculate.py
```

The standard-library script writes [results.json](research/calculations/results.json) and [scenarios.csv](research/calculations/scenarios.csv). It is a research calculation harness, not a reproduction of the full authors’ model.

### A. Check the original growth arithmetic

Original reference assumptions: chip efficiency 1.35×/year; production 1.65×/year; global growth approximately 2.25×/year; 10M H100e in March 2025 and 100M in December 2027; leading company 0.5M in December 2024 and 20M in December 2027. [S01]

- 1.35 × 1.65 = **2.2275**, consistent with a rounded 2.25.
- 10M × 2.25^(33/12) = **93.0M**, rather than exactly 100M.
- Exact growth connecting the global endpoints is 10^(12/33) = **2.310×/year**.
- Exact growth connecting the leading-company endpoints is 40^(1/3) = **3.420×/year**.

Choose either the rounded growth law or the endpoint calibration explicitly. Do not silently force them to agree.

### B. Refit current shipment growth

Regress `log(quarterly H100e shipments)` on quarter index 0–9 using the CSV. The slope implies:

`annual growth = exp(4 × slope) = 2.48136`

`doubling months = 3 × ln(2) / slope = 9.15239`

A two-sided t interval with 8 degrees of freedom gives **2.298–2.679×/year**. This reproduces the published rounded result. It measures regression fit uncertainty, not the full uncertainty in future shipments.

### C. Build an explicit stock-and-flow continuation

Use these provisional anchors: cumulative sold stock at end-2025 = 20M; observed 2026 Q1 and Q2 shipments from S05; future quarterly shipments:

`A(t) = 6,327,416 × g^((t − 1)/4)`

where t=0 denotes Q1 2026 and t=1 denotes Q2. For t≥2, this is a projection. Cumulative sold stock is the starting stock plus subsequent shipments; operational stock at a quarter end includes only shipments whose deployment lag has elapsed. No retirement or power cap is imposed in this illustration.

| Annual shipment growth | End-2027 operational, 0-quarter lag | 1-quarter lag | 2-quarter lag |
| ---------------------- | ----------------------------------: | ------------: | ------------: |
| 2.0×                   |                              104.0M |         86.1M |         71.1M |
| 2.5×                   |                              122.6M |     **97.6M** |         77.7M |
| 3.0×                   |                              141.9M |        109.0M |         84.0M |

Central end-2026 operational stock is **39.3M H100e**. At the latest completed quarter, September 30, the same one-quarter-lag rule gives **31.3M** (=20M+4.980M+6.327M). This is a dated derived estimate, not an observed November 12 inventory. The 20M baseline is approximate and from an earlier vintage; replace it with a consistently dated chip-level dataset before reporting a calibrated forecast.

At 20% leading-lab share, the central end-2027 scenario implies **19.5M H100e**. Its proximity to the old 20M does not validate the rest of the scenario, model capabilities, or research automation.

The scenario range **71–142M** is deliberately broad and is not a 90% credible interval. The original 100M endpoint lies within it. A power-constrained installation schedule could reduce these figures further.

### D. Convert hardware into training budgets

`training FLOP = average allocated fleet × dense FLOP/s per equivalent × utilization × seconds`

Example assumptions: 6M average FP16-normalized H100e, 40% training allocation, 30% model FLOP utilization, 365 days:

`6e6 × 0.40 × 0.989e15 × 0.30 × 31,536,000 = 2.246e28 FP16 FLOP`

The 6M fleet is an example, not a measured lab stock. An Epoch FP8-normalized fleet must first be converted to FP16-equivalents by chip mix. This calculation is a total training budget: a single run additionally needs sufficiently connected hardware, uninterrupted duration, and an allocation within the training budget. Use actual quarter lengths in implementation. Never multiply annual utilization twice to account for idle time.

### E. Inference resource checks

Rubin conversion examples from current dense specifications:

- Bandwidth: 19.2 / 3.6 = **5.33 legacy H100 bandwidth-equivalents**.
- FP16 compute: 4 / 0.989 = **4.04 H100 SXM equivalents**.
- FP8 compute: 17.5 / 1.979 = **8.84 H100 SXM equivalents**.
- Current 19.2 TB/s is **12.7% below** the older 22 TB/s specification.

These different ratios show why a single H100e multiplier cannot size every workload.

For an illustrative dense 10T-parameter FP8 model, weights occupy approximately **10 TB**. At 80% usable capacity, the memory-only minimum is `ceil(10TB / (288GB × .8)) = 44 Rubin GPUs`. This excludes KV cache, activations, replicas, and communication constraints. It says nothing by itself about copies per second or human-equivalent thinking speed.

For deployment, estimate concurrent requests at a specified tokens/s using a model-specific roofline or IPI calculation. Apply measured serving efficiency afterward. Report context length, batch size, architecture, precision, memory reserve, and prefill traffic. Keep the original hypothetical custom inference chip and future model compression as optional scenarios until supported by hardware or benchmark evidence.

### F. Cost and energy checks

The three annual capex guides for Amazon, Alphabet, and Meta sum to **$550–570B**. Adding Microsoft’s latest approximately $170B guide gives **$720–740B**, on mixed accounting bases. This is a corporate spending comparison, not global AI-only capex or cost of the active compute stock. [S16–S19]

For a facility with 10GW rated draw and 80% average load: `10 × .8 × 8,760 / 1,000 = 70.08 TWh/year`. If 10GW instead denotes IT capacity, multiply by PUE to get facility energy. Capacity in GW, energy in TWh, and grid nameplate capacity are different quantities.

## 4. Required inputs still missing

| Input                              | Evidence gap                                                     | Treatment until filled                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Current global installed fleet     | Shipments observable with delay; installation timing incomplete  | Publish shipment and operational series separately; show lag sensitivity.                                                                                       |
| Current lab shares                 | Rental reallocation and parent-company allocations private       | Maintain a provider→user allocation matrix; source each cell or mark unknown.                                                                                   |
| China stock/access                 | Hardware mix, indirect access, and ownership differ              | Separate location, owner, and user; do not retain the old fixed China share as fact.                                                                            |
| Wafer, packaging, HBM constraints  | No reconciled current units, yields, and AI allocations obtained | Obtain foundry/memory disclosures and chip package BOMs; model as constraints, not additive forecasts.                                                          |
| Training utilization               | Workload and system dependent                                    | Test 20/30/40% as chosen assumptions; replace with measured job-level utilization.                                                                              |
| Workload shares                    | No public current pretrain/RL/data/experiment split              | Compare a demand case (50% external, 20% training, 20% experiments/data, 6% internal agents, 4% other) with original scenario; all shares here are assumptions. |
| Frontier model size / KV cache     | Closed-model details private                                     | Use disclosed open architectures for baseline; sweep 0.1–10T active parameters as stress cases, not estimates. Track total vs active MoE parameters.            |
| Inference prices / ownership costs | Contracts and effective discounts differ                         | Collect dated quotes at fixed workload/SLA; distinguish rental from owned TCO.                                                                                  |
| Retirement, PUE, load factor       | No complete vintage/site series                                  | Add explicit ranges and correlate with chip generation and location.                                                                                            |
| Capability per effective compute   | Requires independent capability/algorithmic calibration          | Keep AIFM or another validated capability model separate from physical accounting.                                                                              |

## 5. Plan to use the model with these numbers

1. **Freeze the baseline and provenance.** Keep the supplied HTML as the historical reference. Record retrieval date, measurement period, units, source URL, status, and uncertainty for every input. The two local CSVs and source register below provide the first usable tranche.
2. **Reproduce the original accounts.** Implement the five original layers: production, allocation, workload use, inference, and economics/power. Reproduce selected published outputs under original assumptions. Document discrepancies due to rounding, quarterly versus annual averages, and TPP versus dense FP8 normalization.
3. **Build the refreshed physical baseline.** Import all chip-sales tables, chip conversion specs, and cohorts from a single frozen data release. Start with the measured series in this workfile and use the 2.5× continuation only beyond its last observed quarter. Apply deployment delays and retirement by cohort. Bound installation by live powered capacity, packaging, HBM, and network delivery.
4. **Allocate operational resources.** Rebase each lab from its dated historical interval. Update using energization records and rental allocations. Keep residual users explicit so shares sum to one. Enforce that rented capacity appears once in global supply, even when it appears in both owner and user views.
5. **Run separate workload cases.** Use actual allocations where available; otherwise expose assumptions. Integrate fleet×time over quarters, then convert to training FLOP. Evaluate contiguous training-cluster limits separately from total fleet. For inference, calibrate concurrency at 50/100/200/400 tokens/s using specified architectures and context lengths.
6. **Check cost and power.** Reconcile capex vintages and financing with equipment acquired; compare cloud expense with allocated fleet-hours. Compute IT and facility power from chip mix and overhead. Exclude merely secured or announced capacity from the operational case until commissioned.
7. **Publish sensitivity results before capability conclusions.** Use the 3×3 shipment-growth/deployment grid here, then vary lab share, utilization, allocation, inference efficiency, and power constraints. Show interactions; a single optimistic setting should not silently set every other parameter. Do not assign probabilities without an elicited joint distribution.
8. **Connect to the latest capability model only afterward.** Pin the relevant AIFM version and parameter set; compare August defaults with November conditioning. Map physical experiment/training budgets into its effective-compute definitions. Neither 100M H100e nor a count of serving requests alone implies SAR.
9. **Deliver and refresh.** The next model run should output quarterly global and lab H100e, connected training capacity, training FLOP, inference concurrency/speed curves, facility GW/TWh, and annual versus stock costs through 2027. Refresh after earnings and hardware-spec revisions, retaining old vintages and a change log.

**Acceptance checks for the eventual full model:** owner/user accounting reconciles; allocations total 100%; operational stock cannot exceed delivered stock; connected clusters cannot exceed a lab’s fleet; hardware capacity respects power/network limits; annual compute uses average rather than year-end fleet; all precision and sparsity conversions are explicit. Backtest against historical quarters before giving forward estimates decision weight.

## 6. Source register

All sources accessed 12 November 2026 unless stated otherwise. Links identify the exact publication used, not search result pages.

| ID  | Source and publication date                                                                                                                                                 | Role / access note                                                                                                                           |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| S01 | [Romeo Dean: Compute Forecast](https://ai-2027.com/research/compute-forecast), April 2025                                                                                   | Original framework; supplied local copy also inspected.                                                                                      |
| S02 | [AI 2027 official changelog](https://ai-2027.com/about)                                                                                                                     | Revision history, including December 2025 compute corrections.                                                                               |
| S03 | [AI Futures Model](https://www.aifuturesmodel.com/), August 2026 version                                                                                                    | Version identified in indexed website text; interactive page was not executable here.                                                        |
| S04 | [AI Futures Project: Q3.5 Timelines Update](https://blog.aifutures.org/p/q35-timelines-update-looks-like-the), 10 Nov 2026                                                  | Latest authors’ update located; forecasts and conditioning.                                                                                  |
| S05 | [Epoch: New global AI computing capacity is doubling every 9 months](https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling), 29 Oct 2026                  | Exact ten-quarter published table and regression method; data vintage 19 Oct.                                                                |
| S06 | [Epoch AI chip sales](https://epoch.ai/data/ai-chip-sales), updated 21 Oct 2026                                                                                             | Dataset catalog; [methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology).                                               |
| S07 | [Josh You: Introducing the AI Chip Us<br>ers explorer](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer), 9 Sep 2026                                          | Historical per-lab medians and intervals.                                                                                                    |
| S08 | [Josh You: How much AI compute do frontier labs use?](https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute), May 2026                                   | Approximate cumulative/operational stock and deployment-lag discussion.                                                                      |
| S09 | [Epoch AI chip users](https://epoch.ai/data/ai-chip-users), 9 Sep 2026; [methodology](https://epoch.ai/data/ai-chip-users-documentation/methodology)                        | Definitions; [public model code](https://github.com/epoch-research/ai-compute-users).                                                        |
| S10 | [Epoch: Broadcom TPU compute shipments doubled](https://epoch.ai/data-insights/tpu-production-doubling), 4 Nov 2026                                                         | Latest inspected supplier-specific H100e estimate and uncertainty.                                                                           |
| S11 | [OpenAI CFO: A business that scales with the value of intelligence](https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/), 18 Jan 2026           | Direct historical power disclosure.                                                                                                          |
| S12 | [Epoch hardware methodology: Inference Performance Index v1](https://epoch.ai/data/machine-learning-hardware-documentation/methodology)                                     | Reproducible workload definition; [IPI repository](https://github.com/jasonlizhengjian/inference-performance-index).                         |
| S13 | [The Epoch Brief](https://epochai.substack.com/p/the-epoch-brief-november-11-2026), 11 Nov 2026                                                                             | Confirms Nov 9 IPI launch; main IPI article URL was inaccessible.                                                                            |
| S14 | [Nvidia Vera Rubin NVL72 specifications](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)                                                                        | Live dense throughput, HBM and bandwidth specifications.                                                                                     |
| S15 | [Nvidia H100 specifications](https://www.nvidia.com/en-us/data-center/h100/)                                                                                                | H100 SXM reference and sparsity footnote.                                                                                                    |
| S16 | [Amazon Q3 2026 results](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx)                         | Annual cash capex guidance.                                                                                                                  |
| S17 | [Alphabet Q3 2026 call](https://abc.xyz/investor/events/event-details/default.aspx), 28 Oct 2026                                                                            | Annual capex and infrastructure composition; dynamic URL can change.                                                                         |
| S18 | [Meta Q3 2026 results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)                           | Annual capex including lease principal.                                                                                                      |
| S19 | [Microsoft FY27 Q1 call](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1), 28 Oct 2026                                                          | Revised calendar-2026 capex and delays.                                                                                                      |
| S20 | [AI chip compute forecast backend spreadsheet](https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/edit?gid=1866551567)                     | Rendered sheet inspected; workbook not downloaded.                                                                                           |
| S21 | [Nvidia Rubin architecture](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai), July 2026                               | Older 22TB/s claim; current product page used instead.                                                                                       |
| S22 | [Nvidia Q2 FY27 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/), 26 Aug 2026       | Supplier-side revenue cross-check.                                                                                                           |
| S23 | [OpenAI: Building the compute infrastructure for the Intelligence Age](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/), 29 Apr 2026 | Secured capacity announcement; not operational inventory.                                                                                    |
| S24 | [Epoch AI data centers](https://epoch.ai/data/ai-data-centers)                                                                                                              | Future site-by-site update source. Inspected dashboard says Nov 6, homepage Nov 11; freeze export before treating as one consistent release. |

### Access limits and reproducibility

The public ZIP and CSV download URLs were identified, but shell network access failed DNS resolution and the web reader could not ingest the raw datasets. No raw ZIP was acquired. Local CSVs are **manual transcriptions of accessible published tables**, not full dataset exports. The displayed backend sheet was inspected without a formulas export; no claim is made to have run the authors’ original workbook or interactive AIFM.

For a full refresh, fetch these published exports through a network-capable environment and pin their hashes: `https://epoch.ai/data/ai_chip_sales.zip`, `https://epoch.ai/data/ai_chip_sales_chip_types.csv`, `https://epoch.ai/data/ai_chip_sales_timelines_by_chip.csv`, and `https://epoch.ai/data/ai_chip_users_year_end_by_lab.csv`. Reconcile their vintage and definitions before replacing these transcriptions. Public sources were searched for more recent compute revisions; this workfile reports the latest versions located, not an assurance that every unpublished or paywalled update was found.
