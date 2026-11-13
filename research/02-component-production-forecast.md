# Report 2: updated component-limited compute estimate

**Research cutoff: 12 November 2026.** Scope: global AI accelerator production and operational capacity through December 2027.

## Result and evidential status

The central scenario estimates **104.5 million operational dense-FP8 H100-equivalents at end-2027**, versus **97.6 million** in the [initial trend estimate](01-initial-trend-approach.md). Rounded for practical use: **about 100 million**, conditional on the assumptions below. Combined constrained/expansion scenarios produce **67–173 million**; these are not statistical bounds.

This is a **calibrated component-limited model**: logic silicon, advanced packaging, and HBM separately constrain output, and a hardware mix converts that output to compute. It uses updated vendor performance specifications and public component-supply evidence. It is not a reconstruction of confidential factory production, nor an execution of the original AI 2027 spreadsheet. Absolute baseline resources, hardware mix, die areas for newer chips, yields, and some growth rates remain assumptions or calibration quantities. Public evidence did not establish all the correct manufacturing inputs.

The central bottleneck is packaging **within this model**, not an empirical finding that packaging must be the worldwide bottleneck. The forecast is a conditional supply scenario, with stronger causal structure than aggregate extrapolation but no demonstrated improvement in predictive accuracy.

## Relationship to AI 2027

The original forecast combines usable AI silicon area and performance per area. Packaging and HBM constrain how much silicon becomes usable; front-end wafer supply is treated as less restrictive. Its simplified factors were approximately 1.65× annual usable-silicon growth and 1.35× performance-density growth. [C01]

Here the same resource-accounting idea is made explicit:

```
Packages = min(
    usable AI logic area / average logic area per package,
    usable packaging resources / average packaging burden,
    usable HBM GB / average HBM GB per package)

Shipment compute = Packages × average dense FLOP/s per package
```

“Package” means an accelerator unit, including multichiplet accelerators, not a rack or individual silicon die. A prescribed hardware mix determines each average. The model neither optimizes the product mix nor assumes all capacity can be reallocated freely in reality. Separate process nodes, HBM generations, qualification requirements, and regional trade restrictions are aggregated; this can overstate fungibility.

Unlike the first estimate, **no fitted 2.5× compute-growth multiplier is used**. Component availability and hardware performance generate the compute trajectory. Like the first estimate, it uses Epoch's Q2 2026 shipment level for calibration, so the two estimates are not independent.

## Sourced updates and missing inputs

| Evidence                     | Value inspected                                                                     | How it enters                                                                                                                                  |
| ---------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| HBM supply composition [C02] | End-2026/2027 HBM share of total DRAM bits: 9% / 13%; wafer-input shares: 22% / 30% | Bit-share ratio 13/9 multiplies assumed total DRAM bit growth. Wafer shares are not treated as bit growth.                                     |
| Packaging [C03]              | TSMC plans CoWoS capacity expansion exceeding 60% “by 2027”                         | Informs a **selected** 1.6× annual central resource-growth assumption. The source does not unambiguously establish a 2026-to-2027 annual rate. |
| Blackwell Ultra [C04]        | 72-GPU rack: sparse FP8 720 PFLOP/s, sparse FP16 360 PFLOP/s                        | Divide by 72 and by two: dense 5 and 2.5 PFLOP/s per GPU.                                                                                      |
| Rubin [C05]                  | Dense FP8 17.5; dense FP16 4 PFLOP/s per GPU; 288 GB HBM                            | Direct product-class inputs. No FP4 or application benchmark substituted for FP8.                                                              |
| TPU7x [C06]                  | FP8 4.614; BF16 2.307 PFLOP/s; 192 GiB HBM per accelerator                          | Direct product-class inputs; convert memory to 206.158 decimal GB.                                                                             |
| H100 SXM [C07]               | Dense FP8 1.979 and FP16 0.9895 PFLOP/s; 80 GB                                      | Reference units and legacy hardware class.                                                                                                     |
| TSMC Q3 update [C08]         | Additional N3 capacity planned for 2027; N2 capacity more than doubles in 2027      | Qualitative evidence only. N2 growth is not applied to all AI logic capacity.                                                                  |

