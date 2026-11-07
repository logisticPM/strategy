"""One-time R014 editorial migration; refuses to overwrite run archive."""
from pathlib import Path
import json, re, hashlib
root=Path(__file__).resolve().parents[1]
archive=root/'runs/R014-before'
archive.mkdir(exist_ok=False)
files=['README.md','evidence-ledger.md','hypotheses.md','dashboard.md','research-plan.md','decisions/D002-enterprise-strategy.md']
for name in files:
    target=archive/(name.replace('/','__')+'.txt')
    target.write_bytes((root/name).read_bytes())
def read(name): return (root/name).read_text(encoding='utf-8-sig')
def write(name,text): (root/name).write_text(text,encoding='utf-8')
report='sources/operating-sequence-R014.md'
ledger=read('evidence-ledger.md')
ledger=ledger.replace('## R013 当前审计规则','## R014 当前审计规则').replace('[最新核查](sources/market-share-R013.md)','[最新核查]('+report+')').replace('sources/audit-R013.json','sources/audit-R014.json').replace('累计45项均有使用处置；R013新增5项，不代表45项原文全部复核','累计49项均有使用处置；R014新增4项并复核E020，不代表49项原文全部本轮复核')
start=ledger.index('### E020 '); end=ledger.index('### E023 ',start)
ledger=ledger[:start]+'''### E020 Adanola FY2026增长与利润

- 类型／状态：已核查（指定财报页）；读取2026-11-07。R014处置：限定；替代R012目录限定，历史记录见R014-before。
- 家族：ADANOLA-ACCOUNTS；Adanola Limited单一主体，截至2026-03-31年度；2026-09-07提交，案例前。官方扫描报表印刷第1、11、23页已查看。收入£101.372M，上年84.508M，约+20%；订单+6%、件数+10%；税前利润£17.203M，上年22.192M，约-23%。未披露地区收入；费用和摊销变化影响利润。不证明北美贡献、时尚因果或净盈利增长。FY25收入水平现已核实，旧FY25增长48%仍隔离。
- [原文、精确值和页码](sources/operating-sequence-R014.md) · [原件](sources/adanola-fy2026-R014.pdf)。

'''+ledger[end:]
entries={
'E046':('八季度经营趋势','LULU各季财报；与既有同季证据重叠','已核查','Q3 FY2024至Q2 FY2026八季度：美洲可比-2%、0%、-2%、-4%、-5%、-1%、-5%、-12%。窗口起点已有压力，中途收窄未维持。53周、一周对齐、墨西哥收购及退款限制比较；不认定历史首个拐点或措施因果效果。'),
'E047':('全球Q2品类与渠道三年截面','LULU-Q2-2025；LULU-Q2-2026','已核查','FY2024/25/26 Q2全球两种收入切面；FY2025各品类均增长，FY2026均降。门店、电商均下降，其他渠道增长。非美加交叉表，非完整八季品类史；不把增长差额当新店贡献。'),
'E048':('Athleta同期收缩反证','GAP-Q1-2026；GAP-Q2-2026','已核查','FY2026 Q1净收入270M、可比-11%；Q2收入264M、同比-12%、可比-12%。北美门店252到251。成熟竞品同样承压，不能独证全市场收缩，也不能只选择增长品牌证明Lulu特有问题。'),
'E049':('交易数据公开可得性边界','EARNEST-PRODUCT；CIRCANA-PRODUCT','部分核查','公开产品说明已读；未取得交易面板、授权或目标价格带/加拿大覆盖证明。Earnest Orion是美国卡交易产品，商户金额不等于SKU价格。Circana通用样本不当服装专属样本。网页版本日未知，只作研究可行性，不作案例消费事实。')}
ledger+='\n## R014 经营序列与研究可行性 · 读取2026-11-07\n\n'
for eid,(title,family,status,body) in entries.items():
    ledger+=f'### {eid} {title}\n\n- 类型／状态：{status}；R014处置：限定。家族：{family}。\n- {body}\n- [来源、期间、定位与使用边界]({report})。财报均在案例前发布；可行性网页版本日期未知。\n\n'
