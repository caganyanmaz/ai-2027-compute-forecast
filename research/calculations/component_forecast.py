"""Conditional component-limited model; see ../02-component-production-forecast.md.
Standard library only. Does not fit a compute growth rate. Hardware classes are
proxies, not measured vendor shipment shares. Capacity levels are calibrated.
"""
import csv
import json
from copy import deepcopy
from pathlib import Path
R = Path(__file__).resolve().parents[1]
p = json.loads((R/'data/component_inputs.json').read_text())
hw = p['hardware']
base_mix = p['baseline_mix']
obs = {r['quarter']:float(r['h100e']) for r in csv.DictReader((R/'data/global_shipments.csv').open())}

def avg(mix, field):
    return sum(mix[k]*hw[k][field] for k in mix)

base_n = obs['2026Q2']*hw['H100']['fp8_pf']/avg(base_mix,'fp8_pf')
# These are IMPLIED effective resources, not independent factory measurements.
base_resources = {k:base_n*avg(base_mix,v) for k,v in
                  [('logic','logic_mm2'),('packaging','packaging_units'),('hbm','hbm_gb')]}

def forecast(s):
    rows=[]
    for q in range(2,8): # q=0 is 2026Q1
        progress=(q-1)/6
        years=(q-1)/4
        mix={k:base_mix[k]+progress*(s['end_mix'][k]-base_mix[k]) for k in hw}
        assert abs(sum(mix.values())-1)<1e-10 and min(mix.values())>=0
        # Good output capacity already incorporates yield and allocation.
        growth={'logic':s['logic_growth'], 'packaging':s['packaging_growth'],
                'hbm':(13/9)*s['dram_bit_growth']}
        demand={'logic':avg(mix,'logic_mm2'),
                'packaging':avg(mix,'packaging_units'),
                'hbm':avg(mix,'hbm_gb')*(1+progress*s['extra_hbm_fraction'])}
        limits={k:base_resources[k]*growth[k]**years/demand[k] for k in demand}
        limiting=min(limits,key=limits.get)
        packages=limits[limiting]
        rows.append({'quarter':f'{2026+q//4}Q{q%4+1}', 'q':q,
          'logic_limit_packages':limits['logic'], 'packaging_limit_packages':limits['packaging'],
          'hbm_limit_packages':limits['hbm'], 'bottleneck':limiting,
          'packages':packages, 'mean_fp8_pf':avg(mix,'fp8_pf'),
          'shipment_h100e_fp8':packages*avg(mix,'fp8_pf')/hw['H100']['fp8_pf'],
          'shipment_h100e_fp16':packages*avg(mix,'fp16_pf')/hw['H100']['fp16_pf']})
    flows={0:obs['2026Q1'],1:obs['2026Q2']}
    flows.update({r['q']:r['shipment_h100e_fp8'] for r in rows})
    for r in rows:
        q=r['q']; lag=s['lag']; retirement=s['annual_retirement']
        r['operational_h100e_fp8']=p['opening_stock']*(1-retirement)**((q+1)/4)+sum(
            flows[t]*(1-retirement)**((q-t-lag)/4) for t in range(q-lag+1))
        r['cumulative_shipped_h100e_fp8']=p['opening_stock']+sum(flows[t] for t in range(q+1))
    return rows

all_rows=[]
summaries={}
for name,s in p['scenarios'].items():
    rr=forecast(s)
    all_rows.extend({'scenario':name,**r} for r in rr)
    summaries[name]={'end_2026_operational_h100e_fp8':rr[1]['operational_h100e_fp8'],
      'end_2027_operational_h100e_fp8':rr[-1]['operational_h100e_fp8'],
      '2027_shipments_h100e_fp8':sum(r['shipment_h100e_fp8'] for r in rr if r['q']>=4),
      '2027_shipments_h100e_fp16':sum(r['shipment_h100e_fp16'] for r in rr if r['q']>=4),
      'end_2027_cumulative_shipped_h100e_fp8':rr[-1]['cumulative_shipped_h100e_fp8']}
central=p['scenarios']['central']
sens={}
for key, values in {'logic_growth':[1.3,2.0], 'packaging_growth':[1.35,2.0],
                    'dram_bit_growth':[1.1,1.3], 'lag':[0,2],
                    'annual_retirement':[.05,.1], 'extra_hbm_fraction':[.2]}.items():
    for value in values:
        s=deepcopy(central);s[key]=value
        sens[f'{key}={value}']=forecast(s)[-1]['operational_h100e_fp8']
s=deepcopy(central);s['end_mix']=base_mix
sens['no_hardware_mix_transition']=forecast(s)[-1]['operational_h100e_fp8']
with (R/'calculations/component_quarters.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=all_rows[0]);w.writeheader();w.writerows(all_rows)
result={'implied_baseline_packages':base_n,'implied_baseline_resources':base_resources,
        'scenarios':summaries,'one_at_a_time_end_2027':sens}
(R/'calculations/component_results.json').write_text(json.dumps(result,indent=2)+'\n')
# Accounting and limiting-resource invariants, including exact baseline calibration.
assert abs(base_n*avg(base_mix,'fp8_pf')/hw['H100']['fp8_pf']-obs['2026Q2'])<1e-6
for r in all_rows:
    assert r['packages']<=min(r[k+'_limit_packages'] for k in base_resources)+1e-6
    assert r['operational_h100e_fp8']<=r['cumulative_shipped_h100e_fp8']+1e-6
s=deepcopy(central);s['lag']=0
assert abs(forecast(s)[-1]['operational_h100e_fp8']-forecast(s)[-1]['cumulative_shipped_h100e_fp8'])<1e-6
assert sens['lag=0']>summaries['central']['end_2027_operational_h100e_fp8']>sens['lag=2']
print(json.dumps(result,indent=2))
