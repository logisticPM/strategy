"""Reported USD millions; arithmetic attribution, not causal or recoverable losses."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
cuts={
'geography':{'US':[1415.002,1302.069],'Canada':[321.293,285.815],'Mexico':[21.922,28.888],'China Mainland':[392.898,407.095],'ROW':[374.104,391.764]},
'category':{'Women':[1547.321,1488.241],'Men':[624.598,621.380],'Accessories and other':[353.300,306.010]},
'channel':{'Stores':[1254.952,1173.747],'E-commerce':[993.093,934.630],'Other':[277.174,307.254]}}
out={'units':'USD million','source':'LULU-Q2-2026 Note 3 and MD&A; same family as E039-E047','cuts':{}}
for name,values in cuts.items():
 assert abs(sum(v[0] for v in values.values())-2525.219)<1e-6
 assert abs(sum(v[1] for v in values.values())-2415.631)<1e-6
 out['cuts'][name]={k:{'prior':v[0],'current':v[1],'change':round(v[1]-v[0],3),'growth_pct':round((v[1]/v[0]-1)*100,3)} for k,v in values.items()}
out['sga']={'head_office_increase':45.8,'channel_increase':7.7,'fx_gain_reduction':1.2,'rounded_sum':54.7,'exact_total':54.674,'rounding_residual':0.026,'head_office_components':[14.6,14.1,7.6,6.9,6.4,-3.8],'channel_components':[5.1,1.7,.9,4.2,-4.2]}
assert abs(sum(out['sga']['head_office_components'])-45.8)<1e-6
assert abs(sum(out['sga']['channel_components'])-7.7)<1e-6
out['margin_bridge_bps']={'refund':560,'tariffs_markdowns_price_product_cost_net':-150,'fx':20,'occupancy_depreciation':-180,'distribution_product_departments':-50}
assert sum(out['margin_bridge_bps'].values())==200
out['warning']='Cuts overlap and must not be added. Margin bps rounded; cost increases are not cost-saving opportunities. No causal or investment ranking.'
(root/'models/loss-map-R017.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Three revenue cuts reconcile; rounded margin and expense bridges reconcile')
