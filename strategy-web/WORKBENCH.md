# 战略工作台：使用与更新

本地入口：`offline/index.html`，直接用浏览器打开，无需安装或运行服务器。该文件自带研究快照、界面与计算逻辑；外部来源链接仍需要联网。文件包含项目研究，分享此文件相当于分享其内嵌资料。

五个页面：总览、战略组合、经营与经济模型、证据与假设、研究队列。证据编号可点击，分组说明与原帖索引保留；假设详情显示后续修订。台账中未打包的Word/PDF原件显示为“项目本地附件”，不伪造远程下载地址。

## 单一资料来源

`../strategy-agent/` 是研究原件；`data/research.json` 为构建快照，不单独编辑。同步脚本读取文档、台账与模型，保存来源哈希。同步不是后台监测，托管网页也不会自动读取本地文件。

在本目录运行：

```powershell
python scripts/sync-research.py
node node_modules/typescript/bin/tsc --noEmit
node scripts/build-offline.mjs
npm run build
```

首屏标题/编辑摘要在 `app/page.tsx`，研究结论改变时应一并审核；数字敏感性不构成公司预测。托管更新需重新构建并发布，不能只更新本地台账。

## 运行与托管状态

开发预览：`npm run dev`。默认Vinext架构，源代码可继续编辑。

当前用户已明确授权完整网页、研究台账与原文快照公开至 `logisticPM/strategy` 并启用GitHub Pages。发布目录为仓库根目录 `docs/`，由 `python scripts/prepare-pages.py` 从离线HTML生成；Pages读取main分支的/docs。同步、构建后须运行该脚本并提交推送。

之前的私有Sites项目没有上传源码或部署；`.openai/hosting.json`只保留其身份，当前不使用该托管目标。R009中的审批阻塞为历史记录，不代表本次GitHub公开发布授权不足。

无自动爬取、访谈发送、后台任务、账号系统或在线编辑；本轮不改变战略选择。
