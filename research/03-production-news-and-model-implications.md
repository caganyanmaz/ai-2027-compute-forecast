# Chip-production news: implications for the AI 2027 compute forecast

**Research cutoff: 12 November 2026.** This dossier contains 14 individual news assessments covering logic wafers, HBM, advanced packaging, manufacturing equipment, substrates, and system design. “Dense packaging” is interpreted as advanced 2.5D/3D packaging, including CoWoS and EMIB.

## Assessment

**Keep the physical component-accounting framework, but do not use the original AI 2027 parameter values unchanged.** The strongest challenges are to treating logic supply as nonbinding, assuming a smooth relationship between packaging expansion and accelerator output, pooling all HBM generations, and representing hardware progress with one precision-independent performance multiplier.

The news does **not** establish a single defensible upward or downward revision to global 2027 compute. Factory expansions and increasing resource requirements pull in opposite directions. Several prominent investments contribute after 2027. Most announcements omit qualified output, allocation, or yields, so their impact cannot honestly be converted into a precise number of additional accelerators.

Our previous [component estimate](02-component-production-forecast.md), **104.5M operational dense-FP8 H100e at end-2027**, remains a conditional reference, not a newly validated central forecast. This report adds news-motivated sensitivities without silently changing that reference. It also identifies structural changes needed before treating the estimate as robust.

## How the evidence was evaluated

Searches prioritized company announcements, earnings disclosures, vendor specifications, and analysts' own research published by the cutoff. Earlier announcements are included when they still determine 2027 capacity; “recently rediscovered” is not treated as “newly announced.” This is a targeted assessment of material developments, not an exhaustive news archive. Publication dates and expected production dates are distinguished below. Management forecasts are evidence of plans, not independent verification of delivered capacity.

Each assessment separates the reported development from our inference and proposed action. **High importance** means a plausible material effect on 2027 supply or a core modeling assumption, not high certainty about the numerical effect. The model's current 1.6× logic/packaging growth and 1.733× HBM-bit growth already stand in for expansion; adding facilities on top can double-count it.

| ID  | Development / latest evidence used                 | Importance for 2027 | Recommended treatment                                          |
| --- | -------------------------------------------------- | ------------------- | -------------------------------------------------------------- |
| N01 | TSMC N3/N2 expansion, 15 Oct 2026                  | High                | Model node-specific quarterly ramps                            |
| N02 | ASML growth still below demand, 14 Oct 2026        | High                | Constrain equipment installation; downside scenario            |
| N03 | SK hynix M15X and HBM4 ramp, 28 Oct 2026           | High                | Update HBM4 allocation and ramp, not global revenue multiplier |
| N04 | Samsung HBM4 shipments and scaling, Feb / Oct 2026 | High                | Add qualified supplier diversification                         |
| N05 | Micron Singapore HBM packaging, 2026 reaffirmation | High                | Add 2027 HBM back-end capacity only when quantified            |
| N06 | Micron DRAM expansion: Tongluo and Idaho           | Medium–high         | Partial-year supply; distinguish DRAM from HBM                 |
| N07 | HBM shortages and thinner stacks, 29 Sep 2026      | High                | Separate generation, stack count, capacity, and bandwidth      |
| N08 | Larger packages / CoWoS-L, Sep–Oct 2026            | High                | Update resource burden, not just wafer capacity                |
| N09 | GlobalFoundries interposer agreement, 8 Oct 2026   | Low before 2028     | No direct 2027 increment                                       |
| N10 | Amkor Arizona phase 2, 8 Sep 2026                  | Low before 2028     | No direct 2027 increment                                       |
| N11 | Intel EMIB-T, Jul–Sep 2026                         | Medium–high         | Qualified alternative-capacity upside                          |
| N12 | Substrate/T-glass constraints, 2026 research       | High                | Add a distinct constraint or explicit packaging derating       |
| N13 | Rubin production and performance                   | High                | Replace generic hardware multiplier; validate shipment ramp    |
| N14 | Co-packaged optics / deployment integration        | Medium              | Separate system completion from chip production                |
## N01 — TSMC expands leading-edge logic capacity, but at different nodes and dates

