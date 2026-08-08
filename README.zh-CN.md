# Warren Buffett Deep Agent

<p align="center">
  <img src="./assets/hero.png" alt="Warren Buffett 深度资本配置 Agent — Hall of Fame Studio Agent 002" width="100%">
</p>

<p align="center">
  <a href="./README.md">English</a>
  ·
  <a href="./docs/QUALIFICATION.md">资格边界</a>
  ·
  <a href="./assets/README.md">美术系统</a>
  ·
  <a href="https://github.com/MrMaii/Hall-of-Fame-Studio">Hall of Fame Studio</a>
</p>

<p align="center">
  <img alt="状态：repository-prequalified" src="https://img.shields.io/badge/status-repository--prequalified-7e1f2b?style=flat-square">
  <img alt="12 个专属 Skills" src="https://img.shields.io/badge/dedicated_Skills-12-b99352?style=flat-square">
  <img alt="46 个登记来源" src="https://img.shields.io/badge/registered_sources-46-40362b?style=flat-square">
  <img alt="Apache 2.0" src="https://img.shields.io/badge/license-Apache--2.0-17130f?style=flat-square">
</p>

<p align="center">
  <strong><a href="https://github.com/MrMaii/Hall-of-Fame-Studio">Hall of Fame Studio</a> 的一部分</strong><br>
  开源名人堂中的 Agent 002。
</p>

> 不是名言机器人。不是荐股工具。不是预测市场的神谕。
> 它是一位以证据为基础的**长期所有者与资本配置伙伴**。

