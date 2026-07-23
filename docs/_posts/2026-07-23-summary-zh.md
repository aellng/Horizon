---
layout: default
title: "Horizon Summary: 2026-07-23 (ZH)"
date: 2026-07-23
lang: zh
---

> 从 33 条内容中筛选出 22 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：AI、Generative Models、image generation、open-source、Training from Scratch。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[AI 图像生成通过鹈鹕骑自行车测试发现偏见](https://dylancastillo.co/posts/pelicanmaxxing.html)**
2. **[Mix Studio：免费开源的 ComfyUI 工作流界面](https://www.reddit.com/r/StableDiffusion/comments/1v3rjy1/mix_studio_a_free_open_source_ai_workspace_for/)**
3. **[从头训练图像模型第二部分：各种失败](https://www.reddit.com/r/StableDiffusion/comments/1v3mlnl/im_training_an_image_model_from_scratch_part_2_i/)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [陶哲轩用 ChatGPT 探索雅可比猜想反例](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [Reddit 限制纯 HTML 以阻止爬虫，引发用户不满](https://www.cole-k.com/2026/07/21/reddit/)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [GigaToken：通过 SIMD 实现 1000 倍更快的 LLM 分词](https://github.com/marcelroed/gigatoken/)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：AI 图像生成通过鹈鹕骑自行车测试发现偏见

**关联新闻**: [AI 图像生成通过鹈鹕骑自行车测试发现偏见](https://dylancastillo.co/posts/pelicanmaxxing.html)

**切入角度**: Dylan Castillo 测试了七个 AI 实验室生成的 1008 张 SVG 图像，涵盖八种动物和六种交通工具，发现所有 21 张鹈鹕骑自行车的图像都朝右，这种一致性在其他动物-交通工具组合中未曾出现。 这项调查揭示了 AI 图像生成中微妙的朝向偏见，可能源于训练数据的惯例（例如自行车摄影始终展示右侧的传动系统），并展示了一个可复现的基准来检测模型偏见。 作者从七个实验室（包括 OpenAI、Google、Anthropic）生成了 1008 张 SVG，涉及八种动物和六种交通工具；60%的图像朝右，但鹈鹕骑自行车是唯一一个所有实例都朝右的组合，排除了简单的训练数据记忆。

**可延展方向**: 像 DALL·E、Midjourney 和 Stable Diffusion 这样的 AI 图像生成模型根据文本提示生成图像，但常常会继承训练数据中的偏见。'pelicanmaxxing'基准测试的灵感来自 Simon Willison 反复生成'鹈鹕骑自行车'SVG 来测试模型是否过度拟合热门提示。这项系统分析确认了自行车特有的朝向偏见，很可能源于自行车摄影中常见显示传动系统（右侧）的习惯。

---

### 选题 2：Mix Studio：免费开源的 ComfyUI 工作流界面

**关联新闻**: [Mix Studio：免费开源的 ComfyUI 工作流界面](https://www.reddit.com/r/StableDiffusion/comments/1v3rjy1/mix_studio_a_free_open_source_ai_workspace_for/)

**切入角度**: Mix Studio v1.0.1 已发布，作为一款免费开源图形界面运行在 ComfyUI 之上，为 Flux 2 Klein、Qwen Image Edit 和 Wan 2.2 等模型提供精选工作流和一键安装。 它通过提供类似应用程序的精美体验，大大降低了使用 ComfyUI 强大引擎的门槛，让初学者和专业人士都能通过桌面或移动设备轻松进行高级 AI 图像与视频生成。 该界面包含区域提示、LoRA 管理、多图像编辑、带帧插值的视频后期处理以及内置依赖管理器等功能；目前支持 Windows 和 NVIDIA GPU，最低需要 4 GB VRAM。

**可延展方向**: ComfyUI 是一个基于节点的开源界面，用于使用扩散模型构建生成式 AI 工作流，但其复杂性可能让普通用户望而却步。Mix Studio 通过更直观的 GUI 封装了 ComfyUI，同时复用现有模型和安装，简化了创作流程。

---

### 选题 3：从头训练图像模型第二部分：各种失败

**关联新闻**: [从头训练图像模型第二部分：各种失败](https://www.reddit.com/r/StableDiffusion/comments/1v3mlnl/im_training_an_image_model_from_scratch_part_2_i/)

**切入角度**: 作者详细描述了在单张 RTX 5090 上从头训练文本到图像模型的过程，揭示了浪费 92,000 步的 bug 以及导致模型只能生成雪色斑块的错误。 这种真实的排查经验为在有限硬件上训练生成模型的从业者提供了宝贵的实践教训，表明许多失败源于平凡的代码问题而非深度学习问题。 作者使用了 37,000 个图像-标题对的小数据集，后来扩展到 71 个文件，并发现训练损失与感知的图像质量无关。备份逻辑中的复制粘贴错误每 1,000 步重置模型，浪费了 92,000 步训练。

**可延展方向**: 变分自编码器（VAE）将图像压缩到潜在空间，但不能从文本生成图像。像 Stable Diffusion 这样的文本到图像生成器使用文本编码器（如 CLIP）将标题转换为嵌入，然后输入扩散模型生成图像。

---

1. [陶哲轩用 ChatGPT 探索雅可比猜想反例](#item-1) ⭐️ 9.0/10
2. [GigaToken：通过 SIMD 实现 1000 倍更快的 LLM 分词](#item-2) ⭐️ 8.0/10
3. [Bento：一个完整的离线 HTML 幻灯片编辑器](#item-3) ⭐️ 8.0/10
4. [每个人都应该了解 SIMD——性能优化文章](#item-4) ⭐️ 8.0/10
5. [Reddit 限制纯 HTML 以阻止爬虫，引发用户不满](#item-5) ⭐️ 8.0/10
6. [居家面试项目中隐藏恶意 Git 钩子](#item-6) ⭐️ 8.0/10
7. [融合 JoyAI-Echo 与 LTX-2.3 实现人脸与声音一致性](#item-7) ⭐️ 8.0/10
8. [AI 图像生成通过鹈鹕骑自行车测试发现偏见](#item-8) ⭐️ 7.0/10
9. [关于自己动手与让 AI 代劳的哲学随笔](#item-9) ⭐️ 7.0/10
10. [初创公司 PostgreSQL 生存指南](#item-10) ⭐️ 7.0/10
11. [重返 Kagi：用户回归付费搜索引擎](#item-11) ⭐️ 7.0/10
12. [Ghost Cut 提出原子化剪切粘贴](#item-12) ⭐️ 7.0/10
13. [Mix Studio：免费开源的 ComfyUI 工作流界面](#item-13) ⭐️ 7.0/10
14. [从头训练图像模型第二部分：各种失败](#item-14) ⭐️ 7.0/10
15. [Mage-Flow：微软亚洲研究院推出的高效 40 亿参数 T2I 模型](#item-15) ⭐️ 7.0/10
16. [SenseNova-U1-Infographic-V3：真实信息图编辑测试](#item-16) ⭐️ 7.0/10
17. [SD WebUI Forge Neo 的 Image2Prompt 扩展](#item-17) ⭐️ 7.0/10
18. [Joy Captioner 训练数据被发现包含成人内容水印](#item-18) ⭐️ 7.0/10
19. [科技记者约翰·C·德沃夏克去世，享年 80 岁](#item-19) ⭐️ 6.0/10
20. [对丑陋的人工智能生成菜单和海报的批评](#item-20) ⭐️ 6.0/10
21. [用户分享 Clean Plate LoRA 视频物体移除示例](#item-21) ⭐️ 6.0/10
22. [Krea 2 Identity Edit LoRA v1.2 展示单句提示身份编辑](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [陶哲轩用 ChatGPT 探索雅可比猜想反例](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) ⭐️ 9.0/10

陶哲轩使用 ChatGPT 研究并找到了雅可比猜想（代数几何中一个长期未解的问题）的反例。这场公开分享的对话展示了 AI 如何辅助高级数学研究。 这展示了大型语言模型作为专家数学家协作工具的潜力，可能加速发现和问题解决。同时凸显了领域专业知识在有效提示 AI 以获得突破性成果中的重要性。 反例涉及一个特殊构造的多项式，而非暴力搜索，陶哲轩精确且充满术语的提问对引导 ChatGPT 至关重要。这段对话凸显了在专家引导下，AI 能够处理高级数学工具。

hackernews · gmays · 7月22日 17:30 · [社区讨论](https://news.ycombinator.com/item?id=49010345)

**背景**: 雅可比猜想断言：如果从 n 维空间到其自身的多项式映射的雅可比行列式是非零常数，则该映射具有多项式逆映射。该猜想自 1884 年提出以来一直悬而未决，且以大量错误证明而闻名。2026 年，有人使用另一 AI 模型 Claude 找到了三维及以上的反例，但二维情形仍未解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://www.math.purdue.edu/~ttm/jacobian.html">Jacobian Conjecture</a></li>

</ul>
</details>

**社区讨论**: 评论者对对话记录感到着迷，指出陶哲轩高度具体且专家级的提问是从中提取新见解的关键。有用户强调反例在结构上很精巧，并非暴力搜索的结果，并且对话模式反映了专家如何在自身领域使用大语言模型。

**标签**: `#AI-assisted research`, `#mathematics`, `#Jacobian conjecture`, `#ChatGPT`, `#machine learning`

---

<a id="item-2"></a>
## [GigaToken：通过 SIMD 实现 1000 倍更快的 LLM 分词](https://github.com/marcelroed/gigatoken/) ⭐️ 8.0/10

GigaToken 是一个新的开源工具，声称通过 SIMD 优化的预分词和缓存策略，将大语言模型的分词速度提升高达 1000 倍。 这一加速对于离线预训练数据准备尤为重要，因为对海量数据集进行分词可能耗时且成本高昂。它能够加快训练语料库的迭代周期，从而降低成本并缩短开发时间。 GigaToken 通过 SIMD 指令和激进的预分词映射缓存来优化预分词，避免了使用缓慢的正则表达式引擎。它在不同的 CPU 架构（x86 和 ARM）以及多种分词器上均能实现一致的加速效果。

hackernews · syrusakbary · 7月22日 17:20 · [社区讨论](https://news.ycombinator.com/item?id=49010167)

**背景**: 分词将原始文本转换为 LLM 输入所需的标记（子词/单词）。预分词是分词前的初步步骤，将文本分割成更小的块（如单词）。SIMD（单指令多数据流）是一种并行计算技术，能同时对多个数据点执行相同操作，GigaToken 利用它来加速预分词。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SIMD">SIMD</a></li>
<li><a href="https://huggingface.co/learn/llm-course/en/chapter6/4">Normalization and pre-tokenization · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区对如此大的加速感到印象深刻，有用户称其‘令人难以置信’。不过，多位评论者指出分词在推理时间中占比不到 0.1%，因此优化主要对离线预训练数据准备有益。也有关于过度优化次要组件的调侃，但整体评价积极，肯定了工程上付出的努力。

**标签**: `#tokenization`, `#LLM`, `#optimization`, `#SIMD`, `#pretraining`

---

<a id="item-3"></a>
## [Bento：一个完整的离线 HTML 幻灯片编辑器](https://bento.page/slides/) ⭐️ 8.0/10

Bento 是一个自包含的 HTML 文件（约 560KB），内置完整的幻灯片编辑器、查看器、数据存储和实时协作功能，无需安装即可离线运行。它采用 base64 压缩和加密盲中继实现共享编辑，无需云服务器。 该工具通过提供便携、自包含的离线解决方案，挑战了传统的演示软件，可通过电子邮件或 AirDrop 分享。它可能使幻灯片创作民主化，尤其适合寻求轻量级、零设置协作的开发者与团队。 该文件将幻灯片数据嵌入为 JSON 块，应用以 base64 blob 形式嵌入，浏览器通过 DecompressionStream 解压。协作使用加密盲中继，中继无法看到数据，整个项目在 GitHub 上以 MIT 许可证发布。

hackernews · starfallg · 7月22日 15:19 · [社区讨论](https://news.ycombinator.com/item?id=49008211)

**背景**: 单文件 Web 应用将所有 HTML、CSS、JavaScript 和资源打包在一个.html 文件中，无需服务器即可离线使用和分发。Claude Code 是用于开发 Bento 的 AI 编程助手。加密盲中继确保中继服务器无法读取传输的数据，在实时协作中保护隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blinding_(cryptography)">Blinding (cryptography) - Wikipedia</a></li>
<li><a href="https://github.com/jonathanhudak/Single-File-Web-App">GitHub - jonathanhudak/Single-File-Web-App: No modules, no compilation, just one file · GitHub</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: 创建者分享了关于 JSON 数据块和 base64 压缩的技术细节。一位评论者报告称，在多人同时操作留言簿时，其 M1 Mac 出现死机，提示了潜在的性能问题。其他人赞扬了这一概念，并分享了自己构建的类似单文件工具。

**标签**: `#single-file-application`, `#presentation-tool`, `#web-development`, `#offline-first`, `#hackernews-show`

---

<a id="item-4"></a>
## [每个人都应该了解 SIMD——性能优化文章](https://mitchellh.com/writing/everyone-should-know-simd) ⭐️ 8.0/10

Mitchell Hashimoto 发表文章，主张所有开发者都应了解 SIMD（单指令多数据）这一关键性能优化技术。 SIMD 能在数据并行任务中带来显著加速，理解它有助于开发者编写更高效的代码。该文章引发了关于 SIMD 实用性与其他优化策略的讨论。 现代编译器擅长自动向量化，但可能因假设或数据依赖分支而失败；检查编译器优化报告通常比手动编写 SIMD 代码更有价值。

hackernews · WadeGrimridge · 7月22日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49010648)

**背景**: SIMD 是单指令多数据的缩写，是一种并行处理技术，CPU 使用向量寄存器同时对多个数据元素执行相同操作。它常用于多媒体处理、科学计算和游戏开发中，以加速重复性计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@anilcangulkaya7/what-is-simd-and-how-to-use-it-3d1125faac89">What is SIMD and how to use it. SIMD has been around for... | Medium</a></li>
<li><a href="https://stackoverflow.com/questions/1422149/what-is-vectorization">simd - What is "vectorization"? - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 社区评论观点不一：有人强调在进行 SIMD 优化之前应先进行面向数据的设计，也有人认为 99%的开发者应忽略 SIMD，因为存在更易优化的低垂果实。还有评论强调了检查编译器优化报告的价值。

**标签**: `#SIMD`, `#performance optimization`, `#vectorization`, `#programming`, `#low-level`

---

<a id="item-5"></a>
## [Reddit 限制纯 HTML 以阻止爬虫，引发用户不满](https://www.cole-k.com/2026/07/21/reddit/) ⭐️ 8.0/10

Reddit 已限制对其页面的纯 HTML 版本的访问，使得爬虫在不使用 JavaScript 渲染的情况下更难提取数据。此举实际上针对的是依赖简单 HTML 的 old.reddit.com，被视为逐步淘汰经典界面的步骤。 这一变化通过迫使用户和爬虫使用更重的 JavaScript 渲染页面，削弱了互联网的开放性，影响了自动化工具和偏好轻量浏览的用户。这也引发了对 Reddit 优先考虑投资者利益而非社区的担忧，尤其是在 LLM 生成内容威胁有机讨论的背景下。 爬取纯 HTML 更便宜且更容易，而 JavaScript 渲染需要无头浏览器或基于 AI 的工具。尽管 Reddit 声称出于安全考虑，但用 JavaScript 减慢爬虫效率不高，因为攻击者可以水平扩展；真实动机似乎是淘汰 old.reddit。

hackernews · montroser · 7月22日 12:32 · [社区讨论](https://news.ycombinator.com/item?id=49005747)

**背景**: 网页爬虫传统上通过简单的 HTTP 请求获取纯 HTML 源代码。像新版 Reddit 这样依赖 JavaScript 的网站需要渲染引擎执行脚本后才能获取数据，增加了复杂性和成本。老版 Reddit（old.reddit.com）是仍提供纯 HTML 的经典界面，因此容易受到爬虫攻击。Reddit 在 2018 年的重新设计中引入了大量 JavaScript，并且公司一直在逐步减少对旧界面的支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.firecrawl.dev/glossary/web-scraping-apis/what-is-javascript-rendering-web-scraping">What is JavaScript rendering in web scraping? | Firecrawl Glossary</a></li>
<li><a href="https://www.scrapingbee.com/blog/scraping-javascript-rendered-web-pages/">Effortless Guide to Scraping JavaScript Rendered Web Pages with Python | ScrapingBee</a></li>
<li><a href="https://oldreddit.xyz/">oldreddit - Access Classic Reddit Interface & Design</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持批评态度，认为 Reddit 的安全理由是淘汰 old.reddit 的借口。一些人对 Reddit 质量因机器人和 LLM 回复感到失望，另一些人则警告身份验证和平台控制的更大趋势。大家一致认为 Reddit 的价值已经下降。

**标签**: `#reddit`, `#scraping`, `#web accessibility`, `#LLM`, `#internet censorship`

---

<a id="item-6"></a>
## [居家面试项目中隐藏恶意 Git 钩子](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/) ⭐️ 8.0/10

一名开发者发现，一个居家编程面试项目中隐藏着恶意的 Git 钩子，当受害者执行 git commit 时，该钩子会执行远程负载，揭示了一种针对求职者的新型社会工程攻击手段。 这种攻击利用了求职者对合法招聘流程的信任，对经常不加审查就运行潜在雇主代码的软件开发人员构成严重安全威胁。它强调了开发者在执行代码前检查所有文件（包括隐藏配置文件）的必要性。 恶意钩子隐藏在 .git/hooks 目录中，先检查受害者的操作系统，然后静默执行来自原始 IP 地址的负载。该攻击利用了开发者常见做法：直接运行 git 命令却不检查钩子内容。

hackernews · CITIZENDOT · 7月22日 20:33 · [社区讨论](https://news.ycombinator.com/item?id=49013036)

**背景**: Git 钩子是在特定 Git 事件（如提交或推送）发生时自动运行的自定义脚本。虽然对自动化很有用，但也可能被滥用来执行任意代码。攻击者越来越多地将恶意软件嵌入居家面试项目中，例如“Contagious Interview”攻击活动就利用 SVG 文件中的隐写术。开发者应始终检查 .git/hooks 目录，并谨慎运行不受信任的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks">Git - Git Hooks</a></li>
<li><a href="https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography">Contagious Interview malware in SVG images: DPRK campaign - Elastic</a></li>
<li><a href="https://github.com/muasif80/git-hook-guard">GitHub - muasif80/ git - hook -guard: Auto-scans opened Git repositories...</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了遭遇类似攻击的个人经历，其中一位用户描述了一次精心策划的面试骗局：攻击者关闭摄像头并带有口音交流。其他人指出这成为一种反复出现的趋势，并讨论了在 VSCode 和 Git 等工具中加强防护措施的必要性。

**标签**: `#security`, `#malware`, `#social-engineering`, `#git`, `#cybersecurity`

---

<a id="item-7"></a>
## [融合 JoyAI-Echo 与 LTX-2.3 实现人脸与声音一致性](https://www.reddit.com/r/StableDiffusion/comments/1v3pj1t/i_merged_joyaiechos_crossshot_character_memory/) ⭐️ 8.0/10

一位用户将 JoyAI-Echo 的跨镜头角色记忆与 LTX-2.3 的语音能力融合，使得一句重复的句子就能在视频各镜头间保持人脸与声音一致。融合模型以多种权重格式（bf16、fp8、Q8、Q5、INT8）发布，并附有 ComfyUI 工作流和一个免费的 Hugging Face 演示 Space。 这解决了 AI 视频生成中的一个关键挑战：跨镜头保持角色身份，这对叙事至关重要。通过结合两个开源模型的优势，它使得高质量、一致的视频生成变得普及，无需昂贵的 TTS 或配音。 该技术从每个模型中取其强项：JoyAI-Echo 负责面部一致性，LTX-2.3-distilled 负责语音。提供了五种适配不同硬件的构建，从适用于 16 GB GPU 的 Q5 GGUF（15.5 GB）到 bf16 参考版（43 GB），所有构建均通过相同的激活比较而非肉眼观察渲染进行验证。

reddit · r/StableDiffusion · /u/Minute_Eye_6270 · 7月22日 18:58

**背景**: JoyAI-Echo 是京东智未来学院开发的开源模型，可生成最长 5 分钟的多镜头视频并同步音频，但其语音质量较弱。LTX-2.3-distilled 是 Lightricks 的 LTX-2.3 模型的快速版本，以良好的语音质量著称，但跨镜头时会出现面容漂移。跨镜头角色记忆是一种通过记忆库来维持角色身份的技术，其灵感常源于 StoryMem 等研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://joyai-echo.net/joyai-echo">JoyAI - Echo Open-Source Long Audio-Visual Model</a></li>
<li><a href="https://huggingface.co/Lightricks/LTX-2.3">Lightricks/LTX-2.3 · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2512.19539">StoryMem: Multi-shot Long Video Storytelling with Memory</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#character consistency`, `#model merging`, `#Stable Diffusion`, `#open-source`

---

<a id="item-8"></a>
## [AI 图像生成通过鹈鹕骑自行车测试发现偏见](https://dylancastillo.co/posts/pelicanmaxxing.html) ⭐️ 7.0/10

Dylan Castillo 测试了七个 AI 实验室生成的 1008 张 SVG 图像，涵盖八种动物和六种交通工具，发现所有 21 张鹈鹕骑自行车的图像都朝右，这种一致性在其他动物-交通工具组合中未曾出现。 这项调查揭示了 AI 图像生成中微妙的朝向偏见，可能源于训练数据的惯例（例如自行车摄影始终展示右侧的传动系统），并展示了一个可复现的基准来检测模型偏见。 作者从七个实验室（包括 OpenAI、Google、Anthropic）生成了 1008 张 SVG，涉及八种动物和六种交通工具；60%的图像朝右，但鹈鹕骑自行车是唯一一个所有实例都朝右的组合，排除了简单的训练数据记忆。

hackernews · dcastm · 7月22日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=49010129)

**背景**: 像 DALL·E、Midjourney 和 Stable Diffusion 这样的 AI 图像生成模型根据文本提示生成图像，但常常会继承训练数据中的偏见。'pelicanmaxxing'基准测试的灵感来自 Simon Willison 反复生成'鹈鹕骑自行车'SVG 来测试模型是否过度拟合热门提示。这项系统分析确认了自行车特有的朝向偏见，很可能源于自行车摄影中常见显示传动系统（右侧）的习惯。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=47797357">I wonder when pelican riding a bicycle will be useless... | Hacker News</a></li>
<li><a href="https://locus.sh/blogs/exploring-bias-in-ai-image-generation/">Exploring Bias in AI Image Generation - Locus</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意这一发现，指出自行车摄影惯例解释了朝右的偏见——传动系统在右侧，因此专业照片总是展示那一侧。一些人觉得有可能抓住实验室在这个特定基准上作弊很有趣，同时欣赏其稳健的方法论（8×6 组合共 1008 张图像）。

**标签**: `#AI`, `#image generation`, `#bias`, `#benchmark`, `#machine learning`

---

<a id="item-9"></a>
## [关于自己动手与让 AI 代劳的哲学随笔](https://beej.us/blog/data/ai-making/) ⭐️ 7.0/10

Beej 的博客文章探讨了亲自动手制作与让 AI 代劳之间的哲学区别，质疑了在 AI 辅助下创造与自豪感的本质。 这一讨论触及了软件工程和创造力的核心价值，影响着开发者和艺术家在强大生成式 AI 时代如何看待自己的工作。 文章使用了如雇佣园林公司建造花园等类比，提出了当工作外包给 AI 时关于所有权和自豪感的疑问。

hackernews · erikschoster · 7月22日 15:33 · [社区讨论](https://news.ycombinator.com/item?id=49008440)

**背景**: Beej 以其技术写作和哲学反思而闻名。这篇文章延续了他对 AI 对人类创造力影响以及'制作'意义的探讨。

**社区讨论**: 评论者表达了复杂的感受：有人为自己使用 LLM 而不写代码感到自豪，也有人怀念手动创造的乐趣，担忧人类独创性的丧失。一个共同的主题是效率与创造内在满足感之间的张力。

**标签**: `#AI`, `#creativity`, `#software engineering`, `#philosophy of making`

---

<a id="item-10"></a>
## [初创公司 PostgreSQL 生存指南](https://hatchet.run/blog/postgres-survival-guide) ⭐️ 7.0/10

一篇题为《初创公司 Postgres 生存指南》的博文在 Hatchet 博客上发布，为早期初创企业提供了关于 UUID、锁、ORM 等 PostgreSQL 常见陷阱的实用建议。 该指南解决了许多初创公司面临的常见但关键的 PostgreSQL 问题，对于构建数据密集型应用的工程师来说是宝贵的资源。活跃的社区讨论提供了修正和更深入的见解，增强了文章的实用性。 社区评论者建议使用 UUIDv7 而非 v4，确保确定性锁排序以避免死锁，并质疑文章未提及备份策略。批评者还建议避免使用 ORM，并在许多情况下优先使用序列主键。

hackernews · abelanger · 7月22日 12:36 · [社区讨论](https://news.ycombinator.com/item?id=49005787)

**背景**: PostgreSQL 是一种广泛使用的开源关系型数据库，以其稳健性和高级特性著称。初创公司常采用 PostgreSQL 的可扩展性，但会遭遇锁竞争、ORM 使用不当以及标识符选择不佳等挑战，本指南旨在缓解这些问题。

**社区讨论**: 社区评论提供了宝贵的修正和扩展：一位用户指出缺少备份策略，另一位推荐使用 UUIDv7 而非 UUIDv4 以及确定性锁排序，其他评论者则反对在高流量表中使用 ORM 和级联删除。整体氛围是赞赏但带有批判性，既强调了指南的实用价值，又指出了其中的遗漏。

**标签**: `#postgresql`, `#databases`, `#startups`, `#best-practices`

---

<a id="item-11"></a>
## [重返 Kagi：用户回归付费搜索引擎](https://blog.melashri.net/micro/back-to-kagi/) ⭐️ 7.0/10

一位用户发布了题为《重返 Kagi》的博客文章，详细讲述了他们在离开一段时间后决定重新使用 Kagi 搜索引擎的决定，这篇文章在 Hacker News 上引发了热烈讨论，获得了超过 180 个点赞和 150 条评论。 这场讨论凸显了用户对 Google 等主导搜索引擎的付费、无广告替代方案日益增长的兴趣，并反映出人们对搜索质量、隐私和控制的担忧。社区的积极参与表明有大量用户正在寻求更好的搜索体验。 Kagi 提供每月 10 美元的无限制方案和每月 5 美元、限制 300 次搜索的方案，功能包括 Vim 键绑定、明确选择 AI 选项以及屏蔽或提升特定网站的能力。用户指出，虽然 Kagi 本身仍然很好，但网络内容的整体质量下降了，这影响了搜索结果。

hackernews · speckx · 7月22日 13:08 · [社区讨论](https://news.ycombinator.com/item?id=49006195)

**背景**: Kagi 是一款付费无广告的搜索引擎，于 2021 年推出，总部位于加利福尼亚州帕洛阿尔托。与广告支持的搜索引擎不同，Kagi 完全通过订阅收入运营，不追踪用户也不出售用户的注意力。其名称源自日语中的“键”。讨论中还提到了 Staan.ai，这是一个由 Ecosia 和 Qwant 构建的欧洲搜索索引，被视为一个潜在的替代选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kagi_(search_engine)">Kagi (search engine)</a></li>
<li><a href="https://kagi.com/html/welcome">Kagi Search - A Premium Search Engine</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者表达了褒贬不一的看法：许多人赞赏 Kagi 的质量、隐私和可定制性，但有些用户认为每月 10 美元的价格过高，希望能有更实惠的方案。其他人指出，即使使用 Kagi，网络内容质量的整体下降也限制了搜索体验。此外，还有人对 Staan.ai 等替代方案表现出兴趣。

**标签**: `#search-engine`, `#Kagi`, `#privacy`, `#community-discussion`, `#web-quality`

---

<a id="item-12"></a>
## [Ghost Cut 提出原子化剪切粘贴](https://ishmael.textualize.io/blog/ghost-cut/) ⭐️ 7.0/10

作者在一篇博文中提出了“幽灵剪切”（Ghost Cut）机制，通过使选中文本变淡并在粘贴时才将其放入剪贴板，从而实现剪切操作的原子化。 该提案挑战了长期以来剪切粘贴非原子化的 UX 惯例，有望改善撤销行为并减少文本编辑工作流中的意外数据丢失。 作者建议，在按下 Ctrl+X 后，文本变为非活动状态并变淡，直到用户粘贴或明确复制之前，剪贴板中不会放入任何内容，从而使操作可逆且安全。

hackernews · willm · 7月22日 14:43 · [社区讨论](https://news.ycombinator.com/item?id=49007626)

**背景**: 传统的剪切粘贴操作不是原子化的：剪切会删除文本并将其放入剪贴板，而粘贴则从剪贴板复制。如果用户在剪切后撤销，文本会恢复，但剪贴板仍保留旧内容，这可能导致混淆。Ghost Cut 旨在统一这两个动作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/willmcgugan_introducing-ghost-cut-or-why-cut-paste-activity-7483165474244018177-disz">Introducing Ghost Cut - or why Cut & Paste is broken everywhere...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一；有些人认为非原子性是一个特性而非缺陷，因为他们依赖撤销不影响剪贴板的功能。其他人则欣赏这一提案，因为它能让意外剪切不那么具有破坏性，但也提出了关于多次粘贴行为和无障碍性的问题。

**标签**: `#user experience`, `#text editing`, `#clipboard`, `#HCI`, `#software design`

---

<a id="item-13"></a>
## [Mix Studio：免费开源的 ComfyUI 工作流界面](https://www.reddit.com/r/StableDiffusion/comments/1v3rjy1/mix_studio_a_free_open_source_ai_workspace_for/) ⭐️ 7.0/10

Mix Studio v1.0.1 已发布，作为一款免费开源图形界面运行在 ComfyUI 之上，为 Flux 2 Klein、Qwen Image Edit 和 Wan 2.2 等模型提供精选工作流和一键安装。 它通过提供类似应用程序的精美体验，大大降低了使用 ComfyUI 强大引擎的门槛，让初学者和专业人士都能通过桌面或移动设备轻松进行高级 AI 图像与视频生成。 该界面包含区域提示、LoRA 管理、多图像编辑、带帧插值的视频后期处理以及内置依赖管理器等功能；目前支持 Windows 和 NVIDIA GPU，最低需要 4 GB VRAM。

reddit · r/StableDiffusion · /u/blackmixture · 7月22日 20:09

**背景**: ComfyUI 是一个基于节点的开源界面，用于使用扩散模型构建生成式 AI 工作流，但其复杂性可能让普通用户望而却步。Mix Studio 通过更直观的 GUI 封装了 ComfyUI，同时复用现有模型和安装，简化了创作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>
<li><a href="https://bfl.ai/models/flux-2-klein">FLUX . 2 [ klein ] - Fast, Efficient Image Generation | Black Forest Labs</a></li>
<li><a href="https://qwen.ai/blog?id=qwen-image-edit">Qwen-Image-Edit</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#ComfyUI`, `#image generation`, `#workflow`

---

<a id="item-14"></a>
## [从头训练图像模型第二部分：各种失败](https://www.reddit.com/r/StableDiffusion/comments/1v3mlnl/im_training_an_image_model_from_scratch_part_2_i/) ⭐️ 7.0/10

作者详细描述了在单张 RTX 5090 上从头训练文本到图像模型的过程，揭示了浪费 92,000 步的 bug 以及导致模型只能生成雪色斑块的错误。 这种真实的排查经验为在有限硬件上训练生成模型的从业者提供了宝贵的实践教训，表明许多失败源于平凡的代码问题而非深度学习问题。 作者使用了 37,000 个图像-标题对的小数据集，后来扩展到 71 个文件，并发现训练损失与感知的图像质量无关。备份逻辑中的复制粘贴错误每 1,000 步重置模型，浪费了 92,000 步训练。

reddit · r/StableDiffusion · /u/Creative-Listen-6847 · 7月22日 17:18

**背景**: 变分自编码器（VAE）将图像压缩到潜在空间，但不能从文本生成图像。像 Stable Diffusion 这样的文本到图像生成器使用文本编码器（如 CLIP）将标题转换为嵌入，然后输入扩散模型生成图像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@judyyes10/generate-images-using-variational-autoencoder-vae-4d429d9bdb5">Generate Images Using Variational Autoencoder (VAE) | by DiShi Zhu | Medium</a></li>
<li><a href="https://blog.codescv.com/stable-diffusion-4.html">Stable Diffusion from Begginer to Master (4) Text Encoder and...</a></li>

</ul>
</details>

**标签**: `#Generative Models`, `#Training from Scratch`, `#Stable Diffusion`, `#Image Generation`, `#Deep Learning`

---

<a id="item-15"></a>
## [Mage-Flow：微软亚洲研究院推出的高效 40 亿参数 T2I 模型](https://www.reddit.com/r/StableDiffusion/comments/1v33af2/mageflow_an_efficient_nativeresolution_foundation/) ⭐️ 7.0/10

微软亚洲研究院发布了 Mage-Flow，一个紧凑的 40 亿参数基础模型，用于文本到图像生成和指令驱动编辑，支持原生分辨率输出，仅需 4 步推理即可交互。 该模型推动了任意分辨率下高效、高质量的图像生成，有望降低计算成本并实现实时编辑应用。 Mage-Flow 在原生分辨率下运行，可以生成任意尺寸的图像而无需缩放，并且支持在单一流程中进行指令驱动的编辑。

reddit · r/StableDiffusion · /u/FizzarolliAI · 7月22日 02:38

**背景**: 传统的文本到图像模型通常需要固定的正方形分辨率和多次推理步骤。原生分辨率合成通过处理可变长度序列克服了这一限制，允许以自然宽高比生成图像。Mage-Flow 仅需 4 步即可高效实现这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.github.io/Mage/flow/">Mage-Flow: An Efficient Native-Resolution Foundation ...</a></li>
<li><a href="https://huggingface.co/microsoft/Mage-Flow">microsoft/Mage-Flow - Hugging Face</a></li>

</ul>
</details>

**标签**: `#image generation`, `#AI`, `#foundation model`, `#Microsoft`, `#efficiency`

---

<a id="item-16"></a>
## [SenseNova-U1-Infographic-V3：真实信息图编辑测试](https://www.reddit.com/r/StableDiffusion/comments/1v3f2lx/tested_sensenovau1infographicv3s_editing_on_a/) ⭐️ 7.0/10

一位 Reddit 用户测试了 SenseNova-U1-Infographic-V3 的新编辑功能，成功演示了局部内容插入和全局风格替换，无需重新生成整个信息图。 这解决了 AI 信息图生成中的一个主要痛点：无法在不完全重做的情况下进行小修改（如修正错别字）。它显著提高了工作流程效率和用户控制力。 测试 1 向复古电脑屏幕添加像素文字，保持了正确的透视和颗粒噪点；测试 2 将风格改为乐高和中国新年风格，配以像素字体。V3 还支持基于 bbox 的文字替换、自然语言编辑和布局美化。

reddit · r/StableDiffusion · /u/No-Measurement-5858 · 7月22日 12:43

**背景**: SenseNova-U1 是一系列根据文本描述生成信息图的模型。之前的版本缺乏编辑能力，用户进行任何更改都必须重新运行整个生成过程。V3 引入了原生编辑范式，允许在保留图像其余部分的同时进行定向修改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/sensenova/sensenova-u1-infographic-v3">SenseNova U 1 Infographic V 3 - a Hugging Face Space by sensenova</a></li>
<li><a href="https://github.com/OpenSenseNova/SenseNova-U1">GitHub - OpenSenseNova/ SenseNova - U 1 : SenseNova - U series...</a></li>

</ul>
</details>

**标签**: `#AI`, `#image generation`, `#infographics`, `#editing`, `#StableDiffusion`

---

<a id="item-17"></a>
## [SD WebUI Forge Neo 的 Image2Prompt 扩展](https://www.reddit.com/r/StableDiffusion/comments/1v3sm34/image2prompt_visiontoprompt_tab_for_sd_webui/) ⭐️ 7.0/10

Stable Diffusion WebUI Forge Neo 新增了一个 Image2Prompt 标签页，允许用户上传图片并通过 Qwen2-VL 和 Florence-2 等视觉语言模型生成提示词，并可一键发送到 txt2img 或 img2img。 该扩展填补了 Forge Neo 生态中的功能缺失，帮助 Stable Diffusion 用户直接在界面内逆向工程提示词或为图片添加说明，从而节省时间并简化工作流程。 支持的模型包括 Qwen/Qwen2-VL-2B-Instruct（推荐，约 5 GB 显存）、Qwen2.5-VL-3B-Instruct（约 7 GB）、Qwen2-VL-7B-Instruct（约 16 GB）以及 Microsoft Florence-2 基础版/大号版（轻量，约 1–3 GB，仅生成说明）。模型在首次使用时从 Hugging Face 自动下载。

reddit · r/StableDiffusion · /u/adeliogentile · 7月22日 20:45

**背景**: Stable Diffusion WebUI Forge Neo 是 Forge 项目的延续，基于 Gradio 4.40.0 构建，为 Stable Diffusion 模型的图像生成提供现代界面。视觉语言模型（如阿里巴巴的 Qwen2-VL 和微软的 Florence-2）结合了视觉变换器和大语言模型，能够理解和描述图像。这些模型可以从视觉输入生成详细的文本提示，因此在 AI 艺术工具中可用于图片说明和提示词工程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Stable_Diffusion_WebUI_Forge_Neo">Stable Diffusion WebUI Forge Neo</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/microsoft/Florence-2-base">microsoft/Florence-2-base · Hugging Face</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#image-to-prompt`, `#vision-language model`, `#webui extension`, `#Forge Neo`

---

<a id="item-18"></a>
## [Joy Captioner 训练数据被发现包含成人内容水印](https://www.reddit.com/r/StableDiffusion/comments/1v3cz73/erwhat_exactly_joy_captioner_was_trained_on_lol/) ⭐️ 7.0/10

一位 Reddit 用户发现，Joy Captioner 图像描述模型即使在普通非成人图像上，也偶尔会在生成的描述中提及成人网站水印（如 BRAZZERS.com、METART.com）。 这一发现揭示了训练数据可能被成人内容污染，引发了关于用于训练扩散模型的开源描述模型的伦理和数据来源问题。 水印在描述中持续出现，表明模型从其训练集中的成人图像中学会了关联这些水印。Joy Captioner 被宣传为无审查，但缺乏数据筛选可能引入了问题内容。

reddit · r/StableDiffusion · /u/GuruKast · 7月22日 11:09

**背景**: Joy Captioner 是一个开源、免费且无审查的视觉语言模型（VLM），用于生成描述以训练扩散模型。数据污染是指训练数据中包含非预期的内容，例如露骨材料，这可能导致模型输出有偏见或不适当。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/fpgaminer/joycaption">GitHub - fpgaminer/joycaption: JoyCaption is an image captioning Visual Language Model (VLM) being built from the ground up as a free, open, and uncensored model for the community to use in training Diffusion models. · GitHub</a></li>
<li><a href="https://www.holisticai.com/blog/overview-of-data-contamination">An Overview of Data Contamination: The Causes, Risks, Signs, and Defenses</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区表达了惊讶和批评，强调训练数据需要透明度。一些评论者指出，模型的无审查性质可能吸引低质量或有问题的数据集。

**标签**: `#image captioning`, `#training data`, `#watermark detection`, `#data contamination`, `#AI ethics`

---

<a id="item-19"></a>
## [科技记者约翰·C·德沃夏克去世，享年 80 岁](https://twitter.com/na_announce/status/2079952538040672302) ⭐️ 6.0/10

开拓性科技记者和播客主持人约翰·C·德沃夏克去世，引发社区对其持久影响的广泛反思。 德沃夏克几十年来在科技新闻领域独树一帜，以其反主流观点和对行业初期报道的影响力而闻名。他的去世标志着科技媒体一个时代的结束。 德沃夏克是德沃夏克键盘布局发明者奥古斯特·德沃夏克的侄子。他曾为《PC Magazine》、《InfoWorld》和《MacUser》撰写专栏，并定期出现在 TWiT 播客网络中，后来与主持人利奥·拉波特关系破裂。

hackernews · coleca · 7月22日 19:22 · [社区讨论](https://news.ycombinator.com/item?id=49012070)

**背景**: 约翰·C·德沃夏克 (1946–2026) 是一位多产的科技专栏作家和广播员，自 20 世纪 80 年代起活跃。他以其挑衅性且常反主流的观点闻名，报道范围从个人电脑到科技行业的过度行为。他的风格影响了一代科技记者和播客主持人。

**社区讨论**: 社区评论充满了深深的怀旧和尊重：读者回忆起在《PC Magazine》和《InfoWorld》上读他的专栏，以及他仅凭软件包装盒写评论等趣事。一些人提到他与 TWiT 的利奥·拉波特之间的复杂关系，但总体情绪是对他独特视角和娱乐性的感激。

**标签**: `#John C. Dvorak`, `#technology journalism`, `#obituary`, `#nostalgia`

---

<a id="item-20"></a>
## [对丑陋的人工智能生成菜单和海报的批评](https://blog.fiddery.com/businesses-with-ugly-ai-menu-redesigns/) ⭐️ 6.0/10

一篇博文批评了近期本地商家大量使用人工智能生成的菜单和海报设计，指出虽然技术质量有所提高，但缺乏真实性，损害了消费者信任。 这很重要，因为人工智能生成的设计正变得无处不在，影响客户对真实性和质量的感知。设计中人情味的缺失可能会侵蚀信任和品牌认同，尤其是在餐饮和酒店行业。 文章指出，人工智能设计现在通常包含正确的排版，但千篇一律的外观降低了可信度。一些评论者还担心与实际供应的食物相比，图像可能存在欺骗性。

hackernews · speckx · 7月22日 12:49 · [社区讨论](https://news.ycombinator.com/item?id=49005973)

**背景**: 人工智能图像生成使用扩散模型（如 Stable Diffusion）和生成对抗网络（GAN）等模型，根据文本提示生成图像。这些模型最近在生成连贯文本和布局方面有所改进，使得它们能够用于菜单和海报制作而无明显缺陷。然而，它们仍然缺乏对人类设计原则和品牌标识的细微理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stablediffusionapi.com/models">Stable Diffusion Models — 1,000+ Models for Image Generation API</a></li>
<li><a href="https://github.com/huggingface/diffusers">huggingface/diffusers: Diffusers: State-of-the-art diffusion models ...</a></li>

</ul>
</details>

**社区讨论**: 评论表达了复杂的感受：一些人对 AI 设计中个性的丧失感到惋惜，尤其是在儿童相关场景中；另一些人则指出 AI 海报正成为低努力程度的标志。还有人批评文章模糊了菜单照片中的价格，并希望有像日本那样严格的食品包装法规。

**标签**: `#AI`, `#design`, `#user experience`, `#authenticity`, `#business`

---

<a id="item-21"></a>
## [用户分享 Clean Plate LoRA 视频物体移除示例](https://www.reddit.com/r/StableDiffusion/comments/1v3qqzl/a_few_more_clean_plate_lora_examples/) ⭐️ 6.0/10

一位 Reddit 用户分享了 Clean Plate LoRA 的示例，这是一个利用 Stable Diffusion 和 LTX-2.3 从视频中移除物体的微调模型，并附上了工作流程和提示词。 该 LoRA 提供了一种轻量级的视频物体移除方法，无需复杂的修补或 ControlNet，使 AI 视频编辑社区的用户更容易使用。 该 LoRA 托管在 Hugging Face 上，名称为 Lightricks/LTX-2.3-22b-IC-LoRA-Clean-Plate，采用了特定的图像条件 LoRA（IC-LoRA）架构，使用参考潜在条件，首帧条件概率为 0.1。

reddit · r/StableDiffusion · /u/nazihater3000 · 7月22日 19:41

**背景**: LoRA（低秩适配）是一种通过添加小型适配模块高效微调大模型的技术。LTX-2.3 是 Lightricks 推出的基于 DiT 的音频-视频基础模型。IC-LoRA 通过输入视频帧对模型进行条件控制，用于物体移除等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Clean-Plate">Lightricks/LTX-2.3-22b-IC- LoRA - Clean - Plate · Hugging Face</a></li>
<li><a href="https://comfyui-wiki.com/en/news/2026-07-19-ltx-2-3-clean-plate-ic-lora">LTX-2.3 Clean Plate IC- LoRA : Remove Subjects from Video in ComfyUI</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#LoRA`, `#video editing`, `#computer vision`

---

<a id="item-22"></a>
## [Krea 2 Identity Edit LoRA v1.2 展示单句提示身份编辑](https://www.reddit.com/r/StableDiffusion/comments/1v3akl6/krea_2_identity_edit_beforeafters/) ⭐️ 6.0/10

Krea 2 Identity Edit LoRA v1.2 允许使用单句提示进行身份编辑，无需遮罩或修复，同时保留原始场景和光照。 这展示了身份保留图像编辑的重大改进，使其对创作者更加便捷高效，尽管相对于现有方法属于渐进式进步。 所有编辑均使用单句提示完成，背景和光照完全保持不变；用户指出简短提示比长篇提示效果更好。

reddit · r/StableDiffusion · /u/NatalieCrypto · 7月22日 08:59

**背景**: LoRA（低秩适应）是一种高效微调大模型的技术。Krea 2 Identity Edit 是一个在 SFW 数据上训练的 LoRA 模型，用于进行身份保留的角色重排，允许改变身份、姿势、表情或配饰，同时保持场景一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/conradlocke/krea2-identity-edit">conradlocke/krea2-identity-edit · Hugging Face</a></li>
<li><a href="https://www.krea.ai/">Krea: AI Creative Suite for Images, Video, & 3D</a></li>

</ul>
</details>

**标签**: `#StableDiffusion`, `#LoRA`, `#image editing`, `#AI art`

---