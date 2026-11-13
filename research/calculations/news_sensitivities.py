"""News-motivated stress tests, NOT statistically inferred news adjustments.
Reuses the prior model and regenerates its existing outputs unchanged.
"""
import contextlib
import io
import json
import runpy
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with contextlib.redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(ROOT/'calculations/component_forecast.py'))
f=m['forecast']; central=m['central']; hw=m['hw']
base=f(central)[-1]['operational_h100e_fp8']
rows=[]
def record(name, changes=None, rubin_pack=None):
    s=deepcopy(central);s.update(changes or {})
    old=hw['Rubin']['packaging_units']
    try:
        if rubin_pack is not None:hw['Rubin']['packaging_units']=rubin_pack
        r=f(s)[-1]
    finally:hw['Rubin']['packaging_units']=old
    val=r['operational_h100e_fp8']
    rows.append({'case':name,'changes':changes or {},'rubin_package_burden':rubin_pack,
        'end_2027_operational_fp8_h100e':val,'delta_percent':100*(val/base-1),
        'q4_2027_production_bottleneck':r['bottleneck']})
record('Reference')
record('Slower usable logic growth',{'logic_growth':1.3})
record('Slower usable packaging growth',{'packaging_growth':1.35})
record('Faster usable packaging growth',{'packaging_growth':2.0})
record('Larger Rubin package burden',rubin_pack=1.6)
record('HBM usable bits grow only 1.3x annually',{'dram_bit_growth':1.3/(13/9)})
record('HBM usable bits grow 2x annually',{'dram_bit_growth':2/(13/9)})
record('Rubin reaches 25% of package mix',{'end_mix':{'H100':0,'B300':.5,'TPU7':.25,'Rubin':.25}})
record('Two-quarter commissioning delay',{'lag':2})
record('Joint packaging and Rubin mix stress',{'packaging_growth':1.35,'end_mix':{'H100':0,'B300':.5,'TPU7':.25,'Rubin':.25}},rubin_pack=1.6)
assert abs(base-104494647.17875306)<1e-6
assert rows[2]['end_2027_operational_fp8_h100e']<base<rows[3]['end_2027_operational_fp8_h100e']
assert rows[4]['end_2027_operational_fp8_h100e']<base
assert rows[5]['end_2027_operational_fp8_h100e']<base
out={'status':'Illustrative isolated shocks, not news-derived parameter estimates or probability bounds','results':rows}
(ROOT/'calculations/news_sensitivities.json').write_text(json.dumps(out,indent=2)+'\n')
print('| Illustrative change | End-2027 operational FP8 H100e | Change vs reference |')
print('|---|---:|---:|')
for r in rows:print(f"| {r['case']} | {r['end_2027_operational_fp8_h100e']/1e6:.1f}M | {r['delta_percent']:+.1f}% |")