More recent research was checked: TrendForce's September packaging and HBM updates and its November HBM report listing. They support continued constraints but do not expose a complete usable-capacity dataset in public text. The November report's numerical supplier production tables were not obtained. This report therefore retains the older June numerical HBM-share forecast and labels its vintage; it does not pretend all inputs were updated in November. [C09–C11]

Still missing: consistent quarterly AI-allocated wafer starts by node, good-die yields, package yields and interposer throughput by product, HBM4 good-bit output by supplier, and a worldwide commissioning/power schedule. A supplier's revenue or capex is not substituted for any of these physical quantities.

## Hardware proxies and assumptions

The following four classes represent the fleet's manufacturing demand. They are **not measured worldwide market shares**; AMD, other ASICs, older TPUs, and other products are represented imperfectly by these classes. B300-like and TPU7-like classes in the Q2 baseline are resource/performance proxies, not claims about those exact products' historical deliveries.

| Class      | Dense FP8 PF/s | Dense FP16/BF16 PF/s |  HBM GB | Logic mm² | Packaging units |
| ---------- | -------------: | -------------------: | ------: | --------: | --------------: |
| H100-like  |          1.979 |               0.9895 |      80 |       814 |             0.5 |
| B300-like  |              5 |                  2.5 |     288 |     1,628 |             1.0 |
| TPU7-like  |          4.614 |                2.307 | 206.158 |     1,600 |             0.8 |
| Rubin-like |           17.5 |                    4 |     288 |     1,800 |             1.3 |

Performance values come from C04–C07. H100/B300 logic areas are proxies carried from the original H100/two-die Blackwell assumptions; TPU and Rubin areas are selected assumptions, not verified measurements. All packaging burdens are assumptions, not CoWoS wafer measurements. B300's 288 GB is a class assumption; the inspected rack page gives rounded 20 TB. NVIDIA GB values are treated as nominal decimal GB; Google's explicitly binary GiB is converted. Memory figures do not represent usable model-weight capacity after software overhead.

The central package-count mixture changes linearly over six quarters:

| Class      | Q2 2026 calibration mix | Q4 2027 mix |
| ---------- | ----------------------: | ----------: |
| H100-like  |                     25% |          0% |
| B300-like  |                     50% |         25% |
| TPU7-like  |                     25% |         25% |
| Rubin-like |                      0% |         50% |

These endpoint shares are selected assumptions. Rubin Ultra and future ASIC improvements are not explicitly credited. An additional memory-burden stress represents some risk from larger-memory products without inventing their performance.

## Resource calibration and growth

Let `w_i` be package-count shares, `F_i` dense FP8 PFLOP/s, and `S_0=6,327,416` H100e shipped in Q2 2026. Then:

```
Baseline mean F = sum(w_i × F_i) = 4.14825 PFLOP/s
Baseline packages N_0 = S_0 × 1.979 / 4.14825 = 3,018,612
Logic L_0 = N_0 × mean area = 4.27888 billion good mm²/quarter
Packaging P_0 = N_0 × mean burden = 2.49035 million units/quarter
HBM H_0 = N_0 × mean memory = 650.630 million GB/quarter
```

These are **implied effective resources**, not independent observations of industry output. Calibration sets all three baseline limits equal to baseline packages. Actual spare capacity is unknown; assuming none in each component is consequential. Logic quantities refer to effective good AI-allocated silicon; physical wafer starts cannot be inferred without edge losses, yields, node allocation, and process-specific matching.

For `y` years after Q2 2026:

```
L(y) = L_0 × 1.6^y
P(y) = P_0 × 1.6^y
H(y) = H_0 × [(13/9) × 1.2]^y = H_0 × 1.733333^y
```

Logic's 1.6× is an assumption about combined capacity, AI allocation, and good-area yield. Packaging's 1.6× is an assumption informed by C03. Total DRAM bit growth of 1.2× is an assumption. C02 supplies the 13/9 share ratio, not the full 1.7333× HBM growth rate. Extending this end-2026-to-end-2027 ratio as a constant trajectory from Q2 2026 is another assumption. These are effective supply rates: no second yield penalty is applied.

