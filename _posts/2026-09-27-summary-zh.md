---
layout: default
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> 从 23 条内容中筛选出 6 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：AI agents、DeepSeek、diagramming、Excalidraw、distributed systems。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[Drawgent：可直接在实时 Excalidraw 画布上绘图的编码智能体](https://tangled.org/yanndegat.tngl.sh/drawgent)**
2. **[DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978)**
3. **[Reladraw：可手动控制布局位置的图表语言](https://github.com/reladraw/reladraw)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：Drawgent：可直接在实时 Excalidraw 画布上绘图的编码智能体

**关联新闻**: [Drawgent：可直接在实时 Excalidraw 画布上绘图的编码智能体](https://tangled.org/yanndegat.tngl.sh/drawgent)

**切入角度**: 托管在 Tangled 上的新项目 Drawgent 是一个编码智能体，它不生成图表代码交给人类渲染，而是直接在实时的 Excalidraw 画布上绘图和修改。它的发布在 Hacker News 上引发了 32 条评论的讨论，焦点是人与 AI 协作设计架构时最合适的可视化媒介是什么。 该项目切入正在兴起的“智能体 + 白板”工作流领域，开发者希望 AI 能与自己一起参与架构草图讨论，而不仅仅输出文字。它引发的争论也提供了一个有用信号：在画布 JSON、Mermaid 和纯 HTML 之间，智能体究竟更能驾驭哪种格式。 其新颖性受到限制，因为 Excalidraw 官方已经提供了开源的一方 MCP 端点（mcp.excalidraw.com）以及对应的 GitHub 服务端。评论者还指出，在 Excalidraw 中工作的智能体必须处理大量 JSON，并估算和计算像素坐标与边界框，这是一个反复出现的痛点。

**可延展方向**: Excalidraw 是一款开源的网页虚拟白板与绘图工具，具有标志性的手绘风格，以 MIT 许可证发布，并支持端到端加密的实时协作。MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，用于规范 AI 应用如何连接外部工具、系统和数据源，此后已被 OpenAI、Google DeepMind 等主要厂商采用。

---

### 选题 2：DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱

**关联新闻**: [DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978)

**切入角度**: DeepSeek 发布报告，介绍了名为 DSec（DeepSeek Elastic Compute）的生产级沙箱平台，它通过统一的 SDK 对外提供 FnCall、容器、microVM 和完整虚拟机四种沙箱后端。报告称该平台在 160 台基于 AMD EPYC 的服务器节点上并发运行了 38 万个沙箱。 会写代码并执行代码的 AI agent 需要大量隔离的、短生命周期的执行环境，因此一个经过验证、可扩展到这种规模的弹性沙箱平台直接解决了 agentic AI 系统的一大瓶颈。这也表明 DeepSeek 不只是模型开发者，还在扮演基础设施提供者的角色，其设计选择可能影响其他实验室构建 agent 运行时的方式。 DSec 的核心设计是用统一 SDK 抽象四种隔离层级——FnCall、容器、microVM 和完整虚拟机——让调用方可以按工作负载在启动延迟、隔离强度和资源成本之间做取舍。38 万个沙箱分布在 160 个节点上，平均每节点约 2375 个并发沙箱；此外该论文作者名单极长，还有 31 位作者未能列在页面上。

**可延展方向**: 沙箱是一种隔离的执行环境，让代码在运行的同时无法破坏或窥探宿主机系统；microVM（例如 Firecracker）这类方案可以在接近虚拟机的隔离强度下实现接近容器的启动速度。随着 LLM agent 在工具调用、强化学习训练和评测中越来越多地自己编写并执行代码，平台必须能够并发地创建和销毁成千上万个这样的环境，而不是依赖单一的沙箱运行时。AMD EPYC 是 AMD 的服务器 CPU 产品线，凭借单路高核心数在这类场景中很受青睐，有利于提高沙箱的部署密度并降低成本。

---

### 选题 3：Reladraw：可手动控制布局位置的图表语言

**关联新闻**: [Reladraw：可手动控制布局位置的图表语言](https://github.com/reladraw/reladraw)

**切入角度**: Reladraw 是一门全新的开源图表语言，允许用户以声明式方式定义图表，同时保留对元素摆放位置的精细控制，而不是把布局完全交给自动排版引擎。它已在 GitHub 上发布，提供无需安装的浏览器 Playground、简单的 npm 安装方式，以及可供 Claude 等 AI 代理使用的 skill 技能包来生成图表。 该工具填补了一个真实的空白：Mermaid、Graphviz 等自动布局语言在大型图表或对位置敏感的图表上往往效果不佳，而 Draw.io 等手动编辑器虽然功能强大，但对人来说耗时、对 AI 代理来说难以操作。由于它同时面向人类和代理设计，有望成为 AI 辅助架构与规划工作流中的实用输出格式——在这类场景中，图表生成正逐渐成为关键的沟通对齐手段。 Reladraw 使用 "from: left to: right" 这类相对位置语句，搭配节点（node）与边（edge）声明，并支持样式、主题、背景和分组等构造。它提供可实时编辑、边写边重新求解布局的 Playground，作者还建议将其作为 skill 使用，让代理直接生成图表；不过已有早期用户反馈，某些边界情况（例如为特殊相对位置自动生成曲线箭头）目前处理得还不够智能。

**可延展方向**: 图表即代码（diagram-as-code）工具通常分为两类：一类是以 Mermaid、Graphviz 为代表的自动布局语言，你只描述结构、由引擎决定位置；另一类是 Draw.io 等图形编辑器，每个元素都要手动摆放。Mermaid 在 Markdown 和文档流水线中应用极广，但以对流程图位置控制差而闻名。讨论中提到的 C4 模型是一种流行的软件架构建模方法，按上下文、容器、组件、代码等不同抽象层级来描述系统。Agent Skills 是可复用的指令包（一个 SKILL.md 文件加上可选的脚本与资源），用来教会 AI 代理完成特定任务，Reladraw 也提供了这样一个 skill，让代理能直接输出合法的图表源码。

---

1. [DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](#item-1) ⭐️ 7.0/10
2. [Reladraw：可手动控制布局位置的图表语言](#item-2) ⭐️ 7.0/10
3. [Drawgent：可直接在实时 Excalidraw 画布上绘图的编码智能体](#item-3) ⭐️ 7.0/10
4. [Haskell 论坛热议：在 LLM 时代如何保持编程乐趣](#item-4) ⭐️ 7.0/10
5. [Conversations 开发者离开 Google Play，免费发布应用](#item-5) ⭐️ 7.0/10
6. [十五年后回望 Apple Cards 的起源故事](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 DSec：160 台 EPYC 节点上并发运行 38 万个沙箱](https://arxiv.org/abs/2609.22978) ⭐️ 7.0/10

DeepSeek 发布报告，介绍了名为 DSec（DeepSeek Elastic Compute）的生产级沙箱平台，它通过统一的 SDK 对外提供 FnCall、容器、microVM 和完整虚拟机四种沙箱后端。报告称该平台在 160 台基于 AMD EPYC 的服务器节点上并发运行了 38 万个沙箱。 会写代码并执行代码的 AI agent 需要大量隔离的、短生命周期的执行环境，因此一个经过验证、可扩展到这种规模的弹性沙箱平台直接解决了 agentic AI 系统的一大瓶颈。这也表明 DeepSeek 不只是模型开发者，还在扮演基础设施提供者的角色，其设计选择可能影响其他实验室构建 agent 运行时的方式。 DSec 的核心设计是用统一 SDK 抽象四种隔离层级——FnCall、容器、microVM 和完整虚拟机——让调用方可以按工作负载在启动延迟、隔离强度和资源成本之间做取舍。38 万个沙箱分布在 160 个节点上，平均每节点约 2375 个并发沙箱；此外该论文作者名单极长，还有 31 位作者未能列在页面上。

hackernews · shenli3514 · 9月26日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=49859112)

**背景**: 沙箱是一种隔离的执行环境，让代码在运行的同时无法破坏或窥探宿主机系统；microVM（例如 Firecracker）这类方案可以在接近虚拟机的隔离强度下实现接近容器的启动速度。随着 LLM agent 在工具调用、强化学习训练和评测中越来越多地自己编写并执行代码，平台必须能够并发地创建和销毁成千上万个这样的环境，而不是依赖单一的沙箱运行时。AMD EPYC 是 AMD 的服务器 CPU 产品线，凭借单路高核心数在这类场景中很受青睐，有利于提高沙箱的部署密度并降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22978">[2609.22978] DeepSeek Elastic Compute (DSec): A Sandbox ...</a></li>
<li><a href="https://arxiv.org/html/2609.22978v1">DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for ...</a></li>
<li><a href="https://medium.com/@mohammedabdelaziz399/deepseek-elastic-compute-dsec-the-overlooked-infrastructure-story-in-the-deepseek-v4-25f5ab94fe36">DeepSeek Elastic Compute (DSec): The Overlooked ... - Medium</a></li>

</ul>
</details>

**社区讨论**: 有评论者对 160 台 EPYC 节点上并发运行 38 万个沙箱的规模感到震惊，直言"太疯狂了"。另一些人则把注意力放在这篇有 131 位作者的论文上，认为把每位员工都列在每篇论文上可能是一种刻意的"资产保护"策略，让竞争对手无法得知该挖谁，也有人打趣这么多作者是如何沟通协作的。还有人推测，同样的能力或许能让 agent 集群以 38 万个并发 agent 发动攻击，也有人发问 DSec 是否本质上就是一种"agent substrate"（agent 底座）。

**标签**: `#DeepSeek`, `#distributed systems`, `#sandboxing`, `#AI infrastructure`, `#scalability`

---

<a id="item-2"></a>
## [Reladraw：可手动控制布局位置的图表语言](https://github.com/reladraw/reladraw) ⭐️ 7.0/10

Reladraw 是一门全新的开源图表语言，允许用户以声明式方式定义图表，同时保留对元素摆放位置的精细控制，而不是把布局完全交给自动排版引擎。它已在 GitHub 上发布，提供无需安装的浏览器 Playground、简单的 npm 安装方式，以及可供 Claude 等 AI 代理使用的 skill 技能包来生成图表。 该工具填补了一个真实的空白：Mermaid、Graphviz 等自动布局语言在大型图表或对位置敏感的图表上往往效果不佳，而 Draw.io 等手动编辑器虽然功能强大，但对人来说耗时、对 AI 代理来说难以操作。由于它同时面向人类和代理设计，有望成为 AI 辅助架构与规划工作流中的实用输出格式——在这类场景中，图表生成正逐渐成为关键的沟通对齐手段。 Reladraw 使用 "from: left to: right" 这类相对位置语句，搭配节点（node）与边（edge）声明，并支持样式、主题、背景和分组等构造。它提供可实时编辑、边写边重新求解布局的 Playground，作者还建议将其作为 skill 使用，让代理直接生成图表；不过已有早期用户反馈，某些边界情况（例如为特殊相对位置自动生成曲线箭头）目前处理得还不够智能。

hackernews · jpwalsh234 · 9月26日 17:10 · [社区讨论](https://news.ycombinator.com/item?id=49858513)

**背景**: 图表即代码（diagram-as-code）工具通常分为两类：一类是以 Mermaid、Graphviz 为代表的自动布局语言，你只描述结构、由引擎决定位置；另一类是 Draw.io 等图形编辑器，每个元素都要手动摆放。Mermaid 在 Markdown 和文档流水线中应用极广，但以对流程图位置控制差而闻名。讨论中提到的 C4 模型是一种流行的软件架构建模方法，按上下文、容器、组件、代码等不同抽象层级来描述系统。Agent Skills 是可复用的指令包（一个 SKILL.md 文件加上可选的脚本与资源），用来教会 AI 代理完成特定任务，Reladraw 也提供了这样一个 skill，让代理能直接输出合法的图表源码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/reladraw/reladraw">GitHub - reladraw/reladraw</a></li>
<li><a href="https://reladraw.github.io/reladraw/">reladraw playground</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview">Agent Skills - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者总体反应热烈，认为 Reladraw 找到了现有方案之间的"甜蜜点"，并指出 Mermaid 适合时序图、甘特图这类固定布局，但在位置至关重要的流程图上表现不佳。最有价值的建议是将语言中的拓扑部分（箭头、分组）与布局关注点解耦，这样它还能充当 C4 图表的布局层；另有用户报告了一个 bug：从左到右的边没有渲染成曲线箭头。多位开发者表示会把它加入自家代理的工具箱，并把图表视为在人类心智模型与 AI 代理之间进行高带宽对齐的手段。

**标签**: `#diagramming`, `#DSL`, `#developer-tools`, `#AI-agents`, `#visualization`

---

<a id="item-3"></a>
## [Drawgent：可直接在实时 Excalidraw 画布上绘图的编码智能体](https://tangled.org/yanndegat.tngl.sh/drawgent) ⭐️ 7.0/10

托管在 Tangled 上的新项目 Drawgent 是一个编码智能体，它不生成图表代码交给人类渲染，而是直接在实时的 Excalidraw 画布上绘图和修改。它的发布在 Hacker News 上引发了 32 条评论的讨论，焦点是人与 AI 协作设计架构时最合适的可视化媒介是什么。 该项目切入正在兴起的“智能体 + 白板”工作流领域，开发者希望 AI 能与自己一起参与架构草图讨论，而不仅仅输出文字。它引发的争论也提供了一个有用信号：在画布 JSON、Mermaid 和纯 HTML 之间，智能体究竟更能驾驭哪种格式。 其新颖性受到限制，因为 Excalidraw 官方已经提供了开源的一方 MCP 端点（mcp.excalidraw.com）以及对应的 GitHub 服务端。评论者还指出，在 Excalidraw 中工作的智能体必须处理大量 JSON，并估算和计算像素坐标与边界框，这是一个反复出现的痛点。

hackernews · parasitid · 9月26日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=49857729)

**背景**: Excalidraw 是一款开源的网页虚拟白板与绘图工具，具有标志性的手绘风格，以 MIT 许可证发布，并支持端到端加密的实时协作。MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，用于规范 AI 应用如何连接外部工具、系统和数据源，此后已被 OpenAI、Google DeepMind 等主要厂商采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Excalidraw">Excalidraw</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://github.com/excalidraw/excalidraw">GitHub - excalidraw/excalidraw: Virtual whiteboard for ... Excalidraw | Online whiteboard collaboration made easy Excalidraw Excalidraw+ | Collaborative workspace made simple Excalidraw | Hand-drawn look & feel • Collaborative • Secure Excalidraw</a></li>

</ul>
</details>

**社区讨论**: 评论者对其新颖性普遍持怀疑态度：seemaze 指出 Excalidraw 本身就有官方一方 MCP 端点和服务端；armanj 则表示现有白板方案都不够理想，最终选择了 Mermaid 并自建了一个 Obsidian 插件。4ndrewl 认为图表的真正价值来自绘制过程中的思考而非成品本身，ramoz 则主张用 HTML 替代 Excalidraw 那套 JSON 与像素几何的负担；brumar 还分享了一个类似的开源项目 whiteboard-agents 供对比参考。

**标签**: `#AI agents`, `#Excalidraw`, `#MCP`, `#diagramming`, `#developer tools`

---

<a id="item-4"></a>
## [Haskell 论坛热议：在 LLM 时代如何保持编程乐趣](https://discourse.haskell.org/t/how-to-keep-enjoying-programming-in-a-world-of-llms/14705) ⭐️ 7.0/10

Haskell Discourse 上一个题为“How to keep enjoying programming in a world of LLMs”的帖子在 Hacker News 上引发高热度讨论，获得约 153 分和 208 条评论。开发者们在其中分享亲身经历，讲述 AI 代码生成如何改变他们与编程这门手艺的关系。这个帖子并没有发布任何工具或研究，而是汇集了关于技能退化、手艺认同感流失，以及对部分人而言编程乐趣反而增加的一手体验。 这场讨论反映出软件行业日益凸显的矛盾：随着 LLM 助手成为标配工具，开发者担心把工作外包给它们会侵蚀让工程既有趣又有价值的深层技能与解题直觉。这些担忧直接关联到一系列持续争论——初级工程师该如何培养、资历该如何评判，以及编程究竟仍是手艺型职业，还是会转向更像操作机器的工作。 有评论者指出，凡是交给 LLM 完成的任务，对应的个人技能往往就会退化；一位开发者（beej71）描述自己突然难以规划一个本该轻而易举的小项目架构。也有人持相反体验，hirvi74 表示 LLM 降低了摩擦，让他终于能着手长期搁置的点子、并使用完全不熟悉的语言和技术栈；同时还有多人抱怨生成的代码常常有 bug，或者要花一整晚去调试一个隐蔽问题。

hackernews · signa11 · 9月26日 09:41 · [社区讨论](https://news.ycombinator.com/item?id=49854875)

**背景**: Haskell 是一门静态类型、纯函数式编程语言，社区规模不大但参与度极高，崇尚数学严谨性与手艺精神，其 Discourse 论坛经常出现偏反思性的非技术讨论。这个帖子处于一场更广泛的行业讨论之中：GitHub Copilot、Claude、ChatGPT 等 AI 编程助手已经能根据自然语言提示生成可运行的代码。此处所说的“技能退化”指的是，当工程师把调试、系统设计、阅读陌生代码等任务交给模型后，这些能力因长期不再锻炼而逐渐丧失。

**社区讨论**: 整体情绪褒贬不一。有评论者把这种转变比作老式汽车机械师与现代软件调校汽车的差别——手工工具的手艺让位于打补丁；beej71 警告说，任何交给 LLM 的任务都会导致相应技能退化；Guid_NewGuid 则把这种变化比作流水线厨师的工作被微波炉取代，失去了全部技能表达空间。另一派观点中，hirvi74 认为 LLM 通过降低摩擦让编程更有乐趣，BizarreByte 则指出让编程变得痛苦的其实是工作本身，早在 LLM 出现之前就已如此。

**标签**: `#LLMs`, `#software engineering`, `#developer experience`, `#AI-assisted programming`, `#skill atrophy`

---

<a id="item-5"></a>
## [Conversations 开发者离开 Google Play，免费发布应用](https://gultsch.de/posts/breaking-up-with-google-play/) ⭐️ 7.0/10

开源 Android XMPP 客户端 Conversations 的开发者 Daniel Gultsch 发表了题为《Breaking Up with Google Play》的博文，解释他为何改为在 Google Play 之外分发应用，并免费提供。该博文在 Hacker News 上引发大规模讨论（约 635 分、250 条评论），话题集中在 Play 商店抽成、糟糕的开发者支持以及平台垄断。 这凸显了独立开发者与 Android 应用商店双寡头之间日益加剧的矛盾：开发者愿意为分发付费，却难以接受糟糕的支持与审核体验。如果有更多知名开发者放弃或弱化 Google Play 渠道，用户可能越来越多地依赖第三方商店或侧载，这也会给监管机构和 Google 的守门人政策带来更大压力。 Conversations 是一款基于开放标准、免费开源的 XMPP 客户端；放弃 Play 意味着要依赖 F-Droid 或直接提供 APK 下载等渠道，而在现代 Android 上这需要开启“未知来源”安装并应对 Google 日益升级的警告提示。开发者的不满与其说针对 15% 的抽成，不如说针对 Play 商店缓慢且无用的支持与审核流程。

hackernews · ezst · 9月26日 10:55 · [社区讨论](https://news.ycombinator.com/item?id=49855315)

**背景**: Conversations 是一款基于开放消息标准 XMPP 构建的开源 Android 即时通讯客户端，常被视为坚持开放标准与隐私友好的标杆应用。F-Droid 是只收录自由开源软件的 Android 应用商店，也是 Google Play 之外最主要的替代仓库。侧载（sideloading）指绕过官方商店安装应用，通常通过下载 APK 完成；Google 一直在收紧相关警告与限制，这使得离开 Play 商店会带来触达用户方面的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conversations_(software)">Conversations (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sideloading">Sideloading - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍表示同情，认为只要 Google 提供及时的支持和快速的版本审核，开发者乐意支付 15% 的抽成；问题在于垄断地位让 Google 可以无所顾忌。不少人分享了具体痛点：一位开发者说尝试上架产品一年未果，因为 Google 的手机验证步骤默认有人接听或能收短信来验证支持电话，任何 IVR 系统都会被拒绝；另一位则指出 Play 已从业余爱好者的乐园变成需要营业执照和各类文件的“正经商业平台”，同时不断打压商店之外的安装。总体情绪是对大公司客服的失望，除了在社交媒体上公开喊话，大家并没有找到明确的解决办法。

**标签**: `#Google Play`, `#Android`, `#app-distribution`, `#developer-experience`, `#platform-monopoly`

---

<a id="item-6"></a>
## [十五年后回望 Apple Cards 的起源故事](https://lexontech.org/fifteen-years-later-the-apple-cards-origin-story) ⭐️ 6.0/10

lexontech.org 发表了一篇回顾文章，在 Apple Cards 发布十五年后重新审视这款 2011 年推出的“iPhone 设计、实体卡片寄送”服务。文章因评论区的亲历者补充而更有价值，其中包括 Sincerely 联合创始人 solfox，他描述了当年看到 Apple 发布该功能时那种“被 Sherlocked（被苹果吞掉创意）”的感受。 这场讨论呈现了苹果一贯把第三方应用创意吸收进系统功能的模式，而这种模式至今仍在塑造苹果生态中创业公司的风险。它也说明，即便是一个看起来简单的消费级功能，落地时也需要不寻常的后台物流合作，例如与美国邮政（USPS）谈成特殊的条码扫描安排。 由于苹果不愿在信封上印出可见条码，却又想追踪寄送的每一个环节，苹果与其印刷合作方开发了一种喷涂在信封上的隐形条码，只有在特定紫外光下才能读取，而 USPS 同意在寄出时以及邮件处理中心扫描这些卡片。评论者还指出，真正的凸版印刷（letterpress）传统上追求轻柔的“亲吻式压印（kiss impression）”，而不是 Martha Stewart 所推广的那种深压凹痕效果。

hackernews · ksec · 9月26日 09:13 · [社区讨论](https://news.ycombinator.com/item?id=49854693)

**背景**: Apple Cards 是苹果在 2011 年推出的一项服务，用户可在 iPhone 上设计实体贺卡，再由苹果负责印刷并通过 USPS 寄出；它不应与后来与高盛合作推出的 Apple Card 信用卡混淆。当时 Sincerely 等创业公司已经通过 Postagram 等应用在做“iPhone 下单、实体寄送”的业务。凸版印刷是一种凸版压印技术，把上墨的凸起版面直接压印到纸上，而 USPS 则依靠 Intelligent Mail barcode 等机器可读条码来追踪邮件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_Mail_barcode">Intelligent Mail barcode - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Letterpress_printing">Letterpress printing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Card">Apple Card - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 整体情绪夹杂着怀旧与创业者的无奈：Sincerely 联合创始人回忆当年虽率先做出这一创意，却在被苹果“Sherlocked”时感到又怕又气；另一位评论者则把与 USPS 达成的隐形紫外条码安排视为最精彩的细节。也有人对“创始人主导”的公司持更愤世嫉俗的看法，还有评论者称赞 Cards 的体验极其顺滑、非常“苹果”。

**标签**: `#Apple`, `#product-history`, `#startups`, `#printing`, `#HN-discussion`

---