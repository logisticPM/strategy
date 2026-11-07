# Lululemon Strategy Workbench

UBC Capstone 战略研究工作台，非 lululemon 官方网站。

网页地址：https://logisticpm.github.io/strategy/

五个页面：战略总览、战略组合、经营与经济模型、证据与假设、研究队列。支持证据追溯、筛选、方案比较和经济情景计算。研究结论、管理层解释与假设有不同边界；财务敏感性不构成公司预测。

## 目录

- `strategy-agent/`：研究台账、假设、决策卡、来源记录和历史运行。
- `strategy-web/`：Vinext/React源码、构建快照与离线版本。
- `docs/`：GitHub Pages发布目录，与离线HTML内容一致，无后端依赖。
- 根目录原始文档：研究输入，保留原件。

本仓库经所有者明确授权公开完整研究资料。历史运行记录中的发布阻塞是当时状态；当前发布目标为GitHub Pages，非Sites。

## 更新网页

在仓库根目录运行（Node 24、Python 3.9+）：

```powershell
npm --prefix strategy-web ci
python strategy-web/scripts/sync-research.py
python strategy-web/scripts/check-research.py
node strategy-web/scripts/build-offline.mjs
python strategy-web/scripts/prepare-pages.py
```

最后提交并推送 `main`。Pages使用 `main` 的 `/docs`；本地台账修改不会自动成为已发布内容，需先同步与重新构建。离线入口为 `strategy-web/offline/index.html`。

首屏编辑摘要与指标位于 `strategy-web/app/page.tsx`，研究判断变化时须一并复核。没有自动爬取、后台监测或在线编辑功能。