At Q4 2027, average performance is 11.1535 dense FP8 PFLOP/s. Component constraints allow:

| Component | Supported packages per quarter |
| --------- | -----------------------------: |
| Logic     |                         5.073M |
| Packaging |                     **4.582M** |
| HBM       |                         5.550M |

Therefore Q4 shipments are `4.58193M × 11.1535 / 1.979 = 25.8234M FP8 H100e`. This calculation shows exactly how hardware and components drive the result.

## Production versus operational availability

Opening cumulative sold stock remains approximately 20M H100e at end-2025. Q1/Q2 2026 use the published Epoch shipment estimates. Later quarters use the component model. Central commissioning takes one quarter; central retirement is zero. The inherited baseline and sold-to-deployed timing mismatch remain limitations. Power constraints enter only through the selected delay: no independent power ceiling is enforced.

| Quarter end | Component-model shipments during quarter | Operational stock at quarter end |
| ----------- | ---------------------------------------: | -------------------------------: |
| 2026Q3      |                                    8.64M |                           31.31M |
| 2026Q4      |                                   11.26M |                           39.95M |
| 2027Q1      |                                   14.23M |                           51.20M |
| 2027Q2      |                                   17.61M |                           65.44M |
| 2027Q3      |                                   21.45M |                           83.04M |
| 2027Q4      |                                   25.82M |                      **104.49M** |

All entries use dense-FP8 H100e. Q3 2026 is a retrospective estimate, not a new observed quarter. Total 2027 shipments are **79.11M FP8 H100e**. Cumulative shipped stock reaches **130.32M** by end-2027, of which the last quarter's shipments await commissioning under the central lag.

“Operational” means nominal installed capacity, including committed or busy hardware, before workload utilization. It does not establish spare rental availability, capacity accessible to one organization, or capacity connected for a single training run.

## Precision changes the answer

Rubin's listed dense FP8/FP16 ratio is 4.375, whereas the other modeled classes have a ratio of two. Consequently the same physical 2027 production equals **79.11M FP8 H100e but 48.87M FP16 H100e**. These figures are different performance metrics for the same chips.

The original AI 2027 TPP-based figures cannot be directly equated to this dense-FP8 series. We do not convert the whole existing fleet into FP16 equivalents because its historical chip composition was not recovered. A single multiplier on the aggregate stock would hide this uncertainty. Hardware peak FLOP/s also does not measure realized training or inference throughput.

## Scenario and sensitivity results

All three scenarios share the observed shipment anchor and the same calibrated resource baseline.

| Assumption                         |  Constrained |     Central |   Expansion |
| ---------------------------------- | -----------: | ----------: | ----------: |
| Annual good logic-area factor      |         1.30 |        1.60 |        2.00 |
| Annual packaging-resource factor   |         1.35 |        1.60 |        2.00 |
| Annual total DRAM bit factor       |         1.10 |        1.20 |        1.30 |
| Implied annual HBM bit factor      |        1.589 |       1.733 |       1.878 |
| Q4 2027 mix H100/B300/TPU/Rubin    | 10/40/25/25% | 0/25/25/50% | 0/10/20/70% |
| Additional final HBM burden        |          10% |          0% |          0% |
| Commissioning lag                  |   2 quarters |   1 quarter |  0 quarters |
| Annual operational attrition       |           5% |          0% |          0% |
| **End-2026 operational FP8 H100e** |    **30.2M** |   **39.9M** |   **54.9M** |
| **End-2027 operational FP8 H100e** |    **67.0M** |  **104.5M** |  **173.0M** |

These are chosen joint scenarios, not confidence intervals or exhaustive bounds. The expansion case assumes immediate deployment, so it is particularly optimistic about power and commissioning.

One input changed at a time from central:

