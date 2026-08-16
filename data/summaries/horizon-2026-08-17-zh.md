# Horizon 每日速递 - 2026-08-17

> 从 27 条内容中筛选出 18 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：AI、ComfyUI、LLM、MiniMax H3、Acquisitions。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[Anthropic 公开 Claude 系统提示词，引发社区深度分析](https://platform.claude.com/docs/en/release-notes/system-prompts)**
2. **[OpenH3-IR：开源本地复刻 MiniMax H3 的 Context-IR 阶段](https://www.reddit.com/r/comfyui/comments/1vq9q15/openh3ir_an_open_source_selfhosted_take_on/)**
3. **[Stripe 以超 70 亿美元收购 AI 模型路由公司 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [Anthropic 公开 Claude 系统提示词，引发社区深度分析](https://platform.claude.com/docs/en/release-notes/system-prompts)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [Anthropic 公开 Claude 系统提示词，引发社区深度分析](https://platform.claude.com/docs/en/release-notes/system-prompts)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [Stripe 以超 70 亿美元收购 AI 模型路由公司 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：Anthropic 公开 Claude 系统提示词，引发社区深度分析

**关联新闻**: [Anthropic 公开 Claude 系统提示词，引发社区深度分析](https://platform.claude.com/docs/en/release-notes/system-prompts)

**切入角度**: Anthropic 在其平台文档中发布了 Claude 模型使用的系统提示词，让开发者和研究人员罕见地看到指导模型行为的确切指令。社区成员如 Simon Willison 迅速开始追踪各版本之间的变化，例如 Opus 4.8 与 Opus 5 之间的差异。 系统提示词是 LLM 隐藏的行为层，这种透明性帮助开发者理解 Claude 如何解读安全规则、上下文和用户意图。它也引发了关于这类手工指令到底体现真正智能还是仅仅是工程变通方案的讨论。 Simon Willison 基于 git 的追踪公开了详细的提示词差异，包括新增的 Claude Fable 5 和 Claude Mythos 5 等模型引用。一条重要规则是让 Claude 自行验证图像是否存在，而不是轻信提示词中的暗示。

**可延展方向**: 系统提示词是在用户输入之前提供给语言模型的初始指令集，用于定义其行为、角色和约束。与每次对话都会变化的用户提示词不同，系统提示词保持不变，通常由 AI 提供商精心设计。公开它们可以揭示企业如何塑造模型的安全性和可用性行为。

---

### 选题 2：OpenH3-IR：开源本地复刻 MiniMax H3 的 Context-IR 阶段

**关联新闻**: [OpenH3-IR：开源本地复刻 MiniMax H3 的 Context-IR 阶段](https://www.reddit.com/r/comfyui/comments/1vq9q15/openh3ir_an_open_source_selfhosted_take_on/)

**切入角度**: 开发者 ruashots 发布了 OpenH3-IR，这是一套采用 Apache-2.0 协议的开源 ComfyUI 节点套件，把 MiniMax H3 专有的 Context-IR 提示词编写阶段复刻为自托管服务加 LLM 工具链。它的三个节点接收一句普通描述，生成 H3 训练时所用的长结构化文档，并在渲染前检查、修复输出，全程不调用 MiniMax 的服务器。 这很重要，因为 Context-IR 是本地 MiniMax H3 工作流中缺失的一环：MiniMax 开源了模型权重，却把这一提示词编写阶段保留在托管服务中，这很可能是本地 H3 输出比官方演示更“平”的原因。提供一个开源替代方案，OpenH3-IR 能改善 ComfyUI 用户在本地运行 H3 时的结构化提示词生成、素材对齐和渲染保真度。 OpenH3-IR 由三个节点和一个本地服务组成：它需要一个兼容 OpenAI 的接口（本地或远程均可），并且不会调用 MiniMax 的服务器；节点通过 HTTP 通信，因此服务可以放在与 ComfyUI 不同的机器上。它会对自己的输出执行 109 项机械检查，测试集中还包含 MiniMax 官方发布的 H3 示例，并且这些示例必须全部通过；安装方式为 git clone 加 pip install open-h3-ir，且不会向 ComfyUI 的 Python 环境添加额外包。

**可延展方向**: MiniMax H3 是 MiniMax 开源的通用多模态生成模型，能够理解文本、图像、视频和音频的统一上下文。Context-IR 是 MiniMax 的专有接口阶段，它会深度理解多模态素材之间以及与目标结果之间的关系，并在尽量保持用户原始意图的前提下把理解结果转换成结构化、更丰富的提示词，但该能力只通过 MiniMax 的托管服务提供。ComfyUI 是一个开源、基于节点的界面，用于在本地构建和运行扩散模型工作流。OpenH3-IR 的作用就是在本地为 ComfyUI 用户复现这个原本托管的 Context-IR 环节。

---

### 选题 3：Stripe 以超 70 亿美元收购 AI 模型路由公司 OpenRouter

**关联新闻**: [Stripe 以超 70 亿美元收购 AI 模型路由公司 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion)

**切入角度**: Stripe 已同意以超过 70 亿美元收购 OpenRouter，这家 AI 基础设施初创公司提供统一 API，可路由来自数百个大语言模型的请求。据彭博社报道，这笔交易标志着 Stripe 向 AI 模型路由和支付领域的大幅扩张。 这笔收购使 Stripe 有望成为 AI 经济中的关键中介，可能统一处理整个 AI 生态中的 token 使用和 API 调用支付。它可能重塑开发者获取和支付 LLM 的方式，也凸显了支付基础设施与人工智能日益融合的趋势。 据报道，OpenRouter 仅几个月前才以 13 亿美元估值融资，因此约 70 亿美元的退出意味着估值迅速攀升。该交易还可能锁定各大 AI 实验室的大量 AI 支付量——在 OpenAI 本周早些时候将其支付提供商从 Stripe 换成 Adyen 之后，这一点对 Stripe 尤为关键。

**可延展方向**: OpenRouter 是一个提供统一 API 的平台，可访问来自多家提供商的 500 多个 AI 模型，负责 LLM 路由并提供透明定价。LLM 路由是一种分析传入查询并根据复杂度、成本和性能将其引导至最合适模型的技术。Stripe 是一家为网络商务构建 API 的支付公司；这笔收购暗示它希望像以前抽象化支付底层服务一样，为 LLM 建立类似的抽象层。

---

1. [Stripe 以超 70 亿美元收购 AI 模型路由公司 OpenRouter](#item-1) ⭐️ 9.0/10
2. [Anthropic 公开 Claude 系统提示词，引发社区深度分析](#item-2) ⭐️ 8.0/10
3. [为什么 AI 模型故意变笨：转向外部工具与知识库](#item-3) ⭐️ 8.0/10
4. [NIH 终止面向青年临床研究者的关键资助项目](#item-4) ⭐️ 8.0/10
5. [发展中国家工程师为低成本嵌入式领域的 RISC-V 辩护](#item-5) ⭐️ 7.0/10
6. [AI 积分转售经济：闲置 API 额度的灰色市场](#item-6) ⭐️ 7.0/10
7. [Cloudflare 在切换域名服务器时静默注入分析脚本](#item-7) ⭐️ 7.0/10
8. [MiniMax H3 现可通过 MEOW 47 在 ComfyUI 中完全本地运行](#item-8) ⭐️ 7.0/10
9. [OpenH3-IR：开源本地复刻 MiniMax H3 的 Context-IR 阶段](#item-9) ⭐️ 7.0/10
10. [LTX 2.5 全分辨率 ComfyUI 工作流，无需降采样升采样](#item-10) ⭐️ 7.0/10
11. [Buf 宣布为 Protobuf 提供 LSP 支持，引发社区讨论](#item-11) ⭐️ 6.0/10
12. [Firefox iOS 版新增内置广告拦截功能](#item-12) ⭐️ 6.0/10
13. [圣露西核电站 1 号机组因控制棒掉落而手动停堆](#item-13) ⭐️ 6.0/10
14. [卡西欧计算器运行可用的 Telnet BBS](#item-14) ⭐️ 6.0/10
15. [Minimax H3 社区资讯汇总：新 LoRA、节点与工作流技巧](#item-15) ⭐️ 6.0/10
16. [ReDetail 工作流：用 LTX-2.5 在 24GB 显存上放大 MiniMax H3 视频](#item-16) ⭐️ 6.0/10
17. [在 AMD RX 显卡上启用 Comfy Kitchen Attention 可解决 MiniMax H3 生成缓慢的问题](#item-17) ⭐️ 6.0/10
18. [免费工作流：用 MiniMax H3 在 ComfyUI 中复刻 YouTube 视频](#item-18) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Stripe 以超 70 亿美元收购 AI 模型路由公司 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 9.0/10

Stripe 已同意以超过 70 亿美元收购 OpenRouter，这家 AI 基础设施初创公司提供统一 API，可路由来自数百个大语言模型的请求。据彭博社报道，这笔交易标志着 Stripe 向 AI 模型路由和支付领域的大幅扩张。 这笔收购使 Stripe 有望成为 AI 经济中的关键中介，可能统一处理整个 AI 生态中的 token 使用和 API 调用支付。它可能重塑开发者获取和支付 LLM 的方式，也凸显了支付基础设施与人工智能日益融合的趋势。 据报道，OpenRouter 仅几个月前才以 13 亿美元估值融资，因此约 70 亿美元的退出意味着估值迅速攀升。该交易还可能锁定各大 AI 实验室的大量 AI 支付量——在 OpenAI 本周早些时候将其支付提供商从 Stripe 换成 Adyen 之后，这一点对 Stripe 尤为关键。

hackernews · zacharyozer · 8月16日 20:31 · [社区讨论](https://news.ycombinator.com/item?id=49323381)

**背景**: OpenRouter 是一个提供统一 API 的平台，可访问来自多家提供商的 500 多个 AI 模型，负责 LLM 路由并提供透明定价。LLM 路由是一种分析传入查询并根据复杂度、成本和性能将其引导至最合适模型的技术。Stripe 是一家为网络商务构建 API 的支付公司；这笔收购暗示它希望像以前抽象化支付底层服务一样，为 LLM 建立类似的抽象层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://medium.com/intuitively-and-exhaustively-explained/llm-routing-intuitively-and-exhaustively-explained-5b0789fe27aa">LLM Routing — Intuitively and Exhaustively Explained | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者对这笔交易看法不一，有人质疑一个 API 中间商为何能比 Lyft 等老牌公司市值更高，也有人认为这是 Collison 兄弟掌控 LLM 路由层的明智战略布局。还有人推测收购主要是为了在 OpenAI 转投 Adyen 后保住支付量，另有人对 OpenRouter 客户可能受到的影响以及员工能否分享这笔收益表示怀疑。

**标签**: `#AI`, `#Acquisitions`, `#Payments`, `#LLM`, `#Infrastructure`

---

<a id="item-2"></a>
## [Anthropic 公开 Claude 系统提示词，引发社区深度分析](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 在其平台文档中发布了 Claude 模型使用的系统提示词，让开发者和研究人员罕见地看到指导模型行为的确切指令。社区成员如 Simon Willison 迅速开始追踪各版本之间的变化，例如 Opus 4.8 与 Opus 5 之间的差异。 系统提示词是 LLM 隐藏的行为层，这种透明性帮助开发者理解 Claude 如何解读安全规则、上下文和用户意图。它也引发了关于这类手工指令到底体现真正智能还是仅仅是工程变通方案的讨论。 Simon Willison 基于 git 的追踪公开了详细的提示词差异，包括新增的 Claude Fable 5 和 Claude Mythos 5 等模型引用。一条重要规则是让 Claude 自行验证图像是否存在，而不是轻信提示词中的暗示。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示词是在用户输入之前提供给语言模型的初始指令集，用于定义其行为、角色和约束。与每次对话都会变化的用户提示词不同，系统提示词保持不变，通常由 AI 提供商精心设计。公开它们可以揭示企业如何塑造模型的安全性和可用性行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/system_prompt">System prompt - AI Wiki</a></li>
<li><a href="https://ai.miraheze.org/wiki/System_Prompt">System Prompt - Learn AI</a></li>

</ul>
</details>

**社区讨论**: 社区赞赏这种透明性的稀缺性和价值，Simon Willison 创建了 git 历史记录来可视化提示词演变。也有人质疑，像「自行检查图像是否存在」这样的规则是否说明模型缺乏基本常识；另有一条无关评论担忧论坛对负面 AI 报道存在审核偏倚。

**标签**: `#AI`, `#LLM`, `#System Prompts`, `#Claude`, `#Transparency`

---

<a id="item-3"></a>
## [为什么 AI 模型故意变笨：转向外部工具与知识库](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

一篇新博客文章指出，AI 模型越来越被设计为依赖外部工具和可插拔知识库，而不是将事实存储在模型权重中，故意“变笨”以换取灵活性。这一论点引发了关于事实召回、推理和工具使用之间权衡的讨论。 这很重要，因为它挑战了传统的以基准测试为导向的模型智能观点，并可能改变大型语言模型的构建、评估和部署方式。依赖事实召回、幻觉抑制和知识时效性的开发者、研究人员和用户都将受到影响。 文章指出，在事实召回基准测试 SimpleQA 上，领先的 Gemini 2.5 Pro 仍然答错一半问题，并预测未来模型卡可能完全不再列出知识截止日期。评论者还提到 Cactus 的 Needle——一个 14MB 的工具调用 LLM——作为这一趋势的具体例子。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: AI 模型将学到的模式和事实存储在权重中，权重是缩放每个输入特征影响力的数值参数。检索增强生成（RAG）是一种将 LLM 与外部知识库连接以纳入新信息的技术，而工具使用允许模型调用外部 API。这些外部方法以部分记忆知识换取更大的灵活性和时效性，这正是文章讨论的核心矛盾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval-Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://www.geeksforgeeks.org/deep-learning/the-role-of-weights-and-bias-in-neural-networks/">Weights and Bias in Neural Networks - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持肯定态度，但也进行了批判性讨论。一位用户提出了可插拔知识库的想法，让用户自由组合 SwiftUI 或 GIS 等领域；另一位认为文章已经过时，指出 SimpleQA 长期未更新，而 Gemini 2.5 Pro 已是一年半前的模型。还有评论者质疑推理与事实能否真正分离，尤其在推理人类行为时必须以事实为依据。

**标签**: `#AI`, `#LLMs`, `#tool use`, `#knowledge bases`, `#machine learning`

---

<a id="item-4"></a>
## [NIH 终止面向青年临床研究者的关键资助项目](https://www.science.org/content/article/nih-ending-key-grant-budding-clinical-researchers) ⭐️ 8.0/10

美国国立卫生研究院（NIH）宣布将终止一项面向青年临床研究者的重要职业发展资助，即 K 系列奖项（如 K08/K23），该类奖项提供受保护时间和指导性培训。这一决定推翻了一项长期用于培养临床科学家独立研究能力的项目。 这一削减威胁到将实验室发现转化为临床诊疗的临床科学家人才培养链，可能导致美国生物医学研究长期弱化。这也反映出更广泛的经费不稳定问题，正促使早期职业人才离开学术科研领域甚至移居海外。 K08、K23 等 K 系列奖项旨在为医师科学家提供额外的指导性研究经历，之后他们才能申请独立的 R01 经费。在 NIH 经费动荡的背景下终止该计划，许多实验室已被撤资，整条研究方向被搁置。

hackernews · brandonb · 8月16日 16:14 · [社区讨论](https://news.ycombinator.com/item?id=49321353)

**背景**: 美国国立卫生研究院的职业发展奖（通常称为 K 系列奖项）为青年学者提供薪酬支持和受保护时间，以培养研究技能并最终具备竞争独立 R01 经费的能力。其中 K08 和 K23 专门面向临床科学家，要求其在开展研究项目的同时接受导师指导。T32 等机构培训经费支持大学内的受训者群体，而 K 系列奖项则是面向早期研究人员的个人职业发展经费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.niaid.nih.gov/grants-contracts/career-development-awards">Research Career Development (K) Awards | NIAID: National Institute of Allergy and Infectious Diseases</a></li>
<li><a href="https://controller.ucsf.edu/how-to-guides/sponsored-research-post-award-administration/nih-career-development-awards-k-awards">NIH Career Development Awards (K Awards) | Controller's Office</a></li>
<li><a href="https://grants.nih.gov/grants/guide/pa-files/PA-24-181.html">PA-24-181: Mentored Clinical Scientist Research Career Development ...</a></li>

</ul>
</details>

**社区讨论**: 评论对削减背后的动机和管理表达了深切担忧：有人认为其目的是刻意削弱美国科学，也有人将其归因于 NIH 的管理无能与混乱。许多人警告称这将造成一代青年人才的流失，博士毕业生和博士后因癌症、阿尔茨海默病、帕金森病等领域的经费枯竭而离开美国或放弃研究。

**标签**: `#NIH`, `#science policy`, `#research funding`, `#clinical research`, `#academia`

---

<a id="item-5"></a>
## [发展中国家工程师为低成本嵌入式领域的 RISC-V 辩护](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

一位来自发展中国家的嵌入式工程师发表博客文章，为 RISC-V 回应名为《RISC-V 他们本应更明智》的批评文章。作者认为，在低成本嵌入式应用中，价格和可获得性比性能更重要。 这一不同视角为 RISC-V 的争论补充了关键观点，该争论往往集中于与 ARM64 的性能比较。它强调发展中国家的成本和供应链现实如何可能推动 RISC-V 的采用，并塑造全球嵌入式生态系统。 作者据称称，将 1 美元的芯片运到他的所在地需要 60 至 200 美元，但又称 RISC-V 提供了‘一种以每个零件 10 美分到达我国的架构’。原批评文章认为，RISC-V 可选的 ISA 造成碎片化，且性能不如 ARM64。

hackernews · Narishma · 8月16日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49321717)

**背景**: RISC-V 是一种开放标准的指令集架构（ISA），任何人都可以免费用于设计处理器，无需支付许可费，因此对低成本硬件很有吸引力。开源硬件运动同样鼓励公开分享设计信息。然而，性能和生态碎片化的问题仍是争论话题。这篇博客文章将焦点放在新兴市场中价格和可获得性如何可能重于技术性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://riscv.org/specifications/ratified/">Ratified Specifications - RISC - V International</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_hardware">Open-source hardware - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多欣赏这一新鲜视角，但一些人指出成本论点中的逻辑矛盾，尤其是高运费与 RISC-V 零件每个十美分到达的说法之间的矛盾。还有人质疑运往尼日利亚或孟加拉国的费用是否真的需要 60 美元，另一些人则认为作者与原批评者讨论的是 RISC-V 的不同方面。

**标签**: `#RISC-V`, `#embedded systems`, `#hardware`, `#developing countries`, `#open-source hardware`

---

<a id="item-6"></a>
## [AI 积分转售经济：闲置 API 额度的灰色市场](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

一篇分析文章探讨了转售未使用 AI API 积分的新兴灰色市场，涵盖将多个账户访问权限集中并转售的中继服务。文章指出，此类交易违反平台服务条款，并带来安全风险。 这很重要，因为它暴露了 AI 生态系统中真实的经济与安全压力：积分可以被套利，而账户盗窃和凭证共享等滥用模式威胁着平台方和用户。它还引发了对模型蒸馏的担忧——转售的访问权可能被用来提取模型行为。 关键案例包括一位 YC Startup School 参与者试图转售 2,500 美元积分，以及 OpenAI 等提供商可通过 IP 地址追踪相关中继账户。文章指出，自动化批量注册账户和转售员工福利是延续数十年的老式滥用模式。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI API 提供商通常会向新用户提供免费或促销积分，这些积分可以被集中起来，或以折扣价中继给第三方。转售这些积分通常违反提供商的服务条款，并带来账户被封禁、数据泄露或被用于模型蒸馏等风险。

**社区讨论**: 评论者承认这一灰色市场存在，但看法不一：有人认为这是真实的积分共享，也有人认为风险被低估，或指出分析遗漏了 linux.do、nodeseek 上规模更大的生态。许多人质疑是否有必要信任第三方中继，而一位用户表示自家平台已经实现了类似功能。

**标签**: `#AI credits`, `#token resale`, `#grey market`, `#API abuse`, `#AI economics`

---

<a id="item-7"></a>
## [Cloudflare 在切换域名服务器时静默注入分析脚本](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

一位用户将域名服务器切换到 Cloudflare 以启用通过自定义子域名提供 R2 存储桶服务，结果发现 Cloudflare 悄悄向其纯 HTML、无 JavaScript 的网站注入了分析脚本片段。他必须在 Analytics 仪表盘中手动添加网站，然后才能关闭该片段以选择退出。 这引发了关于大型 DNS/CDN 提供商默认注入第三方脚本的隐私和透明度担忧，可能影响网站所有者对内容的控制以及用户隐私。此事也引发了对侵入性默认设置的讨论，即此类功能应当默认关闭而非默认开启。 被注入的脚本是从 static.cloudflareinsights.com/beacon.min.js 加载的 module 脚本，包含 integrity 哈希和 data-cf-beacon 属性。一些评论者指出，这种注入可能只发生在 Cloudflare 代理 HTTPS 流量时，而不是域名仅设为 DNS 模式的情况下。

hackernews · stagas · 8月16日 17:49

**背景**: Cloudflare Web Analytics 是一项免费、注重隐私的分析服务，平时无需配置即可使用，但这次事件表明它在域名接入时可能被意外启用。R2 是 Cloudflare 的对象存储服务，以零出口流量费著称，而通过自定义子域名提供 R2 存储桶需要将域名服务器迁移到 Cloudflare。该用户的网站是纯 HTML 页面，因此被注入的脚本格外显眼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/web-analytics/">Cloudflare Web Analytics | Cloudflare</a></li>
<li><a href="https://developers.cloudflare.com/r2/">Overview · Cloudflare R 2 docs</a></li>
<li><a href="https://cloudflareinsights.com/">cloudflareinsights.com</a></li>

</ul>
</details>

**社区讨论**: 评论者建议使用 Content-Security-Policy (CSP) 元标签来阻止被注入的脚本，并引用 Cloudflare 关于 'RUM diaries' 的博客来解释其 Web 分析行为。还有人质疑注入是否仅在 Cloudflare 终止 HTTPS（代理模式）时发生，而仅作 DNS 使用的情况不会出现——多位用户报告称他们的 DNS-only 域名并未启用分析。

**标签**: `#Cloudflare`, `#privacy`, `#analytics`, `#DNS`, `#web development`

---

<a id="item-8"></a>
## [MiniMax H3 现可通过 MEOW 47 在 ComfyUI 中完全本地运行](https://www.reddit.com/r/comfyui/comments/1vq17gu/meow_47_minimax_h3_fully_local_in_comfyui/) ⭐️ 7.0/10

Reddit 用户 u/AxonkaiLab 发布了 MEOW 47，将 MiniMax H3 的完整流程带入 ComfyUI，实现完全本地运行。帖子除整合可用外仅提供少量细节。 这使用户能够完全在自己的硬件上运行先进的多模态视频生成模型，免去 API 费用并提升隐私性。同时，它也将 ComfyUI 的生态扩展到最新的开源视频生成模型之列。 MiniMax H3 是一种通用多模态生成模型，能够理解文本、图像、视频和音频的统一上下文，并可生成最多 15 秒、2K 分辨率的原生立体声视频。Reddit 帖子仅包含标题和链接，未提供技术实现细节和系统要求。

reddit · r/comfyui · /u/AxonkaiLab · 8月16日 16:16

**背景**: ComfyUI 是一款流行的基于节点的界面，用于以可视化方式创建 AI 图像和视频生成工作流，并且可以安装在用户的电脑上本地运行。MiniMax H3 又称 Hailuo 3，是 MiniMax 发布的开源模型，官方 API 支持 768P 和 2K 视频输出以及多张参考图。在 ComfyUI 中完全本地运行 H3，意味着用户可以无需依赖云服务，离线构建和执行生成流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://huggingface.co/Comfy-Org/MiniMax-H3">Comfy-Org/ MiniMax - H 3 · Hugging Face</a></li>
<li><a href="https://www.comflowy.com/preparation-for-study/install">Installing ComfyUI – Comflowy</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#MiniMax`, `#local deployment`, `#AI model`, `#integration`

---

<a id="item-9"></a>
## [OpenH3-IR：开源本地复刻 MiniMax H3 的 Context-IR 阶段](https://www.reddit.com/r/comfyui/comments/1vq9q15/openh3ir_an_open_source_selfhosted_take_on/) ⭐️ 7.0/10

开发者 ruashots 发布了 OpenH3-IR，这是一套采用 Apache-2.0 协议的开源 ComfyUI 节点套件，把 MiniMax H3 专有的 Context-IR 提示词编写阶段复刻为自托管服务加 LLM 工具链。它的三个节点接收一句普通描述，生成 H3 训练时所用的长结构化文档，并在渲染前检查、修复输出，全程不调用 MiniMax 的服务器。 这很重要，因为 Context-IR 是本地 MiniMax H3 工作流中缺失的一环：MiniMax 开源了模型权重，却把这一提示词编写阶段保留在托管服务中，这很可能是本地 H3 输出比官方演示更“平”的原因。提供一个开源替代方案，OpenH3-IR 能改善 ComfyUI 用户在本地运行 H3 时的结构化提示词生成、素材对齐和渲染保真度。 OpenH3-IR 由三个节点和一个本地服务组成：它需要一个兼容 OpenAI 的接口（本地或远程均可），并且不会调用 MiniMax 的服务器；节点通过 HTTP 通信，因此服务可以放在与 ComfyUI 不同的机器上。它会对自己的输出执行 109 项机械检查，测试集中还包含 MiniMax 官方发布的 H3 示例，并且这些示例必须全部通过；安装方式为 git clone 加 pip install open-h3-ir，且不会向 ComfyUI 的 Python 环境添加额外包。

reddit · r/comfyui · /u/ruashots · 8月16日 21:50

**背景**: MiniMax H3 是 MiniMax 开源的通用多模态生成模型，能够理解文本、图像、视频和音频的统一上下文。Context-IR 是 MiniMax 的专有接口阶段，它会深度理解多模态素材之间以及与目标结果之间的关系，并在尽量保持用户原始意图的前提下把理解结果转换成结构化、更丰富的提示词，但该能力只通过 MiniMax 的托管服务提供。ComfyUI 是一个开源、基于节点的界面，用于在本地构建和运行扩散模型工作流。OpenH3-IR 的作用就是在本地为 ComfyUI 用户复现这个原本托管的 Context-IR 环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://platform.minimaxi.com/docs/api-reference/video-generation-v2-h3-context-ir">创建 H3-Context-IR 任务 - MiniMax 开放平台文档中心</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#MiniMax H3`, `#open-source`, `#LLM`, `#image generation`

---

<a id="item-10"></a>
## [LTX 2.5 全分辨率 ComfyUI 工作流，无需降采样升采样](https://www.reddit.com/r/comfyui/comments/1vpxiy8/ltx_25_fullresolution_workflows_no/) ⭐️ 7.0/10

一位 Reddit 用户分享了适用于 LTX 2.5 的改编 ComfyUI 工作流，能以全原生分辨率生成图生视频和文生视频，跳过了官方模板中使用的“降采样—渲染—升采样”流程。这些工作流面向 DGX Spark 等高显存 GPU，并使用 LTX 2.5 的 distilled BF16 版本。 这很重要，因为默认的“降采样—升采样”方法会丢失精细细节，尤其是当视频内容偏离首帧时；全分辨率渲染能在每一帧中保留细节。它为高端 GPU 用户提供了一个实用的方法，通过可直接使用的工作流获得更好的 LTX 2.5 输出质量。 作者报告全分辨率文生视频渲染耗时 8×33 秒=264 秒，而官方降分辨率模板为 8×8 秒+3×33 秒=163 秒。这些工作流同时支持 distilled BF16 和 distilled int8-convrot 版本，作者也提醒用户在 ComfyUI 中运行前先检查下载的 JSON 工作流文件。

reddit · r/comfyui · /u/nickinnov · 8月16日 13:48

**背景**: LTX-2.5 是 Lightricks 推出的开源权重视频生成基础模型，旨在让团队自行构建、微调和部署。ComfyUI 是一个开源、基于节点的界面，用于构建扩散模型工作流，每个节点代表一个模型或操作。“降采样—渲染—升采样”技术通过先以较低分辨率渲染来节省显存，再升采样，但当模型需要生成首帧之外的新内容时会损失细节。NVIDIA DGX Spark 是一台配备统一内存的个人 AI 超级计算机，可在本地运行全分辨率渲染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX-2.5: LTX's Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>

</ul>
</details>

**标签**: `#LTX 2.5`, `#ComfyUI`, `#video generation`, `#workflows`, `#AI`

---

<a id="item-11"></a>
## [Buf 宣布为 Protobuf 提供 LSP 支持，引发社区讨论](https://buf.build/blog/protobuf-lsp) ⭐️ 6.0/10

Buf 在一篇题为“Protobuf 已支持 LSP。不用谢”的博文中宣布为 Protobuf 提供语言服务器协议（LSP）支持。该公告推出了一款新的 Protobuf LSP 实现，但社区成员指出类似工具多年前就已存在。 Protobuf 的 LSP 支持可以通过在 .proto 文件中启用自动补全、跳转定义和实时错误检查等 IDE 功能，显著改善开发者体验。这一公告意义重大，因为 Buf 是 Protobuf 工具生态中的重要参与者，其实现选择可能会影响 Protobuf 语言工具的未来发展。 社区对博文的分析表明，该实现从头重新实现了 Protobuf 解析器，而不是复用现有解析库，可能是因为现有实现存在错误恢复方面的限制。在可获得的内容摘要中，博文本身没有包含技术细节，原始公告发布在 Buf 的网站上。

hackernews · theanonymousone · 8月16日 18:48 · [社区讨论](https://news.ycombinator.com/item?id=49322573)

**背景**: Protocol Buffers（简称 Protobuf）是一种语言中立、平台中立、可扩展的序列化结构化数据的机制，最初由 Google 开发。语言服务器协议（LSP）是一种基于 JSON-RPC 的开放协议，标准化了代码编辑器/IDE 与语言服务器之间的通信，从而支持自动补全、跳转定义等功能。Buf 是一家为 Protocol Buffers（gRPC 和 ConnectRPC 背后的模式语言）构建工具的公司，始于 2019 年，目标是解决使用 Protobuf 时的“痛点”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Language_Server_Protocol">Language Server Protocol - Wikipedia</a></li>
<li><a href="https://protobuf.dev/">Protocol Buffers Documentation</a></li>
<li><a href="https://buf.build/docs/ecosystem/">What is Buf ? - Buf Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍批评这篇博文的语气，“别客气”一词被斥为“莫名傲慢”，还有人觉得公司帖子这么写“着实好笑”。有评论者指出，一个开源的 Protobuf LSP 多年前就已存在；有人质疑从头重新实现解析器的做法；还有人讥讽 Google 总在解决没人遇到的问题；不过也有用户称赞 Buf 让 Protobuf 变得“勉强可用”。

**标签**: `#protobuf`, `#LSP`, `#developer-tools`, `#buf`

---

<a id="item-12"></a>
## [Firefox iOS 版新增内置广告拦截功能](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 6.0/10

Mozilla 已将原生广告拦截功能直接集成到 Firefox iOS 版中，用户无需安装单独的扩展或内容拦截器即可屏蔽广告。 这很重要，因为 iOS 浏览器只能使用 WebKit 内核，桌面版 Firefox 的许多扩展在 iOS 上无法使用；内置拦截器简化了普通用户的广告拦截操作，也强化了 Firefox 的隐私定位。 根据 Mozilla 支持页面，内置拦截器可屏蔽 Google、Bing、DuckDuckGo 等搜索引擎结果页上展示的广告。它基于 Apple 的内容拦截器扩展系统，而非 Firefox 桌面版的扩展框架。

hackernews · pentagrama · 8月16日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49319633)

**背景**: Apple 要求 iOS 上的第三方浏览器必须使用 WebKit 内核，因此 Firefox for iOS 无法使用 Gecko 引擎或支持桌面式扩展。iOS 上的广告拦截通常通过 Apple 的 Content Blocker API 实现，该 API 使用 JSON 规则列表过滤 Safari 及基于 WebKit 的浏览器中的内容。Mozilla 此前已提供单独的 iOS 应用 Firefox Focus，通过同一系统提供广告拦截功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/safariservices/creating-a-content-blocker">Creating a content blocker | Apple Developer Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebKit">WebKit - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，uBlock Origin Lite（Safari 版）和 Firefox Focus 早已提供类似的广告拦截功能，有人认为 uBlock Origin Lite 是 iOS 上最好的广告拦截器。也有人对 Firefox iOS 版仍不支持扩展表示失望，并希望 Gecko 引擎最终能在 iOS 上被允许使用。

**标签**: `#Firefox`, `#iOS`, `#adblocker`, `#browser`, `#privacy`

---

<a id="item-13"></a>
## [圣露西核电站 1 号机组因控制棒掉落而手动停堆](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) ⭐️ 6.0/10

佛罗里达州圣露西核电站 1 号机组因三根控制棒掉入反应堆堆芯而手动停堆。该事件触发了安全响应，并引发了调查。 控制棒掉落虽不常见，却是检验反应堆安全系统的重要事件，凸显了压水堆在控制棒插入时会自动趋向安全的设计特点。此次事件也引发了公众对核安全的关注，尤其在历史上曾发生重大核事故的背景下。 该反应堆是位于佛罗里达州圣露西核电站的压水堆，在控制棒掉落后进行了手动停堆。操作人员将调查原因，美国核管理委员会（NRC）也可能审查该事件；以往也曾发生类似事件，提示根本原因可能涉及程序或电气问题。

hackernews · toomuchtodo · 8月16日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49320856)

**背景**: 控制棒用于吸收中子并控制核反应堆的裂变速率。在压水堆中，控制棒通常悬挂在堆芯上方，若失去电源可依靠重力插入堆芯，起到故障安全（scram）作用。单根控制棒掉落本身并不是事故，但属于需要调查和进行安全审查的运行事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scram">Scram - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shutdown_(nuclear_reactor)">Shutdown (nuclear reactor) - Wikipedia</a></li>
<li><a href="https://explorenuclear.com/control-rods/">Control Rods – How to control a nuclear reactor | Explore Nuclear</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，控制棒掉落是一种已知的事件类型，反应堆的设计本身具有安全性，若一根控制棒完全插入便会进入次临界状态。有人提到 2024 年也发生过类似事件，并推测根本原因可能涉及程序问题与电气故障；还有评论者指出，在没有常见参照物的情况下，核风险的传达并不容易。

**标签**: `#nuclear`, `#safety`, `#reactor`, `#news`, `#engineering`

---

<a id="item-14"></a>
## [卡西欧计算器运行可用的 Telnet BBS](https://ei3lh.eu/2026/08/16/a-true-telnet-bbs-on-a-casio-calculator/) ⭐️ 6.0/10

一位开发者详细介绍了如何在卡西欧计算器上实现一个真正可用的、可通过 telnet 访问的公告板系统（BBS），将这台手持设备变成了网络服务器。该项目展示的是实际运行而非模拟的 BBS。 该项目是一项值得关注的业余成就，它将复古计算与网络技术结合，展示了资源极度受限的硬件仍能提供网络协议服务。尽管其更广泛的实际影响有限，但可能会激发其他人尝试将旧设备用作网络端点。 该 BBS 通过 telnet 协议访问，该协议于 1969 年开发，至今仍在一些特定应用中被用于远程终端访问。文章指出，计算器古怪的字体和颜色组合可能导致显示内容难以阅读，这是一个可用性问题。

hackernews · austinallegro · 8月16日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=49319349)

**背景**: 公告板系统（BBS）是一种通过网络交换消息和文件的计算机或应用程序，在万维网出现之前普及，通常通过电话线访问。Telnet 是一种提供命令行界面、用于与远程设备或服务器通信的协议，常用于远程管理。这个项目将这两种复古技术结合到了通常不用于网络的卡西欧计算器上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogtoexpress.blogspot.com/2016/10/bulletin-board-system-grandfather-of.html">Blog To Express: Bulletin Board System - Grandfather of Facebook</a></li>
<li><a href="https://www.extrahop.com/resources/protocols/telnet">Teletype Network Protocol ( Telnet ) — ExtraHop</a></li>
<li><a href="https://www.geeksforgeeks.org/computer-networks/introduction-to-telnet/">Introduction to TELNET - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极且怀旧，评论者回忆起他们自己的旧设备，如卡西欧 IR-7000 和 FX-730P。一位用户称赞了作者类似日志的写作风格，另一位则批评字体和颜色选择导致界面可读性不佳。

**标签**: `#retrocomputing`, `#telnet`, `#casio`, `#bbs`, `#hacking`

---

<a id="item-15"></a>
## [Minimax H3 社区资讯汇总：新 LoRA、节点与工作流技巧](https://www.reddit.com/r/comfyui/comments/1vq5d5u/a_quick_minimax_h3_news_roundup_16th_august_2026/) ⭐️ 6.0/10

这篇 Reddit 帖子汇总了 ComfyUI 中 Minimax H3 的最新社区工具，包括一个 3D 转写实风格的滑块 LoRA、Ref2VA 工作流中视频参考输入的修复方法、用于加速生成的自定义节点，以及一个减少像素伪影的 Sigma Refiner 节点。 这些社区工具解决了生成速度、参考输入处理和视觉伪影等实际痛点，反映出 ComfyUI 中围绕 Minimax H3 的生态系统正在快速成熟。它们让高级 AI 视频生成对业余爱好者和专业创作者都更加易用和可靠。 值得注意的工具包括：ComfyUI-MiniMaxH3Mod，它将参考文件转换为 .safetensors 以加速 Ref2VA 生成；ComfyUI-OrbitSheets，用于构建角色和场景的转身参考模板；以及 ComfyUI-YCNodes-MiniMax-H3，它在 BasicScheduler 和 SamplerCustomAdvanced 之间添加了 Sigma Refiner 节点。Director 时间轴编辑器现已更新至 0.2.2 版本，并提交了三个主要修复；帖子还推荐使用 Tagscanner 剥离 MP4 文件的元数据，以防泄露提示词。

reddit · r/comfyui · /u/optimisticalish · 8月16日 18:56

**背景**: Minimax H3 是 MiniMax 开发的一款通用多模态生成模型，能够理解和生成文本、图像、视频和音频，并可通过 ComfyUI 本地运行。ComfyUI 是一种基于节点的界面，广泛用于构建和分享 AI 生成工作流。LoRA（低秩适配）是一种轻量级微调技术，通过向模型添加小而可训练的网络层，以极低资源实现对风格或概念的控制。Ref2VA 是 H3 中的参考转视频模式，可接受最多 9 张图片、3 个视频和 3 段音频作为输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/ MiniMax - H 3 · Hugging Face</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://docs.comfy.org/tutorials/video/minimax/minimax-h3">MiniMax H3: ComfyUI Workflow Examples - ComfyUI</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#ComfyUI`, `#Minimax H3`, `#tools`, `#workflows`

---

<a id="item-16"></a>
## [ReDetail 工作流：用 LTX-2.5 在 24GB 显存上放大 MiniMax H3 视频](https://www.reddit.com/r/comfyui/comments/1vpqfye/redetail_upscale_minimax_h3_renders_with_the/) ⭐️ 6.0/10

一个名为 ReDetail 的新工作流利用 LTX-2.5 生成式视频放大模型来提升 MiniMax H3 生成视频的分辨率，提供 ComfyUI 拖放式工作流和 Python 命令行工具，并可通过 GGUF 量化路径在 24GB 及以上显存上运行。 该方案将 MiniMax H3 生成与 LTX-2.5 放大两个开放模型打通，使创作者能在本地消费级显卡上生成更高分辨率的视频，降低了对云服务的依赖，从而降低了高质量 AI 视频后期处理的门槛。 ReDetail v1.1 包含六个图内说明面板（安装、片段准备、尺寸、错误处理），并附带占位首帧图像，同时断开画布链接使输出尺寸真正可设置。通过 GGUF 量化路径实现了 24GB 显存运行要求，LTX-2.5 潜空间放大模型可将像素分辨率翻倍，带来接近 4K 的清晰度。

reddit · r/comfyui · /u/DaLyon92x · 8月16日 07:20

**背景**: MiniMax H3 是一个开放权重的通用全模态生成模型，能在统一上下文中理解文本、图像、视频和音频，并在 Hugging Face 上以两个任务专用检查点的形式发布。LTX-2.5 是 Lightricks 推出的视频生成模型系列，其中的潜空间放大模型（x2）可将视频像素分辨率翻倍。ReDetail 将两者结合，在 ComfyUI（节点式 AI 工作流界面）中把 LTX-2.5 放大模型用作 H3 渲染视频片段的后期处理步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://civitai.com/models/2857731/redetail-ltx-25-generative-video-upscaler-v11-workflow-cli">ReDetail: LTX-2.5 generative video upscaler v1.1 (workflow +CLI) - v1.1 | LTX Video ComfyUI Workflows | Civitai</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://huggingface.co/FenomAI/LTX-2.5-Distilled-GGUF">FenomAI/ LTX - 2 . 5 -Distilled-GGUF · Hugging Face</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#video upscaling`, `#AI video`, `#LTX-2.5`, `#VRAM`

---

<a id="item-17"></a>
## [在 AMD RX 显卡上启用 Comfy Kitchen Attention 可解决 MiniMax H3 生成缓慢的问题](https://www.reddit.com/r/comfyui/comments/1vpxg8l/public_service_announcement_if_youre_getting_slow/) ⭐️ 6.0/10

一位 Reddit 用户报告称，在 AMD RX 7800 XT 上通过 --use-ck-attention 启动参数启用 Comfy Kitchen Attention 后，MiniMax H3 生成 5 秒视频的时间从约 60 分钟缩短至 25 分钟。同时还发现可以移除 --low-vram 选项，进一步将时间降至 15 分钟。 这对 AMD GPU 用户来说是一个很有价值的修复方案，因为 AMD 用户在 NVIDIA 优化的注意力后端（如 Sage Attention）上往往性能不佳。这也说明对于 MiniMax H3 这类开放权重多模态模型，注意力后端的选择会带来巨大差异。 该用户指出，Sage Attention 在 AMD 上几乎没有提速效果，因为它只是被模拟运行而非原生支持。Comfy Kitchen Attention 通过 requirements.txt 安装，也可以作为节点使用；它让工作负载足够稳定，因此不再需要 --low-vram 参数。

reddit · r/comfyui · /u/God_Hand_9764 · 8月16日 13:45

**背景**: MiniMax H3 是一个开放权重的通用全模态生成模型，能在统一上下文中处理文本、图像、视频和音频。ComfyUI 依赖注意力后端实现来加速生成；默认后端可能较慢，而 SageAttention 等热门选项主要针对 NVIDIA CUDA 优化。Comfy Kitchen Attention 是 Sage Attention 的一个替代方案，速度快且精度高，官方计划在后续版本中加入 AMD ROCm 后端支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=xX-1ELc1xLc">Comfy Kitchen Attention : a Sage Attention alternative for... - YouTube</a></li>
<li><a href="https://rocm.blogs.amd.com/software-tools-optimization/comfyui-fa-backends/README.html">Understanding Attention Algorithms and Their Backends for Image and Video Generation — ROCm Blogs</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#AMD`, `#MiniMax H3`, `#Performance`, `#Attention`

---

<a id="item-18"></a>
## [免费工作流：用 MiniMax H3 在 ComfyUI 中复刻 YouTube 视频](https://www.reddit.com/r/comfyui/comments/1vqappc/full_video_recreation_workflow_youtube_to_minimax/) ⭐️ 6.0/10

一位 Reddit 用户分享了一个免费的分步工作流，使用 ComfyUI 中的 MiniMax H3 复刻完整的 YouTube 视频。该流程下载源视频，通过 Google AI Studio 的 Gemini 3.1 Pro Preview 进行转写，然后将生成的提示词输入到 MiniMax H3 节点中。 这使得高质量 AI 视频复刻能以零成本实现，结合了流行的开放工具。它展示了一个创作者和开发者可以立即复制的实用流程，降低了 AI 视频制作的门槛。 转写过程需要使用 Pastebin 上托管的特定系统指令，上传视频后用户需输入“follow your system instructions”。MiniMax H3 支持从文本、图像、视频或音频输入生成长达 15 秒的 2K 视频，并带有原生立体声音频。

reddit · r/comfyui · /u/Important-Apple7422 · 8月16日 22:32

**背景**: ComfyUI 是一个开源的、基于节点的图形界面，主要用于 Stable Diffusion 工作流，是当前最流行的 AI 图像和视频生成前端之一。MiniMax H3 是 MiniMax 推出的开放权重通用多模态模型，可以一次性生成带原生音频的视频。Google AI Studio 是一个基于浏览器的平台，用于使用 Google 的 Gemini 模型进行原型开发，提供免费访问强大 AI 工具的能力。这些工具共同构成了帖子中描述的免费视频复刻流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI - Wikipedia</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H 3 - Open-Weights General-Purpose Multimodal Video... | fal</a></li>
<li><a href="https://www.websitebuilderexpert.com/vibe-coding/google-ai-studio/">Google AI Studio : Features, Costs & Limitations (2026)</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#MiniMax H3`, `#Video Generation`, `#Workflow`, `#AI Video`

---

