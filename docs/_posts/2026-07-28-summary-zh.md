---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 34 条内容中筛选出 11 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：background removal、cybersecurity、AI safety、open source、AI。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[FeyNoBg：开源背景去除模型与训练库](https://usefeyn.com/blog/feynobg/)**
2. **[微软推出 MAI-Cyber-1-Flash 网络安全模型](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/)**
3. **[Anthropic 主张对开放权重模型进行强制测试](https://www.anthropic.com/news/position-open-weights-models)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [微软推出 MAI-Cyber-1-Flash 网络安全模型](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [Anthropic 主张对开放权重模型进行强制测试](https://www.anthropic.com/news/position-open-weights-models)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [NVIDIA Cosmos-H-Dreams：手术机器人的实时生成模拟](https://huggingface.co/blog/nvidia/cosmos-h-dreams)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：FeyNoBg：开源背景去除模型与训练库

**关联新闻**: [FeyNoBg：开源背景去除模型与训练库](https://usefeyn.com/blog/feynobg/)

**切入角度**: Feyn Labs 发布了 FeyNoBg，这是一个先进的自动背景去除模型，并开源了用于训练和运行该模型的 Python 库 NoBg。该模型在八个基准测试中的四个上取得了最佳公开分数，在其余基准上误差在 2% 以内。 这为 Adobe 等专有工具提供了一个高质量的开源替代方案，使开发者和研究人员更容易使用背景去除功能。此外，NoBg 标准化了图像抠图的训练和评估工作流程，解决了该领域的一个常见痛点。 FeyNoBg 将 BiRefNet 的特征提取器从 18 个块扩展到 24 个块，同时保留了预训练权重，并在来自 10 个数据集的 26,100 个多样化样本上进行了训练。该模型采用 CC-BY-NC-4.0 许可证（限制商业使用），而 NoBg 库采用 MIT 许可证。

**可延展方向**: 背景去除（图像抠图）是一项常见的计算机视觉任务，通过识别前景并估计每个像素的透明度来将主体与背景分离。许多现有模型以孤立的仓库形式发布，预处理和训练代码不兼容，难以比较或改进。NoBg 为训练和运行此类模型提供了统一的 Python 接口，目前支持 BiRefNet，未来计划支持更多架构。

---

### 选题 2：微软推出 MAI-Cyber-1-Flash 网络安全模型

**关联新闻**: [微软推出 MAI-Cyber-1-Flash 网络安全模型](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/)

**切入角度**: 微软推出了 MAI-Cyber-1-Flash，这是一个轻量级网络安全 AI 模型，旨在处理其 MDASH 多智能体漏洞修复系统中高达 90%的任务，减少对 GPT-5.4 等大型模型的依赖。 该模型承诺将网络安全成本降低一半，同时让先进的 AI 安全技术更易获取，可能改变组织处理漏洞检测和修复的方式。 MAI-Cyber-1-Flash 集成到 MDASH 中，MDASH 协调超过 100 个专门的 AI 智能体。它高效处理常见任务，仅将最昂贵的模型用于 10%的异常困难任务。

**可延展方向**: MDASH（多智能体漏洞识别与修复）是微软的系统，使用一组 AI 智能体进行代码漏洞检测。MAI-Cyber-1-Flash 是经过微调的蒸馏模型，专门用于网络安全，与谷歌的 Gemini 3.5 Flash Cyber 等产品竞争。

---

### 选题 3：Anthropic 主张对开放权重模型进行强制测试

**关联新闻**: [Anthropic 主张对开放权重模型进行强制测试](https://www.anthropic.com/news/position-open-weights-models)

**切入角度**: Anthropic 发布博客文章，澄清其不支持禁止开放权重模型，而是主张对所有具备足够能力的模型（包括开放和封闭模型）进行强制安全测试。 该立场可能影响 AI 监管，因为它来自一家领先的 AI 公司，并涉及开源创新与安全性之间的平衡。辩论凸显了在不妨碍开放开发的情况下定义和实施安全测试的挑战。 Anthropic 强调强制测试应适用于所有具备能力的模型，而不仅仅是开放权重模型。批评者认为，由于测试成本高昂或限制性要求，该提议实际上可能禁止开放权重模型。

**可延展方向**: 开放权重模型允许用户下载预训练的模型权重并在本地运行推理，但由于缺乏训练代码和数据，它们并非完全开源。AI 社区正在讨论开放性、安全性和控制之间的权衡。Anthropic 的提议处于这场辩论的中心，主张在保持模型可访问性的同时进行安全测试。

---

1. [Anthropic 主张对开放权重模型进行强制测试](#item-1) ⭐️ 8.0/10
2. [自包含可移植 Python 发行版助力现代工具](#item-2) ⭐️ 8.0/10
3. [法官驳回谷歌用 DMCA 阻止爬取搜索结果的企图](#item-3) ⭐️ 8.0/10
4. [沃尔沃/埃歇尔车队 API 漏洞致所有车辆受控](#item-4) ⭐️ 8.0/10
5. [缺失下划线导致无辜男子入狱 18 个月](#item-5) ⭐️ 8.0/10
6. [NVIDIA Cosmos-H-Dreams：手术机器人的实时生成模拟](#item-6) ⭐️ 8.0/10
7. [FeyNoBg：开源背景去除模型与训练库](#item-7) ⭐️ 7.0/10
8. [从 React.js 迁移到 HTMX：一个论坛案例研究](#item-8) ⭐️ 7.0/10
9. [Paged Out 第 9 期发布：免费技术杂志](#item-9) ⭐️ 7.0/10
10. [Libsm64：将超级马力欧 64 角色提取为可复用库](#item-10) ⭐️ 7.0/10
11. [微软推出 MAI-Cyber-1-Flash 网络安全模型](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 主张对开放权重模型进行强制测试](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布博客文章，澄清其不支持禁止开放权重模型，而是主张对所有具备足够能力的模型（包括开放和封闭模型）进行强制安全测试。 该立场可能影响 AI 监管，因为它来自一家领先的 AI 公司，并涉及开源创新与安全性之间的平衡。辩论凸显了在不妨碍开放开发的情况下定义和实施安全测试的挑战。 Anthropic 强调强制测试应适用于所有具备能力的模型，而不仅仅是开放权重模型。批评者认为，由于测试成本高昂或限制性要求，该提议实际上可能禁止开放权重模型。

hackernews · surprisetalk · 7月27日 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开放权重模型允许用户下载预训练的模型权重并在本地运行推理，但由于缺乏训练代码和数据，它们并非完全开源。AI 社区正在讨论开放性、安全性和控制之间的权衡。Anthropic 的提议处于这场辩论的中心，主张在保持模型可访问性的同时进行安全测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models ? | Analytics Vidhya</a></li>
<li><a href="https://www.pbs.org/newshour/science/whats-the-difference-between-closed-open‑source-and-open-weight-ai-a-researcher-explains">What's the difference between closed, open‑source and open-weight AI? A researcher explains | PBS News</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source Initiative</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈质疑，认为强制测试会通过施加高昂成本或限制性要求而起到禁令的作用。一些人指责 Anthropic 出于自身利益，指出其 CEO 反对发布可能削弱其封闭高价模型的类似能力。其他人则指出了 Anthropic 在硬件出口管制立场上的不一致。

**标签**: `#AI safety`, `#open-weights`, `#regulation`, `#Anthropic`, `#open-source`

---

<a id="item-2"></a>
## [自包含可移植 Python 发行版助力现代工具](https://gregoryszorc.com/docs/python-build-standalone/main/) ⭐️ 8.0/10

python-build-standalone 项目提供了自包含、高度可移植的 Python 发行版，已被 uv、pipx、Hatch、Poetry 和 Bazel 等现代 Python 工具广泛采用，用于便捷的 Python 安装和打包。 这些可移植发行版消除了用户手动安装 Python 的需求，使得 uv 等工具能够提供无缝的 Python 版本管理，并可将 Python 打包到应用程序（如 macOS 桌面应用）中。这简化了开发流程并提高了可重复性。 这些发行版由 Astral（uv 背后的公司）维护，目前隶属于 OpenAI。社区成员指出，对于将 Python 打包到应用程序中，这些发行版非常理想，相关项目 PyOxy 可以生成包含完整功能 Python 解释器的单文件可执行程序。

hackernews · jcbhmr · 7月27日 18:43 · [社区讨论](https://news.ycombinator.com/item?id=49073942)

**背景**: 传统上，Python 安装来自 python.org 或系统包管理器，这既繁琐又不易移植。可移植 Python 发行版将 Python 编译成自包含包，无需安装即可下载使用，非常适合需要管理多个 Python 版本或将 Python 打包到独立应用程序中的工具链（如 uv）。python-build-standalone 项目通过构建过程生成这些高度可移植的二进制文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://realpython.com/python-uv/">Managing Python Projects With uv: An All-in-One Solution – Real Python</a></li>

</ul>
</details>

**社区讨论**: 主要维护者如 charliermarsh（uv 创建者）在评论中确认 uv 使用这些发行版，并表示大部分工程时间用于跟上上游 CPython。simonw 称赞这些发行版非常适合将 Python 打包到桌面应用中。其他评论提到了用于生成单文件可执行程序的 PyOxy 以及可在多个操作系统上运行的 Cosmopolitan 跨平台二进制文件等替代方案。

**标签**: `#Python`, `#distribution`, `#portable`, `#uv`, `#tooling`

---

<a id="item-3"></a>
## [法官驳回谷歌用 DMCA 阻止爬取搜索结果的企图](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

美国一名法官裁定，谷歌不能利用《数字千年版权法案》（DMCA）阻止 SerpAPI 抓取其搜索结果，驳回了谷歌关于爬取行为绕过了技术保护措施的主张。 这项裁决树立了一个先例，限制企业利用版权法来限制网页爬取行为，这对透明度、竞争和开放网络至关重要。同时这也凸显了讽刺：谷歌本身靠爬取其他网站起家，如今却试图阻止别人爬取其数据。 法官认为，谷歌的搜索结果不具备 DMCA 反规避条款所需的版权保护，且谷歌的安全措施并非为了控制对版权材料的访问。该案涉及谷歌起诉 SerpAPI，后者提供爬取谷歌搜索结果供第三方使用的服务。

hackernews · cdrnsf · 7月27日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: DMCA 的反规避条款禁止绕过控制访问版权作品的技术措施。网页爬取本身一般并不违法，但合法性取决于服务条款和版权等因素。谷歌曾提供搜索 API，但后来将其弃用，导致许多开发者只能依赖爬取。批评者认为，DMCA 已被用于超出立法初衷的目的，用来针对合法竞争者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DMCA_anti-circumvention">DMCA anti-circumvention</a></li>
<li><a href="https://www.eff.org/pages/unintended-consequences-fifteen-years-under-dmca">Unintended Consequences: Fifteen Years under the DMCA | Electronic Frontier Foundation</a></li>
<li><a href="https://blog.apify.com/is-web-scraping-legal/">Is web scraping legal ? Yes, if you know the rules.</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，谷歌在依靠爬取网络起家后却利用 DMCA，具有讽刺意味；并指出谷歌弃用搜索 API 的做法催生了 SerpAPI 等爬取服务的需求。一些人认为，这项裁决对于遏制广告骗局很重要，因为爬取可以揭露误导性的付费结果。

**标签**: `#DMCA`, `#web scraping`, `#Google`, `#legal`, `#copyright`

---

<a id="item-4"></a>
## [沃尔沃/埃歇尔车队 API 漏洞致所有车辆受控](https://eaton-works.com/2026/07/27/my-eicher-hack/) ⭐️ 8.0/10

一名安全研究人员利用沃尔沃/埃歇尔车队管理平台'My Eicher'的 API 漏洞，获得了对所有用户和车辆的管理控制权。该研究人员于 2025 年 11 月负责任地披露了该漏洞，漏洞在数周内被修复，但研究结果于 2026 年 7 月公开。 该漏洞凸显了依赖云的汽车系统中存在的严重安全风险，攻击者可能借此追踪、控制或禁用商用车辆。这强调了车队管理中 API 安全的重要性，并引发了关于车辆所有权和维修权的关键讨论。 该漏洞允许未经授权访问内部 API，从而实现追踪车辆位置、访问驾驶员数据，甚至可能控制车辆功能等操作。研究人员指出，公司在多次跟进后修复了主要问题，但未公开承认该报告。

hackernews · EatonZ · 7月27日 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49070756)

**背景**: 像'My Eicher'这样的车队管理平台利用远程信息处理和 GPS 来帮助商用车车主跟踪和管理车队。这些平台日益基于云，意味着集中式漏洞可能同时暴露成千上万辆车辆。'My Eicher'应用由沃尔沃埃歇尔与 iTriangle Infotech 的合资企业 VE Connected Solutions 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eaton-works.com/2026/07/27/my-eicher-hack/">Exploiting Volvo/Eicher’s fleet management platform to gain control over all users and vehicles</a></li>
<li><a href="https://en.wikipedia.org/wiki/Eicher_Motors">Eicher Motors - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了研究人员耐心的披露时间线，并对现代汽车依赖云服务实现基本功能表示担忧。一些人提到了维修权的影响，并链接了自由软件基金会的视频，而另一些人则幽默地思考老式车辆不受此类漏洞影响。

**标签**: `#security`, `#vulnerability`, `#automotive`, `#IoT`, `#responsible disclosure`

---

<a id="item-5"></a>
## [缺失下划线导致无辜男子入狱 18 个月](https://arstechnica.com/tech-policy/2026/07/police-missed-one-underscore-and-sent-the-wrong-man-to-prison/) ⭐️ 8.0/10

一个 Kik 用户名中缺失的下划线导致一名无辜男子被错误定罪，他在监狱服刑 18 个月后错误才被发现。 此案暴露了数字取证证据处理和法律系统中的严重缺陷，表明一个微小的打字错误如何能毁掉一个人的一生。它突显了对数字证据进行更严格验证以及在错误定罪发生时追究更大责任的必要性。 受害者 Klayme 有一个 Kik 账户，但警方无法证明他在案发期间使用过该账户；没有亲密照片与他相关联。尽管证据薄弱，他仍因引诱未成年人、提供色情材料和持有儿童色情制品被定罪。

hackernews · quantified · 7月27日 22:10 · [社区讨论](https://news.ycombinator.com/item?id=49076116)

**背景**: 数字取证通常依赖用户名来识别嫌疑人，但像缺失下划线这样的错误可能导致误认。在在线儿童剥削案件中，执法部门可能优先考虑快速逮捕而非彻底核实证据。此案与过去因数字证据有缺陷导致错误定罪的案例相似，引发了对这类证据在法庭上可靠性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://whatsmyname.io/">WhatsMyName | Free Username Search for OSINT Research</a></li>
<li><a href="https://whatsmyname.dev/">Free Safe OSINT Username Discovery Tool - WhatsMyName</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑在证据如此薄弱的情况下如何定罪，并指出无辜男子失去的时间和声誉未获赔偿。一些人强调，针对数字传输违禁品的法律容易使人被陷害，而另一些人则要求进行系统性改革以防止类似的不公正。

**标签**: `#wrongful conviction`, `#digital forensics`, `#cybersecurity`, `#criminal justice`, `#evidence`

---

<a id="item-6"></a>
## [NVIDIA Cosmos-H-Dreams：手术机器人的实时生成模拟](https://huggingface.co/blog/nvidia/cosmos-h-dreams) ⭐️ 8.0/10

英伟达发布了 Cosmos-H-Dreams，这是一个实时生成模拟框架，能够即时生成手术场景的逼真视频，用于训练手术机器人。 该框架可以通过生成无限的合成数据，显著加速手术机器人的开发，减少对昂贵且稀缺的真实手术数据的依赖，并在逼真环境中实现更安全的验证。 Cosmos-H-Dreams 将英伟达此前专注于自动驾驶的 Cosmos-Dreams 技术应用于手术场景，利用程序化数据对视觉场景动态进行建模，并实时运行以生成高保真视频帧。

rss · Hugging Face Blog · 7月27日 09:32

**背景**: 生成式模拟利用 AI 模型自动创建逼真的模拟环境和任务，最大限度地减少人工工作。在手术机器人领域，由于隐私和安全限制，获取多样化的真实世界数据具有挑战性。Cosmos-H-Dreams 利用世界基础模型生成逼真视频，类似于 Cosmos-Drive-Dreams 生成驾驶数据的方式，但针对医疗场景进行了定制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itbrief.news/story/nvidia-opens-medical-physics-simulation-framework-for-robots">Nvidia opens medical physics simulation framework for robots</a></li>
<li><a href="https://github.com/nv-tlabs/omni-dreams">GitHub - nv-tlabs/omni-dreams: NVIDIA Cosmos-Dreams (fka NVIDIA OmniDreams) is a world model that generates photorealistic video for autonomous-driving simulation in real time. · GitHub</a></li>

</ul>
</details>

**标签**: `#surgical robotics`, `#generative simulation`, `#NVIDIA`, `#real-time simulation`, `#AI`

---

<a id="item-7"></a>
## [FeyNoBg：开源背景去除模型与训练库](https://usefeyn.com/blog/feynobg/) ⭐️ 7.0/10

Feyn Labs 发布了 FeyNoBg，这是一个先进的自动背景去除模型，并开源了用于训练和运行该模型的 Python 库 NoBg。该模型在八个基准测试中的四个上取得了最佳公开分数，在其余基准上误差在 2% 以内。 这为 Adobe 等专有工具提供了一个高质量的开源替代方案，使开发者和研究人员更容易使用背景去除功能。此外，NoBg 标准化了图像抠图的训练和评估工作流程，解决了该领域的一个常见痛点。 FeyNoBg 将 BiRefNet 的特征提取器从 18 个块扩展到 24 个块，同时保留了预训练权重，并在来自 10 个数据集的 26,100 个多样化样本上进行了训练。该模型采用 CC-BY-NC-4.0 许可证（限制商业使用），而 NoBg 库采用 MIT 许可证。

hackernews · snyy · 7月27日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=49072462)

**背景**: 背景去除（图像抠图）是一项常见的计算机视觉任务，通过识别前景并估计每个像素的透明度来将主体与背景分离。许多现有模型以孤立的仓库形式发布，预处理和训练代码不兼容，难以比较或改进。NoBg 为训练和运行此类模型提供了统一的 Python 接口，目前支持 BiRefNet，未来计划支持更多架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://usefeyn.com/blog/feynobg/">FeyNoBg: A SOTA Model For Background Removal — Feyn</a></li>
<li><a href="https://news.ycombinator.com/item?id=49072462">Show HN: FeyNoBg – Automatic background removal model and training library | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论提出了 FeyNoBg 与 Adobe 的主题选择工具相比如何的问题，一位用户指出 Adobe 在“选择主题”和“选择人物”上都很可靠。许可证选择（CC-BY-NC-4.0）受到质疑，因为 BiRefNet 是 MIT 许可证，作者解释这样选择是为了防止商业滥用，而库本身仍是 MIT。其他评论赞扬了这项工作，并询问了分辨率限制和数据集组装方法。

**标签**: `#background removal`, `#open source`, `#computer vision`, `#machine learning`, `#Python library`

---

<a id="item-8"></a>
## [从 React.js 迁移到 HTMX：一个论坛案例研究](https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/) ⭐️ 7.0/10

Misago 论坛项目从其代码库中移除了 React.js，转而采用 HTMX 来实现用户界面交互，依赖服务器端渲染和超媒体驱动的更新。 这一迁移反映了向更简单的服务器端方法发展的趋势，这些方法减少了前端复杂性，尤其适用于像论坛这样的内容密集型网站，这些网站通常不需要完整的单页应用交互性。 HTMX 通过自定义属性扩展 HTML，直接在 HTML 中启用 AJAX、CSS 过渡、WebSocket 和服务器发送事件，从而无需虚拟 DOM 即可实现部分页面更新。

hackernews · Ralfp · 7月27日 09:58 · [社区讨论](https://news.ycombinator.com/item?id=49067301)

**背景**: React.js 是一个用于构建交互式用户界面的 JavaScript 库，但对于内容大多静态的网站来说，它会增加复杂性。HTMX 是一个轻量级库，通过 HTML 属性实现动态行为，推广超媒体驱动架构，许多开发者认为它在某些用例下更简单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://github.com/bigskysoftware/htmx">GitHub - bigskysoftware/htmx: htmx - high power tools for HTML · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了不同的体验：一些人称赞 HTMX 的简洁性，而另一些人则注意到大型响应负载的性能问题。建议包括将 HTMX 与微型 React 或 Vue 应用结合用于高交互性部分。

**标签**: `#HTMX`, `#React.js`, `#Web Development`, `#Server-Side Rendering`, `#Frontend Migration`

---

<a id="item-9"></a>
## [Paged Out 第 9 期发布：免费技术杂志](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 7.0/10

Paged Out 第 9 期已发布 PDF 版本，这是一本每篇文章仅限一页的免费实验性技术杂志。 本期延续了提供深度技术、极客探索性内容的传统，涵盖底层编程、复古计算和安全等领域，填补了类似 Phrack 等经典杂志的空白。 杂志包含如《C 语言的婴儿步骤》、《次像素动物园》等文章，以及一篇关于可计算镶嵌的文章，重新发现了 Wang 在 1960 年代的工作，将镶嵌问题与停机问题联系起来。

hackernews · laurensr · 7月27日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49070138)

**背景**: Paged Out! 是由 Gynvael Coldwind 于 2018 年创办的免费社区驱动杂志。每期由一页的文章组成，内容涵盖编程、黑客技术、复古计算、电子学和演示场景。该杂志以其高质量的制作和深度内容而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pagedout.institute/">Paged Out!</a></li>
<li><a href="https://gynvael.coldwind.pl/?id=707">Introducing Paged Out! magazine (also CFP) - gynvael.coldwind//vx.log</a></li>

</ul>
</details>

**社区讨论**: 读者反响积极，称该杂志‘技术深厚’且‘设计精美’。一位评论者将其比作现代的 2600 杂志，另一位则比作带有光栅艺术广告的 Phrack。有深入观察者指出，关于可计算镶嵌的文章未经承认地重新发现了 Wang 关于可计算镶嵌的工作。

**标签**: `#hacking`, `#programming`, `#technical magazine`, `#low-level`, `#retro computing`

---

<a id="item-10"></a>
## [Libsm64：将超级马力欧 64 角色提取为可复用库](https://github.com/libsm64/libsm64) ⭐️ 7.0/10

Libsm64 将《超级马力欧 64》中的可操作角色马力欧提取成一个独立的共享库，可集成到任何外部游戏引擎中，并通过例如在《半条命 2》中引入马力欧等演示进行展示。 该项目展示了无需依赖中心化元宇宙平台或区块链资产即可实现跨游戏角色互操作的可行性，为游戏开发者和模组作者提供了复用经典游戏角色的新途径。同时，它也是逆向工程和游戏资产提取领域的一个里程碑。 该库通过 libsm64.h 定义了一个简洁的 C 语言 API；客户端项目只需包含该头文件并加载共享库即可使用。它基于《超级马力欧 64》的完整反编译工作，后者提供了干净且可编译的 C 语言源代码。

hackernews · klaussilveira · 7月27日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49067352)

**背景**: 《超级马力欧 64》是 1996 年在 Nintendo 64 上发布的标志性 3D 平台游戏。多年来其源代码为专有，但社区逆向工程项目成功将游戏二进制反编译为可读的 C 代码。Libsm64 将这些反编译代码中的马力欧角色逻辑封装成共享库，供任何引擎或程序调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/libsm64/libsm64">GitHub - libsm64/libsm64: Mario 64 as a library for use in external game engines · GitHub</a></li>
<li><a href="https://github.com/n64decomp/sm64">GitHub - n64decomp/sm64: A Super Mario 64 decompilation, brought to you by a bunch of clever folks. · GitHub</a></li>
<li><a href="https://godotengine.org/asset-library/asset/3653">Libsm64 Godot - Godot Asset Library</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，评论者称赞该项目是一个富有创意且令人印象深刻的工程成就。有人指出，它无需借助元宇宙或 NFT 的热度便实现了跨游戏角色互操作的承诺；还有用户分享了马力欧在《半条命 2》中的演示视频，并附上了使用 libsm64 的项目列表链接。

**标签**: `#reverse engineering`, `#game development`, `#interoperability`, `#nintendo 64`, `#open source`

---

<a id="item-11"></a>
## [微软推出 MAI-Cyber-1-Flash 网络安全模型](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) ⭐️ 6.0/10

微软推出了 MAI-Cyber-1-Flash，这是一个轻量级网络安全 AI 模型，旨在处理其 MDASH 多智能体漏洞修复系统中高达 90%的任务，减少对 GPT-5.4 等大型模型的依赖。 该模型承诺将网络安全成本降低一半，同时让先进的 AI 安全技术更易获取，可能改变组织处理漏洞检测和修复的方式。 MAI-Cyber-1-Flash 集成到 MDASH 中，MDASH 协调超过 100 个专门的 AI 智能体。它高效处理常见任务，仅将最昂贵的模型用于 10%的异常困难任务。

hackernews · migmartri · 7月27日 16:52 · [社区讨论](https://news.ycombinator.com/item?id=49072361)

**背景**: MDASH（多智能体漏洞识别与修复）是微软的系统，使用一组 AI 智能体进行代码漏洞检测。MAI-Cyber-1-Flash 是经过微调的蒸馏模型，专门用于网络安全，与谷歌的 Gemini 3.5 Flash Cyber 等产品竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/">Introducing MAI-Cyber-1-Flash inside MDASH | Microsoft AI</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/07/27/microsoft-mai-cyber-1-flash-ai-model/">Microsoft unveils MAI-Cyber-1-Flash, promises cybersecurity AI at half the cost - Help Net Security</a></li>

</ul>
</details>

**社区讨论**: 社区评论持怀疑态度，质疑该模型的‘数万亿信号’优势是否真正转化为更好的安全性，还是仅擅长修复微软产品。用户还对访问方式表示沮丧，并将其与微软过去的 AI 失误（如 Phi）进行比较。

**标签**: `#cybersecurity`, `#AI`, `#Microsoft`, `#machine learning`, `#announcement`

---