**News and timing.** On 15 October, TSMC described N3 production starting in Tainan in H1 2027 and Arizona in Q3 2027, with further Taiwan/Japan additions in 2028. N2 annual capacity is expected to more than double in 2027. It also described converting N5 tools toward N3. These are management plans, with some facilities already in construction/tool installation. [TSMC Q3 transcript, pp. 4–5](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf).

**Importance / model verdict: high; revise assumptions, retain framework.** A global leading-edge wafer pool hides product compatibility and competition for particular nodes. Adding N2 capacity does not automatically produce more chips designed for N3. Conversions also make capacity additions non-additive across nodes.

**Adjustment.** Replace `logic_growth` with quarterly node-specific good-area capacity and AI allocation. Give late-2027 starts partial-year credit and allow time for packaging and deployment. Do not set worldwide AI logic growth to 2× merely because N2 doubles. Our prior report already noted this expansion: it is supporting evidence, not an extra uplift. Without wafer allocations/yields, retain a sensitivity such as 1.3× usable logic growth, which gives **96.6M** end-2027 operational H100e versus 104.5M. The 1.3× value is a selected stress, not TSMC guidance.

**Update trigger:** qualified wafer output and AI customer allocation by node and quarter.

## N02 — ASML plans substantial expansion but still cannot meet all expected demand