write('evidence-ledger.md',ledger)
h=read('hypotheses.md').replace('## R013 当前','## R014 当前')
h=h.replace('量增不是速度或效果；快反仍可能放大错误','E046库存下降不证明chase改善；量增不是速度或效果')
h=h.replace('E023仍缺同期同价数据；E041反映渠道下降；未证明宏观主因','E048 Athleta也承压；E023仍缺同期同价数据；未证明宏观主因')
h=h.replace('E012规模与E039压力已复核','E012规模、E039压力及E046持续性已复核')
h=h.replace('无净需求、蚕食和贡献基线；优于核心修复未证','E020增长伴随利润下降；无净需求、蚕食和贡献基线；优于核心修复未证')
h+='\nR014：E046–E049及E020正文复核增加经营持续性、竞品反证及数据可得性边界；不验证原因主次、chase因果或时尚净收益。[本轮报告]('+report+')。\n'
write('hypotheses.md',h)
decision=read('decisions/D002-enterprise-strategy.md').replace('R013核查版','R014核查版').replace('E015样本冲突、E020正文未核、E023仍为缺口','E015样本冲突、E020在R012正文未核（R014已核指定页）、E023仍为缺口')
decision+='''
## R014：持续压力、竞争分化与增长质量

E046确认八季窗口起点美洲可比已降，FY2025 Q4收窄后再恶化。提高P1诊断价值，不证明某项修复措施无效，更不直接形成投资排名。E047三个年度Q2截面显示全球多品类与两大渠道受压；美加品类、渠道和客群桥仍缺。

E048 Athleta同期收缩，与On/Technical Apparel增长并存，支持研究细分需求和执行差异；不能将竞品总增长当Lulu流失份额。E020现已核Adanola FY2026正文：收入约+20%，税前利润约-23%，地域未披露。撤去正文未取得的当前限制，但不恢复旧FY25增长48%或“时尚化提高利润”的推论。H005/H012不升级。

E049公开产品说明不是已取得交易数据。下一步先核团队/学校/客户已有权限与覆盖字段；若无同价同地区面板，停止量化市场/份额贡献。P1研究优先、P2待检、P3国家筛选、P4成本驱动核查均保留；无投资排名、采购或商业实施决定。[八季表、竞品和数据请求](../sources/operating-sequence-R014.md)。
'''
write('decisions/D002-enterprise-strategy.md',decision)
d=read('dashboard.md').replace('更新2026-11-07，R013','更新2026-11-07，R014').replace('## R013当前增量','## R013历史增量')
pos=d.index('## 企业经营信号')
d=d[:pos]+'''## R014 当前增量

- **持续性**：八季窗口起点美洲可比已降；FY2025 Q4收窄后，FY2026 Q1/Q2再到-5%/-12%（E046），不能当最近一季新问题。
- **竞争分化**：Athleta Q2收入和可比均-12%（E048）；增长竞品不代表全市场，也不能直接证明Lulu份额流失。
- **增长质量**：Adanola FY2026收入约+20%、税前利润约-23%（E020）；不能以此证明时尚化提高利润。
- **决策不升级**：P1仍仅研究优先；P2净增量未证。交易产品说明不补同价市场分母（E049）。

[八季度表、三年Q2渠道/品类、竞品及可得性清单](sources/operating-sequence-R014.md)。

'''+d[pos:]
write('dashboard.md',d)
r=read('research-plan.md').replace('R013，2026-11-07','R014，2026-11-07').replace('下一轮先完成1–3的公开披露缺口检查，再做4的有限可比表。','R014已补八季核心经营序列、三年Q2品类/渠道及竞品有限可比表；完整八季交叉明细和1–3的内部缺口未完成。').replace('Adanola查FY2026报表正文','Adanola FY2026正文已于R014核指定页，地区未披露')
r+='\nR014优先下一步：核已有数据权限、实际字段和美加覆盖；再决定是否能构造同价面板。完成情况与停止条件见[可得性清单]('+report+')。不再重复搜索Adanola收入或用更多竞品新闻替代交易分母；访谈、采购和供应商联系未执行。\n'
write('research-plan.md',r)
write('README.md',read('README.md').replace('当前版本R013','当前版本R014')+'\nR014：[八季经营序列、竞品与数据可得性]('+report+')。\n')
audit=json.loads(read('sources/audit-R013.json'))
audit['version']='R014'
audit['scope']='累计49项处置；本轮新增4项并取得Adanola正文。八季经营核心序列及有限竞品对照不补同价格带分母，不量化市场/份额归因。旧项沿用前轮处置，不表示本轮重读。'
for value in audit['evidence'].values(): value['review']='沿用此前记录；'+value['review']
audit['evidence']['E020']=dict(action='限定',review='R014重读扫描财报指定页',reason='确认FY2026收入增长约20%、税前利润下降约23%；未披露地区，旧FY25增长48%仍未核，不验证时尚化盈利。',family='ADANOLA-ACCOUNTS',period='案例前；截至2026-03-31年度')
for eid,(title,family,status,body) in entries.items():
    audit['evidence'][eid]=dict(action='限定',review='R014原文核查；'+status,reason=body,family=family,period='网页版本日未知，仅可行性' if eid=='E049' else '案例前；详见本轮期间表')
