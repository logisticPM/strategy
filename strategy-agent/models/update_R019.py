from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
names=['README.md','dashboard.md','economics.md','research-plan.md','decisions/D002-enterprise-strategy.md']
a=r/'runs/R019-before';a.mkdir(exist_ok=False)
for n in names:(a/(n.replace('/','__')+'.txt')).write_bytes((r/n).read_bytes())
def read(n):return (r/n).read_text(encoding='utf-8-sig')
def write(n,s):(r/n).write_text(s,encoding='utf-8',newline='\n')
requests=[
('Q01','FP&A / Americas finance','USA and Canada separately','country, fiscal_month, category, channel','net_sales, full_price_net_sales, markdown_net_sales, returns_value, contribution_costs','最近8季度，优先最近13个月月度','成交修复 vs 品类/渠道暴露','全价/促销定义、税及运费处理、退货所属期间必须明确'),
('Q02','CRM / digital / retail analytics','USA and Canada separately','country, fiscal_month, channel, new_existing_cohort','active_buyers, orders, visits, conversion, units, realized_unit_price, cohort_repeat_rate','同Q01','获客 vs 转化 vs 频次/客单','仅匿名聚合；跨渠道去重；访客与订单归属不能混算'),
('Q03','Retail finance / real estate','USA, Canada and candidate countries separately','country, store_cohort, fiscal_month','opening_expansion_date, area, net_sales, contribution, rent, capex, exit_cost, local_online_effect','最近8季；新店自开店起','修复/改造/开店/关闭','以店龄和面积分组；不把租赁负债与租金现金双扣'),
('Q04','Supply chain / fulfillment finance','USA and Canada separately','country, month, fulfillment_mode','fulfilled_orders, units, fulfillment_cost, return_cost, lead_time, stockout_rate, aged_inventory','最近13个月','供给与配送效率','商品/配送/服务成本边界与Q01一致；缺码定义及观察窗口明确'),
('Q05','Corporate FP&A / project owners','Corporate','project, fiscal_period, cost_type','baseline_spend, committed_spend, avoidable_spend, termination_cost, benefit_dependency','当年及后续承诺期','保留必要投入 vs 定向效率','区分现金/折旧、一次性/持续、沉没/可避免；不是同比费用即节省'),
('Q06','Team library/data access owner','USA and Canada separately','panel, month, category, price_band, brand','market_spend, brand_spend, buyer_count, frequency, coverage, weighting, effective_price_definition','匹配Q01期间','市场变化 vs 品牌份额','先确认已有许可和覆盖；商户卡金额不能冒充SKU价格带')]
intake={'version':'R019','status':'DRAFT NOT SENT; all values null until received','requested_period_end':'2026-08-02 or latest data available by case cutoff','case_cutoff':'2026-10-08','requests':[]}
for ident,owner,geo,grain,fields,period,decision,definition in requests:
 intake['requests'].append(dict(id=ident,suggested_function=owner,confirmed_owner=None,status='未发送/未取得',geography=geo,grain=grain,fields=fields.split(', '),period=period,decision=decision,definition=definition,received_source=None,coverage=None,values=None))
write('models/data-intake-R019.json',json.dumps(intake,ensure_ascii=False,indent=2)+'\n')
doc='''# R019 最小数据请求与战略决策包

2026-11-07。状态：内部草案，未发送、未采购、未开展试验。本轮无新增外部证据。案例截止2026-10-08；后续取得数据须分别记录发生期、公开/可获得日和读取日。延续R016中立框架，不预选产品或场景。

## 1. 可直接转交的数据请求草案

用途：识别美加经营损失的可干预机制，并比较各动作相对现行计划F的净贡献与资本需求。先确认字段是否已有，不要求为本项目重新搭建整套数据系统。仅请求匿名聚合经营数据，不需要姓名、联系方式或客户明细身份。

建议提供最近8季度；若月度拆分困难，先交最近13个月月度或8季同口径汇总，并注明无法提供的维度、原因与最接近替代口径。请附币种/恒汇率方法、财务历、定义、数据来源、覆盖率、缺失项、访问限制及负责解释口径的职能。下表为建议职能，不代表已有联系人或其承诺。

| ID | 建议职能 | 最小字段/粒度 | 要改变的选择 |
|---|---|---|---|
'''
for ident,owner,geo,grain,fields,period,decision,definition in requests:
 doc+=f'| {ident} | {owner} | {geo}；{grain}；{fields} | {decision} |\n'