| Change                                | End-2027 operational FP8 H100e |
| ------------------------------------- | -----------------------------: |
| No hardware-mix transition            |                          76.9M |
| Logic growth 1.3× / 2.0×              |                 96.6M / 104.5M |
| Packaging growth 1.35× / 2.0×         |                 94.7M / 109.3M |
| Total DRAM bit growth 1.1× / 1.3×     |                104.5M / 104.5M |
| Extra HBM burden 20% by final quarter |                         104.5M |
| Commissioning lag zero / two quarters |                 130.3M / 83.0M |
| Annual attrition 5% / 10%             |                 100.3M / 96.3M |

HBM changes do not affect these particular central sensitivities because packaging remains the active limit for the cohorts commissioned by end-2027. This does not show that HBM supply is unimportant; different allocations, memory intensity, or generation-specific constraints could make it binding. These sensitivities omit uncertainty in baseline product mix, absolute resource calibration, and relative die/package burdens.

## Reproduction and next use

Run `python research/calculations/component_forecast.py` from the workspace root. It reads [inputs and provenance](data/component_inputs.json) and [historical shipments](data/global_shipments.csv), then writes [quarterly component limits and results](calculations/component_quarters.csv) and [scenario/sensitivity output](calculations/component_results.json). It checks baseline calibration, resource limits, stock accounting, and commissioning-lag ordering.

For planning, use the central trajectory only alongside its assumptions. The most useful next improvements are actual package-count mix, generation-specific packaging/HBM allocation, and commissioning dates. Replace calibrated resources with independently sourced physical supply when available; then rerun the same equations. Do not label the result a measured inventory or a fully updated original-model replication until those gaps are resolved.

## Source register

Access cutoff 12 November 2026. Vendor pages are live specifications; dates below identify publication dates where known. Source statements and modeling assumptions are separated above.

- **C01:** AI 2027, [Compute Forecast](https://ai-2027.com/research/compute-forecast), April 2025, and [backend](https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/edit?gid=1866551567). Original framework and historical die-area assumptions; supplied HTML retained unchanged.
- **C02:** TrendForce, [HBM supply and DRAM allocation](https://www.trendforce.com/presscenter/news/20260602-13074.html), 2 June 2026. Public numerical HBM share forecasts; not measured 2027 production.
- **C03:** TrendForce, [Advanced packaging and 3nm capacity](https://www.trendforce.com/presscenter/news/20260430-13028.html), 30 April 2026. Packaging expansion statement and capacity constraints.
- **C04:** NVIDIA, [GB300 NVL72 specifications](https://www.nvidia.com/en-us/data-center/gb300-nvl72/). Rack configuration and sparsity footnote.
- **C05:** NVIDIA, [Vera Rubin NVL72 specifications](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/). Per-GPU dense performance and memory. No application-level speedups used.
- **C06:** Google Cloud, [TPU7x documentation](https://docs.cloud.google.com/tpu/docs/tpu7x). Per-accelerator compute and memory, not per-chiplet values.
- **C07:** NVIDIA, [H100 specifications](https://www.nvidia.com/en-us/data-center/h100/). SXM reference; sparse tensor values divided by two.
- **C08:** TSMC, [Q3 2026 earnings transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf), 15 October 2026. Qualitative node-capacity check; no absolute capacity numbers inserted from this source.
- **C09:** TrendForce, [Packaging update](https://www.trendforce.com/presscenter/news/20260918-13241.html), 18 September 2026. Qualitative check on CoWoS-L and larger-package pressure.
- **C10:** TrendForce, [HBM update](https://www.trendforce.com/presscenter/news/20260929-13255.html), 29 September 2026. Supply tightness and stack choices; price growth not used as bit growth.
- **C11:** TrendForce, [Q4 HBM research listing](https://www.trendforce.com.tw/research/download/RP261104NB), November 2026. Public summary only; underlying production tables unavailable in this research and not used.
- **C12:** Epoch, [Quarterly AI compute shipment series](https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling), 29 October 2026. Q2 calibration and Q1 historical flow; no fitted growth rate used in this model.
- **C13:** Epoch, [Historical fleet discussion](https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute), May 2026, and [deployment methodology](https://epoch.ai/latest/scaling-ai-data-centers-research), September 2026. Opening-stock and lag context, with the definition mismatch noted above.
