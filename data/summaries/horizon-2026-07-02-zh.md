# Horizon 每日速递 - 2026-07-02

> 从 38 条内容中筛选出 24 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：AI、AI Image Generation、image generation、Character Consistency、multimodal。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[Krea2 Turbo 模型过滤器影响 SFW 图像质量；去审查 LoRA 可改善](https://www.reddit.com/r/StableDiffusion/comments/1ul8by5/the_consequences_of_filters_in_models_followup/)**
2. **[LLM 驱动的无限一致性图像面板工作流](https://www.reddit.com/r/StableDiffusion/comments/1ul8ifw/krea2_infinite_number_of_panels_with_consistancy/)**
3. **[SenseNova-U1 Pro 声称原生 8K 输出，与 GPT-Image-2 对比](https://www.reddit.com/r/StableDiffusion/comments/1ulaax5/sensetimes_sensenovau1_pro_claims_8k_native/)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [Senior SWE-Bench：评估 AI 高级工程师的基准](https://senior-swe-bench.snorkel.ai/)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [文章呼吁回归传统网络论坛](https://tedium.co/2026/07/01/online-web-forums-retrospective/)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [Senior SWE-Bench：评估 AI 高级工程师的基准](https://senior-swe-bench.snorkel.ai/)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：Krea2 Turbo 模型过滤器影响 SFW 图像质量；去审查 LoRA 可改善

**关联新闻**: [Krea2 Turbo 模型过滤器影响 SFW 图像质量；去审查 LoRA 可改善](https://www.reddit.com/r/StableDiffusion/comments/1ul8by5/the_consequences_of_filters_in_models_followup/)

**切入角度**: Reddit 用户展示，Krea2 Turbo 模型中的审查过滤器无意中降低了其生成 SFW 图像（如面部表情和瘀伤）的能力，而仅约 200 字节的小型去审查 LoRA 可以恢复这些能力，且不引入新概念。 这凸显了生成式 AI 中安全过滤器的意外副作用，影响了合法的创意和专业用途。它让模型开发者了解实施审查的权衡，以及进行轻量级修正的可能性。 比较中使用了三个 LoRA：Krea2FilterBypass V2 和 V3（各仅修改 2-3 个权重）以及较大的 SNOFS LoRA。V2/V3 LoRA 提供了公平的比较，因为它们仅禁用过滤器，而不引入新风格或概念，而 SNOFS 则带来了额外变化。

**可延展方向**: LoRA（低秩自适应）是一种通过添加小型可训练低秩矩阵来微调大型模型的技术，可在不进行完整重训练的情况下实现高效任务适配。Krea2 Turbo 是一款快速图像生成模型，专为快速迭代优化。审查过滤器通常嵌入模型以防止 NSFW 输出，但可能无意中限制 SFW 能力，如情感表达或身体细节。

---

### 选题 2：LLM 驱动的无限一致性图像面板工作流

**关联新闻**: [LLM 驱动的无限一致性图像面板工作流](https://www.reddit.com/r/StableDiffusion/comments/1ul8ifw/krea2_infinite_number_of_panels_with_consistancy/)

**切入角度**: 这种方法将角色一致性的负担从图像模型转移到语言模型，可能简化工作流程并减少对参考图像、IPAdapter 或 LoRA 的需求。它为生成长篇视觉叙事且角色一致开辟了新的可能性。 该工作流避免了所有传统的一致性技术，如参考图像、IPAdapter、角色 LoRA 和多面板生成。相反，它依靠 LLM（Qwen VLM）在文本提示词中从头重建每个场景的语义状态，确保每个提示词完全自包含。

**可延展方向**: AI 图像生成中的角色一致性是一个长期存在的挑战，通常通过 IPAdapter、参考图像或 LoRA 等技术来解决，这些技术使模型依赖于之前的输出。该工作流提出了一种替代方案：使用大型语言模型（LLM）如 Qwen VLM 为每张图像生成详细、自包含的描述，从而图像模型不需要记忆任何内容。ComfyUI 是一个开源的基于节点界面的扩散模型工作流构建工具，Krea 2 是一个可通过 Hugging Face 访问的高质量图像生成模型。

---

### 选题 3：SenseNova-U1 Pro 声称原生 8K 输出，与 GPT-Image-2 对比

**关联新闻**: [SenseNova-U1 Pro 声称原生 8K 输出，与 GPT-Image-2 对比](https://www.reddit.com/r/StableDiffusion/comments/1ulaax5/sensetimes_sensenovau1_pro_claims_8k_native/)

**切入角度**: 商汤科技预览了 SenseNova-U1 Pro 多模态模型，该模型声称能够原生输出 8K 分辨率的图像，超越了 GPT-Image-2 的 4K 分辨率，并采用统一的“理解-生成-行动”架构，专为专业设计工作流打造。 如果得到验证，这将是生成式 AI 在原生图像分辨率上的重大飞跃，可能颠覆当前 GPT-Image-2 和 Midjourney 等服务不足的专业设计市场。 演示包括杂志版面、学术海报和电影分镜等复杂任务，分辨率高达 16,000×24,000 像素，但这些说法尚未得到验证，独立基准测试仍待公布。

**可延展方向**: 大多数 AI 图像生成器以较低的原生分辨率（例如 1024×1024）生成图像，并依赖放大工具才能达到 4K 或 8K，这可能会引入伪影。统一的“理解-生成”架构将感知和生成集成在一个模型中，从而实现更好的上下文连贯性。声称的原生 8K 输出将完全绕过放大过程。

---

1. [首个能生长和分裂的合成细胞诞生](#item-1) ⭐️ 9.0/10
2. [Senior SWE-Bench：评估 AI 高级工程师的基准](#item-2) ⭐️ 8.0/10
3. [FFmpeg 9.1 新 AAC 编码器提升质量](#item-3) ⭐️ 8.0/10
4. [Cloudflare 推出基于 HTTP 402 和稳定币的变现网关](#item-4) ⭐️ 8.0/10
5. [弹性扩散 Transformer 通过自适应跳块加速 DiT](#item-5) ⭐️ 8.0/10
6. [Oomwoo：自己动手做的开源机器人吸尘器](#item-6) ⭐️ 7.0/10
7. [文章呼吁回归传统网络论坛](#item-7) ⭐️ 7.0/10
8. [图形编程学习指南引发热议](#item-8) ⭐️ 7.0/10
9. [HN 2026 年 7 月‘谁在招聘？’帖子](#item-9) ⭐️ 7.0/10
10. [Weave Robotics 推出 Isaac 1 家用机器人，售价 7999 美元](#item-10) ⭐️ 7.0/10
11. [高通 Linux 2.0 发布，采用上游优先模式](#item-11) ⭐️ 7.0/10
12. [隐蔽 C 语言竞赛：欺骗性代码挑战](#item-12) ⭐️ 7.0/10
13. [工人所有制合作社产品目录上线](#item-13) ⭐️ 7.0/10
14. [Krea2 Turbo 模型过滤器影响 SFW 图像质量；去审查 LoRA 可改善](#item-14) ⭐️ 7.0/10
15. [LLM 驱动的无限一致性图像面板工作流](#item-15) ⭐️ 7.0/10
16. [SenseNova-U1 Pro 声称原生 8K 输出，与 GPT-Image-2 对比](#item-16) ⭐️ 7.0/10
17. [针对 ComfyUI 扩展开发者的 npm 钓鱼诈骗](#item-17) ⭐️ 7.0/10
18. [谷歌安全措施被批损害自由与隐私](#item-18) ⭐️ 6.0/10
19. [Kimi K2.7 代码模型现已登陆 GitHub Copilot](#item-19) ⭐️ 6.0/10
20. [Krea2 与 Gemma 4 生成电影级故事板](#item-20) ⭐️ 6.0/10
21. [用户使用 Krea 2 Turbo 获得令人印象深刻的结果](#item-21) ⭐️ 6.0/10
22. [ComfyUI 新节点：本地 LLM 加载器](#item-22) ⭐️ 6.0/10
23. [ComfyUI 27.0 中 Krea2 的 INT8 ConvRot 与 FP8 Scaled 基准测试对比](#item-23) ⭐️ 6.0/10
24. [在 Blender 中直接生成 3D 资产并渲染视频](#item-24) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [首个能生长和分裂的合成细胞诞生](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/) ⭐️ 9.0/10

由明尼苏达大学 Kate Adamala 博士领导的研究人员创造了 SpudCell，这是首个从零构建的合成细胞，能够生长、复制 DNA 并进行分裂，完成了完整的细胞周期。 这一突破表明，一组最小的非生命组件可以组装起来表现出类似生命的行为，标志着向理解生命起源迈出了重要一步，并为未来在生物技术和医学中的应用铺平了道路。 SpudCell 缺乏细胞骨架，而是采用更简单的分裂机制。该工作最初被《细胞》期刊拒稿，一位审稿人声称 SpudCells 不是真正的生物学。

hackernews · defrost · 7月1日 14:20 · [社区讨论](https://news.ycombinator.com/item?id=48747304)

**背景**: 合成生物学旨在从非生命化学组分创造人工细胞。之前的尝试产生了能够代谢或复制 DNA 但不能分裂的细胞。SpudCell 通过绕过复杂的细胞骨架重组，采用不同的方法实现分裂，从而克服了这一难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpudCell">SpudCell</a></li>
<li><a href="https://www.nytimes.com/2026/07/01/science/spud-cell-what-to-know.html">SpudCell : Scientists Made a Cell With Most of the Hallmarks of Life.</a></li>
<li><a href="https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/">For the First Time, a Cell Built From Scratch Grows and Divides</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中反应不一。有人赞赏这一成就，也有人批评其不寻常的发表过程——Adamala 在将手稿上传到 bioRxiv 之前就向记者发送了禁发稿件。还有一些关于合成生物学未来影响的推测性评论。

**标签**: `#synthetic biology`, `#spudcell`, `#cell division`, `#biotechnology`, `#breakthrough`

---

<a id="item-2"></a>
## [Senior SWE-Bench：评估 AI 高级工程师的基准](https://senior-swe-bench.snorkel.ai/) ⭐️ 8.0/10

Senior SWE-Bench 是一个新的开源基准测试，用于评估 AI 代理在需要高级软件工程师技能的任务上的表现，例如处理不明确的需求和应用新颖的解决方案。 该基准测试填补了 AI 评估中的一个关键空白，专注于更高级别的软件工程能力，可能指导更有能力的编码助手的开发，并影响 AI 代理的招聘与评估。 该基准使用真实的 GitHub 问题和补丁，评估代理在优雅解决方案、代码膨胀和长期项目上下文方面的表现。它可在 Snorkel AI 的网站上获取。

hackernews · matt_d · 7月2日 02:55 · [社区讨论](https://news.ycombinator.com/item?id=48755928)

**背景**: SWE-bench 是一个流行的基准测试，用于评估 AI 模型在软件工程任务上的表现，通常侧重于修复 GitHub 问题中的错误。Senior SWE-Bench 将此概念扩展到更复杂的任务，模拟高级工程师的工作，强调设计决策和可维护性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epoch.ai/benchmarks/swe-bench-verified">SWE-bench Verified | Epoch AI</a></li>
<li><a href="https://www.swebench.com/">SWE-bench Leaderboards</a></li>

</ul>
</details>

**社区讨论**: 社区评论既表达了兴奋也表达了怀疑。一些用户赞赏该基准测试捕捉到了“优雅解决方案”的价值（例如 Opus 模型），而另一些则批评“优雅”标准的主观性，称之为“货物崇拜”。还有建议使用 ELO 评分的对抗性基准，以及担心静态基准测试无法长期提供新颖挑战。

**标签**: `#benchmark`, `#AI`, `#software engineering`, `#LLM evaluation`, `#open-source`

---

<a id="item-3"></a>
## [FFmpeg 9.1 新 AAC 编码器提升质量](https://hydrogenaudio.org/index.php/topic,129691.0.html) ⭐️ 8.0/10

FFmpeg 9.1 推出了一个新的原生 AAC 编码器，显著提升了音频质量，在 128 kbps 下达到或超越了专有的 libfdk_aac 编码器。 这一更新惠及数百万 FFmpeg 用户，提供了一个高质量、许可友好的替代方案，以替代 Core Audio 或 libfdk_aac 等专利 AAC 编码器。 新编码器主要针对 48 kHz 音频进行了优化，并包含对 FFmpeg AAC 解码器中一个多年来未被发现的立体声 PNS 错误的解决方法。

hackernews · ledoge · 7月1日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48747116)

**背景**: AAC 是一种广泛使用的有损音频编解码器，以高效压缩著称。FFmpeg 的原生 AAC 编码器历来被认为质量低于 Apple 的 Core Audio 编码器等替代方案。新编码器旨在缩小这一差距，使 FFmpeg 成为一站式编码和解码解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trac.ffmpeg.org/wiki/Encode/AAC">Encode / AAC – FFmpeg</a></li>
<li><a href="https://en.wikipedia.org/wiki/Audio_codec">Audio codec - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了改进，但也指出 Opus 在低比特率下表现优于 AAC。此外，还讨论了主观音频质量测试的难度以及针对 48 kHz 进行优化的重要性。

**标签**: `#FFmpeg`, `#AAC`, `#audio encoding`, `#codec`, `#multimedia`

---

<a id="item-4"></a>
## [Cloudflare 推出基于 HTTP 402 和稳定币的变现网关](https://blog.cloudflare.com/monetization-gateway/) ⭐️ 8.0/10

Cloudflare 推出了一个变现网关，允许网站运营商通过 HTTP 402 状态码和稳定币支付，对其 Cloudflare 网络后的任何资源进行收费。 这一进展可能彻底改变网络变现方式，实现无需传统支付处理器的无缝小额支付，有望减少机器人滥用，并为内容创作者和 API 提供商创造新的收入模式。 该网关利用与 Coinbase 合作开发的 x402 协议，并集成到 Cloudflare 现有基础设施中，在提供内容前自动请求稳定币支付。

hackernews · soheilpro · 7月1日 13:59 · [社区讨论](https://news.ycombinator.com/item?id=48746914)

**背景**: HTTP 402（请求付款）在 HTTP 标准中已有定义，但很少使用。x402 协议重新利用该状态码进行加密货币支付，实现客户端与服务器之间的直接价值交换，无需中间方。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes">List of HTTP status codes - Wikipedia</a></li>
<li><a href="https://developers.cloudflare.com/agents/x402/">x402 · Cloudflare Agents docs</a></li>
<li><a href="https://blog.cloudflare.com/x402/">Launching the x402 Foundation with Coinbase, and support for x402 transactions</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了兴奋和担忧。一些人称赞了基于代理的小额支付潜力，而另一些人则提出了法律和会计挑战，如发票和增值税。还有人担心垃圾信息增加以及区分机器人和人类的困难。

**标签**: `#cloudflare`, `#monetization`, `#micropayments`, `#web3`, `#stablecoins`

---

<a id="item-5"></a>
## [弹性扩散 Transformer 通过自适应跳块加速 DiT](https://www.reddit.com/r/StableDiffusion/comments/1ukx0ej/elastic_diffusion_transformer_accelerating_sota/) ⭐️ 8.0/10

研究人员提出了弹性扩散 Transformer（E-DiT），这是一种针对扩散 Transformer 的自适应加速框架，它根据输入稀疏性动态跳过 DiT 块，在保持生成质量的同时实现高达 2 倍的加速。 E-DiT 解决了扩散 Transformer 的一个关键效率瓶颈——尽管扩散 Transformer 具有强大的生成能力，但计算成本高昂。这种依赖于样本的自适应方法可以使得在图像和 3D 资产生成等应用中更快地部署高质量生成模型。 E-DiT 为每个 DiT 块配备了一个轻量级路由器，用于预测是否跳过该块以及 MLP 宽度缩减多少。它还引入了一种无需训练的块级特征缓存机制，以消除冗余计算。

reddit · r/StableDiffusion · /u/Dante_77A · 7月1日 20:25

**背景**: 扩散 Transformer（DiT）是一类生成模型，它使用 Transformer 架构而非传统的 U-Net 作为去噪骨干。它们功能强大但计算密集。先前的加速方法如剪枝和蒸馏采用固定的计算缩减，往往会降低质量。E-DiT 利用了生成过程存在依赖于样本的稀疏性这一观察，从而实现选择性计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_Transformer">Diffusion Transformer</a></li>

</ul>
</details>

**标签**: `#Diffusion Transformers`, `#Model Acceleration`, `#Generative AI`, `#Efficiency`

---

<a id="item-6"></a>
## [Oomwoo：自己动手做的开源机器人吸尘器](https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/) ⭐️ 7.0/10

Maker's Pet 推出了 Oomwoo，这是一个开源机器人吸尘器项目，使用 Raspberry Pi、ROS 2、2D LiDAR 和 3D 打印部件，完全离线运行并由社区驱动。 Oomwoo 优先考虑可修复性和模块化，为通常不耐用的商业机器人吸尘器提供了替代方案。它可能降低爱好者和研究人员定制和改进家用机器人的门槛。 目前构建 Oomwoo 的成本明显高于预算型商业激光雷达吸尘器（约 70-80 英镑），价格大约是其 4 倍。硬件被分为自包含模块，允许社区并行开发并通过 pull request 贡献。

hackernews · devicelimit · 7月2日 00:48 · [社区讨论](https://news.ycombinator.com/item?id=48755005)

**背景**: 像 Roomba 这样的机器人吸尘器很常见，但通常是闭源的且难以修复。Oomwoo 使用开源软件（ROS 2、Nav2）和硬件（3D 打印底盘、Raspberry Pi）来打造一个可修复、本地优先的替代品。该项目处于早期阶段，欢迎社区贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/">Building an Open-Source Robot Vacuum — Meet OOMWOO - Makers Pet</a></li>
<li><a href="https://github.com/makerspet/oomwoo/">GitHub - makerspet/oomwoo: Open-source vacuum robot cleaner · GitHub</a></li>
<li><a href="https://www.tomshardware.com/3d-printing/maker-kicks-off-oomwoo-an-open-source-robot-vacuum-you-can-3d-print-and-build-yourself">Oomwoo is a new open-source robot vacuum you can 3D print yourself, sidesteps cloud security risks by running fully offline — project combines Raspberry Pi, 2D LiDAR, and a 3D-printed chassis | Tom's Hardware</a></li>

</ul>
</details>

**社区讨论**: 评论指出，与购买廉价商业产品相比，从头构建 Oomwoo 的成本很高，但许多人称赞其可修复性和开源理念。有人建议利用现有吸尘器的零件来降低成本。

**标签**: `#open source`, `#robotics`, `#hardware`, `#3D printing`, `#IoT`

---

<a id="item-7"></a>
## [文章呼吁回归传统网络论坛](https://tedium.co/2026/07/01/online-web-forums-retrospective/) ⭐️ 7.0/10

一篇刊载于 Tedium 的文章回顾了传统网络论坛的衰落，并主张它们应该回归，指出了深度社区和个性化互动的优势。 这很重要，因为它挑战了现代社交媒体和集中式平台的主导地位，突出了小众的、自托管的社区在深度讨论和长期知识保存方面的价值。 文章承认许多早期论坛在技术上是“糟糕的”，基于 PHP/Ruby 的系统难以维护且存在安全漏洞，但认为其优点超过了这些缺陷。

hackernews · pentagrama · 7月2日 02:30 · [社区讨论](https://news.ycombinator.com/item?id=48755731)

**背景**: 传统网络论坛是按主题和帖子组织的在线讨论平台，在 1990 年代末和 2000 年代初流行。随着 Reddit 和 Facebook 等社交媒体的兴起，它们逐渐衰落，这些社交媒体提供聚合信息流和更轻松的内容发现。文章认为，与当今的平台相比，论坛培养了更紧密的社区和更深入的对话。

**社区讨论**: 评论者表达了对论坛的怀旧之情，一些人强调了讨论的深度和个人认可，但另一些人指出了技术维护的挑战，并认为用户行为已经随时间发生了变化。

**标签**: `#forums`, `#online communities`, `#web development`, `#nostalgia`, `#community design`

---

<a id="item-8"></a>
## [图形编程学习指南引发热议](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/) ⭐️ 7.0/10

一篇题为《学习成为图形程序员需要学什么》的博客文章在 demofox.org 上发布，为有志于成为图形程序员的人提供了实用建议和学习路径。该文章获得了高度关注和热烈的社区讨论。 这篇文章之所以重要，是因为它回应了游戏开发和计算机图形社区中的常见问题，为新手提供了路线图。随附的讨论揭示了关于职业可持续性和该领域快速发展的不同观点。 该博客涵盖了线性代数、渲染管线、着色器编程等主题，但正如一位评论者指出的那样，并未提及基本设计原则。几位社区成员分享了个人资源清单，并就专注于图形编程还是使用现有引擎表达了不同意见。

hackernews · atan2 · 7月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=48750710)

**背景**: 图形编程涉及创建用于渲染图像、动画和视觉效果的软件，通常用于游戏或模拟。它需要扎实的数学基础，尤其是线性代数，以及 GPU 硬件和 DirectX、Vulkan 或 OpenGL 等 API 的知识。该领域以学习曲线陡峭和技术进步迅速著称，主要由 NVIDIA 等公司推动。

**社区讨论**: 讨论呈现出多样化观点：一些评论者建议在游戏开发中使用现有引擎，而另一些人则因图形编程发展迅速且就业机会有限而告诫不要进入该领域。几位用户提供了有用的资源，如线性代数速查表和精心整理的学习清单，同时有人指出该帖子缺少设计原则方面的内容。

**标签**: `#graphics programming`, `#game development`, `#career advice`, `#learning resources`

---

<a id="item-9"></a>
## [HN 2026 年 7 月‘谁在招聘？’帖子](https://news.ycombinator.com/item?id=48747976) ⭐️ 7.0/10

Hacker News 上 2026 年 7 月的月度‘谁在招聘？’帖子已发布，包含科技公司的职位列表，并注明了地点和远程工作政策。 该帖子是科技社区发现招聘公司直接发布的工作机会的中心枢纽，促进了透明度，减少了对第三方招聘机构的依赖。 发布公司必须注明地点和远程状态（REMOTE、REMOTE (US) 或 ONSITE）。只有招聘经理或公司内部人员可以发帖，每家公司限发一条。

hackernews · whoishiring · 7月1日 15:01

**背景**: ‘谁在招聘？’帖子是 Hacker News 上的每月固定栏目，Hacker News 是一个专注于计算机科学和创业的社会新闻网站。由网站创始人创建，允许公司以标准化格式在评论区发布职位空缺。初创公司和成熟科技公司都广泛使用它。

**社区讨论**: 该帖子的评论完全来自公司发布的职位信息，例如一家机器人初创公司、圣犹大儿童研究医院、Aurora Energy Research 和 BREAKFAST Studio。除了职位列表本身，没有其他讨论或评论。

**标签**: `#jobs`, `#hiring`, `#software engineering`, `#remote work`, `#career`

---

<a id="item-10"></a>
## [Weave Robotics 推出 Isaac 1 家用机器人，售价 7999 美元](https://www.weaverobotics.com/isaac-1) ⭐️ 7.0/10

Weave Robotics 宣布推出 Isaac 1 家用机器人，售价 7999 美元，可自主执行洗衣和日常整理等任务，必要时可远程协助，预计 2026 年秋季交付。 此次发布代表了平价家用机器人领域的重要一步，但对远程操作的依赖以及遥远的交付日期引发了对其实际自主性和市场准备程度的质疑。 Isaac 1 默认自主处理洗衣流程和日常整理任务，但使用远程操作协助来保证任务完成。需要远程操作的任务比例未公开。

hackernews · ryanmerket · 7月1日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48750989)

**背景**: 家用机器人长期以来在复杂、非结构化环境中面临挑战。远程操作允许人类操作员远程控制机器人完成困难任务，为最终实现完全自主提供过渡。Weave Robotics 旨在通过远程操作收集训练数据，逐步改进 AI。

**社区讨论**: 评论者对严重依赖远程操作且未明确失败率表示怀疑，并质疑其设计能否处理楼梯或够到床铺。其他人则认为远程操作是一种为未来 AI 收集数据的策略，但对高昂成本和 AI 积分模式进行了讨论。

**标签**: `#robotics`, `#home robot`, `#AI`, `#teleoperation`, `#startup`

---

<a id="item-11"></a>
## [高通 Linux 2.0 发布，采用上游优先模式](https://www.qualcomm.com/developer/blog/2026/06/qualcomm-linux-2-now-available) ⭐️ 7.0/10

高通发布了其 Linux 平台的 2.0 版本，转向上游优先的开放开发模式，统一适用于所有高通 Dragonwing IoT 平台。 此举解决了长期存在的板级支持包 (BSP) 和内核分支碎片化问题，使开发者更容易在嵌入式及物联网应用中使用高通骁龙 SoC。 Qualcomm Linux 2.0 强调上游优先贡献，即驱动和补丁在纳入平台之前会先提交到主线 Linux。该平台现已统一覆盖高通的 Dragonwing IoT 产品线。

hackernews · gilgamesh3 · 7月1日 21:01 · [社区讨论](https://news.ycombinator.com/item?id=48753069)

**背景**: Qualcomm Linux 是一套用于基于高通平台开发产品的软件和工具。在 2.0 版本之前，开发者常面临 BSP 碎片化和特定平台内核分支的问题，导致启动过程繁琐。新的上游优先模式旨在与标准 Linux 内核开发实践保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/qualcomm-linux">Qualcomm Linux · GitHub</a></li>
<li><a href="https://www.cnx-software.com/2026/06/19/qualcomm-promises-a-major-reset-with-upstream-first-qualcomm-linux-2-0-for-dragonwing-iot-platforms/">Qualcomm promises a major reset with upstream-first... - CNX Software</a></li>

</ul>
</details>

**社区讨论**: 社区评论包括对骁龙 X2 支持的期待、要求上游化驱动的建议，以及一位 SBC 购买者好奇供应商是否会以此为基础。总体情绪谨慎乐观，重点关注上游化的实际执行。

**标签**: `#Qualcomm`, `#Linux`, `#Embedded Systems`, `#Snapdragon`

---

<a id="item-12"></a>
## [隐蔽 C 语言竞赛：欺骗性代码挑战](https://underhanded-c.org/) ⭐️ 7.0/10

隐蔽 C 语言竞赛从 2005 年持续到 2013 年，要求程序员编写看似正确但暗中执行恶意操作的 C 代码。该竞赛旨在通过竞争形式教授关于微妙错误和安全漏洞的知识。 这项竞赛意义重大，因为它教育开发者看似无害的代码如何隐藏危险缺陷，提高了对安全编码实践的认识。其历史影响持续影响着安全教育和代码审查技术。 该竞赛由宾汉姆顿大学的 Scott Craver 组织，奖品为 100 至 200 美元的 ThinkGeek 礼品卡。每轮都有特定任务，例如计票错误，参赛作品必须在保持可读性的同时隐藏恶意。

hackernews · ccabraldev · 7月1日 22:39 · [社区讨论](https://news.ycombinator.com/item?id=48754080)

**背景**: 隐蔽 C 语言竞赛的灵感来源于 2004 年 Daniel Horn 的混淆 V 竞赛。其目的是展示即使是简单的 C 代码也可能包含未被检测到的恶意功能，突显了彻底代码审查的重要性。该竞赛现已停办，但仍是一个教育资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Underhanded_C_Contest">Underhanded C Contest</a></li>
<li><a href="https://underhanded-c.org/">The Underhanded C Contest</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了怀旧和赞赏：BiraIgnacio 提到了竞赛的起源和影响，AmazingEveryDay 在 2015 年简单说了“RIP”，pseudohadamard 将竞赛中的浮点数不确定性与现实中的核物理代码审计联系起来。

**标签**: `#C programming`, `#contest`, `#security`, `#underhanded code`

---

<a id="item-13"></a>
## [工人所有制合作社产品目录上线](https://www.workerowned.info/) ⭐️ 7.0/10

一个可搜索的产品目录在 workerowned.info 上线，收录了来自工人所有制合作社的超过 2.2 万件产品。 该目录让消费者更容易找到并购买工人所有制企业的产品，支持道德消费和合作经济。 该网站支持实时搜索和基于位置的筛选，但社区反馈指出缩略图文件过大（有的超过 2MB），需要优化，且部分产品链接可能已过时。

hackernews · IESAI_ski · 7月1日 20:47 · [社区讨论](https://news.ycombinator.com/item?id=48752905)

**背景**: 工人所有制合作社是由员工拥有和经营的企业，通常更注重公平和可持续性。该目录将这些企业的产品整合到一个可搜索的平台，填补了有意识消费者支持工人所有制企业的需求空白。

**社区讨论**: 社区称赞了该项目的初衷，但也提出了建设性意见：建议优化图片大小、添加地图搜索位置、增加产品标签以便筛选，以及允许纠正过时的链接。还有人指出 REI 是零售合作社而非工人所有制合作社，质疑将其列入是否合适。

**标签**: `#directory`, `#worker-owned co-ops`, `#ethical consumption`, `#open data`

---

<a id="item-14"></a>
## [Krea2 Turbo 模型过滤器影响 SFW 图像质量；去审查 LoRA 可改善](https://www.reddit.com/r/StableDiffusion/comments/1ul8by5/the_consequences_of_filters_in_models_followup/) ⭐️ 7.0/10

Reddit 用户展示，Krea2 Turbo 模型中的审查过滤器无意中降低了其生成 SFW 图像（如面部表情和瘀伤）的能力，而仅约 200 字节的小型去审查 LoRA 可以恢复这些能力，且不引入新概念。 这凸显了生成式 AI 中安全过滤器的意外副作用，影响了合法的创意和专业用途。它让模型开发者了解实施审查的权衡，以及进行轻量级修正的可能性。 比较中使用了三个 LoRA：Krea2FilterBypass V2 和 V3（各仅修改 2-3 个权重）以及较大的 SNOFS LoRA。V2/V3 LoRA 提供了公平的比较，因为它们仅禁用过滤器，而不引入新风格或概念，而 SNOFS 则带来了额外变化。

reddit · r/StableDiffusion · /u/lazyspock · 7月2日 04:40

**背景**: LoRA（低秩自适应）是一种通过添加小型可训练低秩矩阵来微调大型模型的技术，可在不进行完整重训练的情况下实现高效任务适配。Krea2 Turbo 是一款快速图像生成模型，专为快速迭代优化。审查过滤器通常嵌入模型以防止 NSFW 输出，但可能无意中限制 SFW 能力，如情感表达或身体细节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://huggingface.co/krea/Krea-2-Turbo">krea/Krea-2-Turbo · Hugging Face</a></li>
<li><a href="https://www.atlascloud.ai/blog/guides/uncensored-ai-image-generator-guide">Uncensored AI Image Generators That Passed Our 2026 Testing</a></li>

</ul>
</details>

**标签**: `#AI`, `#image generation`, `#model safety`, `#LoRA`, `#Stable Diffusion`

---

<a id="item-15"></a>
## [LLM 驱动的无限一致性图像面板工作流](https://www.reddit.com/r/StableDiffusion/comments/1ul8ifw/krea2_infinite_number_of_panels_with_consistancy/) ⭐️ 7.0/10

这种方法将角色一致性的负担从图像模型转移到语言模型，可能简化工作流程并减少对参考图像、IPAdapter 或 LoRA 的需求。它为生成长篇视觉叙事且角色一致开辟了新的可能性。 该工作流避免了所有传统的一致性技术，如参考图像、IPAdapter、角色 LoRA 和多面板生成。相反，它依靠 LLM（Qwen VLM）在文本提示词中从头重建每个场景的语义状态，确保每个提示词完全自包含。

reddit · r/StableDiffusion · /u/aurelm · 7月2日 04:50

**背景**: AI 图像生成中的角色一致性是一个长期存在的挑战，通常通过 IPAdapter、参考图像或 LoRA 等技术来解决，这些技术使模型依赖于之前的输出。该工作流提出了一种替代方案：使用大型语言模型（LLM）如 Qwen VLM 为每张图像生成详细、自包含的描述，从而图像模型不需要记忆任何内容。ComfyUI 是一个开源的基于节点界面的扩散模型工作流构建工具，Krea 2 是一个可通过 Hugging Face 访问的高质量图像生成模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>
<li><a href="https://huggingface.co/spaces/krea/Krea-2">Krea 2 - a Hugging Face Space by krea</a></li>

</ul>
</details>

**标签**: `#AI Image Generation`, `#Character Consistency`, `#Workflow`, `#LLM`, `#Stable Diffusion`

---

<a id="item-16"></a>
## [SenseNova-U1 Pro 声称原生 8K 输出，与 GPT-Image-2 对比](https://www.reddit.com/r/StableDiffusion/comments/1ulaax5/sensetimes_sensenovau1_pro_claims_8k_native/) ⭐️ 7.0/10

商汤科技预览了 SenseNova-U1 Pro 多模态模型，该模型声称能够原生输出 8K 分辨率的图像，超越了 GPT-Image-2 的 4K 分辨率，并采用统一的“理解-生成-行动”架构，专为专业设计工作流打造。 如果得到验证，这将是生成式 AI 在原生图像分辨率上的重大飞跃，可能颠覆当前 GPT-Image-2 和 Midjourney 等服务不足的专业设计市场。 演示包括杂志版面、学术海报和电影分镜等复杂任务，分辨率高达 16,000×24,000 像素，但这些说法尚未得到验证，独立基准测试仍待公布。

reddit · r/StableDiffusion · /u/Wild_Artichoke7648 · 7月2日 06:27

**背景**: 大多数 AI 图像生成器以较低的原生分辨率（例如 1024×1024）生成图像，并依赖放大工具才能达到 4K 或 8K，这可能会引入伪影。统一的“理解-生成”架构将感知和生成集成在一个模型中，从而实现更好的上下文连贯性。声称的原生 8K 输出将完全绕过放大过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://imggen.ai/tools/upscale-image">Free AI Image Upscaler | Upscale Images online up to 8K - ImgGen AI</a></li>
<li><a href="https://liner.com/review/mingflashomni-sparse-unified-architecture-for-multimodal-perception-and-generation">Ming-Flash-Omni: A Sparse, Unified Architecture for Multimodal ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal`, `#image generation`, `#SenseTime`, `#GPT-Image-2`

---

<a id="item-17"></a>
## [针对 ComfyUI 扩展开发者的 npm 钓鱼诈骗](https://www.reddit.com/r/StableDiffusion/comments/1ul5wss/scamers_target_comfyui_extensions_developers_be/) ⭐️ 7.0/10

一名 ComfyUI 扩展开发者收到一封钓鱼邮件，诱骗收件人安装恶意 npm 包或执行 curl|sh 脚本，旨在窃取凭证并向扩展中注入恶意代码。 该骗局针对 ComfyUI 扩展生态系统，可能导致供应链攻击，危害 ComfyUI（一个流行的 Stable Diffusion 界面）的开发者及最终用户。 该邮件推广了一个名为'runaic/aic'的 npm 包，开发者怀疑其中包含恶意软件；骗局还使用 curl|sh 直接执行脚本，绕过了包管理器的安全防护。

reddit · r/StableDiffusion · /u/Obvious_Set5239 · 7月2日 02:43

**背景**: ComfyUI 是一个基于节点的图形用户界面，用于 Stable Diffusion 工作流，允许用户构建和共享 AI 管线，其在 GitHub 上已获得超过 89k 颗星。npm 供应链攻击涉及发布恶意包或入侵合法包，以向开发者环境注入代码；最近的 Shai-Hulud 蠕虫等事件凸显了这一日益增长的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI - Wikipedia</a></li>
<li><a href="https://www.trendmicro.com/en_us/research/25/i/npm-supply-chain-attack.html">What We Know About the NPM Supply Chain Attack | Trend Micro (US)</a></li>
<li><a href="https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/">The npm Threat Landscape: Attack Surface and Mitigations (Updated June 2)</a></li>

</ul>
</details>

**标签**: `#security`, `#phishing`, `#ComfyUI`, `#npm`, `#supply-chain`

---

<a id="item-18"></a>
## [谷歌安全措施被批损害自由与隐私](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 6.0/10

F-Droid 上的一篇评论文章指出，谷歌的安全增强措施（如开发者验证和 Manifest v2 弃用）实际上削弱了用户的自由和隐私。 这场辩论突显了 Android 生态系统中安全性与开放性之间日益加剧的紧张关系，影响了数百万重视设备控制权的用户。 该文章发表于 F-Droid（一个开源 Android 应用仓库），引发了 226 条评论，反映出强烈的社区参与度。

hackernews · drewfax · 7月2日 03:00 · [社区讨论](https://news.ycombinator.com/item?id=48755965)

**背景**: Android 历史上比 iOS 更加开放，允许用户从官方 Play 商店之外安装应用，这种做法称为侧载。谷歌逐步引入了 Play Protect 和开发者验证等安全措施，有人认为这限制了用户自由。F-Droid 是一个推广开源软件、反对谷歌控制的替代应用商店。

**社区讨论**: 评论者对谷歌的做法表示强烈不满，列举了账户封禁和服务中断等例子。有人认为谷歌以“安全”为借口进行控制，而另一些人则建议使用其他移动 Linux 操作系统。大家普遍认为用户自由正在被侵蚀。

**标签**: `#Android`, `#Google`, `#privacy`, `#security`, `#open source`

---

<a id="item-19"></a>
## [Kimi K2.7 代码模型现已登陆 GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/) ⭐️ 6.0/10

Moonshot AI 的开源智能编码模型 Kimi K2.7 Code 现在已经在 GitHub Copilot 中正式上线，作为代码生成和智能代理任务的替代模型。 这一新增功能让 GitHub Copilot 用户能够使用高性能的开源权重模型，为寻求中国 AI 解决方案的团队提供了与 Claude 和 GPT 等专有模型竞争的替代方案。其定价与 Moonshot 的 API 费率一致，可能重塑云 AI 定价格局。 该模型支持 256K 上下文长度、工具调用以及智能代理功能。基准测试表明其性能与 Sonnet 4.6 相当。定价为每百万输入 token 0.95 美元，缓存命中 0.19 美元，每百万输出 token 4.00 美元。

hackernews · unliftedq · 7月2日 04:32 · [社区讨论](https://news.ycombinator.com/item?id=48756602)

**背景**: Kimi K2.7 Code 是由中国 AI 公司 Moonshot AI 开发的开源编码专用智能代理模型。GitHub Copilot 是一个集成在开发环境中的流行 AI 编码助手。2026 年 6 月，GitHub Copilot 引入了新的基于使用量的定价模式，导致大量用户迁移到 Claude Code 和 Codex 等替代品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/resources/kimi-k2-7-code">Kimi K 2 . 7 Code: Open-Source Agentic Coding Model</a></li>
<li><a href="https://platform.kimi.ai/">Kimi API Platform</a></li>

</ul>
</details>

**社区讨论**: 社区讨论呈现混合情绪：一些用户对云 AI 定价变化感到厌倦，并已迁移到本地或替代工具；而另一些用户则欢迎 Kimi K2.7 作为可信的中国提供商提供的可行替代方案。有用户指出其定价与 Moonshot 直接 API 相同，这可能无法缓解成本担忧。

**标签**: `#GitHub Copilot`, `#AI coding assistant`, `#Kimi K2.7`, `#pricing`

---

<a id="item-20"></a>
## [Krea2 与 Gemma 4 生成电影级故事板](https://www.reddit.com/r/StableDiffusion/comments/1ul3ask/2x2_4_panels_cinematic_storyboards_with_krea2_and/) ⭐️ 6.0/10

一位 Reddit 用户分享了一个工作流，结合 Krea2 Turbo 和通过 LM Studio 运行的 Gemma 4 12B，自动生成详细提示词，并根据简单的场景描述生成 2x2 电影级故事板。 该工作流降低了电影制作人、游戏开发者和内容创作者使用本地 AI 工具快速原型化故事板的门槛，在保护隐私的同时提升了创意迭代速度。 Krea2 Turbo（一种 AI 图像生成器）在处理较大网格时存在困难；该工作流为 Gemma 4 12B 精心设计了系统提示词，以生成详细的画面描述，并从 2x2 网格中分割出各面板。

reddit · r/StableDiffusion · /u/MayaProphecy · 7月2日 00:41

**背景**: Krea2 Turbo 是一种专用 AI 模型，可根据文本提示生成图像，但对多面板布局的支持有限。Gemma 4 12B 是 Google 开发的多模态语言模型，能够原生理解图像并生成文本，可通过 LM Studio 在本地运行。LM Studio 是一款桌面应用，允许在本地计算机上私密运行大型语言模型。该工作流整合了这些工具，实现故事板创作的自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12B: a unified, encoder-free multimodal model</a></li>
<li><a href="https://lmstudio.ai/">LM Studio - Local AI on your computer</a></li>

</ul>
</details>

**标签**: `#AI art`, `#storyboard`, `#Krea2`, `#Gemma`, `#workflow`

---

<a id="item-21"></a>
## [用户使用 Krea 2 Turbo 获得令人印象深刻的结果](https://www.reddit.com/r/StableDiffusion/comments/1ul0p0i/ive_been_using_krea_2_turbo_for_literally_3_hours/) ⭐️ 6.0/10

一位 Reddit 用户报告称，在使用 Krea 2 Turbo 进行 1440p 分辨率的 AI 图像生成三个小时后，获得了令人印象深刻的成果，且未使用遮罩、分层或 LoRA 技术。 这表明高质量、高分辨率的 AI 图像可以快速、轻松地生成，无需复杂的后处理，可能降低普通用户的使用门槛，并加速创意工作流程。 这些图像是通过 WanGP 以 1440p 分辨率生成的，用户注意到不需要遮罩、分层或 LoRA，这与典型的高分辨率生成工作流程形成对比。

reddit · r/StableDiffusion · /u/Unit2209 · 7月1日 22:49

**背景**: Krea 2 Turbo 是 Krea 2 的一个快速检查点，Krea 2 是一个文本到图像的扩散模型，旨在产生逼真的输出。WanGP 是一个平台，可以在消费级硬件上本地运行多种 AI 模型，包括 Krea 2 Turbo。通常，使用 AI 模型生成高分辨率图像需要诸如修补（遮罩）、图层合成或使用 LoRA 进行微调等技术才能获得高质量结果。这位用户的体验表明，Krea 2 Turbo 可以跳过其中一些步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/krea/Krea-2-Turbo">krea / Krea - 2 - Turbo · Hugging Face</a></li>
<li><a href="https://wangp.video/">WanGP: All In One AI Video Generator Online Free</a></li>
<li><a href="https://supaimagine.ai/image/krea-2-turbo">Krea 2 Turbo AI Image Generator | SupaImagine</a></li>

</ul>
</details>

**标签**: `#AI image generation`, `#Krea 2 Turbo`, `#Stable Diffusion`, `#WanGP`

---

<a id="item-22"></a>
## [ComfyUI 新节点：本地 LLM 加载器](https://www.reddit.com/r/StableDiffusion/comments/1ul5dcv/introducing_local_llm_loader_a_node_that_makes/) ⭐️ 6.0/10

一个名为(Deno) Local LLM Loader 的新 ComfyUI 节点，允许用户直接将本地大语言模型（如 Ollama 和 LM Studio）接入 ComfyUI 工作流，用于提示生成和自动化。 该节点解决了 ComfyUI 现有 LLM 集成中灵活性和速度的限制，让用户可以轻松切换本地模型，并在链式工作流中保持模型加载，从而简化图像生成流程。 该节点支持多种本地 LLM 后端，包括 Ollama、LM Studio、llama.cpp、vLLM 以及任何兼容 OpenAI 的本地服务器。它还包含一个配套的(Deno) Local LLM Reviewer 节点，可根据审核文本接受或拒绝图像输出。

reddit · r/StableDiffusion · /u/Extension-Yard1918 · 7月2日 02:17

**背景**: ComfyUI 是一个模块化的节点式 AI 图像生成界面，主要使用 Stable Diffusion。用户通过连接节点创建工作流。本地 LLM（如 Ollama 和 LM Studio）允许在个人硬件上运行大语言模型，无需联网，提供隐私和控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://best-of-web.builder.io/library/comfyanonymous/ComfyUI">ComfyUI Overview , Examples, Pros and Cons in 2025</a></li>
<li><a href="https://medium.com/@kapildevkhatik2/how-to-run-and-call-local-llms-with-ollama-a-developers-guide-to-building-offline-ai-apps-1161d9f3a0f8">Run Local LLMs with Ollama : A Developer’s Guide to... | Medium</a></li>
<li><a href="https://lmstudio.ai/">LM Studio - Local AI on your computer</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#local LLM`, `#node`, `#image generation`, `#workflow`

---

<a id="item-23"></a>
## [ComfyUI 27.0 中 Krea2 的 INT8 ConvRot 与 FP8 Scaled 基准测试对比](https://www.reddit.com/r/StableDiffusion/comments/1ukjhag/krea2_int8_convrot_vs_fp8_scaled_in_comfyui_270/) ⭐️ 6.0/10

一位 Reddit 用户发布了在 ComfyUI 0.27.0 中对 Krea2 模型使用 INT8 ConvRot 和 FP8 Scaled 量化方法的基准测试，报告了显著的加速和轻微的输出差异。 该比较为在 RTX 50 系列 GPU 上优化 Krea2 推理速度提供了实践指导，帮助用户在性能与输出质量之间取得平衡。同时也凸显了扩散模型量化技术生态的不断壮大。 基准测试在 RTX 5070 Ti 上运行，操作系统为 Windows 11，ComfyUI 版本为 0.27.0，PyTorch 2.12.0，CUDA 13.0。INT8 ConvRot 模型可在 Hugging Face 的 Comfy-Org/Krea-2 仓库中找到。

reddit · r/StableDiffusion · /u/y3kdhmbdb2ch2fc6vpm2 · 7月1日 11:52

**背景**: 量化通过降低模型权重和激活值的精度来减少内存占用并加速推理。INT8 ConvRot 在量化前对权重和激活进行旋转以去除异常值，而 FP8 Scaled 则使用 8 位浮点数并采用动态逐张量缩放。Krea2 是一款专注于美学的扩散模型，用于创意图像生成。这些技术使得在消费级 GPU 上更高效地运行大型模型成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BobJohnson24/ComfyUI-INT8-Fast">GitHub - BobJohnson24/ComfyUI-INT8-Fast: Custom node to load models in INT8 for 1.5~2X Speed gains on 30 series cards. · GitHub</a></li>
<li><a href="https://docs.vllm.ai/en/v0.5.4/quantization/fp8.html">FP8 - vLLM Documentation</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-krea-2-k2-aesthetic-ai-image-model">What Is Krea 2 (K2)? The Aesthetic-First AI Image Model Explained | MindStudio</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#ComfyUI`, `#quantization`, `#benchmark`, `#Krea2`

---

<a id="item-24"></a>
## [在 Blender 中直接生成 3D 资产并渲染视频](https://www.reddit.com/r/StableDiffusion/comments/1ukxqlp/asset_generation_3d_scene_to_video_all_inside/) ⭐️ 6.0/10

Reddit 上的一个帖子展示了一种工作流程，利用 Pallaidium 插件和 Asset Generator 在 Blender 内部生成 3D 资产并将 3D 场景转换为视频，借助 LTX 和 3DREAL 实现 AI 视频生成。 这种集成消除了寻找外部低多边形资产或离开 Blender 进行视频渲染的需求，为使用 LTX 和 3DREAL 的创作者简化了 3D 到视频的流程。 Pallaidium 是一个免费的开源生成式 AI 电影工作室插件，适用于 Blender 5.2+；Asset Generator 支持使用 FLUX 和 BiRefNet 生成 2D 和 3D 资产，首次运行需要设置环境。

reddit · r/StableDiffusion · /u/tintwotin · 7月1日 20:52

**背景**: LTX Video 和 3DREAL LoRA 是能够将 3D 渲染转换为写实视频的 AI 模型。传统上，用户需要导入外部 3D 资产到 Blender，然后使用单独的工具进行 AI 视频生成。这个工作流程将资产生成和视频渲染直接合并到 Blender 中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tin2tin/Pallaidium">GitHub - tin2tin/Pallaidium: PALLAIDIUM — a generative AI movie...</a></li>
<li><a href="https://github.com/tin2tin/2D_Asset_Generator">GitHub - tin2tin/2D_Asset_Generator: Blender add-on for AI generating 2D assets for visualizations, using FLUX and BiRefNet · GitHub</a></li>
<li><a href="https://hackernoon.com/ltx-23-3dreal-lora-turns-3d-renders-into-photoreal-video">hackernoon.com/ ltx -23- 3 dreal -lora-turns-3d-renders-into-photoreal...</a></li>

</ul>
</details>

**标签**: `#Blender`, `#AI video generation`, `#3D asset generation`, `#Stable Diffusion`, `#workflow`

---

