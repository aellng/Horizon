# Horizon 每日速递 - 2026-09-11

> 从 38 条内容中筛选出 17 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：AI/ML、AI ethics、OpenAI、LLM、AI Agents。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[Cognition 发布 SWE-2 编程模型，声称比肩 Fable 5.1 与 GPT-Astra](https://cognition.com/blog/swe-2)**
2. **[More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201)**
3. **[OpenAI 发布托管式 Agents API，提供托管智能体运行时](https://developers.openai.com/api/docs/guides/agents-api/overview)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [Forgejo 16.0.4 修复模板仓库功能中的严重远程代码执行漏洞](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [Shopify 将移动应用从 React Native 迁回 Swift 和 Kotlin 原生开发](https://shopify.engineering/back-to-native)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：Cognition 发布 SWE-2 编程模型，声称比肩 Fable 5.1 与 GPT-Astra

**关联新闻**: [Cognition 发布 SWE-2 编程模型，声称比肩 Fable 5.1 与 GPT-Astra](https://cognition.com/blog/swe-2)

**切入角度**: Cognition 发布了面向编程的新模型 SWE-2，声称其软件工程能力可与 Fable 5.1 和 GPT-Astra 相抗衡。该发布迅速在 Hacker News 上引发关注，评论者指出 SWE-2 并非从零训练，而是在 Kimi K3 基础上进行后训练得到的。 此次发布为拥挤的编程智能体模型赛道再添一名竞争者，也凸显出业界的一种趋势：在能力强大的开放基座模型之上做后训练，即可快速得到领域专精模型。同时它也加剧了一场持续争论——当 DeepSeek 等开放权重的编程模型在基准上接近时，闭源厂商还能否证明自身价值。 最具争议的细节是两项基准之间的巨大分差：据报道 SWE-2 在 Terminal Bench 2.1 上得分 92.8%，但在仅发布两周的 Terminal Bench 4 上只有 27.3%。评论者认为这一差距反映的是模型对新问题的泛化能力，而非它在其调优任务上的真实水平；此外该模型并未开放权重。

**可延展方向**: Cognition 是 AI 软件工程智能体 Devin 背后的公司，此前曾因演示效果与实际表现存在落差而受到质疑。SWE-2 是一个编程专用大模型，即在已有基座模型（此处为开放模型 Kimi K3）之上通过后训练——额外的强化学习与微调——使其适配编程任务。Terminal Bench 这类基准用于衡量模型完成真实命令行与智能体式软件任务的能力，被广泛用于比较编程模型，但也可以通过针对性优化来刷分，这种做法有时被称作“benchmaxxing”（刷榜）。

---

### 选题 2：More questions about whether researchers can trust OpenAI with unpublished math

**关联新闻**: [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201)

**切入角度**: A Hacker News discussion raising concerns about whether OpenAI can be trusted with researchers' unpublished mathematical ideas, touching on attribution, ChatGPT training on shared chats, and the ethics of AI-assisted mathematical discovery.

---

### 选题 3：OpenAI 发布托管式 Agents API，提供托管智能体运行时

**关联新闻**: [OpenAI 发布托管式 Agents API，提供托管智能体运行时](https://developers.openai.com/api/docs/guides/agents-api/overview)

**切入角度**: OpenAI 正式推出托管式 Agents API，开发者可以把自有工具接入由 OpenAI 托管的智能体运行时，从而无需自行搭建和运维智能体循环、工具执行层与沙箱环境。根据官方文档，开发者也可以选择自行托管沙箱环境，而不必使用 OpenAI 提供的托管沙箱。 这是一次针对快速增长的“智能体脚手架（agent harness）”层的平台化布局：与其让开发者在自己机器上运行开源脚手架，OpenAI 提供了一个托管替代方案，从而加深开发者对其技术栈的依赖。对任何正在构建智能体的团队来说都很重要，因为托管运行时带来的便利，也伴随着关于状态持久化、可移植性与供应商锁定的现实问题。 一个值得注意的技术细节是，沙箱层支持自托管，有评论者指出这可能降低在不同供应商之间迁移的门槛。官方文档涵盖了 API 概览与运行环境（沙箱）配置，但公告本身并未明确说明定价、支持的模型以及运行时可移植性的具体程度。

**可延展方向**: 所谓“智能体（agent）”，是指由大模型驱动的循环系统，它可以调用工具、读取文件、执行命令并完成多步操作，而不只是回答单次提示。要让这个循环稳定运行，需要一套“脚手架（harness）”——即编排代码加上能安全执行代码的沙箱——而从零自建是一项相当大的工程投入。其他厂商也已有类似产品，例如 Claude Managed Agents 和 Google Cloud 的 Agent Runtime，它们把底层基础设施抽象掉，让团队只需编写智能体逻辑。所谓“供应商锁定（vendor lock-in）”，指的是迁移到其他厂商所需承担的转换成本，这也是外界对这类全托管产品最主要的批评点。

---

1. [OpenAI’s Navier-Stokes release included a Lean 4 formal proof](#item-1) ⭐️ 9.0/10
2. [Shopify 将移动应用从 React Native 迁回 Swift 和 Kotlin 原生开发](#item-2) ⭐️ 8.0/10
3. [More questions about whether researchers can trust OpenAI with unpublished math](#item-3) ⭐️ 8.0/10
4. [Forgejo 16.0.4 修复模板仓库功能中的严重远程代码执行漏洞](#item-4) ⭐️ 8.0/10
5. [OpenAI 发布托管式 Agents API，提供托管智能体运行时](#item-5) ⭐️ 7.0/10
6. [Cognition 发布 SWE-2 编程模型，声称比肩 Fable 5.1 与 GPT-Astra](#item-6) ⭐️ 7.0/10
7. [NASA 卫星图像处理技术被用于揭示古代岩画](#item-7) ⭐️ 7.0/10
8. [PlanetScale 推出分片 Postgres 产品 Neki](#item-8) ⭐️ 7.0/10
9. [微软将 Rust 列为一级语言](#item-9) ⭐️ 7.0/10
10. [布朗大学报告：大型科技公司正在重塑军工复合体](#item-10) ⭐️ 7.0/10
11. [Raymond Chen 揭秘 Windows XP 如何挑选你的初始用户头像](#item-11) ⭐️ 7.0/10
12. [索尼因 PlayStation 玩家是否真正“拥有”数字游戏而被起诉](#item-12) ⭐️ 7.0/10
13. [H3 RefMods 被誉为 MiniMax H3 参考模型的“轻量 LoRA”，ComfyUI 中广受好评](#item-13) ⭐️ 7.0/10
14. [Qwen-Image-Edit-2511 对比 SenseNova-U1.5-Lite：多参考图像融合实测](#item-14) ⭐️ 7.0/10
15. [个人开发者用单张 GPU 在 3.5 天内从零训练出 2.1 亿参数文生图扩散 Transformer](#item-15) ⭐️ 7.0/10
16. [文章称人类创造力是 AI 时代最后一道持久的护城河](#item-16) ⭐️ 6.0/10
17. [ComfyUI 中的 MiniMax H3：从《星际迷航大战星球大战》同人短片中学到的经验](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI’s Navier-Stokes release included a Lean 4 formal proof](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 9.0/10

OpenAI's Navier-Stokes announcement reportedly includes a Lean 4 formal proof, sparking HN discussion about AI-driven mathematical discovery and proof verification scalability.

hackernews · ibobev · 9月10日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=49650326)

**标签**: `#AI`, `#formal verification`, `#Lean 4`, `#Navier-Stokes`, `#mathematics`

---

<a id="item-2"></a>
## [Shopify 将移动应用从 React Native 迁回 Swift 和 Kotlin 原生开发](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 工程团队发布了一篇详细文章，讲述其旗舰移动应用如何从 React Native 回退到完全原生的代码库——iOS 使用 Swift，Android 使用 Kotlin。该公告在 Hacker News 上获得 748 分和 499 条评论，工程师们围绕跨平台方案的取舍以及 LLM 辅助重写的兴起展开了讨论。 Shopify 是公开采用 React Native 的最知名公司之一，因此它的转向为“大型成熟应用最终需要各平台专属原生团队”的观点增加了分量。此举也反映出更广泛的行业趋势：LLM 代码生成降低了编写平台专属代码的成本，从而削弱了跨平台框架的主要吸引力之一。 社区成员强调，跨 JavaScript、C++ 和原生线程层排查崩溃的代价，往往高于维护两套独立代码库；也有人指出 React Native 的核心吸引力在于让 Web 开发者也能交付移动应用，而当模型能够生成原生 UI 时，这一优势正在缩小。另一些人则提醒不要把这次迁移主要归功于 LLM，因为重写工作在很大程度上早于大规模的 LLM 代码辅助。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的开源 UI 框架，让开发者用一套 JavaScript/React 代码同时运行在 iOS 和 Android 上，Facebook、微软和 Shopify 都曾是它的用户。Swift 是苹果为 iOS 和 macOS 打造的编译型语言，Kotlin 则是 JetBrains 开发的静态类型语言，Google 在 2019 年将其定为 Android 的首选语言。所谓“回归原生”，就是分别用 Swift 和 Kotlin 编写两套直接调用平台 API 的应用，而不再通过共享的 JavaScript 桥接层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin">Kotlin</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向支持离开 React Native：一位 iOS 工程师表示，多年反对共享代码库之后自己感到“非常被认可”，另一位则称用 LLM 智能体配合 Maestro 测试工具，几乎在一夜之间完成了约 15–20 个页面的类似 Swift/Kotlin 迁移。也有人对“LLM 促成迁移”的说法提出质疑，一位主导过中型 React Native 重写的工程师表示，那项工作大部分发生在重度使用 LLM 之前；另有观点认为，对于全新项目而言，如今几乎没有理由再从 React Native 起步。

**标签**: `#react-native`, `#mobile-development`, `#swift`, `#kotlin`, `#cross-platform`

---

<a id="item-3"></a>
## [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A Hacker News discussion raising concerns about whether OpenAI can be trusted with researchers' unpublished mathematical ideas, touching on attribution, ChatGPT training on shared chats, and the ethics of AI-assisted mathematical discovery.

hackernews · pred_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**标签**: `#AI ethics`, `#OpenAI`, `#research attribution`, `#LLM training data`, `#mathematics research`

---

<a id="item-4"></a>
## [Forgejo 16.0.4 修复模板仓库功能中的严重远程代码执行漏洞](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo 发布 16.0.4 版本，修复了影响 16.0.3 及更早版本的严重远程代码执行（RCE）漏洞，该漏洞与从模板仓库生成新仓库时模板展开操作干扰 git 仓库初始化的过程有关。修复补丁对应 PR #14301，旨在阻止模板展开在初始化 git 仓库时产生干扰。 Forgejo 是被广泛使用的自托管 Git 平台（也是 Codeberg 背后的软件），因此这一严重 RCE 漏洞会让许多未打补丁的自托管实例面临服务器被完全攻陷的风险。该事件还重新引发了争论：在攻击者越来越多地借助 AI 寻找漏洞的背景下，项目近期限制 LLM 生成贡献的立场是否会让自身处于劣势。 据社区成员描述，存在漏洞的流程会克隆模板仓库、删除其 .git 文件夹、对 .forgejo/template 中列出的文件执行变量模板展开，然后重新初始化一个新的 git 仓库——其中的模板展开步骤正是漏洞源头。一位 Gitea 项目负责人澄清 Gitea 对本次发布修复的两个问题均免疫，另有一些用户指出，由于 Codeberg 的速率限制，官方发布说明页面一度无法正常访问。

hackernews · weierstass · 9月10日 15:57 · [社区讨论](https://news.ycombinator.com/item?id=49645907)

**背景**: Forgejo 是一款用 Go 编写的跨平台、开源、自托管的“软件锻造厂”（software forge），不仅托管 Git 仓库，还提供问题跟踪、代码审查、Wiki、持续集成等功能；它是社区治理的 Gitea 分支，而 Gitea 本身又是 Gogs 的分支。模板仓库允许用户基于预定义结构快速搭建新项目，Forgejo 对该功能的实现会在初始化新仓库前对模板文件执行变量替换——这正是本次漏洞所涉及的核心机制。远程代码执行属于最严重的漏洞类别之一，因为它可能让攻击者在受影响的服务器上运行任意命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gitea">Gitea</a></li>

</ul>
</details>

**社区讨论**: 评论者澄清了这两项修复内容并确认 Gitea 不受影响，一位 Gitea 项目负责人提醒不要因安全事件而羞辱项目方，因为这会打击漏洞上报的积极性。一条热门讨论则质疑 Forgejo 近期禁止 LLM 生成贡献的做法是否会让项目处于劣势，因为即便维护者不用 AI，攻击者仍会借助 AI 寻找漏洞。

**标签**: `#security`, `#vulnerability`, `#Forgejo`, `#Git`, `#RCE`

---

<a id="item-5"></a>
## [OpenAI 发布托管式 Agents API，提供托管智能体运行时](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 7.0/10

OpenAI 正式推出托管式 Agents API，开发者可以把自有工具接入由 OpenAI 托管的智能体运行时，从而无需自行搭建和运维智能体循环、工具执行层与沙箱环境。根据官方文档，开发者也可以选择自行托管沙箱环境，而不必使用 OpenAI 提供的托管沙箱。 这是一次针对快速增长的“智能体脚手架（agent harness）”层的平台化布局：与其让开发者在自己机器上运行开源脚手架，OpenAI 提供了一个托管替代方案，从而加深开发者对其技术栈的依赖。对任何正在构建智能体的团队来说都很重要，因为托管运行时带来的便利，也伴随着关于状态持久化、可移植性与供应商锁定的现实问题。 一个值得注意的技术细节是，沙箱层支持自托管，有评论者指出这可能降低在不同供应商之间迁移的门槛。官方文档涵盖了 API 概览与运行环境（沙箱）配置，但公告本身并未明确说明定价、支持的模型以及运行时可移植性的具体程度。

hackernews · aquir · 9月10日 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**背景**: 所谓“智能体（agent）”，是指由大模型驱动的循环系统，它可以调用工具、读取文件、执行命令并完成多步操作，而不只是回答单次提示。要让这个循环稳定运行，需要一套“脚手架（harness）”——即编排代码加上能安全执行代码的沙箱——而从零自建是一项相当大的工程投入。其他厂商也已有类似产品，例如 Claude Managed Agents 和 Google Cloud 的 Agent Runtime，它们把底层基础设施抽象掉，让团队只需编写智能体逻辑。所谓“供应商锁定（vendor lock-in）”，指的是迁移到其他厂商所需承担的转换成本，这也是外界对这类全托管产品最主要的批评点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/managed-agents/overview">Claude Managed Agents overview - Claude Platform Docs</a></li>
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime">Agent Runtime | Gemini Enterprise Agent Platform | Google Cloud ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vendor_lock-in">Vendor lock-in</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：多位评论者欢迎自托管沙箱选项，认为这有助于避免锁定或方便更换供应商，也有人表示在普通 QEMU 虚拟机里运行 Codex 作为个人助手已经非常好用。另一些评论则批评这种推动供应商锁定的做法，并呼吁 OpenAI 把用户付费购买的推理 token 开放出来。一个反复出现的战略判断是，OpenAI 正试图针对大量涌现的开源智能体脚手架构建更持久的护城河，并可能为那些不通过直接 API 暴露的能力做捆绑铺垫。

**标签**: `#OpenAI`, `#AI Agents`, `#API Design`, `#LLM Infrastructure`, `#Vendor Lock-in`

---

<a id="item-6"></a>
## [Cognition 发布 SWE-2 编程模型，声称比肩 Fable 5.1 与 GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition 发布了面向编程的新模型 SWE-2，声称其软件工程能力可与 Fable 5.1 和 GPT-Astra 相抗衡。该发布迅速在 Hacker News 上引发关注，评论者指出 SWE-2 并非从零训练，而是在 Kimi K3 基础上进行后训练得到的。 此次发布为拥挤的编程智能体模型赛道再添一名竞争者，也凸显出业界的一种趋势：在能力强大的开放基座模型之上做后训练，即可快速得到领域专精模型。同时它也加剧了一场持续争论——当 DeepSeek 等开放权重的编程模型在基准上接近时，闭源厂商还能否证明自身价值。 最具争议的细节是两项基准之间的巨大分差：据报道 SWE-2 在 Terminal Bench 2.1 上得分 92.8%，但在仅发布两周的 Terminal Bench 4 上只有 27.3%。评论者认为这一差距反映的是模型对新问题的泛化能力，而非它在其调优任务上的真实水平；此外该模型并未开放权重。

hackernews · seelos · 9月10日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49645443)

**背景**: Cognition 是 AI 软件工程智能体 Devin 背后的公司，此前曾因演示效果与实际表现存在落差而受到质疑。SWE-2 是一个编程专用大模型，即在已有基座模型（此处为开放模型 Kimi K3）之上通过后训练——额外的强化学习与微调——使其适配编程任务。Terminal Bench 这类基准用于衡量模型完成真实命令行与智能体式软件任务的能力，被广泛用于比较编程模型，但也可以通过针对性优化来刷分，这种做法有时被称作“benchmaxxing”（刷榜）。

**社区讨论**: Hacker News 上的整体情绪偏向怀疑：最受关注的是 Terminal Bench 2.1 的 92.8% 与新版 Terminal Bench 4 的 27.3% 之间的差距，被视为基准过拟合的证据。也有人质疑为何要再选一个闭源模型而非 DeepSeek Flash 4.1 等开放替代品，还有人翻出 Cognition 当年被过度炒作的 Devin 演示，并批评 Devin 表现不稳定；不过有评论者承认，若经过强化学习调优的 K3 真能达到 Fable 5 级别的能力，那确实是个值得注意的成果。

**标签**: `#AI/ML`, `#LLM`, `#coding agents`, `#model release`, `#benchmarks`

---

<a id="item-7"></a>
## [NASA 卫星图像处理技术被用于揭示古代岩画](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 7.0/10

NASA 的 Spinoff 技术转移项目报道称，一种名为去相关拉伸（decorrelation stretch）的图像增强算法原本用于提升卫星与行星照片的可读性，如今被应用于考古领域，用以显现肉眼难以察觉的古代岩画与考古图像。 这是 NASA 技术转移的一个典型案例：为行星科学与对地观测而生的工具在文化遗产研究中获得了第二次生命，使考古学家无需接触或破坏遗址，就能探测岩画中微弱的颜料或矿物差异。 去相关拉伸的原理是通过数学方法对图像各颜色通道进行去相关处理并重新分配其方差，从而放大微弱的色彩差异；该算法的经典版本存在数值不稳定的问题，且在线性相关的退化情形下会失效，一些新近的数值方法正试图解决这些问题。

hackernews · gumby · 9月10日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49645437)

**背景**: 去相关拉伸是一种遥感图像增强技术，能够生成色彩对比增强且各通道互不相关的彩色图像，常用于多光谱数据集。NASA 的 Spinoff 项目专门介绍那些为太空任务开发、后被重新用于地面商业或公益产品的技术。遥感考古则是一个成熟的考古学分支，利用机载或星载传感器在不扰动地表的前提下探测古代人类活动的痕迹，例如地下建筑遗迹或岩画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dstretch.com/DecorrelationStretch.pdf">Algorithm Theoretical Basis Document for Decorrelation ...</a></li>
<li><a href="https://www.nasa.gov/space-technology-mission-directorate/technology-transfer-spinoffs/">Technology Transfer and Spinoffs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_sensing_in_archaeology">Remote sensing in archaeology - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者既热情又务实：有人表示假彩色合成是自己理解信号与传感器时的“顿悟”时刻，另一位给出了具体的 GIMP 操作步骤（分解为 LAB、对 A/B 色度通道做自动色阶、再重新合成），还有人分享了自己在吴哥窟用带通滤镜寻找岩画的一手遥感轶事；也有评论者询问是否存在可接入流水线使用的 ImageMagick 实现。

**标签**: `#image-processing`, `#remote-sensing`, `#archaeology`, `#NASA-spinoff`, `#signal-processing`

---

<a id="item-8"></a>
## [PlanetScale 推出分片 Postgres 产品 Neki](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

以 MySQL 分片中间件 Vitess 闻名的 PlanetScale 公司发布了 Neki，这是一款面向 Postgres 水平扩展的全新分片 Postgres 产品。该发布文章在 Hacker News 上引发了 194 分、105 条评论的讨论，批评者指出文章解释了问题和各个技术组件，却始终没有清楚说明 Neki 到底是什么、面向哪些用户。 PlanetScale 是知名的数据库厂商，将其在 Vitess 上的分片经验应用到 Postgres，是一次值得关注的押注——即 Postgres 也能像 MySQL 在 YouTube 和 Slack 那样实现水平扩展。此次发布也加剧了与 Supabase 开源项目 multigres 之间的竞争叙事，使得许可证模式和透明度成为团队选择分片方案时的核心问题。 Neki 目前是闭源的，不过 PlanetScale 的 Neki 官方页面表示，一旦产品成熟并在真实生产负载中经过测试，将会以开源项目的形式发布。评论者还提出了一个尚未解答的技术问题：Neki 是否解决了最终一致性的取舍问题——正是这一取舍让许多团队放弃了 Aurora Global Database 之类的分布式高可用 Postgres 方案。

hackernews · simon_weber · 9月10日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49645686)

**背景**: 分片（sharding）是把一个逻辑数据库拆分成多个更小的分片并分布到多台机器上，从而让负载突破单台服务器的处理上限。Postgres 本身并不内置分片能力，社区长期讨论要将其加入内核，目前则依靠十余个第三方分支和扩展来填补空白。PlanetScale 打造了 Vitess——最初在 YouTube 诞生、用于扩展 MySQL 的开源分片中间件——Neki 正是该公司把这套思路搬到 Postgres 上的尝试。Supabase 的 multigres 是瞄准同一问题的竞争性开源项目，这也正是 Neki 的闭源状态招致如此多批评的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale | Sharded Postgres by the Team Behind Vitess.</a></li>
<li><a href="https://wiki.postgresql.org/wiki/Built-in_Sharding">Built-in Sharding - PostgreSQL wiki</a></li>
<li><a href="https://www.j4mcs.dev/posts/consistency-guarantees/">A Study Guide to Confusingly Named Consistency Guarantees ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体偏向批评。高赞评论抱怨发布文章从未直白说明 Neki 是什么、用途为何；也有人指出 CEO 对 Supabase 的 multigres 的轻蔑态度与 Neki 完全闭源的事实相矛盾；还有评论者直截了当地提问：在 CAP 定理约束下，Neki 如何处理分布式高可用 Postgres 的最终一致性问题。少数人持乐观态度，有评论者预测这一方案将成为新的行业标准。

**标签**: `#postgres`, `#database-sharding`, `#planetscale`, `#distributed-systems`, `#open-source`

---

<a id="item-9"></a>
## [微软将 Rust 列为一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 7.0/10

在 Rust 基金会官网发布的一篇客座文章中，微软正式宣布将 Rust 列为“一级（tier-1）”语言，这意味着 Rust 将获得与微软其他核心语言同等级别的内部工程支持，包括安全可信的工具链构建、官方开发者工具、质量流程、深度平台集成以及合规流程。与该声明同时被讨论的，还有微软提出的目标：借助自动化工具在 2030 年前将约 10 亿行 C/C++ 代码转换为 Rust。 微软既是 C/C++ 工具链（MSVC）最重要的厂商之一，也是主流操作系统与云服务提供商，因此把 Rust 提升到一级语言是一个强烈信号：系统级编程的新项目正在从 C/C++ 之外寻找多样化选择。这可能加速整个行业对 Rust 的采用，促使其他大型平台厂商做出类似承诺，并改变系统程序员的招聘与工具链预期。 微软内部的一级语言地位意味着从本地开发到生产部署有一条“铺好的路”，而不仅仅是允许使用该语言；社区讨论还提到一些颇为激进的具体目标，例如自动化迁移要达到“1 名工程师、1 个月、100 万行代码”，以及 DARPA 资助的项目让 6 个不同团队探索自动将 C 代码翻译为 Rust 的不同方案。这类迁移工具目前大多仍不成熟，而且翻译工作很大程度上是让已有的 C/C++ 行为在 Rust 编译器眼中可见且正确，而非一键完成重写。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是一门通用系统编程语言，由 Graydon Hoare 于 2006 年在 Mozilla 创建，并于 2015 年 5 月发布首个稳定版 Rust 1.0；自 2021 年 2 月起，它由非营利组织 Rust 基金会管理，后者负责该语言的商标、基础设施与资产。Rust 的核心特性是在不使用垃圾回收器的前提下实现内存安全：编译期的“借用检查器（borrow checker）”会追踪引用的生命周期，从而防止内存安全错误和数据竞争。相比之下，C 和 C++ 默认是内存不安全的，这正是各国政府和大型厂商在安全关键软件中推动采用内存安全语言的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language) - Wikipedia</a></li>
<li><a href="https://immunant.com/migrating/">Code Migration :: Immunant, Inc</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应总体正面但并不盲从：一条高赞评论套用了“拥抱、扩展、消灭（embrace, extend, extinguish）”的套路来调侃，另一些人则援引微软“10 亿行代码转换”目标以及 DARPA 资助的 C 转 Rust 项目，认为这一承诺是认真的。多位评论者认为，该声明表明 Rust 已不再是稚嫩的新兴语言，其成熟度已超过 Zig、Odin 等更新的“更好的 C/C++”方案；一位有五年专业 Rust 经验的开发者表示，在做上层应用开发时已找不到选择其他语言的技术理由。

**标签**: `#Rust`, `#Microsoft`, `#programming-languages`, `#systems-programming`, `#memory-safety`

---

<a id="item-10"></a>
## [布朗大学报告：大型科技公司正在重塑军工复合体](https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex) ⭐️ 7.0/10

布朗大学“战争成本”（Costs of War）项目发布的一篇报告，探讨了大型科技公司与硅谷如何改造传统的军工复合体，该话题在 Hacker News 上获得 149 分和 294 条评论。讨论的焦点并不在报告细节本身，而在于硅谷与国防界的联系究竟是不是新事物。 在大型科技公司不断拿下五角大楼云计算与人工智能大单的当下，这篇报告属于及时的政策与产业分析，并再次点燃了工程师和投资人是否应当参与国防项目的争论。它影响到每一位需要权衡军事承包伦理与商业利益的科技从业者。 “战争成本”项目是布朗大学沃森国际与公共事务研究所下属的非党派研究项目，由约 35 位学者、法律专家、人权工作者和医生组成，自 2011 年起持续记录美国“9·11”后战争所带来的直接与间接代价。

hackernews · paimapi · 9月10日 15:47 · [社区讨论](https://news.ycombinator.com/item?id=49645754)

**背景**: 军工复合体指的是把一国军队、国防承包商与政客联结起来的非正式网络，艾森豪威尔总统曾在 1961 年就其对国家的影响发出著名警告。硅谷与五角大楼的关系常被遗忘：仙童半导体（Fairchild）曾为导弹系统供应集成电路，早期大量计算、网络与雷达研究都由 DARPA 和国防部出资。历史学者 Steve Blank 的演讲《硅谷秘史》（The Secret History of Silicon Valley）将这一地区的起源追溯到二战期间麻省理工学院辐射实验室的雷达研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Costs_of_War_Project">Costs of War Project - Wikipedia</a></li>
<li><a href="https://costsofwar.watson.brown.edu/">Costs of War | Brown University</a></li>
<li><a href="https://chrhs.watson.brown.edu/research/affiliated-faculty-research/costs-war">Costs of War | Center for Human Rights and Humanitarian Studies | Brown University</a></li>

</ul>
</details>

**社区讨论**: 评论者大多不认同“硅谷军事化是新现象”的说法：dredmorbius 与 hkchad 都指出硅谷从一开始就由国防部资助，并援引 Steve Blank 的《硅谷秘史》和谷歌的早期资金来源。abeppu 提出了一个反事实的伦理问题——如果当年仙童拒绝为导弹系统制造集成电路，世界是否会更好；chanakya 则追问国防承包本身是否有错，还是这种反对只针对美国公司；gsky 则讽刺道“杀人终究是门大生意”。

**标签**: `#military-industrial-complex`, `#silicon-valley`, `#defense-tech`, `#tech-history`, `#tech-policy`

---

<a id="item-11"></a>
## [Raymond Chen 揭秘 Windows XP 如何挑选你的初始用户头像](https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683) ⭐️ 7.0/10

在 2026 年 9 月发表于其 Old New Thing 博客的一篇文章中，微软工程师 Raymond Chen 解释了 Windows XP 为新用户账户分配头像所用的算法：它逐个遍历候选图片，保留当前选中的那张，并以 1/n 的概率把第 n 张替换进来——这就是所谓的蓄水池抽样（reservoir sampling，即 Algorithm R）。据文中所述，代码在采样满 100 张图片后会停止，作为最后的安全检查。 这篇文章把一段几乎无人察觉的安装期交互细节，变成了关于随机选取的生动教学案例，展示了当集合大小事先未知时如何等概率地随机挑出一项。它同时也体现了 Windows 内部机制类写作的常见主题：那些被固化进已发布代码、用户却永远看不到的小设计决策与防御性限制。 蓄水池抽样的关键在于：即便在开始遍历时并不知道总数 n，也能保证流中每一项最终被选中的概率都相同，皆为 1/n，这正是代码不先统计文件数量再随机挑选的原因。100 张图片的上限是一种防御性约束，而评论者贴出的 GitHub 上泄露的 Windows NT 5 源码，可以用来对照验证具体实现。

hackernews · soheilpro · 9月10日 09:04 · [社区讨论](https://news.ycombinator.com/item?id=49640646)

**背景**: 2001 年发布的 Windows XP 引入了按用户区分的账户头像，会显示在欢迎屏幕、开始菜单和用户磁贴上，安装过程中既可以由用户自行选择，也可能被自动分配。蓄水池抽样是一类经典的流式算法，适用于需要从未知长度甚至无限长的序列中取得等概率随机样本的场景，例如只读取一次文件就随机选出一行。Raymond Chen 是微软的资深工程师，他的博客 The Old New Thing 长期记录 Windows API 与系统内部机制的历史、怪癖和设计理由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683">What algorithm did Windows XP use to choose your initial user ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Windows_XP">Windows XP - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Random_number_generation">Random number generation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍反应热烈，有人称 Raymond Chen 每一篇关于 Windows 内部机制的文章都"像一份小小的圣诞礼物"，也有人贴出了与该算法对应的泄露版 NT5 源码链接。还有人反思了在随机性问题上人类直觉与机器逻辑之间的认知鸿沟，以及这种细致的问题分析在日常工作压力下往往被淹没的现象。

**标签**: `#Windows XP`, `#Windows internals`, `#Raymond Chen`, `#algorithms`, `#randomness`

---

<a id="item-12"></a>
## [索尼因 PlayStation 玩家是否真正“拥有”数字游戏而被起诉](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit) ⭐️ 7.0/10

一起针对索尼的消费者权益诉讼近日受到广泛关注：Hacker News 上相关讨论帖获得约 363 个赞和 120 条评论，并指向一个整理了索尼自家网站上关于玩家“拥有”数字游戏表述的维基页面。该案动议指出，PlayStation 服务条款在第 14 条中设置了强制仲裁条款和集体诉讼豁免条款，而退出条款要求用户在同意协议后 30 天内以书面形式通知索尼才能不受其约束。 此案直指“购买”一款数字游戏到底意味着什么这一核心问题，并可能影响所有数字商店——不仅是 PlayStation——如何撰写其商店页面、许可条款和争议解决条款。由于仲裁条款与集体诉讼豁免让消费者难以联合起诉，判决结果可能影响数百万 PlayStation 用户及其他数字媒体购买者在维权时的实际议价能力。 起诉文件援引索尼自身的营销话术与网站表述，作为玩家被引导相信自己“拥有”所购内容的证据，并引用了一个例子：两名原告分别在不同日期、以不同价格获得了同一款游戏（Resident Evil Requiem），以论证索尼的立场自相矛盾。30 天的书面退出期限相当短，而仲裁通常会把纠纷从公开法院和陪审团审理中移出。

hackernews · haunter · 9月10日 12:18 · [社区讨论](https://news.ycombinator.com/item?id=49642531)

**背景**: 服务条款中的仲裁条款要求消费者与公司之间的争议通过私下仲裁而非法院诉讼解决，通常还会搭配集体诉讼豁免条款，使消费者无法联合提起群体诉讼。数字游戏一般以许可（licence）而非实体商品的形式出售，而数字版权管理（DRM）技术正是执行这些许可的访问控制手段，这也正是指向商店页面中“购买”“拥有”等措辞在法律上如此重要的原因。索尼在这一领域有争议历史——2005 年曾在部分音乐 CD 中植入 rootkit，这也影响了部分评论者对该公司数字内容政策的看法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://briefmydoc.com/terms-and-conditions-explainer">Terms and Conditions Explained in Plain English | BriefMyDoc</a></li>
<li><a href="https://www.denleacarton.com/blog/personal-injury-blog/arbitration-agreements-in-personal-injury-claims-key-insights-from-wu-v-uber-tech-inc/">Arbitration Agreements in Personal Injury... - Denlea & Carton LLP</a></li>

</ul>
</details>

**社区讨论**: 讨论整体上对索尼和强制仲裁持批评态度：有评论者认为，强迫个人接受仲裁本身就应当被认定为非法，因为它唯一的实际用途就是剥夺消费者和劳动者应有的权利。另有人用买书的类比说明——两个人可以各自拥有一本书的副本，但并不拥有同一本副本；还有评论者指出，索尼的这套辩护可能反而打开一扇它宁愿关着的门，因为其逻辑意味着消费者买什么都不算拥有。也有评论者表达了矛盾心态：既称赞索尼的无反相机，又以 rootkit 事件为例，说明该公司在内容业务上确实可能做出糟糕的举动。

**标签**: `#digital ownership`, `#consumer rights`, `#Sony PlayStation`, `#arbitration`, `#DRM`

---

<a id="item-13"></a>
## [H3 RefMods 被誉为 MiniMax H3 参考模型的“轻量 LoRA”，ComfyUI 中广受好评](https://www.reddit.com/r/StableDiffusion/comments/1wclxbj/h3_refmods_are_great_i_highly_advice_trying_it/) ⭐️ 7.0/10

Reddit 用户 /u/Choowkee 发帖推荐 H3 RefMods，并分享了由 malcolmrey 编写的三份社区指南：安装与使用说明、可直接导入的 ComfyUI 工作流，以及自制 RefMod 的创建指南，同时给出 LuisaPinguinnn 的 GitHub 项目 ComfyUI-MiniMaxH3Mod。发帖者称仅用 8 张基础图片、花费几分钟就做出了自己的 RefMod，并表示该技术确实如宣传那样，相当于 H3 参考模型的“轻量 LoRA”。 RefMods 提供了一种免训练的方式，让 MiniMax H3 视频生成中的角色与主体保持一致，而以前每次生成都需要重新输入参考图片或视频。对 ComfyUI 生态的实践者而言，这降低了制作可复用、可分享的风格/角色适配器的门槛，其定位介于提示词工程与完整 LoRA 训练之间。 RefMods 是以 .safetensors 文件形式保存的预编码条件级适配器，而不是经过训练的网络权重，因此制作速度极快——发帖者仅用 8 张图片作为基础素材。作者建议改用 ComfyUI 内部的“Create H3 RefMod”与“Save H3 RefMods”节点来创建，以便更好地控制流程，并指出分享的工作流中的 LoRA power loader 与 spectrum 节点可以删除。该技术主要面向 H3 参考模型（REF2VA），但据称也可用于 FL2VA。

reddit · r/StableDiffusion · /u/Choowkee · 9月10日 15:09

**背景**: MiniMax H3 是一个开放通用的全模态生成模型，能够统一理解文本、图像、视频与音频，并可生成带原生立体声音频、最高 2K 分辨率、时长最长 15 秒的视频。RefMods 全称 Reference Latent Adapters（参考潜变量适配器），是社区为 H3 打造的条件级适配器：不必每次生成都提供参考图片或视频，只需将参考内容一次性编码成极小的适配器文件即可反复使用。ComfyUI 是本地运行扩散模型的热门节点式界面，而 LoRA 是标准的轻量微调技术，这类适配器常被拿来与之类比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/datasets/malcolmrey/various/blob/main/h3-center/docs/MINIMAX_H3_REFMODS_INSTALLATION_AND_USAGE_GUIDE.md">h3-center/docs/MINIMAX_H3_REFMODS_INSTALLATION_AND_USAGE_GUIDE.md · malcolmrey/various at main</a></li>
<li><a href="https://comfyui-wiki.com/en/news/2026-09-07-minimax-h3-refmods">MiniMax H3 RefMods: Zero-Training Reference Adapters</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#ComfyUI`, `#LoRA`, `#MiniMax H3`, `#RefMods`

---

<a id="item-14"></a>
## [Qwen-Image-Edit-2511 对比 SenseNova-U1.5-Lite：多参考图像融合实测](https://www.reddit.com/r/StableDiffusion/comments/1wcm948/qwenimageedit2511_vs_sensenovau15lite/) ⭐️ 7.0/10

一位 Reddit 用户在 r/StableDiffusion 上发布了对 Qwen-Image-Edit-2511 与 SenseNova-U1.5-8B-MoT-Preview 的实测对比，围绕四组多参考图像融合任务得出结论：Qwen 在纹理、光照与阴影质感上更强，而 SenseNova 在空间理解上更有优势。在“猫骑滑板车”的例子里，Qwen 在咖啡桌下生成了一个奇怪的柱子，猫的前爪位置也不自然，而 SenseNova 没有出现这两类瑕疵。 多参考图像编辑——把来自多张源图的主体、道具和光照合并成一个连贯场景——是生成式图像中最棘手的实际任务之一，这次对比为从业者提供了具体参考：当物理合理性与接触真实感比原始纹理质量更重要时该选哪个模型。它也说明像 SenseNova-U1.5 这样体量较小的统一多模态模型，在空间推理上可以胜过更偏重编辑的大型模型，这会影响开发者搭建编辑流水线的方式以及各模型的定位。 测试共四组对比，输入图像一部分由 Krea-2 生成、一部分为真实照片，提示词中包含非常细粒度的约束，例如猫爪与车把的接触、毛发与坐垫边缘的挤压、从正面视角改为四分之三侧视角，以及黄金时刻的轮廓光。Qwen-Image-Edit-2511 是阿里推出的图像编辑模型，在角色一致性、多人编辑、LoRA 支持和几何推理方面有所改进；SenseNova-U1.5-8B-MoT-Preview 则是基于 NEO-unify 框架构建的 80 亿参数原生统一多模态检查点。

reddit · r/StableDiffusion · /u/daniel933912 · 9月10日 15:22

**背景**: 多参考（多图）编辑模型会一次性接收多张输入图像——例如人物、道具和背景——并需要把它们融合成一张新图，同时保留各个主体的身份特征，并让结果在物理上说得通。Qwen-Image-Edit-2511 属于阿里的 Qwen 图像生成系列，于 2025 年 12 月下旬发布，重点强化了角色一致性与几何推理能力。SenseNova-U1.5-8B-MoT 来自商汤的 OpenSenseNova 项目，被描述为基于 NEO-unify 的“原生统一”多模态检查点，也就是说同一个模型同时负责生成与编辑，而不是把多个模块串起来。文中提到的部分测试输入图来自 Krea-2，这是 Krea AI 自研的基础图像模型，主打风格控制与参考图驱动生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen-image-edit-2511">Qwen-Image-Edit-2511: Improve Consistency</a></li>
<li><a href="https://huggingface.co/sensenova/SenseNova-U1.5-8B-MoT">sensenova/ SenseNova - U 1 . 5 -8B-MoT · Hugging Face</a></li>
<li><a href="https://www.krea.ai/krea-2">Krea 2: AI Image Foundation Model & Style Control</a></li>

</ul>
</details>

**标签**: `#image editing`, `#AI model comparison`, `#Qwen`, `#SenseNova`, `#generative AI`

---

<a id="item-15"></a>
## [个人开发者用单张 GPU 在 3.5 天内从零训练出 2.1 亿参数文生图扩散 Transformer](https://www.reddit.com/r/StableDiffusion/comments/1wciz7m/i_trained_a_210m_texttoimage_diffusion/) ⭐️ 7.0/10

Reddit 用户 Ivan Mikhnenkov 完全从零构建并训练了一个 2.1 亿参数的文生图扩散 Transformer：使用 420 万张经过筛选的 256² 图像，在 FLUX.2 VAE 隐空间上做 rectified flow，文本编码器采用 flan-t5-base（最多 128 个 token），整轮训练在一张 RTX PRO 6000 上仅耗时 3.5 天。他公开了 CC BY-NC 许可的模型权重、Hugging Face Space 在线演示、完整代码、训练看板以及对每项设计决策的详细说明。 这表明过去只有资金充裕的实验室才能做的「从零训练生成模型」，如今个人用一张 GPU 在几天内就能完成，大幅降低了独立研究扩散模型架构与训练配方的门槛。他总结的可复用经验（caption 质量、时间步偏移、宽高比分桶、register token、torch.compile）对任何训练小型扩散模型或微调大模型的人都有直接参考价值。 两个值得注意的发现：把 torch.compile 用于训练（而不只是推理）带来了 2.4 倍加速；学习到的 null register 槽位吸收了约 90% 的交叉注意力，这一结果让作者本人也感到意外。他还指出，训练 loss 在第一天之后就不再能反映模型质量，但生成图像仍在持续变好，因此他改用 FID、基于检测器的物体准确率和人类偏好模型来评估；下一步计划是用 Flow-GRPO 做 RL 微调。

reddit · r/StableDiffusion · /u/IvanMikhnenkov · 9月10日 13:18

**背景**: 扩散 Transformer（DiT）通过不断对随机噪声去噪来生成图像，而 rectified flow 是一种变体，它学习从噪声到数据的近似直线传输路径，从而加快采样。现代系统通常不在像素空间操作，而是在变分自编码器（VAE）压缩出的隐空间中去噪——本文用的是 FLUX.2 VAE，其 32 通道隐表示会改变最优的噪声调度。Register token 是附加在 token 序列末尾的可学习槽位，用于吸收高范数的离群激活值、保持注意力图干净；torch.compile 则是 PyTorch 的即时编译器，通过算子融合提升速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cs.utexas.edu/~lqiang/rectflow/html/intro.html">Rectified Flow — Rectified Flow</a></li>
<li><a href="https://bfl.ai/techblog/representation-comparison/index.html">FLUX.2: Analyzing and Enhancing the Latent Space of FLUX ...</a></li>
<li><a href="https://arxiv.org/abs/2309.16588">[2309.16588] Vision Transformers Need Registers - arXiv.org Registers Matter for Pixel-Space Diffusion Transformers Registers Matter for Pixel-Space Diffusion Transformers Register Tokens in Diffusion Transformers - emergentmind.com Vision Transformers Don't Need Trained... Taming Outlier Tokens in Diffusion Transformers GitHub - nickjiang2378/test-time-registers: [NeurIPS '25 ...</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#text-to-image`, `#training`, `#single GPU`, `#torch.compile`

---

<a id="item-16"></a>
## [文章称人类创造力是 AI 时代最后一道持久的护城河](https://www.inventbuild.studio/blog/genuine-creativity-is-your-new-moat) ⭐️ 6.0/10

InventBuild Studio 发布了一篇题为《真正的创造力才是你的新护城河》的博客文章，认为随着 AI 让生产能力趋于同质化，真正的人类创造力将成为最后一种持久的差异化竞争优势。该文被发到 Hacker News 后获得 134 分，并引发 71 条评论。 这篇文章呼应了创业者、产品开发者与投资人之间的一场更广泛讨论：当 AI 让代码、设计和内容的生产成本变得极低时，究竟还有哪些可防御的竞争优势。如果创造力是仅存的护城河，那么初创公司和知识工作者就必须重新思考如何实现差异化，而不能只靠执行速度竞争。 该文属于观点文章而非原创研究，评论区也提出了强烈反驳：有用户认为创造力是一场需要持续投入的“红皇后竞赛”，而非真正的护城河，因为护城河意味着某种被动性和结构性锁定（例如拥有桌面操作系统）。还有人指出，在普通商业网站上追求“真正的创造力”往往只会带来加载缓慢、界面杂乱的页面，把顾客赶走。

hackernews · virgil_disgr4ce · 9月10日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49648732)

**背景**: “经济护城河”一词由沃伦·巴菲特推广，用来描述企业持久的竞争优势——如同护城河保护城堡一般，帮企业抵御竞争对手。这篇文章把这一框架套用到 AI 时代，并借鉴了“AI 商品化”的思路：AI 能力逐渐变成标准化、随处可得的产品，任何玩家都无法独占，从而迫使企业转向别处寻求差异化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Economic_moat">Economic moat - Wikipedia</a></li>
<li><a href="https://www.techpolicy.press/taking-ai-commoditization-seriously/">Taking AI Commoditization Seriously | TechPolicy.Press</a></li>
<li><a href="https://news.ycombinator.com/">Hacker News</a></li>

</ul>
</details>

**社区讨论**: 整体情绪带有质疑与细致辨析，而非单纯否定。最热门的反驳（lordnacho）认为创造力是一场“红皇后竞赛”，缺乏真正护城河所具有的被动性；Animats 则抱怨普通电商网站上的“真正创造力”往往只是过度复杂的页面，反而损害购买体验。也有人彻底重构了问题——zcw100 认为人们应当对过去被迫忍受的低质内容感到愤怒；cat-whisperer 则指出，如今 Lovable、Emergent 这类 AI 设计工具“交付的是别人的品味”，是在约束而非释放创造力。

**标签**: `#AI`, `#startups`, `#business-strategy`, `#creativity`, `#hacker-news-discussion`

---

<a id="item-17"></a>
## [ComfyUI 中的 MiniMax H3：从《星际迷航大战星球大战》同人短片中学到的经验](https://www.reddit.com/r/StableDiffusion/comments/1wcqctw/followup_to_my_last_star_trek_post_i_made_a_star/) ⭐️ 6.0/10

一位 Reddit 用户发布了上一篇帖子的后续，此前他介绍了用 MiniMax H3 在 ComfyUI 中制作 6 分钟《星际迷航：下一代》同人短片的流程，这次则分享了制作《星际迷航大战星球大战》同人短片时学到的新经验。最核心的新发现是：单次生成时长会显著影响对白的表演效果，而把 H3 当作“单镜头生成工具”而不是“整场戏的文生视频工具”，效果会好得多。 对于日益壮大的 AI 电影创作群体而言，这些是可复现的具体工作流经验，他们依赖 ComfyUI 和 H3 这类开放模型，而非封闭的云端视频服务。随着开放多模态视频模型逼近 2K 分辨率与 15 秒原生音频生成能力，真正的瓶颈已不再是模型本身，而是时长调校、参考图控制这类镜头级别的实操技巧。 作者建议先以低分辨率、多种时长（例如 10 秒、11 秒、12 秒）试生成对白密集的镜头，找到语速自然的那个时长后，再投入昂贵的高分辨率渲染；他还提到片中许多镜头是在约 200 万像素 / 全高清规格下生成的，因为这样人物的脸看起来明显不那么像“AI 视频”。他还提醒说，如果提示词没有明确声明摄像机完全静止、构图与人物比例需与参考图保持一致，H3 往往会自己缓慢推镜或重新构图。

reddit · r/StableDiffusion · /u/Glad-Hat-5094 · 9月10日 17:49

**背景**: MiniMax H3 是一款通用多模态生成模型，能够在文本、图像、视频和音频之间理解统一上下文，并输出最高 2K 分辨率、最长 15 秒且带原生立体声的视频。ComfyUI 是一个开源的节点式界面与推理引擎，用户可以把模型、采样器和各类工具串成模块化工作流，因此这类逐镜头电影制作流程通常都在其中搭建。作者的整体流程是：先制作起始图像，再用 ComfyUI 中的 H3 生成一个个镜头，最后在 Adobe Premiere Pro 中完成剪辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fal.ai/minimax-h3">MiniMax H 3 - Open-Weights General -Purpose Multimodal Video Model</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://docs.comfy.org/">ComfyUI Official Documentation - ComfyUI</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#ComfyUI`, `#MiniMax H3`, `#Stable Diffusion`, `#workflow`

---