audit['hypotheses']['H009']['reason']+=' R014 Athleta同期收缩增加竞争分化反证；仍无同价分母。'
audit['hypotheses']['H012']['reason']+=' Adanola增长伴随利润下降，不验证时尚净收益。'
write('sources/audit-R014.json',json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'sources').glob('adanola-*-R014.*')}
write('sources/adanola-manifest-R014.json',json.dumps(hashes,indent=2)+'\n')
write('runs/R014-operating-sequence.md','''# R014 · 2026-11-07

输入：用户同意经营序列、竞品对照和数据可得性检查。案例截止2026-10-08。

完成：E046–E049新增；E020取得扫描报表并核指定页；八季度核心经营表、三个年度Q2品类/渠道、Athleta反证、交易可得性清单。原件及页图保留，哈希见sources/adanola-manifest-R014.json。变更前六份文档见R014-before。

改变：经营压力持续性更清楚；Adanola由目录未核升级到限定财务事实；不能以成长品牌证明时尚高利润。未变：P1仅研究优先，P2不升级，四组合无投资排名。

缺口及停止：公开资料无同价美加市场分母、同客迁移、内部成本和国家队列现金流；完整八季品类/渠道尚未补齐。不量化原因贡献、不无限搜同源新闻。

下一步：核已有授权面板与字段；无权限时明确内部数据请求。不联系供应商、不采购、不开展访谈。网页同步R014后做结构、来源一致性、类型及离线构建检查；这些不构成因果验证。
''')
web=root.parent/'strategy-web'
for name in ['scripts/sync-research.py','scripts/check-research.py','app/page.tsx']:
    p=web/name;s=p.read_text(encoding='utf-8').replace('R013','R014').replace('market-share-R014.md','operating-sequence-R014.md')
    if name.endswith('.py'): s=s.replace('==45','==49')
    else:
        s=s.replace('R014 审计完成','R014 研究更新').replace('新增市场、历史份额与渠道证据 · 45项处置。同价分母仍缺，不量化市场/份额归因。','八季经营趋势、竞品反证与Adanola正文 · 49项处置。同价分母仍缺，P2不升级。').replace('查看处置与撤回清单','查看季度表与决策变化')
    p.write_text(s,encoding='utf-8')
print('R014 canonical edits complete')
