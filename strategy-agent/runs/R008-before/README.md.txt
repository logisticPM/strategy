# Lululemon strategy agent 轻量研究工作台

当前设计：[R007产品地图与wearable fashion](runs/R007-product-map-wearable-fashion.md)、[具体方案](sources/product-map-wearable-fashion-R007.md)。38条证据，本轮只增补E007、不新增样本；全品类档案尚未采集完毕。下列旧运行保留作历史。

当前运行：[R006处理结果与竞品路径](runs/R006-outcomes-switching.md)，[详细记录](sources/outcomes-switching-R006.md)。38条证据，X关键投诉最终结果仍未知；新增4个Reddit行为案例。以下R005等为历史入口。

最新运行：[R005 X核验](runs/R005-x-verification.md)，含[X逐条核验与Reddit比较](sources/x-verification-R005.md)。当前36条证据，E032为部分核查/存在冲突。前轮[Reddit逐例台账](sources/reddit-review-R004.md)保留。用户要求先社媒、后访谈。旧版说明保留作基线。

建立日期：2026-11-07，America/Vancouver。版本：v0.2（R002证据复核）。执行方式：由本项目中的 AI 会话读取本目录规则并维护研究文件，无独立模型服务、定时任务或额外 API 配置。

核心问题：哪些顾客在什么场景仍愿为 Lululemon 的哪些价值支付溢价，哪些需求没有满足，怎样以合理成本修复？

## 从这里开始

1. [Dashboard](dashboard.md)：当前判断、价值适配与 assignment 五个视角。
2. [北美增长修复决策卡](decisions/D001-north-america.md)：选项、取舍和改选条件。
3. [证据台账](evidence-ledger.md)：来源、边界和冲突。
4. [假设清单](hypotheses.md)：支持、反证和检验。
5. [第一轮运行](runs/R001-north-america.md)：本轮做了什么及结果。
6. [下一轮研究设计](research-plan.md)：访谈、概念比较和经济性检验。
7. [R002证据复核与判断调整](runs/R002-evidence-review.md)：本次变化；[年报复核笔记](sources/annual-review-R002.md)列数值与页码。
8. [访谈工具包](interviews/README.md)：可编辑Word提纲、单人记录表和使用说明；先试访，再编码。

## 如何调用

在本项目聊天中输入：

> 按 strategy-agent/AGENTS.md 工作。针对 D001，读取我新增的资料，核查其支持的具体主张，更新证据、假设、决策卡和 dashboard，并新增运行记录。说明哪些判断改变、哪些没变。

也可以使用 [运行提示模板](run-prompt.md)。新会话必须先读本目录，不依赖旧聊天记忆。项目根目录 [AGENTS.md](../AGENTS.md) 提供入口。

## 维护方式

- Markdown 文件是当前状态的权威记录，使用稳定 E/H/D/R 编号互相引用。不要为同一结论建立多个独立版本。
- 原始资料不修改；Word 正文抽取位于 sources/，只用于定位观点，不代表排版审阅或第三方事实核验。
- [源文件清单](sources/manifest.json) 保存输入文件哈希，判断后续文件是否变更。
- 本轮官方网页通过在线读取核查，保留链接、定位与核查日；未保存完整网页存档。动态商品页不保证历史时点或当前库存。
- 年报关键经营、战略与分部附注页已在R002视觉核查；核查范围及页码见复核笔记。不是整份审计，未提供的顾客数据仍缺失。
- 案例信息基准为 2026-10-08；后续资料用于补充讨论并显式标记。

## 检查与能力边界

运行 `python strategy-agent/check.py`。只需 Python 标准库；检查本地链接、唯一编号、交叉引用及源文件哈希。它不联网，也不调用模型。

第一轮是现有研究的初始化与一次实际分析运行，不是盲测，不证明 Agent 比普通聊天更好。下次用未参与搭建的新材料，与相同资料条件下的人工结构化表格进行比较；记录核对时间、漏掉的限定、错引与人工修正。