doc+='''
实际接收状态和定义见[可填写JSON模板](../models/data-intake-R019.json)，所有数值初始为null。不要用0替代未知；没有确认的数据负责人也留null。

第一批优先Q01–Q02的美加总表及Q05项目列表；Q03–Q04用于解释成本和资本；Q06先查是否已有许可。以上是信息顺序，不是投资优先级。如果Q01总额不对账，暂停细分推论。无法提供交叉维度时保留各自边际表，不按比例拼接出虚假交叉表。

## 2. 接收和替代口径规则

| 检查 | 合格标准 | 数据不足时如何处理 |
|---|---|---|
| 时间/币种 | 财务历、截止日及币种明确，区分报告/固定汇率 | 不把月度广义零售与季度Lulu直接算份额；案例后独立层 |
| 总额一致性 | Q01同期间总额与E051/公司披露对账；差异有解释 | 退货归属、税、渠道归属等差异先解决，不“校准”成想要结果 |
| 全价/折扣 | 对交易状态有一致定义，含会员/信用卡优惠处理 | 没有实际定义就不由挂牌价或毛利率推全价率 |
| 顾客与流量 | 匿名队列、新客窗口、去重方法、访问和订单口径明确 | 缺队列则仅报告渠道变化，不推流失率或获客效率 |
| 成本/资本 | 现金、费用、折旧、租赁与营运资金分开 | 缺资本分母不报ROIC；贡献率不能套分部利润率 |
| 市场面板 | 地区、品类、实付价格带、覆盖/权重及品牌一致 | 没有同价分母就不量化市场/份额贡献；公开代理仅作背景 |

## 3. 统一验证卡（可以填写，尚未启动）

每个候选动作必须填写：问题及关联证据 → 目标顾客/业务单元 → 当前计划F → 单一待改变机制 → 对照及分配方式 → 主要结果 → 成本/资本 → 护栏 → 最小值得实现的效果 → 观察期/样本依据 → 停止条件 → 决策负责人。

主要结果优先使用全品牌增量净贡献，含退货与蚕食；点击、喜欢、流量及新品销售是中间指标。门店/地域试验需要处理跨店、线上溢出；不把对照受污染的结果当净增量。若无法随机化，说明匹配与趋势假设及残余偏差。观察期需覆盖退货与合理复购周期，不强行统一30天；样本量由基线波动与经济门槛确定，目前均未知。

| 路线 | 需要区分的机制 | 最关键对照 | 进入投入/停止的条件 |
|---|---|---|---|
| 品牌/获客 | 新客不足还是流量不转化 | 可比地区/人群维持F；控制同期产品/促销 | 净新增贡献覆盖营销及服务成本才扩大；流量增而贡献不增则停止加码 |
| 价格/促销 | 弹性、等待折扣还是价值不足 | 同产品/库存/渠道，独立改变价格变量 | 扣基盘降价损失、退货和渠道迁移仍增贡献；不能只看销量 |
| 产品/供给/购物 | 产品不适配还是缺码/选款障碍 | 先保证最合适现款、正确选码及可得性 | 现款解决则不做新品；产品变更需实际保留与净贡献，不先指定日常裤 |
| 相邻需求 | 真新任务还是替换本品牌购买 | 现款及“不买”、实际竞品，展示质量一致 | 扣蚕食、开发与库存风险后成立；仅偏好或折扣成交不扩大 |
| 门店/国际 | 新增需求还是渠道转移 | 同店龄/区域及当地线上总贡献 | 项目现金回报达资本要求并保品牌；无资本信息不排序国别 |
| 效率/费用 | 可避免浪费还是必要能力 | 维持服务/质量基线的可比业务单元 | 节约扣实施/退出及损失贡献后为正；护栏受损即停 |

## 4. 纯假设算例：门槛如何改变选择

**以下所有输入均为研究者任意设定，单位US$M；不是Lululemon事实、预测、预算或批准门槛。只看同一选定期间的经营贡献，未加入税、资本/营运资金及时间，不能据此算投资ROI。**

- 成交/获客：假设新增固定支出5、增量贡献率25%、另损失原业务贡献1，需要新增净销售24才能达到当期贡献盈亏平衡。若全品牌净增量已包含蚕食，则不可再扣一次1。
- 相邻方案：同样支出5、贡献率25%，但假设蚕食原业务贡献3，则所需项目净销售32。数字不同来自假设，不表示相邻方案天然较差。
- 效率方案：假设节约10、实施费3、损失贡献4，同期净改善3；若执行时间不同须重排现金流，不把这3当永久年节省。
- 降价：假设原净单价100、单位变动成本60，降至95且成本不变、无其他费用，需要单位销量约增加14.29%才能维持原贡献。该算例不估需求弹性，也不建议降价5%。

经营门槛：增量净销售=(新增固定支出+未在净增量中体现的蚕食贡献)/增量贡献率。贡献率须扣增量商品、关税、履约及交易变动费用。现金投资比较另建时序，不能把capex和折旧双扣。

[可复算脚本](../models/decision_gates_R019.py)与[9格敏感性及4个算例](../models/decision-gates-R019.json)保留所有假设。贡献率为非正时，此简单销售增长公式没有有限正向解，需要重新设计经济机制。

## 5. 当前决策与无数据时的交付

保留现行计划F为对照，优先低成本、可逆的数据核实与验证设计；尚不建议增加某项商业预算。wearable fashion及其他新品均按同一门槛处理，不在例子中取得默认位置。

若团队没有目标数据：咨询交付应明确哪些判断由公开事实支撑、哪些选择有条件成立、哪些参数足以反转排序，并展示上述门槛敏感性。不能因为未取得内部数据便把最熟悉的故事选成最佳战略，也不必无限延长检索。下一步实际依赖是团队/客户确认Q01–Q06可用性；本包准备就绪但未发送。访谈、对外请求、采购和商业试验均未启动。
'''
write('sources/decision-pack-R019.md',doc)
write('economics.md',read('economics.md').replace('R011，美元US$M','R019，美元US$M')+'\n## R019 统一行动门槛\n\n[数据与验证包](sources/decision-pack-R019.md)新增获客/成交、价格、相邻需求、效率的显式假设门槛及接收规则。所有算例是研究者输入，不提升为事实或投资排名；模型未覆盖资本/税与时间，因此不是ROI评估。\n')
write('research-plan.md',read('research-plan.md').replace('R018，2026-11-07','R019，2026-11-07')+'\n## R019 当前下一步：填写可用性，不再重复检索\n\n[决策包](sources/decision-pack-R019.md)已完成Q01–Q06字段、建议职能、接收校验、替代口径、验证卡及假设门槛。请求未发送，数据未取得。下一实质输入为团队确认已有数据可用性；无数据时使用条件性决策与敏感性，不伪造最佳方案。\n')
d=read('decisions/D002-enterprise-strategy.md').replace('R018经营诊断版','R019条件决策版');idx=d.index('## R018 当前边界')
d=d[:idx]+'''## R019 当前交付：可执行的验证设计，非已实施策略

Q01–Q06数据请求草案、接收规则与六类行动验证卡已完成；未发送或开展商业试验。四个显式假设算例展示盈亏平衡和反转条件，不形成方案排名。保留F及中立框架，先核数据可用性；缺资料时交付条件性选择，不用故事替代依据。[决策包及计算](../sources/decision-pack-R019.md)。

'''+d[idx:];write('decisions/D002-enterprise-strategy.md',d)
d=read('dashboard.md').replace('更新2026-11-07，R018','更新2026-11-07，R019');idx=d.index('## R018 当前结论')
d=d[:idx]+'''## R019 当前交付：数据请求与行动验证包

6组数据请求、接收检查、6类行动验证卡，以及4个纯假设门槛算例已备妥。**未发送请求、未取得新数据、未开展商业试验。** 不把示例门槛或现行研究优先级当投资排名。

下一实质输入是团队确认可用数据；缺数据时采用条件性决策与敏感性，停止重复同源搜索。[查看可直接使用的决策包](sources/decision-pack-R019.md)。

'''+d[idx:];write('dashboard.md',d)
write('README.md',read('README.md').replace('当前版本R018','当前版本R019')+'\nR019：[最小数据请求与战略决策包](sources/decision-pack-R019.md)，未发送/未实施。\n')
audit=json.loads(read('sources/audit-R018.json'));audit['version']='R019';audit['scope']='R019为数据请求和验证设计，无新增外部证据；54项处置沿用R018。算例全部为假设，不作方案排名。'
write('sources/audit-R019.json',json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
write('runs/R019-decision-pack.md','''# R019 · 2026-11-07

输入：用户同意从公开边界转向最小请求与行动门槛。输出：6组数据请求及null接收模板、口径校验、6类验证卡、4个纯假设算例及9格敏感性。更新经济说明、队列、D002/dashboard和网页；54证据、14假设不变。

所有商业效果输入均为研究者假设，不称事实/预测/ROI；无新外部研究。未发送请求、联系第三方、采购、访谈或启动试验。下一步依赖团队数据可用性；没有数据就条件性决策而非重复搜索。历史入口存R019-before。

验证：门槛脚本算术、快照/引用、类型及网页构建；不等于经济参数有效或策略收益验证。
''')
web=r.parent/'strategy-web'
for n in ['scripts/sync-research.py','scripts/check-research.py','app/page.tsx']:
 p=web/n;s=p.read_text(encoding='utf-8').replace('R018','R019').replace('capital-conversion-R019.md','decision-pack-R019.md')
 if n.endswith('page.tsx'):s=s.replace('现金、资本与全价披露边界已核 · 54项处置。转向数据请求和行动门槛，不以缺参数排名。','数据请求、验证卡及假设门槛已就绪 · 未发送/未实施。54项证据不变，不输出虚假ROI排名。').replace('查看披露边界与行动门槛','查看数据请求与验证卡')
 p.write_text(s,encoding='utf-8',newline='\n')
print('R019 decision pack ready; no external request sent')
