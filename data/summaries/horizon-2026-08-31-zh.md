# Horizon 每日速递 - 2026-08-31

> 从 34 条内容中筛选出 21 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：Stable Diffusion、video editing、video generation、MiniMax H3、watermark removal。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[MiniMax H3 角色设定图工作流：正面/侧面/背面，完全本地运行](https://www.reddit.com/r/StableDiffusion/comments/1w2dujd/i_turned_that_h3_as_an_image_editor_post_into_a/)**
2. **[Reddit 用户分享使用 ProPainter 节点本地去除视频水印](https://www.reddit.com/r/StableDiffusion/comments/1w2dtfg/remove_watermark_from_videos/)**
3. **[MMH3 加速器评测：Sage+Spectrum 质量最佳，速度减半](https://www.reddit.com/r/StableDiffusion/comments/1w2z2ua/mmh3_several_accelerators_tested_for_quality/)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI 安全与软件治理

- **关联热点**: [QubesOS 披露 QSB-118：复制到 VM 错误报告通道可致任意代码执行](https://www.qubes-os.org/news/2026/08/29/qsb-118/)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 2. 算力芯片与服务器

- **关联热点**: [HR Endless Sampler：16GB 显存渲染无限长度 Minimax H3 视频](https://www.reddit.com/r/StableDiffusion/comments/1w25d7g/hr_endless_sampler_now_you_can_create_minimax_h3/)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

### 3. AI 创作工具

- **关联热点**: [HR Endless Sampler：16GB 显存渲染无限长度 Minimax H3 视频](https://www.reddit.com/r/StableDiffusion/comments/1w25d7g/hr_endless_sampler_now_you_can_create_minimax_h3/)
- **可能影响**: 图像、视频、音频与提示工程工具迭代，可能提升 AI 内容生产和创意软件方向的关注度。
- **示例股票**: 万兴科技（300624.SZ）、昆仑万维（300418.SZ）

---

## 最值得发的 3 个选题

### 选题 1：MiniMax H3 角色设定图工作流：正面/侧面/背面，完全本地运行

**关联新闻**: [MiniMax H3 角色设定图工作流：正面/侧面/背面，完全本地运行](https://www.reddit.com/r/StableDiffusion/comments/1w2dujd/i_turned_that_h3_as_an_image_editor_post_into_a/)

**切入角度**: 一位 Reddit 用户基于 MiniMax H3 构建了一个两阶段 ComfyUI 工作流：输入一张人脸照片和一张服装图片，即可生成正面/侧面/背面角色设定图面板，并可选择添加姿态、道具、表情或背景面板。该工作流在 3090 24GB 显卡上完全本地运行，约 3.5 分钟即可生成完整设定图。 这展示了 MiniMax H3 作为图像编辑器的实用本地应用，将此前分享的“单次六编辑”技术扩展到角色设定图创作。它为角色设计师和游戏美术师提供了一种快速、私密且成本低廉的替代方案，无需依赖云端生成器，尽管在姿态和道具一致性方面仍存在已知局限。 该工作流使用 MiniMax H3 ref2v int8 剪枝版配合 4 步 Turbo LoRA（权重 0.75）、T=1 图像 VAE、er_sde/sgm_uniform 采样器，共 8 步；阶段一约需 100-125 秒，阶段二约需 105 秒。作者指出若干问题：道具会在各面板间重复出现、背面头发变平、躺姿和坐姿不可靠；工作流 JSON 已发布在 GitHub，需要 rgthree 和 toobusy 节点。

**可延展方向**: MiniMax H3 是一个开源的全模态生成模型，能够联合理解文本、图像、视频和音频，并可生成最高 2K 分辨率、15 秒时长、带原生立体声的视频。ComfyUI 是一种基于节点的图像/视频生成工作流构建界面，而角色设定图则是游戏和动画概念设计中使用的多视图参考图。该工作流改编了 H3 的参考到视频（reference-to-video）能力，通过使用 Turbo LoRA 和特定采样设置来生成静态画面，从而将模型转变为本地图像编辑器。

---

### 选题 2：Reddit 用户分享使用 ProPainter 节点本地去除视频水印

**关联新闻**: [Reddit 用户分享使用 ProPainter 节点本地去除视频水印](https://www.reddit.com/r/StableDiffusion/comments/1w2dtfg/remove_watermark_from_videos/)

**切入角度**: 一位 Reddit 用户分享了一个完全本地、易于使用的视频静态水印去除方案，该方案基于 ProPainter 节点和几个常见的自定义节点，并已发布到 Civit AI 平台。 这为云处理或手动去除水印提供了一种实用的替代方案，让视频编辑者拥有免费且保护隐私的工具。同时也展示了 ProPainter 如何在 Stable Diffusion 生态中被用于实际的视频编辑任务。 该方案依赖于 ProPainter Nodes，即 ProPainter 视频修复框架的 ComfyUI 实现，并且专门针对静态水印有效。原始 ProPainter 项目已正式移除水印去除演示以防止不当使用，因此这类社区方案显得尤为值得注意。

**可延展方向**: ProPainter 是一个视频修复框架，结合了循环光流补全、双域传播和掩码引导的稀疏 Transformer，用以填充视频帧中被遮挡或损坏的区域。视频修复是指通过生成合理的内容来替换视频中不需要的物体或水印。Civit AI 是一个流行的 AI 艺术模型与工作流分享平台，包括为 ComfyUI（Stable Diffusion 的基于节点的界面）开发的自定义节点。

---

### 选题 3：MMH3 加速器评测：Sage+Spectrum 质量最佳，速度减半

**关联新闻**: [MMH3 加速器评测：Sage+Spectrum 质量最佳，速度减半](https://www.reddit.com/r/StableDiffusion/comments/1w2z2ua/mmh3_several_accelerators_tested_for_quality/)

**切入角度**: 一位 Reddit 用户总结了 33 分钟的 MMH3 视频生成加速器评测视频，报告称 Sage+Spectrum 组合在半速下仍能提供非常好的画质。帖子还分享了回退技巧：如果画质不佳，可以去掉 Spectrum，仅使用 Sage。 MMH3（MiniMax H3）是重要的开源视频生成模型，加速方法直接影响其实用性。用户主导的画质对比有助于从业者为自己的工作流选择合适的加速器，尤其是在 Stable Diffusion 和视频生成社区。 视频测试了包括 Turbo、EasyCache 0.10 和 Sage+SolAttn 在内的多种加速器，但测试者对这些方案并不满意。评测者主要关注面部、反射和整体布局，并使用了精心设计的测试仪表盘，涵盖文生视频、图生视频和参考生视频片段。

**可延展方向**: MMH3，又称 MiniMax H3，是一个开源多模态视频模型，能统一理解文本、图像、视频和音频输入，支持视频生成、基于参考的创作和编辑。Sage 和 Spectrum 等加速器是无需训练的扩散模型推理加速技术，而 EasyCache 则通过缓存变换向量来加速视频扩散。对于扩散模型，这类加速器通常以牺牲部分画质来换取更低的延迟。

---

1. [QubesOS 披露 QSB-118：复制到 VM 错误报告通道可致任意代码执行](#item-1) ⭐️ 9.0/10
2. [黏菌类比：组织如何平衡集中与分散协调](#item-2) ⭐️ 8.0/10
3. [Zig 为 ArrayList 引入指针稳定性锁](#item-3) ⭐️ 8.0/10
4. [欧盟委员会在 ProtectEU 战略中重启加密后门计划](#item-4) ⭐️ 8.0/10
5. [Storyteller 用强制对齐实现沉浸式阅读自动化](#item-5) ⭐️ 8.0/10
6. [HR Endless Sampler：16GB 显存渲染无限长度 Minimax H3 视频](#item-6) ⭐️ 8.0/10
7. [算法证实 Reddit 用户关于地球最长直线路径的猜测](#item-7) ⭐️ 7.0/10
8. [Omarchy Linux 漏洞：任意用户进程可提权至 root](#item-8) ⭐️ 7.0/10
9. [Breeze TTS 2 开放权重模型登顶 TTS 排行榜](#item-9) ⭐️ 7.0/10
10. [用户自制转换器让 FastH3 LoRA 适配 ComfyUI，速度提升约 3 倍](#item-10) ⭐️ 7.0/10
11. [Haiku 操作系统时隔两年发布 R1/beta6](#item-11) ⭐️ 6.0/10
12. [宜家家具改造：DIY 创意与社区见解](#item-12) ⭐️ 6.0/10
13. [用户尝试用 REFMOD 创建 Linus Tech Tips 视频模组](#item-13) ⭐️ 6.0/10
14. [免费开源 Topaz 替代方案：SeedVR2 + TensorRT 视频修复](#item-14) ⭐️ 6.0/10
15. [优化设置让 MiniMax H3 视频生成时间大幅缩短](#item-15) ⭐️ 6.0/10
16. [MiniMax H3 角色设定图工作流：正面/侧面/背面，完全本地运行](#item-16) ⭐️ 6.0/10
17. [高分辨率噪声掩码实现 ComfyUI 中的潜空间引导运动迁移](#item-17) ⭐️ 6.0/10
18. [通过流体替换测试 MiniMax-H3 的物理知识](#item-18) ⭐️ 6.0/10
19. [Seamless Video Continuation in the new Minimax Seed Hunter v1.2 release! Workflow + Guide](#item-19) ⭐️ 6.0/10
20. [Reddit 用户分享使用 ProPainter 节点本地去除视频水印](#item-20) ⭐️ 6.0/10
21. [MMH3 加速器评测：Sage+Spectrum 质量最佳，速度减半](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [QubesOS 披露 QSB-118：复制到 VM 错误报告通道可致任意代码执行](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 9.0/10

QubesOS 发布了 Qubes 安全公告（QSB）118，披露了 'qvm-copy-to-vm' 工具错误报告函数中的一个严重漏洞，该漏洞允许在 Dom0 中执行任意代码。当从 Dom0 复制文件到虚拟机时，攻击者控制的错误消息会被传递给 system() 调用，从而触发此漏洞。 这一漏洞意义重大，因为 QubesOS 以安全为核心设计，通过虚拟机隔离不同活动；一旦 Dom0 被攻破，整个安全隔离模型就会失效，可能暴露所有虚拟机和数据。该漏洞也表明，即使是精心设计的隔离系统，在错误处理路径上也可能存在被忽视的攻击面。 该漏洞影响 Dom0 版本的 'qvm-copy-to-vm'；VM 到 VM 的变体不受影响，因为其错误报告函数没有使用 system()。由于 QubesOS 的最佳实践不鼓励在 Dom0 中进行日常工作，实际利用需要用户从 Dom0 复制文件，因此攻击面受到限制。

hackernews · vntok · 8月30日 08:51 · [社区讨论](https://news.ycombinator.com/item?id=49496918)

**背景**: QubesOS 采用基于隔离（安全分区）的安全模型，利用 Xen 虚拟机监控器下的轻量级虚拟机（VM）来隔离程序和系统组件。Dom0 是拥有系统完整控制权的管理域，因此 Dom0 一旦被攻破，所有隔离保证都将失效。'qvm-copy-to-vm' 是用于在虚拟机之间安全复制文件的工具，其 Dom0 版本在错误报告路径中错误地将不可信输入传递给了 system() 调用。Qubes 安全公告（QSB）是 Qubes 安全团队用于公开披露漏洞并附带影响分析的官方机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://doc.qubes-os.org/en/latest/developer/system/architecture.html">Architecture — Qubes OS Documentation</a></li>
<li><a href="https://doc.qubes-os.org/en/latest/developer/system/security-design-goals.html">Security design goals — Qubes OS Documentation</a></li>
<li><a href="https://www.qubes-os.org/news/2026/08/29/qsb-118/">QSB-118: Dom0 arbitrary code execution in qvm-copy-to-vm error reporting | Qubes OS</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体上对这一漏洞表示严肃对待，有人指出错误报告后门通道是常被忽视的攻击向量。另一些人则指出，实际风险有限，因为利用需要从 Dom0 复制文件，而这并不被推荐，且 VM 到 VM 的变体不受影响。部分评论还延伸到关于 QubesOS 领导层变动以及 CPU 架构安全难度的更广泛讨论。

**标签**: `#security`, `#qubesos`, `#vulnerability`, `#arbitrary-code-execution`

---

<a id="item-2"></a>
## [黏菌类比：组织如何平衡集中与分散协调](https://komoroske.com/slime-mold/) ⭐️ 8.0/10

Komoroske 发表了一篇文章，用黏菌的类比来探讨组织设计，分析团队如何平衡集中式与分散式协调。该文为工程团队架构和决策流程提供了一个分析框架。 这篇文章为正在应对协作开销问题的工程管理者和团队负责人提供了新的视角。借鉴生物体中高效网络形成的原理，组织可以设计出更具适应性的结构。 文章借鉴了黏菌生物学，其中单细胞自组织成管状网络，在效率与韧性之间取得平衡。社区评论将这一理念与‘松散耦合、高度一致’的团队联系起来，并指出了实际落地的困难。

hackernews · rzk · 8月30日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49499891)

**背景**: 黏菌是一种既能以单细胞形式存在、又能聚合成多细胞网络的生物，它们通过‘stigmergy’（间接协调机制）进行协作——行动在环境中留下痕迹，进而刺激后续行动。去中心化的组织结构将决策权从顶层分散出去，例如 Spotify 的 squad 模式。这个类比有助于解释团队中集中控制与局部自主之间的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Slime_mold">Slime mold - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stigmergy">Stigmergy - Wikipedia</a></li>
<li><a href="https://www.aihr.com/hr-glossary/decentralized-organizational-structure/">What Is a Decentralized Organizational Structure? | HR Glossary</a></li>

</ul>
</details>

**社区讨论**: 评论者推荐了《The Art of Action》等相关书籍，并指出海军陆战队在保持顶层任务的同时将决策权下放。也有人质疑决策质量是否取决于员工素质，还有人承认这个类比很有道理，但在现实组织中落地仍然困难。

**标签**: `#organizational-design`, `#coordination`, `#team-structure`, `#management`, `#systems-thinking`

---

<a id="item-3"></a>
## [Zig 为 ArrayList 引入指针稳定性锁](https://ziglang.org/devlog/2026/#2026-08-27) ⭐️ 8.0/10

Zig 在 2026 年 8 月 27 日的开发日志中宣布为 `std.ArrayList` 增加指针稳定性特性，通过显式的“锁定”API 固定底层存储，使已有的指针和切片保持有效。该功能源于此前跟踪的 Issue #19326 和 #19327（分别针对 ArrayList 与 MultiArrayList）。 这很重要，因为动态数组扩容时通常会令指针和切片失效，而这正是隐蔽 bug 的常见来源；Zig 的显式锁定 API 为开发者提供了一种可通过调试检查来避免意外失效的方式。它同时还引发了关于在 Zig 中究竟应默认使用稳定指针、索引、还是其他数据结构的讨论。 根据社区讨论，该安全检查只在 Debug 和 ReleaseSafe 模式下生效；在 ReleaseFast 下不会强制检查，这可能削弱该特性对性能敏感代码的保障。此外，API 需要程序员手动获得锁，并在使用指针的代码区域中保持锁存活，而不是由编译器自动推断或强制管理。

hackernews · tosh · 8月30日 14:41 · [社区讨论](https://news.ycombinator.com/item?id=49499095)

**背景**: `ArrayList` 是 Zig 标准库中的动态数组类型，类似于 C++ 的 `std::vector`；扩容时重新分配内存会使引用其内部缓冲区的指针、切片和迭代器失效。Zig 的提案增加了显式的指针稳定性锁，让程序员可以固定缓冲区，并选择启用运行时或调试安全检查。同一想法也由 ziglang/zig#19327 跟踪，计划用于 `MultiArrayList`。C++ 开发者常常面临 `vector` 迭代器失效问题，而 Rust 则通过编译期的借用检查来保证指针生命周期安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ziglang/zig/issues/19326">introduce pointer stability safety locks to array lists · Issue #19326 · ziglang/zig</a></li>
<li><a href="https://github.com/ziglang/zig/issues/19327">introduce pointer stability safety locks to MultiArrayList · Issue #19327 · ziglang/zig</a></li>
<li><a href="https://learningzig.org/lessons/21-data-structures">Data Structures · Learn Zig | LearningZig.org</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有评论者（如 amluto）认为这种锁需要程序员手动记得使用，因而弱于 Rust 在编译期的强制保障；portly 则认为这是与 Zig 哲学一致的又一道显式“绊线”。_bohm 质疑，需要元素稳定指针时 ArrayList 是否本身就是错误的数据结构，是否应改用索引或无环链表；afdbcreid 指出 ReleaseFast 下检查会被移除；stub_out 则称赞 Zig 解决了 C++ 开发者长期面对的痛点。

**标签**: `#Zig`, `#language design`, `#memory safety`, `#data structures`, `#programming`

---

<a id="item-4"></a>
## [欧盟委员会在 ProtectEU 战略中重启加密后门计划](https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement) ⭐️ 8.0/10

2025 年 4 月 1 日，欧盟委员会公布了其 ProtectEU 内部安全战略，重新推动强制要求加密后门以协助执法。该战略旨在提升安全能力，但批评者认为它损害了数字权利。 这一政策推动可能从根本上削弱数百万欧盟公民的加密保护，影响整个欧盟的隐私与安全。它也反映出政府要求获取加密通信例外权限的更大趋势，将对全球科技公司和标准产生深远影响。 战略新闻稿中“为执法部门提供更有效工具”的表述被解读为强制要求后门，但一些评论者指出欧盟文本本身可能没那么明确。数字权利组织 EDRi 称该战略是“向数字反乌托邦未来又迈进了一步”。

hackernews · nickslaughter02 · 8月30日 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49499394)

**背景**: ProtectEU 是欧盟委员会于 2025 年 4 月 1 日提出的内部安全战略，旨在帮助欧盟成员国保护社会免受恐怖分子、犯罪和网络威胁。加密后门是安全系统中故意留下的漏洞，使执法部门能够访问加密数据，但也会带来被犯罪分子和恶意行为者利用的风险。关于后门的争论由来已久，需要在安全需求与基本隐私权和网络安全之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://home-affairs.ec.europa.eu/news/commission-presents-protecteu-internal-security-strategy-2025-04-01_en">Commission presents ProtectEU Internal Security Strategy</a></li>
<li><a href="https://edri.org/our-work/protecteu-security-strategy-a-step-further-towards-a-digital-dystopian-future/">‘ ProtectEU ’ security strategy - European Digital Rights (EDRi)</a></li>
<li><a href="https://epthinktank.eu/2025/08/04/the-new-european-internal-security-strategy-protecteu/">The new European internal security strategy : ProtectEU | Epthinktank</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上持批评态度，认为欧盟委员会权力过大，未来领导层可能滥用后门。另一些人强调在 AI 安全担忧背景下削弱加密的危险，并指出私密数据被武器化的历史先例；也有部分人要求查看欧盟实际文本以核实后门的说法。

**标签**: `#encryption`, `#privacy`, `#EU policy`, `#security`, `#backdoors`

---

<a id="item-5"></a>
## [Storyteller 用强制对齐实现沉浸式阅读自动化](https://smoores.dev/post/automating_immersive_reading/) ⭐️ 8.0/10

开发者 smoores 重新实现了 Storyteller（一个开源、自托管的朗读平台）中的强制对齐算法，使其能自动将有声书朗读与文本高亮同步。新算法不仅支持句子级同步，还增加了单词级高亮。 它的重要性在于，高质量的开源沉浸式阅读工具可以媲美亚马逊 WhisperSync 等商业服务，让用户自主掌控自己的无 DRM 图书。精确对齐能改善无障碍体验，也支持边听边读、以及从有声书切回文本时继续阅读等场景。 Storyteller 由可自托管的服务器和移动应用组成，用于对齐电子书与有声书；作者提到，理解 CTC（Connectionist Temporal Classification）输出是这套重量级对齐方法的一部分。这次重写花了大约一周的专注时间，现在能为朗读图书提供逐词高亮。

hackernews · smoores · 8月30日 11:46 · [社区讨论](https://news.ycombinator.com/item?id=49497854)

**背景**: 强制对齐（forced alignment）是一种语音处理技术，利用语音识别模型自动确定文稿中每个单词或句子在音频录音中的起止位置，而不是人工标注。Storyteller 是一个开源项目，常被形容为亚马逊 WhisperSync 的自托管替代品，让用户将自己拥有的无 DRM 电子书和有声书结合起来，实现同步阅读与收听。该平台由服务器和移动应用两个核心组件构成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://storyteller-platform.dev/docs/welcome/">Welcome to Storyteller | Storyteller - storyteller-platform.dev</a></li>
<li><a href="https://storyteller-platform.dev/">Storyteller Docs | Storyteller</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11449383/">The Mason-Alberta Phonetic Segmenter: a forced alignment system...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍给予好评，mobeets 称这项工作“令人印象深刻”，并询问 Storyteller 是否适合记录收听位置以便稍后继续阅读。其他人则讨论了实际应用差异：justinhunt 将其与匹配学生口语朗读文本的做法相比较，cainxinth 描述了类似的校对工作流，而 SamBam 质疑对于阅读障碍者来说，单词级高亮是否真的比整句高亮更好。

**标签**: `#forced-alignment`, `#audiobooks`, `#speech-recognition`, `#open-source`, `#reading`

---

<a id="item-6"></a>
## [HR Endless Sampler：16GB 显存渲染无限长度 Minimax H3 视频](https://www.reddit.com/r/StableDiffusion/comments/1w25d7g/hr_endless_sampler_now_you_can_create_minimax_h3/) ⭐️ 8.0/10

一款名为 HR Endless Sampler 的新 ComfyUI 节点可将生成过程拆分成小块，从而仅用 16GB 显存渲染任意长度的 Minimax H3 视频（包括 1080p）。它使用 Gemma 4 12B QAT 来协调各块之间的提示词，目前仍处于 alpha 阶段。 这一创新解决了以往消费级 GPU 在 AI 视频生成上的显存瓶颈，只能生成长度很短的片段。它能让更多创作者和开发者使用长格式 AI 视频生成功能，具有重要的实用价值。 该节点替换了 SamplerCustomAdvanced 节点，并将上一块生成的 latent 直接传给下一块，无需经过 VAE 解码/编码，从而避免细节损失。它还包含预览、保存和加载节点，可保存每个块的提示词以及 EXR 浮点颜色帧。

reddit · r/StableDiffusion · /u/rhradec · 8月30日 02:36

**背景**: Minimax H3 是一个开源的 omni-modal 生成模型，能以最高 2K 分辨率和 15 秒时长生成带原生立体声音频的视频。ComfyUI 是一个基于节点的生成式 AI 应用，用户可以通过节点构建图像、视频、音频等复杂工作流。采用量化感知训练（QAT）的 Gemma 4 可以显著降低在本地消费级 GPU 上运行大语言模型所需的内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MiniMax-AI/MiniMax-H3">GitHub - MiniMax-AI/MiniMax-H3 · GitHub</a></li>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/">Gemma 4 with quantization-aware training - The Keyword</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#AI video generation`, `#VRAM optimization`, `#Minimax H3`, `#Generative AI`

---

<a id="item-7"></a>
## [算法证实 Reddit 用户关于地球最长直线路径的猜测](https://arxiv.org/abs/1804.07389) ⭐️ 7.0/10

2018 年，研究人员 Rohan Chabukswar 和 Kushal Mukherjee 发表论文，用优化算法计算了地球表面水上和陆上的最长直线路径，证实了 Reddit 用户关于水路线的猜测。 这项研究将非正式的互联网说法转化为经过验证的计算结果，展示了算法和公开海拔数据如何解决有趣但又非平凡的地理空间问题。它还提供了一种可复用的算法，可在地球上任意位置寻找类似的路径。 该算法在普通笔记本电脑上分别用约 10 分钟和约 45 分钟找到了水上路径和陆上路径。研究人员将低于海平面的区域视为水域，有评论者指出这可能导致死海附近的合法陆地路径被漏掉。

hackernews · joebig · 8月30日 08:23 · [社区讨论](https://news.ycombinator.com/item?id=49496782)

**背景**: 在球面上，两点之间的最短路径是大圆的一段弧，地球上的"直线"对应大圆航线。该论文使用海拔和海底地形数据，搜索地球上所有可能的大圆路径，以确定哪些路段连续处于水域或陆域之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2018/04/30/143150/computer-scientists-have-found-the-longest-straight-line-you-could-sail-without-hitting/">Computer scientists have found the longest straight line you could...</a></li>
<li><a href="https://www.weforum.org/stories/emerging-technologies/these-are-the-world-s-longest-straight-lines/">How scientists are using algorithms to calculate the world’s longest ...</a></li>
<li><a href="https://nerdist.com/article/longest-line-sail-across-earth/">How Long Can You Sail a Straight Line Across the Earth ? - Nerdist</a></li>

</ul>
</details>

**社区讨论**: 评论者很喜欢这篇论文的叙述，认为一个随机的 Reddit 帖子被严谨算法所证实，并分享了可视化内容和相关项目。有评论者指出一个潜在缺陷：从塞内加尔到中国的更长陆地路径可能被遗漏，因为算法将死海等低于海平面的地形视为水域。

**标签**: `#geography`, `#algorithms`, `#mathematics`, `#geospatial`, `#data-analysis`

---

<a id="item-8"></a>
## [Omarchy Linux 漏洞：任意用户进程可提权至 root](https://0xcc.io/posts/omarchy-root-creds/) ⭐️ 7.0/10

Omarchy Linux 被曝出一处新漏洞：任何非特权用户进程都能提权为 root。该公告发布在 0xcc.io，并因该发行版被热炒为“vibecoded”而受到广泛关注。 这一漏洞意义重大，因为 Omarchy 是 DHH 创建的基于 Arch 的发行版，并受到科技网红的广泛推广；如此简单的提权漏洞动摇了其可信度，也引发了对炒作驱动型发行版安全性的更大质疑。因推荐而安装该系统的用户如今可能面临严重的本地安全风险。 该漏洞在 0xcc.io 的文章《Omarchy: Any User Process Can Escalate to Root》中被披露。Omarchy 是 DHH 推出的“意见化”Arch Linux 发行版，预装了一整套精选软件和配置文件，近期被 NetworkChuck、Primeagen 等网红博主广泛宣传。

hackernews · trap0xcc · 8月30日 15:59 · [社区讨论](https://news.ycombinator.com/item?id=49499854)

**背景**: Omarchy 是 Ruby on Rails 作者 DHH（David Heinemeier Hansson）发布的 Linux 发行版，本质上是在 Arch Linux 之上叠加定制软件与配置。该发行版近期在 YouTube 和社交媒体上被大量推广，形成一股热潮。“Vibe coding”是 Andrej Karpathy 提出的概念，指直接以自然语言让 AI 生成代码，而开发者不深究、不完整审查输出结果的开发方式。在 Linux 中，root 指拥有全部系统权限的超级用户，因此任何用户进程都能从普通用户提权到 root 的漏洞属于典型的高危提权漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://omarchy.org/">Omarchy — Beautiful, Fun & Opinionated Linux by DHH</a></li>
<li><a href="https://github.com/basecamp/omarchy">GitHub - basecamp/ omarchy : Beautiful, Modern & Opinionated Linux</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 不少评论者将 Omarchy 斥为“vibecoded”产物，并翻出此前 USB 描述符被直接送入 shell 的旧账。也有人认为这并非 Omarchy 独有，指出 sudo 本质上是“安全剧场”，而 Linux 缺少真正的桌面沙箱机制；还有用户建议直接用原版 Arch 或 rootless Podman，而不应追捧被炒作起来的发行版。

**标签**: `#security`, `#linux`, `#privilege-escalation`, `#vulnerability`, `#distro`

---

<a id="item-9"></a>
## [Breeze TTS 2 开放权重模型登顶 TTS 排行榜](https://www.reddit.com/r/StableDiffusion/comments/1w2kt0c/breeze_tts/) ⭐️ 7.0/10

Breeze TTS 2 是一个新发布的开放权重文本转语音（TTS）模型，专为实时交互而设计。它在 Artificial Analysis TTS 排行榜的开放权重模型中排名第一，并且表现优于前沿专有系统。 这一里程碑表明开放权重语音模型可以击败封闭的商业产品，可能重塑 TTS 市场。开发者可以获得高质量、实时的模型，并自己托管和定制。 该模型支持开放式自然语言指令跟随，可用于无参考语音设计和有参考引导的语音方向。它还具备超低延迟流式传输，支持响应迅速、富有表现力的交互。

reddit · r/StableDiffusion · /u/CryptoBeth96 · 8月30日 15:38

**背景**: 开放权重模型会公布其学习到的神经网络参数，任何人都可以下载、检查并在本地运行该系统。Artificial Analysis TTS 排行榜通过盲测人类评估对语音模型进行排名，听众并排比较样本并投票选出更自然的语音。无参考语音设计允许用户用自然语言描述一种声音，而无需提供示例录音。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/lets-code-future/open-weight-ai-models-what-they-are-and-why-openais-next-move-matters-f86fe481973a">Open - Weight AI Models : What They Are, and Why... | Medium</a></li>
<li><a href="https://artificialanalysis.ai/text-to-speech/arena">Speech Arena - Top AI Speech Models | Artificial Analysis</a></li>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/Qwen3- TTS : Qwen3- TTS is an open-source series...</a></li>

</ul>
</details>

**标签**: `#TTS`, `#AI`, `#open-source`, `#speech`, `#ML`

---

<a id="item-10"></a>
## [用户自制转换器让 FastH3 LoRA 适配 ComfyUI，速度提升约 3 倍](https://www.reddit.com/r/StableDiffusion/comments/1w2ssyd/fastvideos_new_4step_h3_lora_doesnt_work_in/) ⭐️ 7.0/10

一位 Reddit 用户发布了 NikoDemon80/ComfyUI-FastH3-Lora-Converter，这是一个将 FastVideo 为 MiniMax H3 推出的 FastH3 4 步 LoRA 转换为 ComfyUI 兼容 .safetensors 文件的脚本。使用该脚本后，ComfyUI 只需 6 步即可生成视频，而不是原来的 20 步，在 RTX 3070 Ti 上将渲染时间缩短到约三分之一。 这填补了一个兼容性缺口——FastVideo 官方的 FastH3 LoRA 在 ComfyUI 中会被静默忽略；现在本地用户无需自定义节点即可获得显著加速。它让 MiniMax H3 这样的开源视频模型在日常流程中更实用，也展示了社区工具能快速解决生态碎片化问题。 不兼容的原因是 ComfyUI 使用的重打包 MiniMax H3 模型具有不同的层名，且注意力层被合并，导致原版 LoRA 的权重完全没有生效。该转换器会丢弃一组只能部分加载的层；由于 ComfyUI 以不兼容的格式存储步进信息，因此必须使用 6 步而不是 4 步。基准测试显示，544x960、124 帧的片段在 LoRA 下渲染耗时 2 分 45 秒，而原版需 7 分钟。

reddit · r/StableDiffusion · /u/Sad_Berry_4621 · 8月30日 20:41

**背景**: LoRA 是一种参数高效的微调技术，通过向现有模型添加小型适配器权重来适配特定任务，而无需重新训练完整模型。ComfyUI 是一个开源的节点式生成式 AI 界面，广泛用于本地 Stable Diffusion 和日益增多的视频模型。FastVideo 最近开源了 FastH3，这是一个基于 MiniMax H3 后训练的速度 LoRA，旨在将去噪步数从 20 步减少到 4 步；该转换器使其适用于 ComfyUI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI - Wikipedia</a></li>
<li><a href="https://haoailab.com/blogs/fasth3-preview/">FastVideo FastH3 V1: Open-Weight 4-Step Sparse Distilled ...</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#LoRA`, `#FastVideo`, `#MiniMax`, `#Video Generation`

---

<a id="item-11"></a>
## [Haiku 操作系统时隔两年发布 R1/beta6](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6) ⭐️ 6.0/10

Haiku R1/beta6 于 2026 年 8 月 26 日正式发布，恰逢 Haiku 诞生 25 周年后约一周。这是 Haiku 两年来首个官方版本，包含了近两年的开发成果，重点改进了功能和整体稳定性。 此次发布对 Haiku 这个小众操作系统社区而言是一个重要里程碑，表明这一开源的 BeOS 继承者仍在积极开发中。虽然对该受众之外的影响有限，但它突显了在主流平台日益服务化、强调遥测的时代，轻量且注重隐私的操作系统仍有吸引力。 这个 beta 版本包含了自 beta5 以来的大量进展，并提供了详细的发布说明供用户参考。不过，社区已报告在部分硬件（如 ThinkPad X1 Yoga 第三代）上出现启动回归问题，但可以通过安全模式等变通方法解决。

hackernews · metrofun · 8月30日 16:01 · [社区讨论](https://news.ycombinator.com/item?id=49499867)

**背景**: Haiku 原名 OpenBeOS，是一个免费开源操作系统，延续了 BeOS 的遗产，在大部分组件重新实现的同时追求二进制兼容性。该项目始于 2001 年，目前仍处于 beta 阶段，强调速度、简洁和效率，面向个人计算。本次发布恰逢项目 25 周年之后，凸显了社区驱动开发已走过四分之一世纪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6">Haiku R1/beta6 has been released! | Haiku Project</a></li>
<li><a href="https://www.haiku-os.org/get-haiku/r1beta6/release-notes/">R1/beta6 – Release Notes | Haiku Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/Haiku_(operating_system)">Haiku (operating system)</a></li>

</ul>
</details>

**社区讨论**: 社区反应喜忧参半：一些用户称赞 Haiku 的视觉设计及其在音乐制作等小众工作流中的潜力，而另一些用户则报告在特定笔记本上出现启动崩溃的回归问题。有用户指出 Linux 现在同样流畅且自带容器支持，可能削弱 Haiku 的轻量优势；还有用户认为无障碍访问是采用 Haiku 的主要障碍。

**标签**: `#Haiku`, `#Operating System`, `#Open Source`, `#Beta Release`

---

<a id="item-12"></a>
## [宜家家具改造：DIY 创意与社区见解](https://greenlightning.eu/diy/hacking-ikea-furniture/) ⭐️ 6.0/10

greenlightning.eu 上的一篇关于改造宜家家具的博客文章引发了热烈讨论，获得了 264 分和 177 条评论。虽然文章本身没有可见内容，但社区讨论涉及 CAD 图纸、宜家的设计影响力以及实用的定制案例。 宜家改造展示了价格亲民的大规模量产家具如何被改造成个性化作品，体现了更广泛的 DIY 与升级再造趋势。社区的热烈反响凸显了宜家对设计品味的深远文化影响，以及共享 CAD 资源对爱好者的日益重要。 社区成员分享了实用资源：vanrohan 分享了一个改造比利书柜以隐藏管道的案例，并指出常见宜家产品很容易找到 CAD 图纸；Beijinger 提到了像 ikeahackers.net 这样的平台。不过，ssharp 认为，与使用原材料直接制作相比，改造宜家产品在成本、精力和质量上的权衡可能并不总是划算。

hackernews · greenlightning · 8月30日 11:39 · [社区讨论](https://news.ycombinator.com/item?id=49497810)

**背景**: 宜家改造是指对宜家产品进行修改或重新利用以制作定制家具的做法，这一趋势在疫情期间显著增长。如今，专门的社区和企业提供定制桌腿、罩子、把手和柜门等宜家配件。CAD（计算机辅助设计）软件让设计师能够创建详细的 2D 图纸或 3D 模型，爱好者们用它来规划和分享自己的家具改造方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ikeahackers.net/">IKEA Hacks + DIY Ideas - IKEA Hackers</a></li>
<li><a href="https://thehustle.co/the-thriving-business-of-ikea-hacking">The thriving business of ‘ Ikea hacking ’</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer-aided_design">Computer-aided design - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 总体上，评论对宜家改造持正面态度，bborud 称赞宜家让大众也能接触现代美学，vanrohan 则欣赏平价家具易于定制的特点。然而，ssharp 质疑成本、精力和质量的权衡是否值得，class3shock 则表达了对宜家家具质量的不满。讨论中还出现了像 ikeahackers.net 这样的实用资源。

**标签**: `#DIY`, `#IKEA`, `#furniture`, `#CAD`, `#hacking`

---

<a id="item-13"></a>
## [用户尝试用 REFMOD 创建 Linus Tech Tips 视频模组](https://www.reddit.com/r/StableDiffusion/comments/1w2tg3f/linus_tech_tips_just_experimenting_with_refmod_by/) ⭐️ 6.0/10

Reddit 用户（u/chaindrop）使用 REFMOD 从旧的 SDXL 时代数据集中提取了一个 Linus Tech Tips 风格模组，生成一个无需参考图片即可使用的.safetensor 文件。最终 AI 生成视频由 MiniMax H3 创建，提示词描述了一个男子吃 NVIDIA GPU 的吃播视频，带有 ASMR 声音。 这个实验表明，可以为 AI 视频生成提取可复用的身份/风格模组，未来可能无需参考图片即可生成内容。它展示了 REFMOD 的早期实际应用，可能降低创作者的使用门槛，并推动个性化 AI 视频工作流的发展。 该模组是使用 REFMOD 仓库中的 ComfyUI 节点构建的，作者表示目前仍在实验阶段。模型权重以.safetensor 文件格式安全存储，应用模组后，仅通过文本提示词即可使用 MiniMax H3 生成视频。

reddit · r/StableDiffusion · /u/chaindrop · 8月30日 21:06

**背景**: REFMOD 是一种从数据集中提取可复用“模组”的新方法，以 ComfyUI 插件（ComfyUI-MiniMaxH3Mod 仓库）的形式实现，针对 MiniMax H3 视频模型。Safetensors 是一种安全的机器学习张量存储格式，不会允许代码执行，广泛用于 Stable Diffusion 工作流。MiniMax H3 是新一代多模态 AI 视频生成平台，支持从文本、图片和参考材料创建视频。该实验将上述要素结合起来，从依赖参考图片的生成方式转向基于模组的生成方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Luisacaotica/ComfyUI-MiniMaxH3Mod">GitHub - Luisacaotica/ComfyUI-MiniMaxH3 Mod : Under...</a></li>
<li><a href="https://design.minimax.io/tools/ai-video-generator">AI Video Generator for Text & Image to Video - MiniMax H3 ...</a></li>
<li><a href="https://docs.fileformat.com/data/safetensors/">SAFETENSORS - Stable Diffusion Model - What is SAFETENSORS ...</a></li>

</ul>
</details>

**标签**: `#StableDiffusion`, `#REFMOD`, `#AI video generation`, `#model fine-tuning`, `#experimentation`

---

<a id="item-14"></a>
## [免费开源 Topaz 替代方案：SeedVR2 + TensorRT 视频修复](https://www.reddit.com/r/StableDiffusion/comments/1w2ri4b/free_open_source_topaz_alternative/) ⭐️ 6.0/10

一款新的免费开源 Windows 工具 VRGDG SeedVR2 TensorRT Studio 将 SeedVR2 视频修复与 TensorRT 加速的 VAE 解码相结合。它提供 GPU 加速的本地放大与修复功能，并支持预览、可断点续跑的渲染以及实用的输出控制。 这让普通用户无需订阅 Topaz，也能用上研究级的视频修复模型。它也展示了 TensorRT 加速如何让高质量 2K 视频增强在消费级 RTX GPU 上变得实用。 在 NVIDIA RTX 5090 上，使用最大的 7B Sharp FP16 模型，一段 8 秒的低分辨率视频大约只需 8 分钟即可放大增强到 2K。该工具仍处于测试阶段，支持中断后可续跑的检查点，并且完全在本地离线运行。

reddit · r/StableDiffusion · /u/Cheap_Credit_3957 · 8月30日 19:52

**背景**: SeedVR2 是字节跳动推出的一步式扩散 Transformer 模型，用于通用视频修复，可以在单步中还原任意分辨率的视频。TensorRT 是 NVIDIA 的推理优化库，可在 NVIDIA GPU 上加速深度学习任务，包括 VAE 解码。VAE（变分自编码器）将视频帧压缩成较小的潜在表示进行处理，再把结果解码回像素。像 Topaz 这样的商业工具也提供类似的修复和放大功能，但属于付费闭源软件，因此这款开源替代方案格外引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ByteDance-Seed/SeedVR">GitHub - ByteDance-Seed/SeedVR: Repo for SeedVR2 (ICLR2026 ...</a></li>
<li><a href="https://arxiv.org/html/2506.05301v2">SeedVR2: One-Step Video Restoration via - arXiv.org</a></li>
<li><a href="https://lilys.ai/en/notes/nvidia-20251101/getting-started-nvidia-torch-tensorrt">Getting Started with NVIDIA Torch- TensorRT</a></li>

</ul>
</details>

**标签**: `#video restoration`, `#upscaling`, `#SeedVR2`, `#TensorRT`, `#open source`

---

<a id="item-15"></a>
## [优化设置让 MiniMax H3 视频生成时间大幅缩短](https://www.reddit.com/r/StableDiffusion/comments/1w2xr12/h3_default_template_vs_larrys_turbo_with/) ⭐️ 6.0/10

一位 Reddit 用户将 MiniMax H3 在 ComfyUI 中的默认工作流（20 步、res_multistep、simple）与优化设置（8 步、er_sde、sgm_unified、Comfy Kitchen Attention 和 Larry 的 Turbo LoRA）进行了对比。优化后的工作流将一段 0.2MP/8 秒片段的生成时间从 2 分 16 秒缩短到 45 秒，另一段则从 6 分 3 秒缩短到 1 分 51 秒。 这表明使用现成的工具即可显著加快 H3 视频生成速度，ComfyUI 用户进行迭代式剪辑和原型制作会因此快得多。同时也体现了 Turbo LoRA 和高级采样器在减少高分辨率视频计算时间方面的实用价值。 优化设置具体包括：将步数从 20 步减为 8 步，使用 er_sde 采样器、sgm_unified 噪声调度、Comfy Kitchen Attention，以及 Larryvrh/ComfyUI-MiniMax-H3-Turbo 提供的 Turbo LoRA。对比片段均为 0.2MP 分辨率、8 秒时长；帖子中没有透露测试硬件和具体提示词。

reddit · r/StableDiffusion · /u/desktop4070 · 8月31日 00:08

**背景**: MiniMax H3 是上海 AI 公司 MiniMax 推出的通用多模态生成模型，可处理文本、图像、视频和音频任务。ComfyUI 是一种开源、基于节点的生成式 AI 工作流界面，常用于 Stable Diffusion 等模型。LoRA（低秩适配）是一种可训练的模块，用来微调基础模型；Turbo LoRA 经过蒸馏，能在更少的采样步数下生成高质量结果，从而减少生成时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://github.com/Comfy-Org/ComfyUI">GitHub - Comfy-Org/ComfyUI: The most powerful and modular ...</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/ MiniMax - H 3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#MiniMax H3`, `#video generation`, `#optimization`, `#Turbo LoRA`

---

<a id="item-16"></a>
## [MiniMax H3 角色设定图工作流：正面/侧面/背面，完全本地运行](https://www.reddit.com/r/StableDiffusion/comments/1w2dujd/i_turned_that_h3_as_an_image_editor_post_into_a/) ⭐️ 6.0/10

一位 Reddit 用户基于 MiniMax H3 构建了一个两阶段 ComfyUI 工作流：输入一张人脸照片和一张服装图片，即可生成正面/侧面/背面角色设定图面板，并可选择添加姿态、道具、表情或背景面板。该工作流在 3090 24GB 显卡上完全本地运行，约 3.5 分钟即可生成完整设定图。 这展示了 MiniMax H3 作为图像编辑器的实用本地应用，将此前分享的“单次六编辑”技术扩展到角色设定图创作。它为角色设计师和游戏美术师提供了一种快速、私密且成本低廉的替代方案，无需依赖云端生成器，尽管在姿态和道具一致性方面仍存在已知局限。 该工作流使用 MiniMax H3 ref2v int8 剪枝版配合 4 步 Turbo LoRA（权重 0.75）、T=1 图像 VAE、er_sde/sgm_uniform 采样器，共 8 步；阶段一约需 100-125 秒，阶段二约需 105 秒。作者指出若干问题：道具会在各面板间重复出现、背面头发变平、躺姿和坐姿不可靠；工作流 JSON 已发布在 GitHub，需要 rgthree 和 toobusy 节点。

reddit · r/StableDiffusion · /u/inazma44 · 8月30日 10:21

**背景**: MiniMax H3 是一个开源的全模态生成模型，能够联合理解文本、图像、视频和音频，并可生成最高 2K 分辨率、15 秒时长、带原生立体声的视频。ComfyUI 是一种基于节点的图像/视频生成工作流构建界面，而角色设定图则是游戏和动画概念设计中使用的多视图参考图。该工作流改编了 H3 的参考到视频（reference-to-video）能力，通过使用 Turbo LoRA 和特定采样设置来生成静态画面，从而将模型转变为本地图像编辑器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://github.com/MiniMax-AI/MiniMax-H3">GitHub - MiniMax-AI/MiniMax-H3 · GitHub</a></li>
<li><a href="https://comfyui-wiki.com/en/news/2026-08-13-minimax-h3-turbo-ref2v">MiniMax H 3 Turbo Ref 2 V v0.1: 4-Step... | ComfyUI Wiki</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#MiniMax H3`, `#character sheet`, `#image editing`, `#local generation`

---

<a id="item-17"></a>
## [高分辨率噪声掩码实现 ComfyUI 中的潜空间引导运动迁移](https://www.reddit.com/r/StableDiffusion/comments/1w2s3ck/high_resolution_noise_masks_for_latent_guided/) ⭐️ 6.0/10

ComfyUI-H3-Motion-Context-MultiRef 仓库的最新更新新增了一个节点和工作流，用于潜空间引导的运动迁移，通过自定义的精细噪声掩码在目标潜空间中保留源视频的微弱痕迹。v2v 节点还惰性 monkeypatch 了 ComfyUI 核心行为，将噪声掩码等级从 256 提升到 4096，并改用 FP32 精度，避免 0.9995 这样的细粒度值被舍入丢失。 这很重要，因为精确的运动迁移一直是视频生成中的长期难题，而更精细的噪声掩码粒度能让潜空间保留原本会丢失的微弱引导信号。它为 ComfyUI 用户提供了一种实用的新技巧，也可能推动核心项目采用更高粒度的掩码。 monkeypatch 是有条件的：节点会检测 ComfyUI 环境，只在当前粒度不够时才应用补丁。此次更新还新增了 AV 扩展、音乐视频生成和 de-rope 扩展的工作流，以及用于潜空间掩码和自定义关键帧的工具节点。

reddit · r/StableDiffusion · /u/stonyleinchen · 8月30日 20:14

**背景**: 潜空间扩散模型通过将源内容编码到压缩的潜空间，然后逐步去噪来生成视频；噪声掩码控制哪些潜空间区域被去噪以及去噪的强度。在运动迁移中，源视频的运动被注入目标潜空间，但如果噪声掩码粒度太粗或精度太低，微弱的引导痕迹可能会丢失。ComfyUI 是一个流行的基于节点的界面，用于 Stable Diffusion 及相关生成工作流，像这样的自定义节点为高级用户扩展了其功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ditflow.github.io/">Video Motion Transfer with Diffusion Transformers</a></li>
<li><a href="https://docs.comfy.org/interface/nodes-2">Nodes 2.0 - ComfyUI</a></li>
<li><a href="https://arxiv.org/html/2502.04669v1">A Comprehensive Review on Noise Control of Diffusion Model</a></li>

</ul>
</details>

**标签**: `#stable-diffusion`, `#comfyui`, `#motion-transfer`, `#video-generation`, `#latent-diffusion`

---

<a id="item-18"></a>
## [通过流体替换测试 MiniMax-H3 的物理知识](https://www.reddit.com/r/StableDiffusion/comments/1w2fuky/testing_minimaxh3_physics_knowledge/) ⭐️ 6.0/10

Reddit 用户/u/jaryP 使用 H3-Ref 模型，将 Pexels 视频中的水替换为沙子、岩石和可燃蜂蜜，以测试 MiniMax-H3 的物理理解能力。该实验采用 day-zero 参考工作流和 int8 convrot 模型，结果显示岩石翻滚和蜂蜜混合较为逼真，但火焰效果不令人信服。 这一社区实验揭示了 AI 视频模型在多大程度上内化了物理常识，这是实现逼真生成的关键挑战。此类发现有助于开发者找出弱点（例如火焰物理），并在未来版本中优先改进。 用户指出未使用外部参考，并观察到岩石滚过杯子、蜂蜜在壶上留下痕迹等具体交互。工作流采用 9:16 宽高比、MP 0.6，提示词通过 Pastebin 分享；修正比例的视频发布在 Streamable 上。

reddit · r/StableDiffusion · /u/jaryP · 8月30日 12:07

**背景**: MiniMax-H3 是一个开放权重的多模态视频模型，可生成最长 15 秒的 2K 视频并带有原生立体声音频，同时支持多模态参考以完成编辑任务。H3-Ref 变体通过用户提供的输入进行条件生成，实现基于参考的视频编辑——此处即用水以外的新流体替换水。'day-zero ref 工作流'指社区开发的 H3-Ref 使用流程，常搭配 int8 量化版'convrot' VAE 以降低显存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fal.ai/minimax-h3">MiniMax H 3 - Open-Weights General -Purpose Multimodal Video Model</a></li>
<li><a href="https://morphic.com/resources/how-to/minimax-h3-guide">How to use MiniMax H3: references, editing, and audio</a></li>
<li><a href="https://comfyui-wiki.com/en/tutorial/advanced/video/minimax/minimax-h3">MiniMax H3 in ComfyUI: Complete Video Generation ... | ComfyUI Wiki</a></li>

</ul>
</details>

**标签**: `#MiniMax-H3`, `#AI video generation`, `#physics modeling`, `#community experiment`

---

<a id="item-19"></a>
## [Seamless Video Continuation in the new Minimax Seed Hunter v1.2 release! Workflow + Guide](https://www.reddit.com/r/StableDiffusion/comments/1w24f9g/seamless_video_continuation_in_the_new_minimax/) ⭐️ 6.0/10

A Reddit post presents a workflow and guide for seamless video continuation using the new Minimax Seed Hunter v1.2 release.

reddit · r/StableDiffusion · /u/foxdit · 8月30日 01:49

**标签**: `#AI video generation`, `#Minimax`, `#workflow`, `#video continuation`

---

<a id="item-20"></a>
## [Reddit 用户分享使用 ProPainter 节点本地去除视频水印](https://www.reddit.com/r/StableDiffusion/comments/1w2dtfg/remove_watermark_from_videos/) ⭐️ 6.0/10

一位 Reddit 用户分享了一个完全本地、易于使用的视频静态水印去除方案，该方案基于 ProPainter 节点和几个常见的自定义节点，并已发布到 Civit AI 平台。 这为云处理或手动去除水印提供了一种实用的替代方案，让视频编辑者拥有免费且保护隐私的工具。同时也展示了 ProPainter 如何在 Stable Diffusion 生态中被用于实际的视频编辑任务。 该方案依赖于 ProPainter Nodes，即 ProPainter 视频修复框架的 ComfyUI 实现，并且专门针对静态水印有效。原始 ProPainter 项目已正式移除水印去除演示以防止不当使用，因此这类社区方案显得尤为值得注意。

reddit · r/StableDiffusion · /u/qdr1en · 8月30日 10:19

**背景**: ProPainter 是一个视频修复框架，结合了循环光流补全、双域传播和掩码引导的稀疏 Transformer，用以填充视频帧中被遮挡或损坏的区域。视频修复是指通过生成合理的内容来替换视频中不需要的物体或水印。Civit AI 是一个流行的 AI 艺术模型与工作流分享平台，包括为 ComfyUI（Stable Diffusion 的基于节点的界面）开发的自定义节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shangchenzhou.com/projects/ProPainter/">ProPainter for Video Inpainting - Shangchen Zhou</a></li>
<li><a href="https://github.com/sczhou/ProPainter">GitHub - sczhou/ProPainter: [ICCV 2023] ProPainter: Improving ... [2309.03897] ProPainter: Improving Propagation and ... GitHub - daniabib/ComfyUI_ProPainter_Nodes: ️ ComfyUI ... ProPainter: Improving Propagation and Transformer for Video ... ProPainter: Improving Propagation and Transformer for Video ... ProPainter - a Hugging Face Space by sczhou</a></li>
<li><a href="https://civitai.com/">Civitai | Discover and Create AI Art</a></li>

</ul>
</details>

**标签**: `#video editing`, `#watermark removal`, `#ProPainter`, `#Stable Diffusion`, `#local processing`

---

<a id="item-21"></a>
## [MMH3 加速器评测：Sage+Spectrum 质量最佳，速度减半](https://www.reddit.com/r/StableDiffusion/comments/1w2z2ua/mmh3_several_accelerators_tested_for_quality/) ⭐️ 6.0/10

一位 Reddit 用户总结了 33 分钟的 MMH3 视频生成加速器评测视频，报告称 Sage+Spectrum 组合在半速下仍能提供非常好的画质。帖子还分享了回退技巧：如果画质不佳，可以去掉 Spectrum，仅使用 Sage。 MMH3（MiniMax H3）是重要的开源视频生成模型，加速方法直接影响其实用性。用户主导的画质对比有助于从业者为自己的工作流选择合适的加速器，尤其是在 Stable Diffusion 和视频生成社区。 视频测试了包括 Turbo、EasyCache 0.10 和 Sage+SolAttn 在内的多种加速器，但测试者对这些方案并不满意。评测者主要关注面部、反射和整体布局，并使用了精心设计的测试仪表盘，涵盖文生视频、图生视频和参考生视频片段。

reddit · r/StableDiffusion · /u/reeight · 8月31日 01:09

**背景**: MMH3，又称 MiniMax H3，是一个开源多模态视频模型，能统一理解文本、图像、视频和音频输入，支持视频生成、基于参考的创作和编辑。Sage 和 Spectrum 等加速器是无需训练的扩散模型推理加速技术，而 EasyCache 则通过缓存变换向量来加速视频扩散。对于扩散模型，这类加速器通常以牺牲部分画质来换取更低的延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.minimax.io/docs/guides/video-generation">Video Generation - MiniMax API Docs</a></li>
<li><a href="https://github.com/ruwwww/ComfyUI-Spectrum-sdxl">ComfyUI Spectrum SDXL Node - GitHub</a></li>
<li><a href="https://www.emergentmind.com/topics/easycache-framework">EasyCache : Adaptive Caching for Diffusion Models</a></li>

</ul>
</details>

**标签**: `#video generation`, `#accelerators`, `#quality assessment`, `#Stable Diffusion`, `#MMH3`

---

