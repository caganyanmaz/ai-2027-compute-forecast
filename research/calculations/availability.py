"""Narrow global availability forecast; all quantities in H100-equivalents.
Baseline remains approximate: no reconciled chip-cohort export available.
"""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
observed={r['quarter']:float(r['h100e']) for r in csv.DictReader((ROOT/'data/global_shipments.csv').open())}

def stock(t,growth=2.5,lag=1,retirement=0,base=20e6):
    # t=0 is 2026Q1. Retirement stress is on operational capacity only.
    # Opening stock is treated as commissioned by end-2025 for retirement purposes.
    total=base*(1-retirement)**((t+1)/4)
    for q in range(t-lag+1):
        label=f'{2026+q//4}Q{q%4+1}'
        added=observed.get(label,observed['2026Q2']*growth**((q-1)/4))
        total+=added*(1-retirement)**((t-q-lag)/4)
    return total
rows=[]
for t in range(2,8):
    rows.append({'quarter':f'{2026+t//4}Q{t%4+1}',
      'central_h100e':stock(t),
      'stress_low_h100e':stock(t,2.0,2,.10),
      'stress_high_h100e':stock(t,3.0,0,0),
      'status':'derived_estimate' if t==2 else 'forecast'})
sensitivity={
 'baseline_18M':stock(7,base=18e6), 'baseline_22M':stock(7,base=22e6),
 'growth_2x':stock(7,growth=2), 'growth_3x':stock(7,growth=3),
 'lag_0q':stock(7,lag=0), 'lag_2q':stock(7,lag=2),
 'retirement_5pct':stock(7,retirement=.05), 'retirement_10pct':stock(7,retirement=.10)}
with (ROOT/'calculations/availability.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
(ROOT/'calculations/availability_sensitivity.json').write_text(json.dumps(sensitivity,indent=2)+'\n')
assert all(r['stress_low_h100e']<=r['central_h100e']<=r['stress_high_h100e'] for r in rows)
assert stock(7,lag=0)>=stock(7,lag=1)>=stock(7,lag=2)
assert stock(7,retirement=.1)<stock(7,retirement=.05)<stock(7)
print(json.dumps({'quarters':rows,'sensitivity':sensitivity},indent=2))