这是 Hall of Fame Studio（主仓库名为
[Hall of Fame Studio](https://github.com/MrMaii/Hall-of-Fame-Studio)）中
Warren Buffett Deep Agent 的独立开源发行版。

它把仓促、从众压力和模糊恐惧，转化为四个可检查的问题：我们知道
什么、什么会造成永久损失、什么还能做成可逆选择、资金/时间/注意力的
下一最佳用途是什么。

它不声称复制 Warren Buffett，不代表本人，不知道其当前持仓，也不提供
官方投资意见。

## 发布视觉系统

<p align="center">
  <img src="./assets/teaser.gif" alt="Warren Buffett Agent-002 Archive Plate 动态研究" width="100%">
</p>

这里的公众人物是研究对象；真正发布的产品，是一套关于证据、所有者
视角、机会成本、生存、坦率和修订的决策系统。

整套发布统一采用 **Archive Plate**：3:2 横版深色石材场域、温暖铜金衬线文字、
右侧竖向人物窗、左侧身份排版和克制的档案元数据。成品海报已经包含构图与文字，
媒体脚本只负责保持这套视觉，不再叠加第二套方框或标题。

## 动态演示

<p align="center">
  <img src="./assets/demo.gif" alt="动态演示：Warren Buffett Archive Plate 的克制动态研究" width="100%">
</p>

这段动态研究是确定性制作的，只在保留成品构图的基础上加入克制的档案式移动。
Agent 的判断结构由能力章节和图表说明，不由海报伪装成实时模型录屏。

<p align="center">
  <img src="./assets/diagrams/01-decision-lens.svg" alt="Warren Buffett Agent 决策透镜" width="100%">
</p>

## 三分钟上手

### 1. 安装为 Codex Skill

PowerShell：

```powershell
git clone https://github.com/MrMaii/Warren-Buffett-Agent.git "$env:USERPROFILE\.codex\skills\warren-buffett-agent"
```

macOS / Linux：

```bash
git clone https://github.com/MrMaii/Warren-Buffett-Agent.git ~/.codex/skills/warren-buffett-agent
```

### 2. 从决策开始，不从名人模仿开始

```text
$warren-buffett-agent

我们可以收购一家较小的竞争对手，但会消耗大部分现金。
请把真实商业逻辑与“必须立刻行动”的压力分开：列出永久损失路径、
可逆替代方案，以及这笔资本的下一最佳用途。
```

### 3. 任务明确时，直接索要具名产物

```text
$warren-buffett-agent

使用 $weigh-opportunity-cost。比较扩建销售团队、重做 onboarding 和保留现金。
返回 Opportunity Cost Ledger：赢家、下一最佳方案、可能推翻选择的假设和复核日期。
```

普通聊天使用 0 个硬 Skill；探索默认 0 个；一般任务只使用 1–3 个。
具体证券、大额资金或其他高风险决定，必须补齐有日期的一手资料、下行分析
和适当的人类复核。

## 能力集群：它能帮你做什么

<p align="center">
  <img src="./assets/diagrams/02-capability-clusters.svg" alt="12 个 Skills 组成的四大能力集群" width="100%">
</p>

### A. 看懂企业

判断企业如何真正创造所有者价值；检验护城河究竟来自客户行为还是宣传；
把管理层当作资本受托人而不是演讲者来评估。

| Skill | 什么时候用 | 具名产物 |
|---|---|---|
| [`analyze-business-quality`](./agent/skills/analyze-business-quality/SKILL.md) | 需要现金引擎、增量回报、韧性和再投资跑道 | `Business Quality Dossier` |
| [`map-economic-moat`](./agent/skills/map-economic-moat/SKILL.md) | 品牌、网络效应、转换成本或成本优势需要攻击者测试 | `Moat Map` |
| [`evaluate-management-stewardship`](./agent/skills/evaluate-management-stewardship/SKILL.md) | 需要拆开评估激励、坦率、治理、继任与资本记录 | `Stewardship Dossier` |

### B. 把经济实质转成价值

从会计报告重构 Owner Earnings；用范围而不是装饰性单点估值；把不确定性
转化成明确的价格或交易结构缓冲。

| Skill | 什么时候用 | 具名产物 |
|---|---|---|
| [`normalize-owner-earnings`](./agent/skills/normalize-owner-earnings/SKILL.md) | 利润、营运资本、维持投入和稀释遮住了所有者现金 | `Owner Earnings Bridge` |
| [`estimate-intrinsic-value`](./agent/skills/estimate-intrinsic-value/SKILL.md) | 需要保守/基准/有利三情景与每股桥接 | `Intrinsic Value Range` |
| [`demand-margin-of-safety`](./agent/skills/demand-margin-of-safety/SKILL.md) | 信息不完美时必须选择行动、等待、研究或放弃 | `Margin of Safety Decision` |

### C. 配置资本并保护生存

比较下一美元的所有真实用途；暴露隐藏相关性；找到杠杆、流动性或义务会
迫使团队做坏决定的第一个断点。

| Skill | 什么时候用 | 具名产物 |
|---|---|---|
| [`allocate-capital`](./agent/skills/allocate-capital/SKILL.md) | 再投资、并购、回购、分红、还债和现金同时竞争 | `Capital Allocation Board` |
| [`weigh-opportunity-cost`](./agent/skills/weigh-opportunity-cost/SKILL.md) | 多个好选择争夺资金、时间、注意力或声誉 | `Opportunity Cost Ledger` |
| [`stress-test-downside-and-leverage`](./agent/skills/stress-test-downside-and-leverage/SKILL.md) | 债务到期、契约、流动性和被迫出售路径重要 | `Downside and Leverage Map` |
| [`construct-concentrated-portfolio`](./agent/skills/construct-concentrated-portfolio/SKILL.md) | 研究组合需要高信念，但不能隐藏共同失败模式 | `Portfolio Architecture Memo` |

### D. 知道边界，并像所有者一样沟通

准确说明真正理解什么、还需要研究什么；把坏消息、经济后果、责任和纠正
动作告诉长期伙伴，而不羞辱人或用声望压人。

| Skill | 什么时候用 | 具名产物 |
|---|---|---|
| [`assess-circle-of-competence`](./agent/skills/assess-circle-of-competence/SKILL.md) | 决策依赖团队可能并未真正理解的变量 | `Circle of Competence Gate` |
| [`communicate-with-owner-candor`](./agent/skills/communicate-with-owner-candor/SKILL.md) | 董事会、伙伴或所有者需要事实、错误、责任和纠正 | `Owner Decision Memo` / `Shareholder Letter` / `Board Update` |

## 怎样用得更好

高质量请求应说明：谁是所有者、时间跨度、现实替代方案、约束、已有证据、
不可逆损失和希望获得的产物。

| 弱请求 | 更好的请求 |
|---|---|
| “这只股票好吗？” | “使用截至今天的最新一手披露，画出企业质量、Owner Earnings、毁损路径和推翻论点的证据；不要替我下交易指令。” |
| “巴菲特会怎么做？” | “把这三种现金用途换算到同一所有者单位，给出第一名与下一最佳方案之间的决策差值。” |
| “鼓励我耐心一点。” | “区分只是难受的部分与可能造成永久伤害的部分，再给一个保留选择权的小步骤。” |
| “写一封股东信。” | “先说坏结果；对照原承诺与实际结果；量化经济后果；说明责任、纠正动作与复核日期。” |

<p align="center">
  <img src="./assets/diagrams/03-mode-router.svg" alt="四种对话模式与 Skill 上限" width="100%">
</p>

## 为什么它是 Deep Agent

- 46 个登记来源，使用 documented-real-person 证据类型。
- 56 条原子观察，覆盖不同语境。
- 11 条行为主张，包含反证和运行规则。
- 7 类 human-core 文档：身份、声音、关系、魅力、沟通、心理、行为模式。
- 12 个可调用 Skills；每个都有输入、方法、具名产物、STOP、失败模式、
  安全规则、自检和测试。
- 4 种交互模式，避免金融框架侵入普通聊天和脆弱时刻。
- Buffett 专属质量门：检查伪造回忆、廉价安慰、用能力圈赶走用户、无证据
  确定性、语言错配、不完整财务逻辑和 all-in 建议。

<p align="center">
  <img src="./assets/diagrams/04-quality-loop.svg" alt="人物专属质量门闭环" width="100%">
</p>

可追踪链：

```text
来源 → 原子观察 → 行为主张 → 运行规则 → 测试 → 可观察行为
```

## 接入其他 Agent Host

运行包没有第三方依赖。Host 只需要：

1. 把 [`agent/RUNTIME.md`](./agent/RUNTIME.md) 作为精简运行宪法；
2. 用 [`agent/agent.json`](./agent/agent.json) 为普通任务选择最多 1–3 个 Skills；
3. 只有需要深层整合时才加载 [`agent/AGENT.md`](./agent/AGENT.md) 与行为文档；
4. 发布回答前运行 [`evaluateBehavior`](./agent/runtime/qualityGate.js)，必要时修订一次，
   再发布或返回有边界的 fallback。

```js
import { evaluateBehavior } from './agent/runtime/qualityGate.js';

const violations = evaluateBehavior(userMessage, draftResponse, conversationContext);
if (violations.length > 0) {
  // 修复真正负责的证据、runtime 或 Skill 规则。
}
```

## 验证

运行时验证只需要 Node.js 20+。重建发布素材另需 Python 3 与 Pillow。

```bash
npm run validate
npm run fingerprint
npm test
npm run media:build
```

候选指纹：

```text
sha256:4736e707ef1e4a851cee104822598af6246b9f3a89038a42a261cced898ab448
```

当前状态：**`repository-prequalified`**。它表示仓库门槛通过、可以进入人类
Director qualification；不表示历史人物被复制、收益有保证，或 Director 已记录
`pass`。详见 [资格边界](./docs/QUALIFICATION.md)。

## 主发布海报

<p align="center">
  <img src="./assets/poster.png" alt="Warren Buffett Deep Agent-002 主 Archive Plate" width="640">
</p>

这是统一的 3:2 Archive Plate：深色石材场域、温暖铜金编辑风文字、右侧人物窗、
左侧身份排版和克制档案元数据都已包含在成品图内。脚本会把它原样复制到所有
静态表面，不再添加第二个清晰窗口或标题系统。明确排除股票代码墙、美元雨、
Berkshire 官方视觉、未核实名言和胜利姿态。每项资产的任务和限制见
[美术资产系统](./assets/README.md)。

## 从 Agent 002 到 Hall of Fame Studio

这个仓库是一位 Agent；Hall of Fame Studio 是围绕它建立的机构。

[Hall of Fame Studio](https://github.com/MrMaii/Hall-of-Fame-Studio) 是一个开源、
local-first 的环境：从 Talent Market 招募人物 Agent，在 Persona Chat 中测试，
组成项目团队，并通过 Leader、Reviewer、证据、修订、Flow Graph 与 Proof Map
进行治理。

独立 Agent 可以单独工作；进入 Studio 后，它可以反对产品负责人、评审重资本
方案、把实时事实问题交给专家，再整合成所有者决策，而不是把所有 Agent 压成
同一个通用助手。

<p align="center">
  <a href="https://github.com/MrMaii/Hall-of-Fame-Studio">
    <img src="./assets/diagrams/05-hall-of-fame-network.svg" alt="Warren Buffett Agent 位于 Hall of Fame Studio 网络中" width="100%">
  </a>
</p>

阅读 [Hall of Fame Studio 的完整愿景](./docs/HALL-OF-FAME-STUDIO.md)。

## 金融与身份边界

本软件用于分析、教育和决策支持。它**不是金融建议**，不执行交易，不承诺收益；
缺少相关的一手资料、用户真实义务和适当复核时，不得给出当前买卖结论。

项目与 Warren Buffett、Berkshire Hathaway 无关联，未获其授权或背书。详见
[NOTICE.md](./NOTICE.md)。原创软件、runtime 规则、Skills、测试、文档、图表与
项目制作素材使用 [Apache License 2.0](./LICENSE)；第三方研究来源保留各自权利。
