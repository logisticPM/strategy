"""One-time R015 reconciliation; raw input and ID/date table created separately."""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
archive=root/'runs/R015-before';archive.mkdir(exist_ok=False)
names=['README.md','dashboard.md','evidence-ledger.md','hypotheses.md','research-plan.md','decisions/D001-north-america.md','decisions/D002-enterprise-strategy.md']
for name in names:(archive/(name.replace('/','__')+'.txt')).write_bytes((root/name).read_bytes())
def read(name):return (root/name).read_text(encoding='utf-8-sig')
def write(name,s):(root/name).write_text(s,encoding='utf-8',newline='\n')
rows=json.loads(read('sources/x-dedup-R015.json'))
# Coding is based on visible primary post text and explicitly inspected profile fields.
codes={
'R01':('加拿大；资料Toronto','明确购买自述；停止购买声明，尚非持续停购观察','重复质量与溢价不符；原帖仍可见。创作者/partners背景保留，不能证明制造缺陷率。'),
'R02':('加拿大；资料Calgary','自称高消费会员并使用旧款；新版购买、停购未确认','与R01同线程；168/128为回忆比较，币种/SKU未核，不计算涨价率。'),
'R03':('未知；沿用R005资料核查','9月下单、错投与不会再订的自述','品牌回复重新查看并邀私信已复读；解决/退款未知，不能写完全不回应。'),
'R04':('未知；沿用R005资料核查','旅行用包一次后申请退货被拒的自述','旅行功能失配加退货摩擦；不证明缺陷、违规或停购。'),
'R05':('未知','穿着外观不满；购买未明确','抓绒裤品牌与宽松Lulu单品关系未确认；不证明Lulu保暖优势。'),
'R06':('未知','二手发现/兴趣，付款未知','报告将找到写成购买；未证明二手成交或新品价格弹性。'),
'R07':('未知；沿用R005资料核查','卫衣购买明确；自认final sale不能退','无实际退货申请结果或停购；不能自动认定缺陷。'),
'R08':('不用于Lulu地区统计','停购自述的品牌归属不明','父帖以Alo为主题，回复未明确点名Lulu；继续排除Lulu流失样本。'),
'R09':('未知','拥有并喜爱；购买时点/价格未知','保留正面喜爱，不证明近期全价复购。'),
'R10':('未知','用已有Define和leggings参加派对的计划','不是已参加、办公需求或新增购买；中性用途。'),
'R11':('未知','购买夹克意向受家庭决策阻碍','阻碍原因未说明，撤销确定预算标签。'),
'R12':('未知','上衣穿反、标签露出自述','使用细节，不证明技术失败或减购。'),
'R13':('未知','自己穿6号；同事订2号为转述','不是自己的合身失败，不支持质量/尺码缺陷。'),
'R14':('加拿大；资料Banff','明确买过首发，喜欢旧logo位置','购买正面和设计变更负面并存，不能简写纯正面。'),
'R16':('未知；本轮资料未显示地点','已有Define试穿后满意；购买信息未知','短引文“firs so well now”；同作者回复“before my first day”提示可能工作关联，但未确认雇主/雇佣，不当独立付费顾客证明。'),
'R17':('美国；资料Baltimore, MD','自述拥有Lulu、UA、Fashion Nova多条leggings','保留多品牌拥有；不能证明替代方向、混穿频率或因存量而少买。父帖“1000”是夸张表达，不作件数。'),
'R18':('未知；本轮资料未显示地点','穿Lulu套装及男友玩笑的自述','“scuba diving”是潜水玩笑，不是Scuba产品线识别；中性，不证明满意或流失。'),
'R19':('未知；本轮资料未显示地点','拥有数条Align、接缝破洞，对近期获得的产品质量不满','原文“is it even worth returning”是退换询问；未发生已确认退货、拒退、停购或转牌。购入日期、批次、使用强度和缺陷原因未知。'),
'R20':('未知；本轮资料未显示地点','穿整套Lulu出门散步自述','中性日常场景，非近期购买、全价意愿或office wear需求。'),
'R21':('未知；本轮资料未显示地点','在Lulu被建议小一码','谁建议、是否试穿/下单及结果未明；不能确定店员、合身失败或负面满意度。'),
'R22':('未知；本轮资料未显示地点','找到自己套装感到高兴','拥有/喜爱；非购物发现或新购买。'),
'R23':('未知；本轮资料未显示地点','他人赠予物品中列Lulu leggings为常用','原文“that subs have gotten me”；保留受赠使用，不当本人付费、价格接受或复购。'),
'R24':('不继续核地区','自称“fake Lululemon set”','排除正品体验。不能推断因价格而买仿品或Lulu销售流失。'),
'R26':('不继续核地区','计划穿Ole Miss卫衣及未注明品牌leggings','LuLu是作者昵称；正文不确认Lululemon，排除。')}
assert len(rows)==24 and sum(r['prior'] for r in rows)==14
for r in rows:
 region,behavior,limit=codes[r['case']]
 r.update(region=region,behavior=behavior,limitations=limit,body_review='2026-11-07浏览器原帖正文已读',time_layer='案例截止日后',excluded=r['case'] in ['R08','R24','R26'],prior_case=('C'+r['case'][1:]) if r['prior'] else None)
