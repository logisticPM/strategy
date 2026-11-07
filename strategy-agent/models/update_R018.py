"""Disclosure-boundary review and decision gates; no ROI estimates."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
names=['README.md','dashboard.md','evidence-ledger.md','hypotheses.md','research-plan.md','enterprise-diagnosis.md','decisions/D002-enterprise-strategy.md']
a=r/'runs/R018-before';a.mkdir(exist_ok=False)
for n in names:(a/(n.replace('/','__')+'.txt')).write_bytes((r/n).read_bytes())
def read(n):return (r/n).read_text(encoding='utf-8-sig')
def write(n,s):(r/n).write_text(s,encoding='utf-8',newline='\n')
cash={'units':'USD million','period':'First two quarters, not Q2 alone','prior':{'cfo':209.722,'ppe_cash':330.161,'buybacks_cash':715.672},'current':{'cfo':589.278,'ppe_cash':277.056,'buybacks_cash':695.105}}
for k in ['prior','current']:
 cash[k]['cfo_less_ppe_cash']=round(cash[k]['cfo']-cash[k]['ppe_cash'],3)
 cash[k]['after_buybacks_arithmetic']=round(cash[k]['cfo_less_ppe_cash']-cash[k]['buybacks_cash'],3)
cash['warning']='Not company FCF, distributable cash or optimal buyback assessment. Includes working-capital/tax timing and refund effects; excludes other cash flows.'
write('models/cash-boundary-R018.json',json.dumps(cash,indent=2)+'\n')
report='''# R018 成交、资本效率与公开披露边界

读取2026-11-07，案例截止2026-10-08。重读[Q2 FY2026 10-Q](https://www.sec.gov/Archives/edgar/data/1397187/000139718726000127/lulu-20260802.htm)：现金流印刷页7、分部政策页16、现行计划页21、可比定义页30–31、流动性页32、门店页34–35。Q1全价表述来自[6月4日官方公告](https://corporate.lululemon.com/newsroom/press-releases/2026/06-04-2026-210523775)；与既有财报家族重叠，不算独立市场验证。

## 1. 已补核的经营与资本事实

| 项目 | 上年同期 | 本年同期 | 口径与解读 |
|---|---:|---:|---|
| 上半年经营现金流，US$M | 209.722 | 589.278 | 非Q2单季；现金改善不证明盈利修复 |
| 上半年购建固定资产现金，US$M | 330.161 | 277.056 | 全球现金支出；不是当期费用，也非区域分配 |
| 经营现金流减购建固定资产，US$M | -120.439 | 312.222 | 自算桥，非公司定义FCF或可分配现金 |
| 上半年回购现金，US$M | 715.672 | 695.105 | 与前行相减本期为-382.883；不是经营亏损或破产判断 |
| 直营门店（年初→8月2日） | 811 | 825 | 半年净增14；不是同比净增数或新开总数 |
| 美国店数（年初→8月2日） | 379 | 380 | 无开店日期、面积和店级盈利；不能用国别全渠道收入除店数算坪效 |
| 加拿大店数（年初→8月2日） | 71 | 74 | 同上；净增不说明旧店生产力 |
| 第三方经营网点（年初→8月2日） | 45 | 53 | 授权/供应安排，不与直营门店当同等收入单元相加 |

现金算术见[结果及定义](../models/cash-boundary-R018.json)。公司称经营资产/负债变动带来现金流同比改善464.7M，涉及库存与所得税支付时点等；同期净利润下降，不能将经营现金改善全部视为可持续经营效率收益。退款已包含在财务结果，不在本表再次机械剔除；这里不是现金流正常化。

投资支出下降的解释为供应链基础设施及电商技术投入下降，部分被直营店新开、翻修和搬迁投入增长抵消，主要涉及美洲和EMEA。没有分别披露金额；不能断言停止供应链投资、扩店是错误或计算各项目ROI。

## 2. 确认披露限制，避免制造假指标

Note 11明确说明公司不按分部报告资本支出和资产，因为CODM不按该信息审阅。故本份财报不能构造分部投入资本或ROIC；更不能用分部营业利润率代替。地区收入增长也不补资本分母。

可比销售包含成熟直营门店和全部电商，扩建后须满足12个完整财月；排除新店、某些临时关闭/搬迁及已关闭门店。电商含店取、门店发货及跨店调货。因此可比下降不是纯成熟门店下降，线上收入不是纯配送中心履约；不能由收入变化计算配送单位成本或店群生产力。

国别×品类×渠道、成熟/新店现金回报、订单履约成本、退货/缺码、买家频次及全价贡献仍未取得。本轮只说明所检材料及检索边界，不声称所有公开材料都绝无披露。

## 3. 全价销售：有改善说法，无可复算贡献桥

Q1官方公告管理层称北美全价销售出现环比改善，但没有在该表述中提供金额、比例、可比基数或客群。Q2 10-Q将提高全价销售依赖度列为现行计划的一部分，不等于已经实现。不能把不同季度定性表述拼成已证明的持续修复，也不能用全渠道收入或综合毛利率反推全价收入。

本轮定向搜索发现第三方Q2电话会结果摘要提及markdown基点，但打开正文返回403；未将摘要数字入台账或用它拆毛利。Q1官方表述与Q2计划的证据强度分别标记，未假称取得完整电话会。

## 4. 团队数据权限：仍不能假设有交易面板

一次UBC官方域名定向检索返回[图书馆商业数据库指引](https://sba.ubc.ca/guide/home-based-business-guide/find-industry-info/library-databases)，列举公司/行业研究资源；没有确认Earnest/Circana目标面板订阅。搜索未找到不等于学校没有；未登录CWL、未读取订阅数据、未联系馆员/供应商。指南日期/版本未核，只作研究导航，不进入案例市场证据。

## 5. 从搜集资料转向可改变决定的门槛

| 暂定动作 | 现在能做的判断 | 扩大投入需要什么 | 应停止/转向的条件 |
|---|---|---|---|
| 成交修复诊断 | 美加损失及公司漏斗解释足以支持诊断，不足以选择产品或营销 | 匹配美加渠道/客群的全价净贡献；区分新客、频次、转化、件单量与价格 | 流量上涨但净贡献不增，不追加同样获客投入；问题被库存/选码解决则不开发新品 |
| 门店/配送效率审查 | 占用/配送压力及门店投入增长值得核；不预设关闭 | 按成熟度分组的店级贡献、租赁/退出、capex、线上蚕食和每单履约成本 | 扣退出费/服务损失后无净收益则不关店；新店只是转移原渠道收入则不据总收入扩张 |
| 总部费用审查 | 部分成本驱动已知；不能把同比增量当节省池 | 项目承诺、一次性/持续、可避免成本、取消成本及价值损失 | 费用必要或削减损害品质/增长则保留 |
| 新品/新市场 | 普通候选，无默认倾向 | 相对F的真实增量、全价保留、扣蚕食与资本的回报 | 概念喜欢但无支付、只替换同品牌销售或回报不足则不扩大 |
| 回购与投资资金分配 | 本期回购超过简单经营现金减capex；需同框比较 | 流动性、季节性、承诺、估值及经营项目风险回报 | 不能只因半年现金差额就断言停回购；不能把回购计作经营增长 |

公式只定义门槛，不填收益：项目增量贡献＝增量净销售×增量贡献率－持续新增费用－蚕食贡献损失；资本决策另纳入capex、营运资金、租赁/退出和时间，不将资本支出一次当期费用重复扣。阈值由可比基线及资本要求确定，当前不虚设百分比。

## 6. 最小数据请求与明确停止点

请求尚未发送：最近8季美加月度/季度的①渠道×品类净收入、全价/折扣、退货、毛利；②新老客、访问/转化、购买频次、件单量及实付价；③成熟/新店贡献、开扩店日期/面积、capex/租赁及线上蚕食；④履约单量、配送/退货成本与库存缺码；⑤总部项目、必要性与取消成本。各字段须有币种、期间、定义、匿名聚合层级和数据负责人。

本轮到达这些参数的公开资料边界。下一步应核团队已有授权数据或使用上述门槛做受限情景，不继续从同一10-Q反复提取新“证据票”，也不重复扩搜泛泛评论。没有数据时保留条件性选择；访谈仍后置、未外联/采购/实施商业措施。
'''
write('sources/capital-conversion-R018.md',report)
ledger=read('evidence-ledger.md').replace('## R017 当前','## R018 当前').replace('sources/audit-R017.json','sources/audit-R018.json').replace('[本轮损失地图](sources/loss-map-R017.md)','[本轮资本与成交边界](sources/capital-conversion-R018.md) · [损失地图](sources/loss-map-R017.md)').replace('累计52项均有使用处置；R017新增2项同源财报核查，不代表52项原文全部本轮复核','累计54项均有使用处置；R018新增2项财报与披露边界核查，不代表54项独立研究或本轮全核')
ledger+='''
## R018 成交、现金与资本披露边界

### E053 现金、投资方向与分部资本披露限制

- 类型／状态：已核查；处置：限定。读取2026-11-07，FY2026上半年/8月2日，案例前。家族LULU-Q2-2026，与E040/E052同源。
- 经营现金589.278M、购建固定资产277.056M、回购现金695.105M；简单经营现金减购建为312.222M，不是公司FCF或最优回购判断。现金改善含营运资金/税时点因素。总capex下降但门店投入增长；未给项目金额。Note 11明确不按分部报告资本支出及资产，不能据分部利润计算ROIC。
- [原文页码、门店口径、算术及门槛](sources/capital-conversion-R018.md)。资本与费用不可混算；不能据此直接停店/停回购。

### E054 全价成交表述及指标定义边界

- 类型／状态：已核查（官方表述及定义，未取得全价贡献数据）；处置：限定。家族LULU-Q1-2026及LULU-Q2-2026，非独立消费者证据；案例前。
- Q1公告称北美全价销售环比改善，缺量化基数；Q2提高全价依赖为计划，不是已实现。可比含成熟门店及全部电商、部分履约在门店，不能当纯店效或纯线上履约。美加全价率/净贡献和单位配送成本仍缺。
- [来源、排除的403转录摘要及下一步](sources/capital-conversion-R018.md)。不从综合毛利反推全价销售，不证明现行修复成功/失败。
'''
write('evidence-ledger.md',ledger)
h=read('hypotheses.md').replace('## R017 当前','## R018 当前').replace('国家成熟/新店现金流、capex、租赁与线上蚕食；未达门槛不扩量','E053确认分部资本未披露；需国家成熟/新店现金流、capex、租赁与线上蚕食；未达门槛不扩量')
h+='\nR018：E053明确资本分母缺口和现金时点影响，H013不升级；E054全价改善为定性表述，H007/H010不获得效果验证。停止重复同源参数搜索，转最小数据请求和条件门槛。\n'
write('hypotheses.md',h)
summary='''
## R018 当前边界：不能以现金或总增长替代回报

E053确认上半年经营现金改善包含营运资金/税时点；capex总额下降但门店投入增加，且公司明确不披露分部资本支出/资产。E054确认全价改善仅有定性表述，可比/电商为全渠道口径。无法从现有资料计算地区ROIC、全价贡献或配送单位成本。

当前选择：有条件推进成交、店群/配送与费用诊断；不据此普降价、追加营销、关店或停止回购，P2/P3未获扩量依据。下一步转已有授权数据核实和项目门槛，不反复搜同源财报填缺口。[门槛、字段与停止点](../sources/capital-conversion-R018.md)。
'''
d=read('decisions/D002-enterprise-strategy.md').replace('R017经营诊断版','R018经营诊断版');idx=d.index('## R017 当前增量');write('decisions/D002-enterprise-strategy.md',d[:idx]+summary+'\n'+d[idx:])
d=read('dashboard.md').replace('更新2026-11-07，R017','更新2026-11-07，R018');idx=d.index('## R017 当前诊断')
d=d[:idx]+'''## R018 当前结论：进入数据与项目门槛阶段

现金改善不等于盈利修复；总capex下降不代表门店投资收缩。分部资本支出/资产明确未披露，不能计算地区ROIC（E053）。全价销售只有定性改善表述，尚无可复算贡献桥（E054）。

**保留成交与效率诊断，暂不选定产品、营销、关店或扩张方案。** 已列最小数据字段及改变行动的条件；停止重复同源搜索，不以缺参数制造ROI排名。[资本与成交边界、行动门槛](sources/capital-conversion-R018.md)。

'''+d[idx:];write('dashboard.md',d)
write('enterprise-diagnosis.md',read('enterprise-diagnosis.md').replace('更新2026-11-07，R017','更新2026-11-07，R018')+'\nR018：[成交/资本边界](sources/capital-conversion-R018.md)确认分部资本明确未披露、现金改善包含时点因素；不从店数和国别全渠道收入计算坪效，亦不由综合毛利推全价贡献。\n')
write('research-plan.md',read('research-plan.md').replace('R017，2026-11-07','R018，2026-11-07')+'\n## R018 停止重复检索的参数\n\n已核本份10-Q不披露分部资本；未取得美加全价/顾客队列、店群与配送单位成本。下一步核团队已授权数据并逐项填[最小请求与决策门槛](sources/capital-conversion-R018.md)，不继续从同份财报创造证据数量。UBC公开检索未确认目标交易面板，未登录/外联/采购。数据无法取得时做显式假设的受限情景，不输出投资排名。\n')
write('README.md',read('README.md').replace('当前版本R017','当前版本R018')+'\nR018：[成交、资本披露边界与行动门槛](sources/capital-conversion-R018.md)。\n')
audit=json.loads(read('sources/audit-R017.json'));audit['version']='R018';audit['scope']='累计54项处置；本轮2项为财报现金/资本边界及全价定义，同源不可重复加权。下一步转最小数据与项目门槛，无投资排名。'
for eid,reason in [('E053','现金改善含时点影响；资本分母明确不按分部披露，不计算ROIC或回购最优性。'),('E054','全价定性表述非贡献序列；全渠道定义不支持纯门店或配送效率推算。')]:audit['evidence'][eid]=dict(action='限定',review='R018核官方披露与定义',reason=reason,family='LULU-Q2-2026' if eid=='E053' else 'LULU-Q1-2026；LULU-Q2-2026',period='案例前')
audit['hypotheses']['H013']['reason']+=' R018公司明确未按分部披露资本支出/资产，不能构造地区ROIC。'
write('sources/audit-R018.json',json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
write('runs/R018-capital-conversion.md','''# R018 · 2026-11-07

输入：继续经营诊断。核10-Q现金、门店、资本政策、可比定义及全价计划；官方Q1表述与第三方转录线索分开，403正文未采信摘要数字。UBC公开检索未确认目标面板，无登录/采购/外联。

新增E053/E054，54项累计不等于独立研究。完成现金算术、披露边界、行动门槛和最小数据请求；D002/dashboard同步。现金改善不是修复、费用不是节省、分部利润不是ROIC；无投资排名。

下一步转团队授权数据/门槛，不重复搜同源参数。访谈后置，未商业实施。文件、快照、算术、类型和构建验证不代表因果。原入口存R018-before。
''')
web=r.parent/'strategy-web'
for n in ['scripts/sync-research.py','scripts/check-research.py','app/page.tsx']:
 p=web/n;s=p.read_text(encoding='utf-8').replace('R017','R018').replace('loss-map-R018.md','capital-conversion-R018.md')
 if n.endswith('.py'):s=s.replace('==52','==54')
 else:s=s.replace('国别收入、全球品类与渠道损失，毛利及费用驱动已补核。52项处置；原因与ROI仍未排序。','现金、资本与全价披露边界已核 · 54项处置。转向数据请求和行动门槛，不以缺参数排名。').replace('查看损失地图与费用桥','查看披露边界与行动门槛')
 p.write_text(s,encoding='utf-8',newline='\n')
assert cash['current']['cfo_less_ppe_cash']==312.222
assert cash['current']['after_buybacks_arithmetic']==-382.883
print('R018 complete; cash arithmetic checked')
