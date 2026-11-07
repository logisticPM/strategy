"""Illustrative one-period operating contribution gates, not forecasts or ROI."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
def sales_gate(fixed, margin, lost_contribution=0):
    if margin<=0: raise ValueError('Positive incremental contribution margin required')
    return (fixed+lost_contribution)/margin
rows=[]
for fixed in [1,5,10]:
 for margin in [.2,.3,.4]:
  rows.append(dict(assumed_fixed_cost_m=fixed,assumed_margin=margin,break_even_incremental_net_sales_m=round(sales_gate(fixed,margin),6)))
tests={'sales_gate':sales_gate(5,.25,1),'new_offer_sales_gate':sales_gate(5,.25,3),'cost_action_net':10-3-4,'price_cut_required_unit_lift':(100-60)/(95-60)-1}
assert tests['sales_gate']==24 and tests['new_offer_sales_gate']==32 and tests['cost_action_net']==3
assert abs(tests['price_cut_required_unit_lift']-1/7)<1e-9
out={'status':'ALL INPUTS INVENTED; no company-calibrated forecast, ranking, NPV or approved threshold','units':'USD million unless price example; all flows same chosen period','sales_sensitivity':rows,'illustrations':tests,'missing':['capital and working capital','tax and timing','baseline variance and detectable effect','company hurdle rate','actual incremental margin and cannibalization']}
(root/'models/decision-gates-R019.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('9 sensitivity cells and 4 illustrative gates verified; all inputs hypothetical')