write('sources/x-dedup-R015.json',json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
report='''# R015 X补充报告去重与原帖复核

核查2026-11-07；案例截止2026-10-08。输入为[用户补充原件](x-supplement-user-R015.txt)，原件含不采纳的推论；不是已核查台账。逐条ID、UTC及America/Vancouver日期见[机器记录](x-dedup-R015.json)。

## 计数、方法与时间层

最终表38行：12行明确重复、2行缺各自回复链接（R15/R25），剩24个不同帖子ID和24个不同账号。R15/R25不能确认彼此独立，也不能补造为两例。24条中R01–R14与R005的C01–C14逐一重复，只有10条新链接/新账号；不同账号不保证独立真实个人，R01/R02属于同一线程。R006后续结果记录也纳入去重，不重复累计。

本轮在未登录的浏览器逐条读到全部24篇正文及日期；复读R08父帖及R03品牌回复，检查8位新增相关作者和3位已知加拿大作者的公开资料。未登录、未联系作者，未检查照片真实性、收据、付款、批次或缺陷原因。未知地区不凭用户名、语言或运动队推断；公开所在地不是交易所在地。

24条都在2026-10-19至11-07，晚于10月8日。页面显示当地时间与ID推导的Vancouver时间一致，UTC与当地日期可差一天（例如R16、R20）。ID时间仅作一致性检查，正文另经浏览器读取。不得将本轮内容倒灌进案例日前已知证据。

排除R08（品牌归属不明）、R24（自称假货）、R26（未提Lululemon，昵称误收）后，剩21条相关内容，其中13条旧链接、8条新增。**21不是21次购买或21个流失案例；本轮新增8条没有明确停购声明。** 地区明确的相关作者为加拿大3位、美国1位，其余17位未知；不构成地区代表性样本。美国新增R17只有多品牌拥有自述，不能称新增美国流失证据。

前一条聊天中“只能确认ID日期、未成功读正文”只反映当时抽查路径；本轮正文读取已完成。既有14条早在R005已核，本轮补充报告不能把它们包装成新样本。保留此前原始报告，不沿用其中“38独立案例”或“核心驱动更突出”的结论。

## 逐条台账（全部为案例后补充）

表中R编号来自这次输入，不能与Reddit的R编号混用；旧C编号指R005。日期为页面显示的2026年Vancouver时间。

| 本轮原帖／旧记录 | 页面时间 | 地区依据 | 可确认经历 | 处置与边界 |
|---|---|---|---|---|
'''
for r in rows:
 report+=f"| [{r['case']}]({r['url']})／{r['prior_case'] or '新增'} | {r['vancouver'][5:16].replace('T',' ')} | {r['region']} | {r['behavior']} | {r['limitations']} |\n"
report+='''
地区资料：[Toronto](https://x.com/lifewitsonduren)、[Calgary](https://x.com/YYC_Cowtown)、[Banff](https://x.com/dearjohnsummit)、[Baltimore](https://x.com/Toriistoryy_)。原帖未给出交易地，不将所在地当购买市场。

关键上下文：[R08父帖](https://x.com/lifeofbi/status/2117292651913351225)以Alo为主，内含未经本轮核验的财务评论，不纳入财务台账；[R03品牌回应](https://x.com/lululemon/status/2118882258669261087)表示愿进一步查看，不等于问题已解决；[R16同作者回复](https://x.com/moamoa4evr/status/2118565721190088941)未确认雇佣身份。缺链接R15/R25仍待核，未重复搜索价值观主题补数。

## 与既有Reddit和假设的交叉比较

| 问题 | 本轮新增X能支持什么 | 与Reddit对照及不能推导的结论 |
|---|---|---|
| 衣橱饱和 H002 | R17多品牌存量、R22已有套装 | Reddit已有因存量减购和存量多仍买的正反个案；本轮没有“因为够了而少买”，不增加饱和机制确认数 |
| 新鲜感 H001 | 主要新增使用场景，R16合身满意 | 不证明缺少新款是减购原因；旧R14反而喜欢旧设计；不重复算新增支持 |
| 价格 H003 | 受赠、拥有、穿着不提供实付价 | R23不能作价格接受；R24仿品不证明降档购买动机；没有价格弹性或同价转牌证据 |
| 产品 H004 | R19 Align接缝破洞自述；R16合身正面 | 与Reddit使用负面/满意并存；只补产品机制线索，不是北美缺陷率或主因 |
| 购物 H010 | R19仅询问是否值得退换，R21仅尺码建议 | 不是已发生服务失败；R03已有品牌回应仍未证解决；不扩大服务流失数 |
| 日常需求 H005/H012 | R18/R20日常穿用，R23受赠使用 | 说明已有产品被使用，不证明新产品净需求、办公场景、全价复购或扣蚕食贡献 |

Reddit沿用[逐例核查](reddit-review-R004.md)及[R005交叉比较](x-verification-R005.md)，本轮未重读全部Reddit原帖，不合并分母、平台比例或证据家族。检索停止不表示达到理论饱和，更不能声称已覆盖主要流失原因。

## 决策处置

E050作为一项案例后补充核查记录，不把每条轻量帖增设为战略证据票数。H004增加有限个案，H002/H003/H005/H012不升级。D002的P1研究优先和P2待检不变。最有价值的后续字段是明确购买日期、SKU、价格、实际退换结果和后续购买；无法取得时保留未知，不继续用低信息量穿着帖凑数。
'''
write('sources/x-supplement-review-R015.md',report)
ledger=read('evidence-ledger.md').replace('## R014 当前','## R015 当前').replace('[最新核查](sources/operating-sequence-R014.md)','[最新X补充核查](sources/x-supplement-review-R015.md) · [经营序列](sources/operating-sequence-R014.md)').replace('sources/audit-R014.json','sources/audit-R015.json').replace('累计49项均有使用处置；R014新增4项并复核E020，不代表49项原文全部本轮复核','累计50项均有使用处置；R015新增1项案例后补充核查，不代表50项原文全部本轮复核')
ledger+='''
## R015 案例截止日后补充 · 不进入2026-10-08已知证据

### E050 X补充报告去重、使用经历与误收纠正

- 类型／状态：已核查（24篇正文及指定公开资料；只确认自述）；处置：限定。核查2026-11-07；帖子2026-10-19至11-07，全部案例后。
- 家族：各X原帖/线程；其中14条与R005/C01–C14及E033–E038既有基础重叠，不能加权重复。38行仅24个不同链接；10条新链接中2条排除（假货、品牌无关），另有旧R08继续排除。共21条相关内容，非21次购买/流失；新增8条没有明确停购声明。
- R19新增Align接缝破洞自述，但无已退货或停购；R16合身满意；R17多品牌拥有；R23受赠使用。3位加拿大、1位美国为公开所在地自述，交易地未知。其余17位未知；仅明确地区不代表北美样本具有代表性。
- [24条逐例、购买/地区/日期和Reddit比较](sources/x-supplement-review-R015.md) · [机器去重表](sources/x-dedup-R015.json) · [用户原件（含待纠正结论）](sources/x-supplement-user-R015.txt)。不支持原因排序、全价意愿或wearable fashion净收益；R15/R25无独立链接继续待核，不计数。
'''
write('evidence-ledger.md',ledger.rstrip()+'\n')
h=read('hypotheses.md').replace('## R014 当前','## R015 当前').replace('E030/E033/E034有使用与服务自述','E030/E033/E034有使用与服务自述；E050案例后新增Align接缝自述与合身正面')
h+='\nR015：E050全部案例后；24链接中14重复，新增8条相关内容没有明确停购声明。H004仅补有限个案；使用、拥有、受赠不升级H002饱和、H003价格接受或H005/H012净需求。所有因果判断不变。[核查报告](sources/x-supplement-review-R015.md)。\n'
write('hypotheses.md',h)
for name in ['decisions/D001-north-america.md','decisions/D002-enterprise-strategy.md']:
 s=read(name).replace('R014核查版','R015核查版')
 s+='\n## R015 案例后X补充，不提升建议强度\n\nE050确认24篇正文，其中14篇重复既有记录；新增10篇中假货与品牌无关两篇排除，8篇相关内容无明确停购声明。Align接缝自述增加产品线索；使用、拥有、受赠不证明新增全价需求。地区新增一位美国资料自述作者，但非美国流失个案。全部发表于案例截止日后；不反向解释截至10月8日的可知信息。P1研究优先、P2待检及各原因不排序的判断不变。[逐例与边界](../sources/x-supplement-review-R015.md)。\n'
 write(name,s)
d=read('dashboard.md').replace('更新2026-11-07，R014','更新2026-11-07，R015').replace('## R014 当前增量','## R014 经营研究增量')
idx=d.index('## R014 经营研究增量')
d=d[:idx]+'''## R015 案例截止日后观察 · 与核心经营证据分开

X补充38行→24个不同链接→14条旧记录＋10条新链接。全部正文已读；排除新链接中的假货及品牌无关两条后，新增8条相关内容，**没有新增明确停购声明**。旧R08品牌不明仍排除，总计21条相关内容并非21次购买（E050）。

新增Align接缝破洞与合身满意并存；使用/拥有/受赠不等于近期全价购买。公开所在地3位加拿大、1位美国，其余17未知，交易地未确认。帖子均晚于2026-10-08，不进入案例日已知依据。P1研究优先、P2待检不变。[逐条去重、正文与地区核查](sources/x-supplement-review-R015.md)。

'''+d[idx:]
write('dashboard.md',d)
write('README.md',read('README.md').replace('当前版本R014','当前版本R015')+'\nR015：[X补充去重与案例后证据](sources/x-supplement-review-R015.md)。\n')
write('research-plan.md',read('research-plan.md').replace('R014，2026-11-07','R015，2026-11-07')+'\nR015完成本次24条X正文核查和去重，新增8条相关内容；继续停止低信息量扩样。仅跟进能补购买日期/SKU/实付价/已处理结果的公开材料，不主动联系作者。全部案例后单列，不改变企业研究优先级。\n')
a=json.loads(read('sources/audit-R014.json'));a['version']='R015';a['scope']='累计50项处置；R015复读24条X原帖，14条重复，10条新增中2条排除。全部案例后，新增8条相关内容无明确停购声明；不改变原因排序。其余处置沿用前轮。'
a['evidence']['E050']=dict(action='限定',review='R015浏览器逐条读24篇正文及指定资料',reason='案例后补充；14条重复，新增8条相关内容非8次购买/流失。排除假货、品牌无关及旧品牌不明，不支持原因主次或时尚净收益。',family='X原帖/线程；14条与R005重叠',period='案例后：2026-10-19至11-07')
a['hypotheses']['H004']['reason']+=' E050案例后新增Align接缝自述及合身正面，非缺陷率。'
write('sources/audit-R015.json',json.dumps(a,ensure_ascii=False,indent=2)+'\n')
write('sources/x-manifest-R015.json',json.dumps({name:hashlib.sha256((root/'sources'/name).read_bytes()).hexdigest() for name in ['x-supplement-user-R015.txt','x-dedup-R015.json','x-supplement-review-R015.md']},indent=2)+'\n')
write('runs/R015-x-supplement.md','''# R015 · 2026-11-07

输入：用户授权与既有X去重、正文/购买/地区复核、案例后单列并更新台账和dashboard。读取AGENTS和R005/R006。

完成：38行拆为24链接、12重复行、2缺链接；14链接与旧记录重复，10新增。浏览器读取24正文、2关键上下文、11公开资料页；21条相关内容（13旧＋8新），不当购买样本数。病例/个人身份、付款、缺陷率未独立核实。不保存无关个人资料。

变化：新增有限产品与使用线索，纠正假货、昵称误收、受赠和意向编码；E050单列案例后。假设/两张决策卡/dashboard同步；经营序列仍保留。之前聊天抽查未取得正文不覆盖R005核验历史。

未变：四原因无法排序、P1研究优先、P2未验证。停止：不扩搜低信息量穿着帖；R15/R25无回复链接不计数。下一步只跟进实际结果、SKU/价格等高信息字段，访谈继续后置。

验证：同步快照、链接/编号、来源哈希、类型与离线构建；计数断言检查。结构验证不是消费者真实性或因果验证。原始资料保留哈希，变更前文档见R015-before。
''')
web=root.parent/'strategy-web'
for name in ['scripts/sync-research.py','scripts/check-research.py','app/page.tsx']:
 p=web/name;s=p.read_text(encoding='utf-8').replace('R014','R015').replace('operating-sequence-R015.md','x-supplement-review-R015.md')
 if name.endswith('.py'):s=s.replace('==49','==50')
 else:s=s.replace('八季经营趋势、竞品反证与Adanola正文 · 49项处置。同价分母仍缺，P2不升级。','X补充24链接：14重复、8条新增相关内容 · 全部案例后，无新增明确停购声明。').replace('查看季度表与决策变化','查看逐条去重与核查')
 p.write_text(s,encoding='utf-8',newline='\n')
print('R015 updated; 24 links, 14 old, 10 new, 21 relevant, 8 new relevant')
