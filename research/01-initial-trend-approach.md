# Report 1: initial approach and findings

Research cutoff: **12 November 2026**. This report records what the initial estimate actually did. The separate [component report](02-component-production-forecast.md) describes the new estimate.

## Conclusion

The initial estimate was **a log-linear extrapolation of Epoch's aggregate compute shipments, followed by stock accounting**. It was not a rerun of AI 2027's chip-production model. Hardware specifications were researched, but they did not determine the projected shipments. Describing that result as a component-level update would have been incorrect.

It estimated approximately **39.3 million operational dense-FP8 H100-equivalents at end-2026 and 97.6 million at end-2027**. These are conditional global hardware-capacity estimates, before workload utilization. They are not available rental inventory or resources accessible to a particular lab.

## Evidence used

| Input               | Value and provenance                                                                                                           | Limitation                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Quarterly shipments | Ten Epoch estimates, Q1 2024–Q2 2026, in [CSV](data/global_shipments.csv). Latest: 4,980,154 in Q1 2026; 6,327,416 in Q2. [I1] | Estimated shipments, not a hardware census; underlying vintage 19 October 2026.                                     |
| Opening stock       | Approximately 20 million cumulative sold H100e at end-2025. [I2]                                                               | Rounded baseline from a different publication vintage.                                                              |
| Deployment delay    | One quarter centrally; zero/two quarters in sensitivity. [I3]                                                                  | Epoch uses a three-month delivery-to-deployment lag, but our sold-stock anchor is not identical to delivered stock. |
| Attrition           | Zero centrally; 5–10% annually in stress tests                                                                                 | Selected assumptions, not observed retirement rates.                                                                |

[I3] separately reports approximately 20.3 million delivered H100e at end-2025. The initial calculation retained the older rounded sold-stock anchor rather than silently combining definitions. Both estimates still need a synchronized cohort-level baseline.

## Calculation

For quarterly shipment observations `S_i`, with `i=0,…,9`:

```
ln(S_i) = a + b × i + residual_i
annual growth factor = exp(4b) = 2.4813628
shipment doubling time = ln(2)/(4b) × 12 = 9.1524 months
```

The fitted 90% regression interval for annual growth is 2.298–2.679. This describes fit uncertainty conditional on the input estimates; it does not include uncertainty in those estimates or future supply constraints.

The implementation rounded the growth assumption to 2.5× annually and anchored future shipments to the actual last published quarter, rather than the fitted intercept:

```
S_q = 6,327,416 × 2.5^((q−1)/4), q ≥ 2
q=0: 2026Q1; q=1: 2026Q2
Operational_q = 20,000,000 + sum(S_j, j=0,…,q−1)
```

The last equation is the central case: one-quarter commissioning delay and no retirement. Published Q1/Q2 observations replace projections for those quarters. Thus end-2027 includes shipments through Q3 2027; Q4 shipments commission in 2028.

| Result                    |   End-2026 |    End-2027 |
| ------------------------- | ---------: | ----------: |
| Central operational stock |      39.3M |       97.6M |
| Combined stress scenarios | 29.2–50.6M | 64.7–141.9M |

Low stress combined 2× shipment growth, two-quarter lag, and 10% annual attrition. High stress combined 3× growth, zero lag, and zero attrition. These are scenario endpoints, not probability intervals.

Reproduce with `python research/calculations/recalculate.py` and `python research/calculations/availability.py` from the workspace root. The latter generates [quarterly results](calculations/availability.csv) and [sensitivities](calculations/availability_sensitivity.json).

## Findings and limits

1. The inspected Epoch series supports a historical shipment-growth rate around 2.5× annually. Continued growth at that rate is an assumption.
2. The authors' November update concerns timelines and research acceleration; it does not provide a newly measured worldwide hardware inventory or a complete replacement of the manufacturing inputs. [I4]
3. The original AI 2027 framework separates silicon production and performance per silicon area. Its simplified assumptions include roughly 1.65× annual silicon growth and 1.35× performance-density growth. The initial calculation did not update those mechanisms. [I5]
4. The initial numerical proximity to AI 2027's approximately 100M end-2027 figure was not validation: the definitions, hardware performance metric, assumptions, and calibration differ.
5. No packaging, HBM, logic-node, yield, or power constraint can alter the initial forecast except indirectly through the chosen aggregate growth rate or delay. That is the main reason to construct the second model.

## Sources

All accessed during this research, cutoff 12 November 2026. The broader source register remains in the [workfile](../AI%202027%20Compute%20Forecast%20%E2%80%94%20Research%20Workfile.md).

- **I1:** Epoch, [New global AI computing capacity is doubling every 9 months](https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling), 29 October 2026. Published quarterly table and regression.
- **I2:** Epoch, [How much AI compute do frontier labs use?](https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute), May 2026. Approximate historical stock anchor.
- **I3:** Epoch, [Scaling AI data centers research](https://epoch.ai/latest/scaling-ai-data-centers-research), 16 September 2026. Delivered stock and deployment methodology.
- **I4:** AI Futures Project, [Q3.5 Timelines Update](https://blog.aifutures.org/p/q35-timelines-update-looks-like-the), 10 November 2026. Latest authors' update located; not a physical inventory update.
- **I5:** AI 2027, [Compute Forecast](https://ai-2027.com/research/compute-forecast), and its [backend spreadsheet](https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/edit?gid=1866551567). Original manufacturing framework. Rendered material inspected; workbook not executed.
