"""Source-derived arithmetic; does not estimate market share."""
from pathlib import Path
import json
channels={
 'stores':(1254.952,1173.747),
 'ecommerce':(993.093,934.630),
 'other':(277.174,307.254),
}
rows={k:dict(prior=a,current=b,change=round(b-a,3),growth_percent=round((b/a-1)*100,4)) for k,(a,b) in channels.items()}
assert abs(sum(v['prior'] for v in rows.values())-2525.219)<1e-6
assert abs(sum(v['current'] for v in rows.values())-2415.631)<1e-6
assert abs(sum(v['change'] for v in rows.values())+109.588)<1e-6
result=dict(unit='US$M',period='Q2 FY2026 versus Q2 FY2025',geography='Global, not US/Canada channel split',channels=rows,
 us_july_clothing_store_nominal_sales_growth_percent=round((28163/26962-1)*100,4),
 market_share_estimate=None,reason='No matched country/category/price/channel market denominator')
Path(__file__).with_name('market-bridge-R013.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
