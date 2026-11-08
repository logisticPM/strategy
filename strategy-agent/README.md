# Lululemon 战略研究工作台

## R021 当前选择与比较规则

[最新复核](sources/response-paths-R021.md)及D002优先于R020历史选择。美加经营范围优先；核心产品创新、成交体验、品牌触达并行。低风险执行顺序不等于效果/预算排名；核心创新属于P1，不自动划入P2。仅公开数据边界不变。


## R020 当前范围（优先于下方历史待办）

只用免费公开数据。不得把内部数据、客户/学校权限、付费面板或访谈作为默认下一步；公开不可得就保留未知并给有边界的建议。R019数据请求转历史参考，未发送。按经营问题→价值缺口→竞争行动形成建议顺序；不要把因果不确定等同无法提出任何战略判断。以[本轮综合](sources/public-strategy-synthesis-R020.md)和D002为当前选择。


当前版本R021，2026-11-07。由当前会话执行的轻量工作流，不是后台自动运行服务。

网页入口：[离线战略工作台](../strategy-web/offline/index.html)，使用浏览器打开。[使用与更新说明](../strategy-web/WORKBENCH.md)。网页读取构建时快照；资料更新后需同步重建。用户已授权完整公开至GitHub并启用Pages，目标地址为 https://logisticpm.github.io/strategy/ ，部署结果见R010。

任务是帮助CEO选择盈利增长组合与资源取舍；顾客、产品和社媒研究用于检验这些选择。wearable fashion是一项候选，不是研究预设结论。

## 阅读入口

1. [Dashboard](dashboard.md)：当前判断、变化和缺口。
2. [D002企业决策](decisions/D002-enterprise-strategy.md)：主问题和暂定选择。
3. [经营问题地图](enterprise-diagnosis.md)：规模、增长、利润与已知/未知。
4. [战略组合](strategy-options.md)及[经济模型说明](economics.md)：替代路线、取舍和门槛。
5. [研究优先级](research-plan.md)：按能否改变选择分配研究工作。

追溯：[证据台账](evidence-ledger.md)、[假设](hypotheses.md)、[北美D001](decisions/D001-north-america.md)、[工作规则](AGENTS.md)、[运行提示](run-prompt.md)、[R008记录](runs/R008-enterprise-reset.md)。

## 运行与检查

在项目根目录运行 `python strategy-agent/models/enterprise_economics.py` 生成算术与假设敏感性结果，再运行 `python strategy-agent/check.py` 检查文件、引用与原始资料哈希。它们不验证因果、市场代表性或商业收益。

新来源先入台账，再更新假设、决策与dashboard，保留每轮记录。案例截止2026-10-08；案例后资料单列。公开证据不足时记录缺口，不用推断补数。

R001–R007及原始资料保留；重构前入口快照在 `runs/R008-before/`。全品类深档案采集和访谈均未启动，亦未创建自动监测。

R011已完成[D002证据与假设审计](sources/audit-R011.md)，当前假设表已整合历史修订；网页分开显示审计处置和来源读取状态。

R013：[市场、份额与渠道核查](sources/market-share-R013.md)。

R014：[八季经营序列、竞品与数据可得性](sources/operating-sequence-R014.md)。

R015：[X补充去重与案例后证据](sources/x-supplement-review-R015.md)。

R016：[取消预设方向的研究框架](sources/strategy-reset-R016.md)。日常裤与wearable fashion不再默认优先；历史方案保留作备选。

R017：[经营损失地图与竞争性解释](sources/loss-map-R017.md)。

R018：[成交、资本披露边界与行动门槛](sources/capital-conversion-R018.md)。

R019：[最小数据请求与战略决策包](sources/decision-pack-R019.md)，未发送/未实施。
