"""Research arithmetic, standard library only. Not the authors' full model.
Run from any directory. Inputs are manually transcribed published estimates.
Outputs are deterministic illustrations, not calibrated probability forecasts.
"""
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT / 'data/global_shipments.csv').open()))
y = [math.log(float(r['h100e'])) for r in rows]
xbar = (len(y)-1)/2
ybar = sum(y)/len(y)
sxx = sum((i-xbar)**2 for i in range(len(y)))
slope = sum((i-xbar)*(v-ybar) for i,v in enumerate(y))/sxx
intercept = ybar-slope*xbar
se = math.sqrt(sum((v-intercept-slope*i)**2 for i,v in enumerate(y))/(len(y)-2)/sxx)
fit = {'annual_growth_factor': math.exp(4*slope),
       'doubling_months': 3*math.log(2)/slope,
       'annual_factor_90pct_regression_interval': [math.exp(4*(slope+d*1.859548*se)) for d in (-1,1)]}
# S08 approximate cumulative sold baseline. This is a separate vintage from S05.
base_sold = 20_000_000
actual_2026 = {0:4_980_154, 1:6_327_416}
scenarios = []
for growth in (2.0, 2.5, 3.0):
    additions = dict(actual_2026)
    for t in range(2,8):
        additions[t] = actual_2026[1]*growth**((t-1)/4)
    for lag in (0,1,2):
        for year,end in ((2026,3),(2027,7)):
            # At these endpoints all pre-2026 shipments have cleared <=2q lag.
            available = base_sold + sum(additions[t] for t in range(end-lag+1))
            scenarios.append({'year':year,'annual_shipments_growth_factor':growth,
                              'deployment_lag_quarters':lag,
                              'h100e_no_retirements':available,
                              'status':'illustrative_projection'})
central = next(r['h100e_no_retirements'] for r in scenarios if r['year']==2027 and r['annual_shipments_growth_factor']==2.5 and r['deployment_lag_quarters']==1)
# Keep annual average and period-end stocks distinct.
lab_fleet = 6_000_000 # chosen example average, NOT a measured 2026 fleet
seconds = 365*24*3600
flop = lab_fleet*0.4*0.989e15*0.3*seconds
results = {
 'regression':fit,
 'scenarios':scenarios,
 'latest_complete_quarter_2026Q3_illustrative_operational_h100e': base_sold+sum(actual_2026.values()),
 'central_2027_h100e':central,
 'central_2027_lab_h100e_at_20pct_share':0.2*central,
 'endpoint_anchored_original_2026_h100e':10e6*10**(21/33),
 'endpoint_anchored_original_2027_h100e':100e6,
 'original_growth_product':1.35*1.65,
 'original_40x_three_year_cagr':40**(1/3),
 'original_mar2025_to_dec2027_10x_cagr':10**(12/33),
 'original_225x_for_33months_h100e':10e6*2.25**(33/12),
 'lab_2025_sum_of_medians_h100e':sum(float(r['h100e_median']) for r in csv.DictReader((ROOT/'data/lab_compute_2025.csv').open())),
 'training_example_fp16_flop':flop,
 'rubin_bandwidth_h100_be':19.2/3.6,
 'rubin_fp16_h100_equiv':4/0.989,
 'rubin_fp8_h100_equiv':17.5/1.979,
 'rubin_vs_22TB_bandwidth_change_pct':100*(19.2/22-1),
 'example_rubin_chips_for_10T_fp8_weights':math.ceil(10e12/(288e9*0.8)),
 'example_energy_TWh_for_10GW_80pct_load':10*0.8*8760/1000,
 'capex_three_companies_2026_usd_billion_range':[220+195+135,220+205+145],
 'capex_four_companies_2026_mixed_basis_usd_billion_range':[220+195+135+170,220+205+145+170],
}
(ROOT/'calculations/results.json').write_text(json.dumps(results,indent=2)+'\n')
with (ROOT/'calculations/scenarios.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(scenarios[0]));writer.writeheader();writer.writerows(scenarios)
print(json.dumps({k:v for k,v in results.items() if k!='scenarios'},indent=2))