**News and timing.** ASML's 14 October release says planned supply will fall short of customers' demand in both 2027 and 2028. Its stated expansion plan includes approximately 30% more low-NA EUV and immersion capacity in 2027; it is exploring further 2028 expansion and providing productivity upgrades. [ASML Q3 release](https://www.investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026).

**Importance / model verdict: high; challenges unconstrained expansion.** Equipment delivery, installation, and qualification can limit fab ramps. However, unmet demand does not mean production is shrinking or missing the earlier AI 2027 forecast.

**Adjustment.** Schedule new wafer capacity only after equipment commissioning. Distinguish new scanner deliveries from productivity improvements to installed tools. Do not impose a 30% ceiling on AI wafer output: equipment production is a flow, installed equipment is a stock, and AI allocation can change. Use the slower-logic scenario as a stress; do not stack it mechanically with N01 as though these were independent shocks.

**Evidence strength / trigger:** strong evidence of management's supply outlook, incomplete evidence on affected AI-node output. Update when tool delivery dates and fab bottlenecks are identified.

## N03 — SK hynix aims to ramp M15X fully and shift toward HBM4

**News and timing.** The 28 October release targets maximum M15X capacity by year-end to increase HBM4 output. Management expects HBM4 to exceed HBM3E in both shipment volume and revenue in Q4 2026. This is a near-term ramp target, not a disclosed good-bit capacity table. [SK hynix Q3 results](https://news.skhynix.com/en/q3-2026-business-results/).

**Importance / model verdict: high; supports supply growth and product transition.** This reduces the plausibility of a scenario with no HBM4 industrial ramp. It does not prove sufficient supply for every Rubin-class device or validate our aggregate HBM-growth assumption.

**Adjustment.** Split HBM3E and HBM4 supply, include qualification and yields, and replace the assumed trajectory when good-bit output becomes available. Do not multiply all worldwide HBM supply by one supplier's revenue growth. M15X should be part of the supply forecast, not an addition on top of a forecast already incorporating it.

**Quantitative implication.** Raising annual aggregate HBM-bit growth from 1.733× to 2× leaves our central output at **104.5M**, because packaging still binds. The news can improve resilience without increasing modeled output.

**Update trigger:** actual M15X ramp, HBM4 good-bit shipments, and contracted qualified allocation.

## N04 — Samsung's commercial HBM4 shipments broaden the supplier base

**News and timing.** Samsung announced commercial HBM4 shipments on 12 February, using a 1c DRAM process and 4nm base die. Its 29 October results reported substantially expanded HBM4 sales. [February announcement](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing), [October results](https://news.samsung.com/be/samsung-electronics-announces-third-quarter-2026-results).

**Importance / model verdict: high; revise supplier shares and dependencies.** A fixed historical supplier-share proxy becomes less reliable as another supplier scales a new generation. HBM also depends on logic-base-die production, so memory supply is not entirely independent of foundry capacity.

**Adjustment.** Build supplier-by-generation output, qualified customer allocations, and base-die requirements. Do not interpret announced HBM sales growth as equivalent bit growth: price and product mix matter. Do not assume interchangeable qualification for all accelerators. This supports diversified-supply scenarios, but no numerical global uplift is justified by the disclosed sales statements alone.

**Evidence strength / trigger:** company evidence supports commercial availability; public information does not establish all yields or customer approvals. Upgrade the forecast when qualified quantities, not simply sales revenue, are disclosed.

## N05 — Micron's Singapore HBM packaging can matter in 2027; its new NAND fab cannot

**News and timing.** Micron's January 2026 Singapore announcement reaffirms meaningful HBM-packaging contribution in 2027. The separately announced $24B NAND wafer project starts output in H2 2028. The original HBM facility announcement dates to January 2025, before the original AI 2027 forecast. [2026 update](https://investors.micron.com/news/press-release/2026/Micron-Breaks-Ground-on-Advanced-Wafer-Fabrication-Facility-in-Singapore-01-26-2026/default.aspx), [original HBM announcement](https://investors.micron.com/news/press-release/2025/Micron-Breaks-Ground-on-New-HBM-Advanced-Packaging-Facility-in-Singapore-01-08-2025/default.aspx).

**Importance / model verdict: high for HBM, no direct 2027 uplift from NAND.** HBM stack assembly is distinct from CoWoS assembly of accelerators and memory. Expanding one does not automatically expand the other.

**Adjustment.** Put Singapore HBM capacity in the memory back-end constraint, subject to DRAM die supply and qualification. Assign the NAND project **zero direct 2027 accelerator-capacity increment**. Treat the HBM update mainly as confirmation of a previously announced ramp; it is not automatically a surprise against the original forecast.

**Evidence strength / trigger:** announced schedule is clear; effective HBM output is not quantified. Add a numerical increment only after identifying ramped stack throughput, yields, and whether existing supplier forecasts already include it.

## N06 — Micron's Tongluo acquisition and Idaho ramp offer partial-year DRAM upside

**News and timing.** Micron's January Tongluo announcement expected meaningful DRAM wafer output in H2 2027; its current Idaho project page schedules initial DRAM output in 2027. TrendForce's January analysis estimated Tongluo phase-one capacity above 10% of Micron's end-2026 global capacity. [Micron Tongluo announcement](https://investors.micron.com/news/press-release/2026/Micron-Signs-Letter-of-Intent-to-Purchase-Tongluo-Site-Begin-Strategic-Partnership-with-PSMC-01-17-2026/default.aspx), [Idaho project](https://www.micron.com/us-expansion/id), [TrendForce estimate](https://www.trendforce.com/presscenter/news/20260119-12883.html).

**Importance / model verdict: medium–high; positive capacity evidence, uncertain HBM conversion.** A plant can be material to one supplier while modest relative to the worldwide market. Wafer starts are not immediately packaged HBM shipments.

**Adjustment.** Use a quarterly ramp and a separate HBM allocation. Illustratively, an increment of 10% of supplier capacity operating for half a year is about 5% of that supplier's annual capacity-equivalent output before ramp losses—not 10% of worldwide annual HBM. Multiply by physical supplier share, relative bit yield, and HBM allocation; revenue share is not a substitute.

**Evidence strength / trigger:** project timing supported by company statements; 10% is an analyst projection, not verified output. Obtain current ramp guidance and generation-specific production before revising the global total. The January schedule is retained as a dated plan, not asserted to be the latest detailed Tongluo timetable.

## N07 — Persistent HBM constraints may change accelerator memory configurations

**News and timing.** On 29 September, TrendForce projected continued HBM tightness in 2027 and reported consideration of 8-high rather than 12-high stacks. Its 121% blended-price-growth forecast reflects supply pressure and product mix, not physical supply growth. [TrendForce HBM update](https://www.trendforce.com/presscenter/news/20260929-13255.html).

**Importance / model verdict: high; a structural challenge to fixed memory burden.** Lower memory per accelerator can stretch available bits across more devices, while reducing capacity for workloads that need large resident models or KV caches. Base dies and stack assembly remain required.

**Adjustment.** Model memory bits, stack/base-die counts, bandwidth, and qualified HBM generations separately. Under equal die density and stack count, replacing 12 layers with eight cuts memory bits per device to 2/3 and permits at most 1.5× as many devices **if memory bits alone bind**. This is conditional arithmetic, not a prediction of adoption or realized throughput.

**Sensitivity / trigger:** an assumed slowdown to 1.3× usable HBM-bit growth reduces our reference to **95.4M**. Revise actual device memory only after product specifications change; do not lower published Rubin memory because vendors are merely evaluating alternatives. The earlier report already cited this shortage evidence, so it is not an additional independent shock.

## N08 — Larger CoWoS-L packages can absorb capacity expansion

**News and timing.** TrendForce's 18 September research expects CoWoS-L to remain mainstream through 2028 as AI package sizes increase. TSMC's October call describes 5-reticle-size production and work toward larger packages. [TrendForce packaging research](https://www.trendforce.com/presscenter/news/20260918-13241.html), [TSMC transcript, p. 12](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf).

**Importance / model verdict: high; revise packaging resource intensity.** More wafer or panel throughput need not yield proportional accelerator output. Larger footprints, more complex assembly, and yield losses can offset capacity growth.

**Adjustment.** Replace generic packaging units with product-specific area, process steps, and good-package yield when available. Our assumed Rubin burden of 1.3 is not a measured interposer ratio. Raising it to 1.6 gives **98.8M**, an illustrative stress rather than a source-derived correction. Do not turn the original April “over 60% by 2027” expansion wording into an independently verified annual growth rate.

**Evidence strength / trigger:** strong direction-of-change evidence; insufficient quantitative burden data. Track qualified good packages per month by product. Existing packaging expansion and larger-package effects must be applied together, not counted as independent full-size gains/losses.

## N09 — GlobalFoundries' TSMC interposer agreement starts too late for 2027

**News and timing.** On 8 October, GlobalFoundries announced a $2B multiyear agreement supporting TSMC's CoWoS ecosystem, with volume production ramping at Malta in H1 2028. [GlobalFoundries announcement](https://gf.com/news-and-events/news/globalfoundries-reaches-agreement-to-establish-us-based-supply-of-silicon-interposers-for-advanced-ai-packaging/).

**Importance / model verdict: low for 2027, potentially material later; no reason to raise 2027 production.** Interposers are one stage of advanced packaging, not completed accelerators.

**Adjustment.** Assign **zero direct 2027 output increment** on the disclosed schedule. For 2028 onward, add qualified interposer output only where it relieves the active bottleneck. Avoid counting GF's output again inside a TSMC ecosystem-capacity total that includes subcontracting.

**Evidence strength / trigger:** clear announced agreement and target date; no disclosed package-equivalent throughput. Reassess only upon an earlier qualified ramp or quantified 2028 output. The contract's dollar value cannot be converted directly into chips.

## N10 — Amkor's expanded Arizona campus is mainly a post-2027 development

**News and timing.** Amkor announced a phase-two expansion on 8 September, bringing planned investment to $12B and total cleanroom area to about 93,000 m². Phase-two construction starts in late 2027, with completion expected by end-2029. Its earlier phase-one announcement targets production in early 2028. [Phase-two announcement](https://ir.amkor.com/news-releases/news-release-details/amkor-technology-announces-phase-2-arizona-advanced-packaging), [phase-one schedule](https://ir.amkor.com/news-releases/news-release-details/amkor-technology-breaks-ground-new-semiconductor-advanced).

**Importance / model verdict: low for 2027; reject a premature uplift.** Construction completion and cleanroom area do not measure qualified AI package throughput.

**Adjustment.** Assign **zero direct 2027 capacity increment** for these Arizona production ramps. Model subsequent output by packaging technology and customer qualification. Do not assume all campus floor space is AI accelerator CoWoS-equivalent capacity or treat the $12B total as incremental to every earlier investment announcement.

**Update trigger:** actual production start, equipment fit-out, qualified technologies, and AI customer volumes.

## N11 — Intel EMIB-T offers an alternative, but not instantly fungible capacity

**News and timing.** Intel's 29 July technical update describes EMIB-T and its power/signal routing support for advanced memory. TrendForce's September research anticipates 2027 customer adoption while still expecting CoWoS-L to lead through 2028. [Intel technical update](https://www.intel.com/content/www/us/en/newsroom/news/intel-foundry/intels-us-advanced-packaging-enables-next-generation-ai-semiconductors.html), [TrendForce analysis](https://www.trendforce.com/presscenter/news/20260918-13241.html).

**Importance / model verdict: medium–high; challenges a fixed TSMC-only proxy.** Alternative capacity can relieve constraints, but designs need compatible packaging, substrates, qualification, and customer allocation. A GPU designed for CoWoS cannot simply move to any spare EMIB line.

**Adjustment.** Add a separate technology-specific capacity pool, assigned only to qualified products. Preserve CoWoS capacity for products that cannot migrate. Treat additional usable packaging as an upside scenario until quantities are disclosed. Increasing aggregate packaging growth from 1.6× to 2× produces **109.3M**, only 4.6% above reference because another resource becomes limiting.

**Evidence strength / trigger:** technology availability is company-supported; customer timing is an analyst forecast, not a verified universal migration. Require production contracts/qualified volumes before changing the central case.

## N12 — ABF substrates and specialty glass can become independent bottlenecks

**News and timing.** Counterpoint's public 2026 substrate-research summary describes T-glass pressure, more complex packages, and delayed new capacity. TrendForce's April research independently identifies constraints extending into substrates and packaging materials. Counterpoint's displayed publication date was not established precisely; its summary discusses H1 2026, and should not be presented as a November measurement. [Counterpoint research summary](https://counterpointresearch.com/en/reports/From-T-Glass-Crisis-Capacity-Erosion-The-Multi-Year-Substrate-Shortage), [TrendForce April analysis](https://www.trendforce.com/presscenter/news/20260430-13028.html).

**Importance / model verdict: high; a missing constraint in a three-resource model.** Available logic, HBM, and CoWoS equipment do not guarantee complete packages if substrates or other materials are short.

**Adjustment.** Add substrate-qualified output as another minimum constraint. Until measured, represent it through an explicitly identified reduction in **effective** packaging growth: 1.35× instead of 1.6× gives **94.7M**. Do not add a separate substrate penalty if the effective packaging number already includes it. Analyst shortage percentages are not directly transferable to worldwide accelerator production.

**Evidence strength / trigger:** analysts' own research supports the mechanism; public summaries lack a complete supplier/product denominator. Update using qualified substrate deliveries and material lead times, not price inflation alone.

## N13 — Rubin changes the performance metric and requires a real shipment ramp

**News and timing.** NVIDIA's 31 May announcement described production ramping but put production shipments in the fall. Its current product specifications list 17.5 PFLOP/s dense FP8 and 4 PFLOP/s dense FP16 per Rubin GPU. [Production announcement](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory), [current specifications](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/).

**Importance / model verdict: high; do not retain a universal performance-growth factor.** The original workbook's approximately 6 PFLOP/s FP16 Rubin assumption exceeds the current 4 PFLOP/s listing by 50%; the current value is one-third lower. This is a like-precision specification comparison, not proof of a one-third fleet-wide reduction. The FP8/FP16 ratio also changes, making one H100-equivalent series insufficient for all workloads.

**Adjustment.** Use separate FP8 and FP16 series and actual product mix. Our previous component model already uses these current specifications: applying another “Rubin uplift” would double-count them. Its assumed linear mix ramp, including Rubin-like output in Q3 2026, is not an observed shipment history. Replace it with dated production cohorts when volumes are known. A lower 25% final Rubin share versus 50% gives **91.7M**.

**Evidence strength / trigger:** high for published peak specs, low for our assumed worldwide shares. Marketing workload speedups must not multiply nominal FLOP/s. Production announcements weaken a blanket “Rubin stalled” claim, but do not establish yield or shipment targets were met.

## N14 — Co-packaged optics may help system delivery without increasing GPU production

**News and timing.** NVIDIA's May production announcement includes Spectrum-X co-packaged-optics switches and system deployment integration. Its reported efficiency improvements are vendor comparisons for particular networking/system configurations. [NVIDIA announcement](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory).

**Importance / model verdict: medium; separates produced chips from usable systems.** Better networking efficiency can ease part of the system power burden. Conversely, missing switches, optics, cooling, or electrical equipment can delay otherwise completed accelerators.

**Adjustment.** Track finished-system completion and energization after chip packaging. Do not apply a network-specific efficiency factor to total data-center power or assume it eliminates commissioning delay. A two-quarter rather than one-quarter delay reduces the reference to **83.0M** operational H100e; this quantifies exposure, not a delay proven by this news.

**Evidence strength / trigger:** vendor evidence establishes a product claim, not a worldwide deployment improvement. Update the lag only from delivered-system and operational-site dates. This is an extension to availability accounting, not a reason to discard manufacturing accounting.

## What should change in the forecast now?

**Required methodological changes:** distinguish node and HBM-generation compatibility; distinguish HBM stack packaging from accelerator packaging; represent growing package resource requirements; retain separate performance precisions; model factory ramps and deployment by quarter. Add substrate/system constraints where evidence can quantify them. These changes address structural weaknesses rather than merely tweaking a growth rate.

**Numerical treatment now:** retain the previous 104.5M only as a reference scenario, with the following transparent stresses. Do not publish a new “news-adjusted central estimate” by choosing arbitrary adjustments that happen to offset. The news establishes mechanisms and schedules more strongly than aggregate magnitudes.

| Illustrative change from reference | End-2027 operational FP8 H100e | Change |
|---|---:|---:|
| Reference | 104.5M | — |
| Usable logic growth 1.6× → 1.3× | 96.6M | −7.6% |
| Usable packaging growth 1.6× → 1.35× | 94.7M | −9.4% |
| Usable packaging growth 1.6× → 2.0× | 109.3M | +4.6% |
| Rubin packaging burden 1.3 → 1.6 units | 98.8M | −5.5% |
| Usable HBM-bit growth 1.733× → 1.3× | 95.4M | −8.7% |
| Usable HBM-bit growth 1.733× → 2.0× | 104.5M | 0.0% |
| Final Rubin share 50% → 25%, difference to B300 | 91.7M | −12.2% |
| Commissioning delay one → two quarters | 83.0M | −20.5% |
| Joint: packaging 1.35×, Rubin burden 1.6, Rubin share 25% | 81.6M | −21.9% |

These are **selected counterfactuals**, not estimated news effects, confidence intervals, or exhaustive bounds. Except for the last row, changes are isolated. Effects cannot be added: the binding constraint switches. The sensitivity code preserves the original resource calibration and input files. The original broad 67–173M joint scenario range remains a different exercise.

## Incorporating an actual facility announcement

Use a capacity bridge rather than a headline multiplier:

```
Incremental qualified supply in quarter q
 = announced nameplate throughput
 × fraction installed and ramped in q
 × good-output yield
 × relevant AI/product allocation
 × qualification availability
 − displaced or transferred existing output
```

Use units appropriate to the stage: good logic die area, qualified HBM bits/stacks, or good product-specific packages. Exclude facilities outside the forecast horizon. Check whether each expansion is already included in the supplier's aggregate guidance. Feed the revised resource constraints into the minimum-capacity model, then apply shipment-to-operational timing. Do not multiply extra scanners, extra wafers, and extra packaging together as independent compute growth factors.

**Most valuable next observations:** monthly qualified CoWoS-L output by product; Rubin shipment cohorts; HBM4 good-bit and base-die allocations; N3 AI wafer allocations/yields; actual deployment dates. These would justify numerical revisions more directly than capex totals or construction announcements.

## Reproducible files and research limitations

Run `python research/calculations/news_sensitivities.py` from the workspace root. It reuses the existing component model, regenerates its original outputs unchanged, and writes [news sensitivities](calculations/news_sensitivities.json). Baseline and direction checks pass. The [script](calculations/news_sensitivities.py) exposes every numerical stress; none is mislabeled as a measured production parameter.

Links beside each news assessment are the supporting sources, accessed 12 November 2026. Paid underlying production tables were not obtained. Unconfirmed social-media reports and secondhand capacity figures were not used to set numerical inputs. Searches did not establish a comprehensive census of disruptions or alternative Chinese accelerator supply; absence from this dossier is not evidence those risks or suppliers are irrelevant. Factory announcements primarily support conditional scenarios until output and qualification are observed.
