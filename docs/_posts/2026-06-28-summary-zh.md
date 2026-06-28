---
layout: default
title: "Horizon Summary: 2026-06-28 (ZH)"
date: 2026-06-28
lang: zh
---

> 从 38 条内容中筛选出 23 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：LLM inference、ComfyUI、AMD Strix Halo、speculative decoding、quantization。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[DSpark：推测解码加速 LLM 推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)**
2. **[ComfyUI 插件实现运行时 4 位量化，Ideogram 4 提速 4 倍](https://www.reddit.com/r/StableDiffusion/comments/1uhqasg/i_built_a_comfyui_node_for_runtime_4bit/)**
3. **[AMD Strix Halo RDMA 集群搭建指南](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [后 Mythos 时代的网络安全：保持冷静，继续前进](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [IP Crawl 绘制数千开放网络摄像头，引发隐私争议。](https://ipcrawl.com/)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [DSpark：推测解码加速 LLM 推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：DSpark：推测解码加速 LLM 推理

**关联新闻**: [DSpark：推测解码加速 LLM 推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

**切入角度**: DeepSeek 发布了 DSpark 推测解码框架，同时发布了详细论文和两个 Hugging Face 模型（DeepSeek-V4-Flash-DSpark 和 DeepSeek-V4-Pro-DSpark），这些模型内置了草稿模块。 DSpark 显著加速了 DeepSeek-V4 的推理（每用户吞吐量比 MTP-1 提升 60-85%），这对降低 LLM 应用延迟至关重要；这种开放创新与美国实验室日益保密的做法形成对比。 DSpark 是一种服务优化，它将轻量级草稿模块附加到现有的 DeepSeek-V4 权重上，而非全新模型；它通过 DeepSpec 仓库以 MIT 许可证完全开源。

**可延展方向**: 推测解码是一种推理优化技术，其中小型草稿模型快速提出多个 token，大型目标模型在单个前向传递中验证它们，从而降低延迟。它已成为在不牺牲准确性的情况下加速 LLM 推理的标准方法。

---

### 选题 2：ComfyUI 插件实现运行时 4 位量化，Ideogram 4 提速 4 倍

**关联新闻**: [ComfyUI 插件实现运行时 4 位量化，Ideogram 4 提速 4 倍](https://www.reddit.com/r/StableDiffusion/comments/1uhqasg/i_built_a_comfyui_node_for_runtime_4bit/)

**切入角度**: 一位开发者发布了 QuantFunc，这是一个 ComfyUI 插件，通过自定义 CUDA 内核实现运行时 4 位量化，在 RTX 4090 上将 Ideogram 4 模型（1024×1024，12 步）的推理时间从约 30 秒降至约 8 秒，实现了约 4 倍加速，且无需预量化的检查点文件。 该插件允许用户对任何现有扩散模型动态应用 4 位量化，大幅缩短推理时间，同时保持接近 fp16 基准的质量，从而使高质量图像生成更易用、更高效。 该插件使用自定义 CUDA 内核在加载时对模型权重进行量化，无需预量化检查点；开发者称 4 位量化后质量接近 fp16 基准，并邀请社区在其他模型和 GPU 上进行测试。

**可延展方向**: 量化将模型权重的数值精度降低（例如从 16 位浮点数降至 4 位整数），从而减少内存占用并提高推理速度。传统量化需要单独的预量化检查点，而运行时量化在加载模型时应用该技术，使其兼容任何现有模型。ComfyUI 是一个流行的基于节点的 Stable Diffusion 工作流界面。

---

### 选题 3：AMD Strix Halo RDMA 集群搭建指南

**关联新闻**: [AMD Strix Halo RDMA 集群搭建指南](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md)

**切入角度**: 一份关于使用 AMD Strix Halo 硬件搭建 RDMA 集群以跨多个节点高效运行大型语言模型的详细指南已在 GitHub 上发布。 该指南使家庭实验室爱好者和小型 AI 研究人员能够利用多节点 AMD Strix Halo 系统进行本地 LLM 推理，弥合了消费级硬件与企业集群之间的差距。 该设置使用 ConnectX-5 Ex VPI 网卡进行 RDMA 网络通信，支持节点间高达 256GB 的统一内存，带宽高。基准测试显示在 DeepSeek V4 Flash 和 GLM 5.2 等模型上具有竞争力的性能。

**可延展方向**: RDMA（远程直接内存访问）允许服务器之间无需 CPU 或操作系统参与即可传输数据，实现低延迟和高吞吐量。AMD Strix Halo 将强大的 CPU、GPU（RDNA 3.5）和高达 128GB 的统一内存集成在单个平台上，适合 AI 工作负载。该指南结合了这两种技术，构建了一个经济高效的多节点 LLM 推理集群。

---

1. [DSpark：推测解码加速 LLM 推理](#item-1) ⭐️ 9.0/10
2. [OpenRA 为现代重塑经典 RTS](#item-2) ⭐️ 8.0/10
3. [金融科技手册引发货币存储最佳实践争论](#item-3) ⭐️ 8.0/10
4. [数据分布中的可疑不连续点](#item-4) ⭐️ 8.0/10
5. [IP Crawl 绘制数千开放网络摄像头，引发隐私争议。](#item-5) ⭐️ 8.0/10
6. [ComfyUI 插件实现运行时 4 位量化，Ideogram 4 提速 4 倍](#item-6) ⭐️ 8.0/10
7. [Sana 1.6B 三值量化压缩：体积缩小 8.6 倍，质量接近无损](#item-7) ⭐️ 8.0/10
8. [Decomp Academy：学习将 GameCube 游戏反编译为匹配的 C 代码](#item-8) ⭐️ 7.0/10
9. [AMD Strix Halo RDMA 集群搭建指南](#item-9) ⭐️ 7.0/10
10. [福特用 AI 替代工人适得其反，Hacker News 网友热议](#item-10) ⭐️ 7.0/10
11. [罗宾·威廉姆斯独白引发 AI 批判争论](#item-11) ⭐️ 7.0/10
12. [后 Mythos 时代的网络安全：保持冷静，继续前进](#item-12) ⭐️ 7.0/10
13. [公共 DNS 解析器选择指南](#item-13) ⭐️ 6.0/10
14. [TownSquare：为网站添加临时聊天的小型存在层](#item-14) ⭐️ 6.0/10
15. [亚洲 AI 初创公司推出类似 Mythos 的模型](#item-15) ⭐️ 6.0/10
16. [Krea2 风格迁移首次发布，使用 RoPE](#item-16) ⭐️ 6.0/10
17. [LanPaint 新增 Krea2 Turbo 图像修复支持](#item-17) ⭐️ 6.0/10
18. [ComfyUI 原生支持 INT8 量化](#item-18) ⭐️ 6.0/10
19. [在 RTX 3060 12GB 上训练 Krea 2 LoRA：一个慢速指南](#item-19) ⭐️ 6.0/10
20. [Qwen-Image 在动漫风格上表现出惊人的一致性](#item-20) ⭐️ 6.0/10
21. [为 Krea 2 工作流中的 SageAttention 添加安全补丁](#item-21) ⭐️ 6.0/10
22. [新模型训练角色 LoRA 所需步数减少](#item-22) ⭐️ 6.0/10
23. [NeuralCompanion 重大更新：新增 Discord 语音和安卓控制](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DSpark：推测解码加速 LLM 推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) ⭐️ 9.0/10

DeepSeek 发布了 DSpark 推测解码框架，同时发布了详细论文和两个 Hugging Face 模型（DeepSeek-V4-Flash-DSpark 和 DeepSeek-V4-Pro-DSpark），这些模型内置了草稿模块。 DSpark 显著加速了 DeepSeek-V4 的推理（每用户吞吐量比 MTP-1 提升 60-85%），这对降低 LLM 应用延迟至关重要；这种开放创新与美国实验室日益保密的做法形成对比。 DSpark 是一种服务优化，它将轻量级草稿模块附加到现有的 DeepSeek-V4 权重上，而非全新模型；它通过 DeepSpec 仓库以 MIT 许可证完全开源。

hackernews · aurenvale · 6月27日 09:18 · [社区讨论](https://news.ycombinator.com/item?id=48696585)

**背景**: 推测解码是一种推理优化技术，其中小型草稿模型快速提出多个 token，大型目标模型在单个前向传递中验证它们，从而降低延迟。它已成为在不牺牲准确性的情况下加速 LLM 推理的标准方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/">A Hitchhiker’s Guide to Speculative Decoding – PyTorch</a></li>
<li><a href="https://research.google/blog/looking-back-at-speculative-decoding/">Looking back at speculative decoding</a></li>
<li><a href="https://www.marktechpost.com/2026/06/27/deepseek-releases-dspark-a-speculative-decoding-framework-that-accelerates-deepseek-v4-per-user-generation-60-85-over-mtp-1/">DeepSeek Releases DSpark, a Speculative Decoding Framework That ...</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，用户称赞 DeepSeek 相比美国实验室的开放性和创新性；一些人希望 DSpark 能集成到 DwarfStar 等本地推理工具中，并提到了 DeepSeek-V4 的成功实际使用体验。

**标签**: `#LLM inference`, `#speculative decoding`, `#DeepSeek`, `#AI acceleration`, `#open research`

---

<a id="item-2"></a>
## [OpenRA 为现代重塑经典 RTS](https://www.openra.net/) ⭐️ 8.0/10

OpenRA 是一个开源项目，重制并现代化了《红色警戒》《命令与征服》和《沙丘 2000》等经典即时战略游戏，并改进了平衡性和新增了功能。 该项目在保留经典 RTS 玩法的同时，为现代玩家进行了优化，使备受喜爱的作品重新可用，并培养了活跃的多人游戏社区。 OpenRA 包含模组支持、自定义地图和现代化引擎，并进行了平衡性重做，例如允许盟军火炮射程超过苏联特斯拉线圈。

hackernews · tosh · 6月27日 12:10 · [社区讨论](https://news.ycombinator.com/item?id=48697560)

**背景**: OpenRA 是一个免费开源引擎，重写了经典《命令与征服》系列游戏。原版《红色警戒》于 1996 年由西木工作室发布，被认为是有史以来最伟大的游戏之一。艺电在 2008 年将其免费发布，并于 2020 年推出了重制版合集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openra.net/">OpenRA - Classic strategy games rebuilt for the modern era</a></li>

</ul>
</details>

**社区讨论**: 社区评论称赞 OpenRA 的平衡性改进和现代功能，用户表示其体验比原版显著提升。有人表达怀旧之情并感谢 EA 对项目的容忍，还有人提到了竞技回放和仍然活跃的玩家群体。

**标签**: `#open-source`, `#gaming`, `#RTS`, `#classic-games`

---

<a id="item-3"></a>
## [金融科技手册引发货币存储最佳实践争论](https://w.pitula.me/fintech-engineering-handbook/) ⭐️ 8.0/10

这场争论之所以重要，是因为错误的货币表示可能导致四舍五入误差、财务损失以及整个金融科技行业的合规问题，影响数百万用户。 该手册因内容浅薄和提供不良建议而受到批评，特别是关于使用 IEEE 754 浮点数表示货币值，这种做法已知会导致精度错误。

hackernews · signa11 · 6月27日 10:28 · [社区讨论](https://news.ycombinator.com/item?id=48696982)

**背景**: IEEE 754 是大多数编程语言使用的浮点运算标准，它无法精确表示许多十进制分数，因此不适用于要求精确性的金融计算。最佳实践建议使用整数表示最小单位（如分）或定点十进制类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IEEE_754">IEEE 754 - Wikipedia</a></li>
<li><a href="https://cardinalby.github.io/blog/post/best-practices/storing-currency-values-data-types/">Storing currency values: data types, caveats, best practices ·</a></li>
<li><a href="https://thenewstack.io/what-data-type-should-you-use-for-storing-monetary-values_2/">What Data Type Should You Use for Storing Monetary Values? - The New Stack</a></li>

</ul>
</details>

**社区讨论**: 评论者强烈警告不要以浮点数存储货币值，xlii 表示如果看到这种做法会“尖叫着跑开”。lxgr 警告不要在 API 交换中使用最小单位精度。不过，belmarca 指出该手册收集了有用的信息，大部分是正确的，而 jdw64 则反思了在多样化的金融科技经验中定义优秀编程的困难。

**标签**: `#fintech`, `#software engineering`, `#monetary representation`, `#IEEE 754`, `#best practices`

---

<a id="item-4"></a>
## [数据分布中的可疑不连续点](https://danluu.com/discontinuities/) ⭐️ 8.0/10

Dan Luu 的文章分析了人类行为和系统设计如何在经验分布中造成不自然的峰值，使用了马拉松完赛时间和税收悬崖等例子。 该分析揭示了激励和阈值如何扭曲数据，对政策设计、优化以及统计证据的解释具有重要意义。 文章指出，由于配速小组的存在，马拉松完赛时间在每 30 分钟间隔处出现聚集；英国税收制度中的尖锐悬崖也导致高边际税率和相应的行为反应。

hackernews · tosh · 6月27日 13:32 · [社区讨论](https://news.ycombinator.com/item?id=48698151)

**背景**: 经验分布通常因自然变异而呈现平滑模式。然而，人为阈值（如税档或时间目标）可能会造成尖锐的不连续点，容易被误认为是自然现象。理解这些人为痕迹对于准确解释数据和评估政策至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=28452926">Suspicious Discontinuities | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了现实中的例子：一位跑者提到为了跑进 2:30 而拼尽全力，另一位详细介绍了英国税收悬崖，包括儿童保育和个人津贴递减。关于取消经济状况调查的建议引发了关于普适服务与定向福利的讨论。

**标签**: `#data analysis`, `#statistics`, `#behavioral economics`, `#public policy`, `#optimization`

---

<a id="item-5"></a>
## [IP Crawl 绘制数千开放网络摄像头，引发隐私争议。](https://ipcrawl.com/) ⭐️ 8.0/10

一个名为 IP Crawl 的新网站编录了数千个可公开访问的网络摄像头，允许任何人浏览和观看来自未加密的物联网摄像头的实时画面。 该项目鲜明地揭示了物联网设备普遍存在的安全问题——它们通常带有默认凭据和未加密的流。这使得隐私、制造商责任以及暴露这些画面的伦理问题变得紧迫。 IP Crawl 通过扫描使用未加密的 HTTP 或 RTSP 协议的摄像头来工作，许多摄像头从未更改过出厂默认设置。该网站包含来自海康威视、Axis、Wyze 等知名制造商的画面。

hackernews · arm32 · 6月27日 19:09 · [社区讨论](https://news.ycombinator.com/item?id=48700834)

**背景**: 许多物联网设备，尤其是网络摄像头，出厂时带有默认的用户名和密码，用户很少更改。加上未加密的流媒体协议，这些设备很容易在公共互联网上被发现。研究表明，全球有超过 40,000 个此类摄像头暴露在外，且问题已持续多年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ipcrawl.com/">IP Crawl — open webcam catalog</a></li>
<li><a href="https://alec.is/posts/ip-crawl-exposing-the-massive-open-webcam-crisis/">IP Crawl: Exposing The Massive Open Webcam Crisis | Alec Armbruster</a></li>
<li><a href="https://www.securitymagazine.com/articles/101692-40-000-iot-security-cameras-are-exposed-online">40,000 IoT Security Cameras Are Exposed Online | Security ...</a></li>

</ul>
</details>

**社区讨论**: 评论表达了不安，用户将网站比作窥视私人住宅的望远镜。一位评论者指出这并非新现象，并链接到一篇 2012 年的文章。另一人识别出显示英国大麻种植室的特定画面，其他人则仅对观看陌生人的生活感到毛骨悚然。

**标签**: `#security`, `#privacy`, `#webcams`, `#IoT`, `#ethics`

---

<a id="item-6"></a>
## [ComfyUI 插件实现运行时 4 位量化，Ideogram 4 提速 4 倍](https://www.reddit.com/r/StableDiffusion/comments/1uhqasg/i_built_a_comfyui_node_for_runtime_4bit/) ⭐️ 8.0/10

一位开发者发布了 QuantFunc，这是一个 ComfyUI 插件，通过自定义 CUDA 内核实现运行时 4 位量化，在 RTX 4090 上将 Ideogram 4 模型（1024×1024，12 步）的推理时间从约 30 秒降至约 8 秒，实现了约 4 倍加速，且无需预量化的检查点文件。 该插件允许用户对任何现有扩散模型动态应用 4 位量化，大幅缩短推理时间，同时保持接近 fp16 基准的质量，从而使高质量图像生成更易用、更高效。 该插件使用自定义 CUDA 内核在加载时对模型权重进行量化，无需预量化检查点；开发者称 4 位量化后质量接近 fp16 基准，并邀请社区在其他模型和 GPU 上进行测试。

reddit · r/StableDiffusion · /u/lesesis · 6月28日 07:00

**背景**: 量化将模型权重的数值精度降低（例如从 16 位浮点数降至 4 位整数），从而减少内存占用并提高推理速度。传统量化需要单独的预量化检查点，而运行时量化在加载模型时应用该技术，使其兼容任何现有模型。ComfyUI 是一个流行的基于节点的 Stable Diffusion 工作流界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QuantFunc/ComfyUI-QuantFunc">GitHub - QuantFunc/ComfyUI-QuantFunc · GitHub</a></li>
<li><a href="https://huggingface.co/QuantFunc/Nunchaku-Qwen-Image-2512">QuantFunc/Nunchaku-Qwen-Image-2512 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#quantization`, `#GPU acceleration`, `#Stable Diffusion`, `#CUDA`

---

<a id="item-7"></a>
## [Sana 1.6B 三值量化压缩：体积缩小 8.6 倍，质量接近无损](https://www.reddit.com/r/StableDiffusion/comments/1uhoo93/clarklabsclarkairsana16b158bit_hugging_face/) ⭐️ 8.0/10

Clark Labs 发布了 Sana 1.6B 文本到图像模型的压缩版本，采用三值量化将每个权重降至约 1.85 比特，模型体积从 3.21 GB 缩小到 374 MB（缩小 8.6 倍），同时保持接近 FP16 的图像质量。 这一突破使大型文本到图像模型更易于在边缘设备和本地部署，存储和内存需求降低近一个数量级，且质量损失很小。 量化采用分组缩放并保留约 5%的高精度参数（包括条件层和投影层）。打包的三值 safetensors 文件仅 374 MB，同时提供了解压后的 BF16 版本以保持兼容性。

reddit · r/StableDiffusion · /u/LumenLime · 6月28日 05:30

**背景**: 三值量化将神经网络权重映射为三个可能的值 {-1, 0, +1}，与 16 位或 32 位浮点格式相比，大幅缩小模型尺寸并降低计算成本。Sana 模型是 NVIDIA 开发的线性扩散变压器，用于高效高分辨率图像合成。这种压缩技术使得大型变压器模型能在资源有限的设备上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2303.01505">[2303.01505] Ternary Quantization: A Survey - arXiv.org TropComplique/trained-ternary-quantization - GitHub Ternary Quantization in Neural Networks - emergentmind.com TRQ: Ternary Neural Networks With Residual Quantization TRQ: Ternary Neural Networks With Residual Quantization A Survey on Binary and Ternary Neural Networks and Their ...</a></li>
<li><a href="https://github.com/NVlabs/Sana">GitHub - NVlabs/Sana: SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer · GitHub</a></li>

</ul>
</details>

**标签**: `#model compression`, `#ternary quantization`, `#text-to-image`, `#efficient AI`, `#Sana`

---

<a id="item-8"></a>
## [Decomp Academy：学习将 GameCube 游戏反编译为匹配的 C 代码](https://decomp-academy.dev/) ⭐️ 7.0/10

Decomp Academy 是一个互动式教育平台，教用户如何将 GameCube 游戏中的 PowerPC 汇编反编译为匹配的 C 代码，并使用实时的 Metrowerks CodeWarrior GC/2.0 编译器验证精确的指令级匹配。 该工具降低了参与游戏反编译项目的门槛，可能加速经典 GameCube 游戏（如星际火狐大冒险、马里奥派对 4、密特罗德 Prime）的保存和修改。 该网站目前提供超过 250 节课，从基础概念开始，部分课程使用活跃反编译项目中的真实函数。所有课程都以 Markdown 格式存储在公开的 GitHub 仓库中，便于贡献。

hackernews · jackpriceburns · 6月28日 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48703412)

**背景**: 游戏反编译的目标是生成可读的 C 代码，当使用原始工具链（如 Metrowerks CodeWarrior）编译时，生成与原始游戏相同的二进制文件，这称为“匹配”反编译。这个过程比使用通用反编译器（如 Ghidra）更为严格，传统上需要深入的汇编和 C 语言知识。Decomp Academy 为这一小众技能提供了结构化的学习路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://macabeus.medium.com/game-decompilation-using-ai-4d47b65f8852">Development Journey on Game Decompilation Using AI | by Bruno Macabeus | Medium</a></li>
<li><a href="https://github.com/encounter/decomp-toolkit">GitHub - encounter/decomp-toolkit: A GameCube & Wii decompilation toolkit · GitHub</a></li>
<li><a href="https://daniel-mccarthy.github.io/MW/">Metrowerks CodeWarrior releases</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出对将 LLM 和分步逆向工程应用于反编译的兴趣，以及一位用户在课程中通过提前返回“作弊”。总体情绪积极，赞赏简化的网络界面以及为正在进行项目做贡献的潜力。

**标签**: `#reverse-engineering`, `#game-decompilation`, `#gamecube`, `#assembly`, `#education`

---

<a id="item-9"></a>
## [AMD Strix Halo RDMA 集群搭建指南](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md) ⭐️ 7.0/10

一份关于使用 AMD Strix Halo 硬件搭建 RDMA 集群以跨多个节点高效运行大型语言模型的详细指南已在 GitHub 上发布。 该指南使家庭实验室爱好者和小型 AI 研究人员能够利用多节点 AMD Strix Halo 系统进行本地 LLM 推理，弥合了消费级硬件与企业集群之间的差距。 该设置使用 ConnectX-5 Ex VPI 网卡进行 RDMA 网络通信，支持节点间高达 256GB 的统一内存，带宽高。基准测试显示在 DeepSeek V4 Flash 和 GLM 5.2 等模型上具有竞争力的性能。

hackernews · jakogut · 6月28日 00:46 · [社区讨论](https://news.ycombinator.com/item?id=48703258)

**背景**: RDMA（远程直接内存访问）允许服务器之间无需 CPU 或操作系统参与即可传输数据，实现低延迟和高吞吐量。AMD Strix Halo 将强大的 CPU、GPU（RDNA 3.5）和高达 128GB 的统一内存集成在单个平台上，适合 AI 工作负载。该指南结合了这两种技术，构建了一个经济高效的多节点 LLM 推理集群。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/gpu-specs/amd-strix-halo.g1096">AMD Strix Halo GPU Specs | TechPowerUp GPU Database</a></li>
<li><a href="https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-395.html">AMD Ryzen™ AI Halo Developer Platform with Ryzen™ AI Max+ 395 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_direct_memory_access">Remote direct memory access - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该指南充满热情，pixelpoet 指出成功使用 128GB Strix Halos 进行 DeepSeek V4 Flash 推理，速度可用。jcastro 正在搭建一个三节点代理操作系统工厂，sdlkj-称赞 RDMA 是从消费级 GPU 到更大内存配置的桥梁。部分成员讨论了使用 ConnectX-5 与更便宜的 ConnectX-3 网卡之间的权衡。

**标签**: `#AMD Strix Halo`, `#RDMA`, `#LLM inference`, `#cluster computing`, `#homelab`

---

<a id="item-10"></a>
## [福特用 AI 替代工人适得其反，Hacker News 网友热议](https://www.the-independent.com/tech/ford-ai-automation-human-workers-b3003787.html) ⭐️ 7.0/10

福特试图用 AI 系统替代人工质检员，但此举适得其反，导致质量问题并重新雇佣了部分工人。文章称这是一个警示故事，但 Hacker News 评论者认为这些 AI 工具已经过时，且结果实际上是积极的。 这个故事凸显了在不了解 AI 局限性的情况下过度依赖 AI 的风险，尤其是在制造业质量控制中。它也展示了技术社区的观点如何挑战媒体叙事，强调了在报道 AI 应用时需要平衡。 据 Hacker News 用户 WarmWash 称，所涉及的 AI 系统并非大型语言模型，而是基于 CNN 的旧式视觉检测工具（MAIVIS 和 AiTriz），运行在定制 IBM 硬件上。用户 arjie 指出，福特重新雇佣了部分工人，并达到了顶级质量排名，表明这种方法奏效了。

hackernews · speckx · 6月28日 03:09 · [社区讨论](https://news.ycombinator.com/item?id=48703968)

**背景**: 福特在质量方面有着悠久的历史，1990 年代的广告强调'质量是第一要务'，但近几十年来质量下降。基于 AI 的视觉检测已在制造业中使用多年，但像 CNN 这样的旧系统在应对变异和光照方面存在局限。文章的叙事可能过度简化了自动化与人类专业知识之间的复杂相互作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dabrico.com/machine-vision-inspection/">7 Limitations of Traditional Machine Vision Inspection</a></li>
<li><a href="https://www.numberanalytics.com/blog/expert-systems-smart-manufacturing">Expert Systems: The Future of Smart Manufacturing</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论大多质疑文章的负面框架。Murphomatic 警告董事会对 AI 的过度依赖，而 WarmWash 澄清了所使用的具体过时技术。Arjie 认为此举实际上提高了质量，将其比作类似 DOGE 的效率方法。Incipient 的评论不完整且似乎偏离主题。

**标签**: `#AI`, `#automation`, `#Ford`, `#labor`, `#quality control`

---

<a id="item-11"></a>
## [罗宾·威廉姆斯独白引发 AI 批判争论](https://jayacunzo.com/blog/your-move-chief) ⭐️ 7.0/10

Jay Acunzo 的一篇文章认为，电影《心灵捕手》中罗宾·威廉姆斯的独白完美捕捉了人们对 AI 生成内容的不安感，在 Hacker News 上引发了讨论。 这场讨论凸显了围绕 AI 模仿人类表达却缺乏真实体验的文化张力，影响公众认知和舆论走向。 独白强调品尝草莓或失去亲人等经历，AI 无法真正拥有，这突显了对生成式 AI 的核心批评。

hackernews · herbertl · 6月28日 01:28 · [社区讨论](https://news.ycombinator.com/item?id=48703452)

**背景**: 罗宾·威廉姆斯在 1997 年电影《心灵捕手》中的独白对比了书本知识与亲身经历。文章将此应用到 AI 上，AI 能生成流畅文本但缺乏具身体验，加剧了 AI 取代人类创造力的焦虑。

**社区讨论**: 评论者意见分歧：有人赞同独白精准指出了 AI 因缺乏真实体验而令人不安的原因，而另一些人则认为独白自以为是，或主张 AI 即使没有个人经历也能产生有价值的见解。有反驳者引用《银翼杀手》中罗伊·巴蒂的‘雨中泪水’台词，认为虚构角色也能表达深刻的失去感。

**标签**: `#AI`, `#culture`, `#discussion`, `#technology`

---

<a id="item-12"></a>
## [后 Mythos 时代的网络安全：保持冷静，继续前进](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/) ⭐️ 7.0/10

一篇博文指出，围绕 Anthropic 未发布的 Mythos AI 模型的网络安全恐慌被夸大了，强调配置错误和内存安全等传统问题仍是主要威胁。 这一观点有助于安全专业人员专注于行之有效的风险管理，而不是追逐围绕新 AI 漏洞的炒作，有望减少供应商驱动的恐慌蔓延。 Mythos 是 Anthropic 的 Claude Fable 5 模型的一个变体，专为漏洞发现而设计，但因安全担忧未公开发布。文章指出，即使是 Deepseek V4 Flash 这样的先进模型也能发现漏洞，但核心风险依然是那些日常问题。

hackernews · Versipelle · 6月27日 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48698559)

**背景**: Mythos 是 Anthropic 开发的一种大型语言模型，用于发现软件漏洞。该公司认为其公开发布过于危险，引发了争论。许多网络安全供应商一直在推销针对 Mythos 的解决方案，导致被指责为恐吓营销。这符合网络安全领域长期存在的张力：在新型 AI 威胁与持久存在的常见问题之间平衡注意力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-mythos-and-why-are-experts-worried-about-anthropics-ai-model/">What is Mythos, Anthropic’s unreleased AI model, and how ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为内存安全和配置错误比 Mythos 带来的恐惧更为紧迫。一位用户指出，供应商在没有任何真实信息的情况下立即开始推销解决方案。另一位强调了 LLM 在 CTF 挑战中的有效性，暗示该领域必须适应。

**标签**: `#cybersecurity`, `#AI`, `#memory safety`, `#risk management`, `#hype`

---

<a id="item-13"></a>
## [公共 DNS 解析器选择指南](https://evilbit.de/dns-resolver-guide.html) ⭐️ 6.0/10

这份指南比较了公共 DNS 解析器，重点介绍了隐私、安全功能以及强制门户的行为。 随着互联网用户对隐私越来越关注，选择可信赖的 DNS 解析器变得至关重要；该指南帮助用户权衡速度、隐私和公共网络可用性之间的利弊。 该指南涵盖了包括 NextDNS 和 Cloudflare 在内的免费和付费服务，并针对强制门户（通常需要使用网络自身的 DNS）提供了具体建议。

hackernews · pawal · 6月27日 22:11 · [社区讨论](https://news.ycombinator.com/item?id=48702273)

**背景**: 公共 DNS 解析器是将域名转换为 IP 地址的服务，通常用作 ISP 提供 DNS 的替代方案，以获得更好的速度或隐私。强制门户是公共 Wi-Fi 上拦截网络流量的登录页面，通常通过劫持 DNS 直到用户接受条款。它们会干扰自定义 DNS 设置，需要变通方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Captive_portal">Captive portal</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：一些用户运行自己的 DNS 以完全控制，而另一些用户依赖 NextDNS 等服务。一个常见的痛点是强制门户需要更改 DNS，但没有通用解决方案。一些用户建议使用本地 DNS 代理或 DoH 来绕过限制。

**标签**: `#DNS`, `#privacy`, `#security`, `#networking`

---

<a id="item-14"></a>
## [TownSquare：为网站添加临时聊天的小型存在层](https://cauenapier.com/blog/townsquare_release/) ⭐️ 6.0/10

TownSquare 是一个新发布的小型存在层，网站可以嵌入它来显示当前在线用户，并支持无需账户或注册的临时聊天。 该工具旨在恢复网络上真实人类存在的感受，促进社区互动而无需社交网络的复杂性。它可能影响网站设计实时互动功能的方式。 TownSquare 有意设计为遗忘型：没有账户、个人资料、关注者数和永久聊天记录；消息仅在参与者在线时存在。它被设计为轻量级的可嵌入小部件。

hackernews · eustoria · 6月27日 17:11 · [社区讨论](https://news.ycombinator.com/item?id=48699928)

**背景**: 存在层是一种薄软件层，用于在网站上显示用户的在线状态，类似于旧即时通讯软件中的好友列表或早期网页的侧边栏小部件。临时聊天意味着用户离开时消息自动删除，鼓励自发、低风险的对话。TownSquare 重振了这一概念，灵感来自怀旧网络功能，如“My Blog Log”或 ff0000 多人空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://partridge.substack.com/p/what-the-presence-layer-actually">What the Presence Layer Actually Is - by Brittany Partridge</a></li>
<li><a href="https://github.com/cLLeB/ephemeral-chat">GitHub - cLLeB/ephemeral-chat: Privacy based communication</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论褒贬不一，但总体怀旧：一些用户深情回忆过去的类似工具（例如通过“My Blog Log”结识配偶），而另一些用户则觉得界面令人困惑或不吸引人。少数评论者希望有工具能促进线下聚会，而非临时在线聊天。

**标签**: `#web development`, `#presence`, `#ephemeral`, `#community`, `#social`

---

<a id="item-15"></a>
## [亚洲 AI 初创公司推出类似 Mythos 的模型](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/) ⭐️ 6.0/10

包括 Sakana AI 在内的亚洲 AI 初创公司，在 Anthropic 对其先进 AI 实施出口禁令之际，推出了类似 Anthropic 的 Mythos 的模型，如 Fugu 多智能体编排系统。 这些发布旨在填补 Anthropic 模型出口限制留下的空白，但社区反馈显示成本高昂且性能不稳定，令人质疑它们相较于现有模型（如 Opus）的实际效用。 Fugu 并非单一整体模型，而是一个多智能体编排系统，它将任务路由到多个底层模型（如其 OpenRouter 页面所述）。用户报告称，20 美元套餐很快耗尽，且结果比 Anthropic 的 Opus 更慢、更差。

hackernews · bogdiyan · 6月27日 13:10 · [社区讨论](https://news.ycombinator.com/item?id=48697958)

**背景**: Claude Mythos 是 Anthropic 未发布的大型语言模型，旨在发现软件漏洞；公司出于安全担忧未予发布。Sakana AI 的 Fugu 于 2026 年推出，自称是一个可通过单一 API 访问的多智能体系统，旨在与前沿模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>
<li><a href="https://sakana.ai/fugu-release/">Sakana Fugu: One Model to Command Them All</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达怀疑：用户报告 Fugu 昂贵且缓慢，有人指出它在一次提示中就消耗了 20 美元且未能达到 Opus 的输出水平。其他人指出 Fugu 不是模型而是路由系统，并且在没有标准化测试的情况下，基准比较令人困惑。

**标签**: `#AI`, `#startups`, `#models`, `#export ban`, `#Fugu`

---

<a id="item-16"></a>
## [Krea2 风格迁移首次发布，使用 RoPE](https://www.reddit.com/r/StableDiffusion/comments/1uhpiov/krea2_style_transfer_first_release/) ⭐️ 6.0/10

Krea2 风格迁移方法首次发布，该方法使用 RoPE（旋转位置嵌入）在 ComfyUI 中实现无需训练的风格迁移。文章提供了安装步骤和工作流程技巧，用于将单张参考图像的风格应用于文本到图像输出。 这引入了一种新颖的、无需训练的风格迁移方法，适用于基于 DiT 的模型，能够更好地控制风格强度并减少伪影。它可能简化和增强 ComfyUI 中 Stable Diffusion 用户的风格迁移工作流程。 该方法对参数变化敏感，关键参数包括 scale start、scale end 和 adain strength。作者建议大多数风格起始块范围为 7-999，并指出更详细的提示可以使用更少的风格块。

reddit · r/StableDiffusion · /u/Winter_unmuted · 6月28日 06:16

**背景**: Krea2 是一个具有高级风格控制能力的 AI 图像基础模型，支持情绪板和风格参考。RoPE（旋转位置嵌入）最初用于语言模型，此处被改编用于 ComfyUI 中 DiT（扩散变换器）模型的无需训练的风格迁移。ComfyUI 是 Stable Diffusion 的流行基于节点的界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.krea.ai/developers/krea-2/style-transfer">Style transfer - Krea</a></li>
<li><a href="https://github.com/BigStationW/ComfyUi-Untwisting-RoPE">GitHub - BigStationW/ComfyUi-Untwisting-RoPE: Training-free ...</a></li>
<li><a href="https://www.runcomfy.com/comfyui-nodes/ComfyUi-Untwisting-RoPE">ComfyUi-Untwisting-RoPE detailed guide | ComfyUI</a></li>

</ul>
</details>

**标签**: `#style transfer`, `#Stable Diffusion`, `#RoPE`, `#ComfyUI`

---

<a id="item-17"></a>
## [LanPaint 新增 Krea2 Turbo 图像修复支持](https://www.reddit.com/r/StableDiffusion/comments/1uhltc3/krea2_turbo_inpainting_with_lanpaint/) ⭐️ 6.0/10

通用图像修复工具 LanPaint 现已支持 Krea2 Turbo，这是一个支持 LoRA 和提示增强的快速文本到图像模型。用户只需加载图片、绘制遮罩并输入提示词即可进行修复。 这一集成扩展了 LanPaint 的模型兼容性，让用户能够使用前沿的高速模型进行图像修复。它简化了 AI 艺术家的创作流程，无需等待专有修复模型即可利用最新扩散模型。 LanPaint 是一款无需训练、通用的图像修复/外绘工具，适用于任何扩散模型。Krea2 Turbo 支持开箱即用，此外 LanPaint 还支持 Ideogram4、Flux2 Klein 以及 Wan2.2 视频修复等其他模型。

reddit · r/StableDiffusion · /u/Mammoth_Layer444 · 6月28日 03:02

**背景**: 图像修复（Inpainting）是指重建图像中缺失或修改部分的过程，广泛应用于 AI 艺术创作。许多新扩散模型缺乏专用的修复版本，因此像 LanPaint 这样的通用工具很有价值。Krea2 Turbo 由 Krea 于 2026 年发布，是 Krea2 文本到图像模型的快速迭代版本，旨在保持原有能力的同时大幅缩短生成时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.krea.ai/blog/krea-2-turbo">Introducing Krea 2 Turbo - Krea</a></li>
<li><a href="https://github.com/scraed/LanPaint">GitHub - scraed/LanPaint: High quality training free inpaint ...</a></li>

</ul>
</details>

**标签**: `#stable diffusion`, `#inpainting`, `#tool`, `#AI art`

---

<a id="item-18"></a>
## [ComfyUI 原生支持 INT8 量化](https://www.reddit.com/r/StableDiffusion/comments/1uhcg69/comfyui_now_natively_supports_int8_tested_and/) ⭐️ 6.0/10

ComfyUI 现已原生支持加载 INT8 量化的扩散模型和文本编码器，并经社区测试确认。有用户在 Hugging Face 上分享了多个量化模型，包括 Krea 2 和 LTX-2.3 的模型及相应工作流。 原生 INT8 支持使用户能够以更低内存占用和更快推理速度运行扩散模型，使高质量图像生成在消费级 GPU 上更易实现。这也为量化的更广泛采用铺平了道路。 当前实现支持常规 INT8 量化，但尚未支持 ConvRot 方法，不过用户预计未来会更新。该用户还计划发布教程，讲解如何使用基于 CUDA 的 GPU 将任意 Comfy 模型转换为 INT8。

reddit · r/StableDiffusion · /u/Winougan · 6月27日 20:03

**背景**: INT8 量化将模型权重精度从 32 位浮点数降低到 8 位整数，显著减少内存占用并加速推理，尤其是在具有 Tensor Cores 的 GPU 上。该技术广泛用于大型语言模型，但直到最近才在扩散模型中较为常见，Quanto 等工具弥补了这一差距。ConvRot 是一种较新的基于旋转的量化方法，可实现 4 位推理，但尚未原生集成到 ComfyUI 中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/quanto-diffusers">Memory-efficient Diffusion Transformers with Quanto and Diffusers</a></li>
<li><a href="https://arxiv.org/abs/2512.03673">ConvRot: Rotation-Based Plug-and-Play 4-bit Quantization for ...</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#INT8`, `#quantization`, `#StableDiffusion`, `#performance`

---

<a id="item-19"></a>
## [在 RTX 3060 12GB 上训练 Krea 2 LoRA：一个慢速指南](https://www.reddit.com/r/StableDiffusion/comments/1uh95sz/training_krea_2_lora_on_rtx3060_12gb_a_slow/) ⭐️ 6.0/10

一位用户分享了在 RTX 3060 12GB 显卡上训练 Krea 2 LoRA 的详细指南，通过降低分辨率、禁用样本生成等妥协方案，在内存不足错误下仍取得了成果。 该指南表明，VRAM 有限的消费级显卡仍能微调 Krea 2 等现代图像模型，从而扩大了无需高端硬件的爱好者与独立创作者的准入门槛。 作者以 768 分辨率、1250-1500 步训练 LoRA（而非 LoKr），需要 64GB RAM 用于卸载，并指出 AI Toolkit 在 12GB 显卡上训练 LoKr 会立即 OOM 崩溃；Musubi Tuner 可能效率更高。

reddit · r/StableDiffusion · /u/repolevedd · 6月27日 17:50

**背景**: Krea 2 是一个开源图像基础模型，专注于美学与风格生成。LoRA（低秩适应）是一种参数高效的微调方法，其所需 VRAM 少于 LoKr（低秩 Kronecker），后者使用不同的分解方式。在 RTX 3060 12GB 等消费级显卡上训练因 VRAM 限制而充满挑战，通常需要将内存卸载至系统 RAM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.krea.ai/krea-2">Krea 2: AI Image Foundation Model & Style Control</a></li>
<li><a href="https://github.com/ostris/ai-toolkit/">GitHub - ostris/ai-toolkit: The ultimate training toolkit for ...</a></li>
<li><a href="https://www.runcomfy.com/trainer/ai-toolkit/flux-2-klein-lokr-vs-lora-character-training">LoKr vs LoRA Training for FLUX Klein: Which Gives Better ...</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#LoRA`, `#VRAM`, `#Krea`, `#Training`

---

<a id="item-20"></a>
## [Qwen-Image 在动漫风格上表现出惊人的一致性](https://www.reddit.com/r/StableDiffusion/comments/1uhq8ol/qwenimage_consistency_is_kinda_wild/) ⭐️ 6.0/10

一名 Reddit 用户报告称，使用默认的 ComfyUI 工作流提示时，Qwen-Image 能够在多个随机种子间一致地保持 1990 年代 OVA 动漫风格（平涂赛璐珞着色、胶片颗粒、光照），尽管背景和手部细节不够稳定。 这一观察凸显了 Qwen-Image 作为动漫风格图像生成专用工具的潜力，而模型的一致性在该领域往往具有挑战性，并表明该模型在这些用例中被低估了。 用户使用了官方 ComfyUI 工作流中的默认提示，仅改变随机种子，观察到角色风格保持稳定，而背景和手部细节有所退化。该模型（Qwen-Image）是阿里巴巴 Qwen 团队开发的 20B 参数 MMDiT 模型。

reddit · r/StableDiffusion · /u/chanteuse_blondinett · 6月28日 06:57

**背景**: Qwen-Image 是阿里巴巴 Qwen 团队开发的 20B 参数图像生成模型，采用 MMDiT 架构。它能够实现高保真文本渲染和精确图像编辑。ComfyUI 是一个开源、基于节点的界面，用于构建和运行扩散模型工作流，常与 Stable Diffusion 和 Qwen-Image 等模型一起使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen-Image">Qwen-Image - Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen-Image">GitHub - QwenLM/Qwen-Image: Qwen-Image is a powerful image ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>

</ul>
</details>

**标签**: `#Qwen-Image`, `#image consistency`, `#anime generation`, `#Stable Diffusion`

---

<a id="item-21"></a>
## [为 Krea 2 工作流中的 SageAttention 添加安全补丁](https://www.reddit.com/r/StableDiffusion/comments/1uhj0tt/krea_2_krea_2_turbo_sageattention_guard_patch_for/) ⭐️ 6.0/10

一位社区开发者发布了一个针对 ComfyUI-KJNodes 的补丁包，为 Patch Sage Attention KJ 节点添加了防护措施，确保其安全处理 Krea 2 和 Krea 2 Turbo 模型，能够检测模型修补器、仅允许批准的注意力路径，并提供针对不支持配置的回退方案。 该补丁可防止在使用 SageAttention 与 Krea 2 模型时出现崩溃和不安全的注意力修改，从而在 ComfyUI 中实现更可靠、更稳定的图像生成工作流，而无需用户完全禁用优化。 该补丁包括检测 Krea 2 模型修补器、对扩散注意力路径进行白名单管理、跳过不支持的形状/掩码/数据类型/头数量，以及干运行验证模式。它还能避免触及 Qwen 注意力路径，并已在 SageAttention 1.0.6 和 Krea 2 Turbo/RAW 模型上测试通过。

reddit · r/StableDiffusion · /u/SurrealByDesign · 6月28日 00:47

**背景**: SageAttention 是一种针对注意力机制的 8 位量化方法，可在 GPU 上加速 Transformer 模型。Krea 2 是一个开源图像基础模型，专注于创意和风格化生成。ComfyUI-KJNodes 是 ComfyUI 的自定义节点集合，其中包含 Patch Sage Attention 节点。如果没有防护措施，将 SageAttention 应用于 Krea 2 模型可能因不支持的配置而导致错误或崩溃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/thu-ml/SageAttention">GitHub - thu-ml/SageAttention: [ICLR2025, ICML2025 ...</a></li>
<li><a href="https://www.krea.ai/krea-2">Krea 2: AI Image Foundation Model & Style Control</a></li>
<li><a href="https://github.com/kijai/ComfyUI-KJNodes">GitHub - kijai/ComfyUI-KJNodes: Various custom nodes for ...</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#ComfyUI`, `#SageAttention`, `#Krea`, `#attention optimization`

---

<a id="item-22"></a>
## [新模型训练角色 LoRA 所需步数减少](https://www.reddit.com/r/StableDiffusion/comments/1uhqkvj/is_the_number_of_steps_needed_to_train_character/) ⭐️ 6.0/10

一位用户报告称，使用 Krea 2 和 AI-Toolkit 训练角色 LoRA 只需要大约 2000 步，而使用 Z-Image 等旧工具则需要 8000 步，且质量相当甚至更好。 这一观察表明，新模型和工具在 LoRA 训练效率上显著提升，可能降低创作者的入门门槛，并加速角色微调的迭代。 用户对两次训练使用了相同的 80 张图像数据集；使用 Z-Image 时，最佳结果在 3000-3600 步之间，而使用 Krea 2 时，最佳步数在 1400-1600 步之间。用户指出，Krea 2 的 2000 步可能略微过拟合。

reddit · r/StableDiffusion · /u/piero_deckard · 6月28日 07:16

**背景**: LoRA（低秩适应）是一种参数高效的微调技术，通过向预训练模型添加轻量级适配器，以最小计算成本实现特定任务定制。Krea 2 是 Krea AI 推出的新一代基础模型，专为美观图像生成设计。AI-Toolkit 是一个开源扩散模型训练套件，简化了在消费级硬件上的 LoRA 训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://www.krea.ai/krea-2">Krea 2: AI Image Foundation Model & Style Control</a></li>
<li><a href="https://github.com/ostris/ai-toolkit/">GitHub - ostris/ai-toolkit: The ultimate training toolkit for ...</a></li>

</ul>
</details>

**标签**: `#LoRA`, `#Stable Diffusion`, `#model training`, `#AI art`, `#fine-tuning`

---

<a id="item-23"></a>
## [NeuralCompanion 重大更新：新增 Discord 语音和安卓控制](https://www.reddit.com/r/StableDiffusion/comments/1uhdxje/major_neuralcompanion_release_ready/) ⭐️ 6.0/10

NeuralCompanion 发布重大更新，集成了 Discord 语音桥接、安卓远程控制应用、MuseTalk 动画支持，以及伴侣球升级、角色扮演改进等众多增强功能。 此次更新大幅拓展了 NeuralCompanion 的功能，使其更接近可完全交互的本地 AI 伴侣，能在语音频道中运行并远程控制，可能吸引更多 AI 伴侣领域的用户。 Discord 语音桥接允许在 Discord 频道中进行语音输入/输出，安卓应用支持局域网控制和聊天，MuseTalk 集成为伴侣球增加了实时唇形同步功能。许多功能仍为实验性，建议全新安装。

reddit · r/StableDiffusion · /u/lainol · 6月27日 21:04

**背景**: NeuralCompanion 是一款开源、本地优先的 Windows AI 伴侣，支持实时聊天、语音、头像和视觉回复。MuseTalk 是一种实时唇形同步模型，可根据音频输入动画化面部，而伴侣球是可定制的叠加头像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Rakile/NeuralCompanion">GitHub - Rakile/NeuralCompanion</a></li>
<li><a href="https://github.com/TMElyralab/MuseTalk">GitHub - TMElyralab/MuseTalk: MuseTalk: Real-Time High ...</a></li>
<li><a href="https://roboticcontent.com/neuralcompanion/">NeuralCompanion - Robotic Content</a></li>

</ul>
</details>

**标签**: `#NeuralCompanion`, `#AI companion`, `#voice integration`, `#MuseTalk`, `#Stable Diffusion`

---