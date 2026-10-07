# Horizon 每日速递 - 2026-10-07

> 从 39 条内容中筛选出 21 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：Claude Code、AI video generation、LLM、ComfyUI、Mistral。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[博客观点：Claude Code 的建议消息功能服务的是模型，而非用户](https://www.zohaib.cc/blog/smartest-claude-code-feature)**
2. **[Claude 写剧本，MiniMax H3 与 ComfyUI 渲染 25 个场景的 AI 喜剧短片](https://www.reddit.com/r/StableDiffusion/comments/1wz82c3/and_how_does_that_make_you_feel_an_ai_short/)**
3. **[Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型](https://mistral.ai/news/mistral-large-4//)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [博客观点：Claude Code 的建议消息功能服务的是模型，而非用户](https://www.zohaib.cc/blog/smartest-claude-code-feature)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型](https://mistral.ai/news/mistral-large-4//)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型](https://mistral.ai/news/mistral-large-4//)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：博客观点：Claude Code 的建议消息功能服务的是模型，而非用户

**关联新闻**: [博客观点：Claude Code 的建议消息功能服务的是模型，而非用户](https://www.zohaib.cc/blog/smartest-claude-code-feature)

**切入角度**: 一篇发表在 zohaib.cc 上的博客文章认为，Claude Code 的“建议消息”（suggested message）功能——即为用户提议下一条提示词——主要的受益者是模型及其训练数据，而不是坐在终端前的开发者。该文章在 Hacker News 上引发了讨论，达到约 100 分、51 条评论，许多读者在争论这一功能究竟是纯体验优化，还是一种数据收集手段。 这篇文章把一个小小的界面细节上升为关于激励机制的问题：如果某个 AI 编程工具的功能主要是为了产生训练信号，那么开发者的日常工作实际上就变成了无偿的数据标注。它也呼应了专业开发者日益增长的担忧：自己的工作流究竟有多少正被少数几家 AI 厂商收割。 这一说法属于推测而非有据可查的事实——Anthropic 从未把建议消息描述为训练数据机制，而且有评论者指出，只要把任意对话截断到用户发言之前，就可以让模型预测出一条看似合理的用户提问，因此这个显性功能未必是采集训练数据所必需的。同样值得记住的是，Claude Code 在本地终端中运行，直接与模型 API 通信，无需后端服务器或远程代码索引，并且在修改文件或执行命令前会请求用户授权。

**可延展方向**: Claude Code 是 Anthropic 推出的智能体式编程工具，运行在开发者的终端里，可以读取并修改本地代码库，并在用户批准的前提下执行命令。“建议消息”是该工具给出的、作为开发者下一轮输入候选的短提示词，类似于电子邮件和聊天应用中常见的“建议回复”。大语言模型通过在海量文本（其中包含对话记录）上做“预测下一个 token”的目标来训练，因此“聊天界面是否在暗中塑造自己日后学习的数据”这一问题一直是热门话题。

---

### 选题 2：Claude 写剧本，MiniMax H3 与 ComfyUI 渲染 25 个场景的 AI 喜剧短片

**关联新闻**: [Claude 写剧本，MiniMax H3 与 ComfyUI 渲染 25 个场景的 AI 喜剧短片](https://www.reddit.com/r/StableDiffusion/comments/1wz82c3/and_how_does_that_make_you_feel_an_ai_short/)

**切入角度**: Reddit 用户 r/StableDiffusion 上的一位作者展示了一套高度自主的 AI 电影制作流程：Claude 独立完成了故事、五个角色、全部对白以及 25 个场景的剧本，拍出一部 3 分钟的心理医生诊室喜剧；MiniMax H3（Singularity ref2va v1.3 加 8-step 768p turbo LoRA）配合 ComfyUI 视频构建器渲染了所有场景，并自带语音与音效，总渲染时间约 6.3 小时。人类只提供了一段简短的提示词，并在中途对某个不听话的场景做了一次干预。 它说明具备代理能力的 LLM 工作流正与开源视频生成模型融合，把编剧、选角、配音、音效、配乐和质检等整支剧组的工作压缩进一条自动化流水线，这一趋势正在重塑个人创作者和小型工作室的产能边界。对 Stable Diffusion 与 ComfyUI 社区而言，这是一个可复现的具体案例，说明节点图已从单次出图工具演变为真正的生产基础设施。 角色先用 Z-Image（Turbo）生成三视图参考表；H3 采用两遍工作流——先跑 Singularity 模型，第二遍使用 8-step LoRA、4 步、0.35 降噪——并在每个场景中逐字复用同一段角色声音描述，以保证 H3 原生语音的一致性。质检也大幅自动化：用 Whisper 将音频与剧本比对，逐角色检查音高与音色，失败镜头重拍，配乐由 MiniMax Music 3 生成，最终母带归一化到 -14 LUFS，音画同步最差偏差仅 5 毫秒。

**可延展方向**: MiniMax H3 是一个开放的通用全模态生成模型，可统一理解文本、图像、视频与音频，并在同一次生成中输出原生同步立体声，API 支持最长 15 秒、最高 2K，开源权重在短边原生生成 768p。ComfyUI 是面向生成式 AI 流水线的开源节点式可视化图编辑与执行后端，让创作者能把 H3、Z-Image、Whisper 等模型串联成一套自动化工作流。Z-Image 是为高质量生成和强角色一致性设计的图像基础模型（并有 Turbo 版本），这正是它被用来生成演员参考表的原因。

---

### 选题 3：Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型

**关联新闻**: [Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型](https://mistral.ai/news/mistral-large-4//)

**切入角度**: Mistral 正式发布 Mistral Large 4（ML4）：这是一个开放权重的多模态旗舰模型，总参数量 1.05 万亿，采用 Mixture-of-Experts 架构，激活参数 52B，并配有 1.6B 的视觉编码器，完全在 Mistral 位于欧洲的自有数据中心、用约 3800 块 NVIDIA Grace Blackwell GPU 从零训练而成。该模型由 CEO Arthur Mensch 在阿布扎比 AI Everything 大会上介绍，并带来一个只有“high”和“none”两档的新推理开关，在视觉与网络安全基准上表现突出。 这是欧洲迄今为止最强的开放权重前沿模型之一，训练与推理都完全在欧盟境内完成，对于有数据主权要求的企业意义重大，也说明前沿级训练未必需要超大规模厂商级别的算力。它在网络安全基准上的高分和颇具竞争力的视觉表现，使其成为中国开源实验室以及顶级闭源模型之外的一个现实替代方案，尤其适合日常使用和防御性安全场景。 该模型采用细粒度 Mixture-of-Experts 设计，总参数 1.05 万亿、激活参数 52B，另配一个独立的 1.6B 视觉编码器；其推理控制粒度相当粗糙，只支持“high”和“none”两档，早期实测显示两档差异并不明显。有测试者测得其价格约为 4 月发布的 Mistral Medium 3.5 的十分之一，同时在某个数据分析基准上把准确率从 58% 提升到 74%。

**可延展方向**: Mixture-of-Experts（MoE）是一种只对模型参数的一小部分进行激活的架构——在这里就是 1.05 万亿参数中的 52B——从而让实验室在扩大总容量的同时不必为每次请求付出全部算力成本。NVIDIA 的 Grace Blackwell 是继 Hopper 之后的 GPU 世代，其中 GB200 超级芯片把 Grace CPU 与 Blackwell GPU 组合在一起，主打大规模 AI 训练。推理开关（或称“推理强度”设置）用于告诉模型在作答前投入多少内部思考，以延迟和成本换取多步推理任务的准确率，许多厂商会在“none”和“high”之间提供多个档位。

---

1. [OpenAI 在 GitHub 发布 722 篇 AI 生成的数学手稿](#item-1) ⭐️ 9.0/10
2. [弗朗西斯·哈尔岑因冰立方中微子天文台获 2026 年诺贝尔物理学奖](#item-2) ⭐️ 9.0/10
3. [Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型](#item-3) ⭐️ 8.0/10
4. [谷歌发布 EmbeddingGemma 2：Apache 2.0 许可的轻量多模态嵌入模型](#item-4) ⭐️ 8.0/10
5. [OpenTPU：由 AI 智能体设计的开源 AI 加速器](#item-5) ⭐️ 8.0/10
6. [派拉蒙 Skydance 完成 1110 亿美元与华纳兄弟探索的合并](#item-6) ⭐️ 8.0/10
7. [HunyuanImage 3.0（80B）在单张 12–24 GB 显卡上原生运行于 ComfyUI](#item-7) ⭐️ 8.0/10
8. [Hugging Face Diffusers v0.41.0 发布：集成 Qwen-Image 2.1 并启用新发布策略](#item-8) ⭐️ 7.0/10
9. [OpenAI Decisions API 进入公测，主打快速分类判断](#item-9) ⭐️ 7.0/10
10. [AnyPS5 无模拟器将 PS5 二进制移植到 PC，已映射 87% 系统库](#item-10) ⭐️ 7.0/10
11. [博客观点：Claude Code 的建议消息功能服务的是模型，而非用户](#item-11) ⭐️ 7.0/10
12. [Gleam 编译器改为直接生成 Erlang 抽象形式，不再输出 Erlang 源码](#item-12) ⭐️ 7.0/10
13. [OpenSSH 10.6 修复压缩侧信道问题，并放弃 macOS 沙箱支持](#item-13) ⭐️ 7.0/10
14. [多伦多 VPN 服务商因合法访问法案计划撤离加拿大](#item-14) ⭐️ 7.0/10
15. [FastVideo 的 FastH3 视频模型现已可在单台消费级显卡上运行](#item-15) ⭐️ 7.0/10
16. [欧盟《人工智能法案》将于 12 月 2 日起禁止“脱衣”类 AI 工具](#item-16) ⭐️ 7.0/10
17. [TII 发布 Falcon-Emirati：面向阿联酋方言与文化的定制大模型](#item-17) ⭐️ 6.0/10
18. [OmniChar 的 ComfyUI 工作流为 .char 角色加入一致克隆语音与口型同步](#item-18) ⭐️ 6.0/10
19. [Forge Neo 扩展让 MiniMax H3 在 16 GB 显存上生成带声音的视频](#item-19) ⭐️ 6.0/10
20. [Claude 写剧本，MiniMax H3 与 ComfyUI 渲染 25 个场景的 AI 喜剧短片](#item-20) ⭐️ 6.0/10
21. [MiniMax H3 ref2va：在 ComfyUI 中排查动漫视频画质忽好忽坏](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 在 GitHub 发布 722 篇 AI 生成的数学手稿](https://openai.com/index/sharing-ai-progress-in-mathematics/) ⭐️ 9.0/10

OpenAI 在 GitHub 上开源了名为 openai/math 的仓库，其中包含由一款尚未发布的内部前沿模型在模型开发评测过程中生成的 722 篇数学手稿，按 372 个相关族分组。这些论文附带了 Lean 证明形式化文件，并声称解决了多个长期未解难题，例如 Barnette 猜想、有理数域上的希尔伯特第十问题以及唯一博弈猜想。 如果这些结果得到验证，将标志着 AI 辅助数学可能出现范式转变，表明前沿模型能够挑战真正未解的研究难题，而非仅做教科书式练习。这一发布同样重要，因为 OpenAI 表示其现有数学基准已经饱和，说明 AI 评测正被推向真实、尚未解决的数学问题。 该仓库以 Apache-2.0 许可证发布，并包含用于辅助验证的 Lean 形式化文件，不过 OpenAI 指出验证仍不均衡，仍需独立核查。有评论者注意到，该列表声称完整解决了前 500 个未解难题中的 90 个，其中排名较高的包括有理数域上的希尔伯特第十问题（第 22 位）、唯一博弈（第 29 位）以及 Landau–Siegel 零点不存在性（第 48 位）。

hackernews · OfficialTurkey · 10月6日 22:17 · [社区讨论](https://news.ycombinator.com/item?id=49984923)

**背景**: Lean 是一种交互式定理证明器，允许数学家以计算机可检查的形式语言编码证明，这也是形式化文件在验证 AI 生成数学时居核心地位的原因。唯一博弈猜想是计算复杂性理论中的基础性假设，支撑着大量不可近似性结果；Barnette 猜想则是图论命题，断言任何 3-连通三次平面图都是哈密顿图；而希尔伯特第十问题关乎丢番图方程的可解性。如此规模的声明并不寻常，在被数学界接受之前通常需要同行评审和形式化验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/sharing-ai-progress-in-mathematics/">Sharing AI progress in mathematics - OpenAI</a></li>
<li><a href="https://github.com/openai/math">GitHub - openai/math</a></li>
<li><a href="https://www.unite.ai/openai-releases-722-math-manuscripts-from-an-unreleased-ai-model/">OpenAI Releases 722 Math Manuscripts From an Unreleased AI ...</a></li>

</ul>
</details>

**社区讨论**: 评论者既感到震撼又保持怀疑：有人指出该列表声称解决了前 500 个未解难题中的 90 个，还有人引用了 Kevin Buzzard 关于「一个理解全部现代纯数学的心智能看多远」的评论。一位理论计算机科学／调度方向的从业者以 1979 年提出的三机器单位作业调度问题为例，说明其中也包含规模较小但长期未解的结果，而其他人则强调此类声明需要仔细验证。

---

<a id="item-2"></a>
## [弗朗西斯·哈尔岑因冰立方中微子天文台获 2026 年诺贝尔物理学奖](https://www.nobelprize.org/prizes/physics/2026/) ⭐️ 9.0/10

2026 年诺贝尔物理学奖授予冰立方中微子天文台（IceCube）首席研究员弗朗西斯·哈尔岑，以表彰他构想并领导建造这座埋藏在南极冰层下、体积约一立方公里的探测器，以及在高能天体物理中微子发现上的决定性贡献。该探测器建于南极阿蒙森–斯科特南极点科考站，其光学传感器阵列于 2010 年 12 月完工，而它的首次重大升级也已在 2026 年 2 月宣布完成部署。 这一奖项标志着中微子天文学从探测实验成长为一门真正的观测学科，其地位可与早先因发现中微子、探测宇宙中微子而颁发的诺贝尔奖相提并论。它有望为“多信使天文学”以及冰立方-Gen2、地中海 KM3NeT 等下一代探测器带来更多资金与关注。 冰立方的传感器称为数字光学模块（DOM），每个模块内含一个光电倍增管和一块数据采集电路板，60 个模块串成一条“弦”，通过热水钻在冰层中融孔后下放至 1450 至 2450 米深处。由于中微子发生相互作用的概率极低，探测器必须做得极其庞大，并深埋冰下以屏蔽宇宙线本底，这也使得数据量极为庞大、统计显著性始终是分析中的主要挑战。

hackernews · solarist · 10月6日 09:48 · [社区讨论](https://news.ycombinator.com/item?id=49976265)

**背景**: 中微子是一种不带电荷、质量极小，且只通过弱核力和引力与其他物质作用的基本粒子，因此被称为“幽灵粒子”——数以万亿计的中微子可以穿过整个地球而不被吸收。中微子天文学正是利用这一点：中微子从源头沿直线飞行、不受磁场偏折，因而能揭示光学望远镜无法观测的高能宇宙过程。探测方式是间接的：当中微子偶尔与冰中的原子发生碰撞时，会产生高速带电粒子，这些粒子在冰中发出微弱的蓝色切伦科夫辐射，被埋在冰下的光学传感器记录下来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IceCube_Neutrino_Observatory">IceCube Neutrino Observatory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neutrino_astronomy">Neutrino astronomy</a></li>
<li><a href="https://icecube.wisc.edu/">IceCube – IceCube Neutrino Observatory</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论热度很高（532 分、176 条评论），整体情绪极为热烈：有评论者详细解释了中微子为何被称为“幽灵粒子”，以及切伦科夫辐射如何让探测成为可能。还有多人分享了自己与项目的亲身联系，其中一位曾在 2009 年前往南极点参与建设，并打趣说自己“在那儿待了一整段时间却一个中微子都没看见”；另一位则讲述了同事专程飞往南极点，只为给数据处理系统安装 Debian 的经历。

**标签**: `#physics`, `#neutrino astronomy`, `#Nobel Prize`, `#IceCube`, `#scientific research`

---

<a id="item-3"></a>
## [Mistral 发布 Large 4：在欧洲用 3800 块 Blackwell GPU 训练的万亿参数开源模型](https://mistral.ai/news/mistral-large-4//) ⭐️ 8.0/10

Mistral 正式发布 Mistral Large 4（ML4）：这是一个开放权重的多模态旗舰模型，总参数量 1.05 万亿，采用 Mixture-of-Experts 架构，激活参数 52B，并配有 1.6B 的视觉编码器，完全在 Mistral 位于欧洲的自有数据中心、用约 3800 块 NVIDIA Grace Blackwell GPU 从零训练而成。该模型由 CEO Arthur Mensch 在阿布扎比 AI Everything 大会上介绍，并带来一个只有“high”和“none”两档的新推理开关，在视觉与网络安全基准上表现突出。 这是欧洲迄今为止最强的开放权重前沿模型之一，训练与推理都完全在欧盟境内完成，对于有数据主权要求的企业意义重大，也说明前沿级训练未必需要超大规模厂商级别的算力。它在网络安全基准上的高分和颇具竞争力的视觉表现，使其成为中国开源实验室以及顶级闭源模型之外的一个现实替代方案，尤其适合日常使用和防御性安全场景。 该模型采用细粒度 Mixture-of-Experts 设计，总参数 1.05 万亿、激活参数 52B，另配一个独立的 1.6B 视觉编码器；其推理控制粒度相当粗糙，只支持“high”和“none”两档，早期实测显示两档差异并不明显。有测试者测得其价格约为 4 月发布的 Mistral Medium 3.5 的十分之一，同时在某个数据分析基准上把准确率从 58% 提升到 74%。

hackernews · Philpax · 10月6日 13:15 · [社区讨论](https://news.ycombinator.com/item?id=49977979)

**背景**: Mixture-of-Experts（MoE）是一种只对模型参数的一小部分进行激活的架构——在这里就是 1.05 万亿参数中的 52B——从而让实验室在扩大总容量的同时不必为每次请求付出全部算力成本。NVIDIA 的 Grace Blackwell 是继 Hopper 之后的 GPU 世代，其中 GB200 超级芯片把 Grace CPU 与 Blackwell GPU 组合在一起，主打大规模 AI 训练。推理开关（或称“推理强度”设置）用于告诉模型在作答前投入多少内部思考，以延迟和成本换取多步推理任务的准确率，许多厂商会在“none”和“high”之间提供多个档位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.mistral.ai/models/mistral-large-4-0">Mistral Large 4 - Mistral AI | Mistral Docs</a></li>
<li><a href="https://mistral.ai/news/mistral-large-4/">Introducing Mistral Large 4 | Mistral</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区整体态度积极但偏技术性：simonw 指出 high/none 推理开关对输出几乎没影响，“high”甚至比“none”产生更少的输出 token，不过他认为这是他见过最好的 Mistral 模型。abixb 提出效率方面的疑问：一个仅用约 4000 块 GB 系列 GPU 训练的万亿参数模型，为何能接近 Kimi 最新模型的表现；prodigycorp 称赞其在视觉和网络安全基准上的领先，认为它是一款优秀的“防御型模型”；michaelkdev 把它视为欧洲主权 AI 的一步；chriddyp 则报告在 Plotly 的数据分析基准上准确率从 58% 升到 74%，而价格只有 Mistral Medium 3.5 的十分之一。

**标签**: `#LLM`, `#Mistral`, `#AI Models`, `#Benchmarks`, `#Model Release`

---

<a id="item-4"></a>
## [谷歌发布 EmbeddingGemma 2：Apache 2.0 许可的轻量多模态嵌入模型](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) ⭐️ 8.0/10

谷歌发布了 EmbeddingGemma 2，这是一个采用 Apache 2.0 许可的开放嵌入模型，提供约 2.7 亿参数的纯文本版本和 4.4 亿参数的文本加视觉版本，面向本地自托管的嵌入向量生成。它把文本（在较大版本中还包括图像）映射到同一个向量空间，将 EmbeddingGemma 系列从纯文本检索扩展到多模态场景。 嵌入模型是 RAG 流程、语义搜索和智能体记忆的核心组件，因此一个许可宽松、可在本地运行的小模型同时消除了调用托管嵌入 API 的成本和厂商依赖。由于嵌入向量通常是针对海量文档一次性计算并长期存储的，开放许可的模型还能避免专有嵌入接口一旦下线、已存好的向量全部作废的风险。 该模型面向本地运行，谷歌的开发者文档描述了一个统一的 768 维嵌入空间，并支持 Matryoshka 表示学习（MRL），开发者可据此把向量截断到更短的维度，但会牺牲一部分准确率。多模态版本可同时处理文本和图像，社区成员指出它适合 MediaPipe 这类端侧流水线；不过谷歌各页面给出的参数规模和模态覆盖范围有所出入，使用者应以模型卡为准。

hackernews · ilreb · 10月6日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=49980487)

**背景**: 嵌入模型把文本、图像等内容转换成数值向量，使语义相近的内容在向量空间中彼此靠近；这些向量被用于语义搜索、去重、聚类以及检索增强生成（RAG）——即大语言模型在回答前先检索相关文档。像 CLIP 这样的多模态嵌入模型把文本和图像放进同一个坐标空间，因此照片和它的文字描述可以直接比较。MRL 是一种训练技巧，允许同一个嵌入向量按需截断成更短的维度；而二值量化则把每个维度压缩成 1 个比特，以节省内存并加快大规模向量的比对速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/en/embeddinggemma-2-the-developer-guide/">EmbeddingGemma 2: The Developer Guide- Google Developers Blog</a></li>
<li><a href="https://ai.google.dev/gemma/docs/embeddinggemma">EmbeddingGemma | Google AI for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论整体非常正面：simonw 赞赏 Apache 2.0 许可，认为专有的托管嵌入模型不适合需要长期存储数百万向量的流程，因为模型一旦被下线就会造成破坏；minimaxir 则欢迎终于出现一个兼顾多模态的优秀中等规模嵌入模型，并暗示自己有尚未发布的本地嵌入工具。kaycebasques 询问二值量化能否作为 MRL 的替代方案用于 EmbeddingGemma 2，其他人则强调端侧文本加图像的用例，并称谷歌开放的权重接近其在 Android 手机上部署的版本。

**标签**: `#embeddings`, `#open-source-models`, `#multimodal`, `#Gemma`, `#RAG`

---

<a id="item-5"></a>
## [OpenTPU：由 AI 智能体设计的开源 AI 加速器](https://github.com/FeSens/openTPU) ⭐️ 8.0/10

GitHub 项目 FeSens/openTPU 发布了一款开源 AI 推理加速器，其硬件设计本身由 AI 辅助完成，沿用了作者此前用于生成 RISC-V CPU 核心的同一套方法。据作者介绍，该 TPU 最初每秒只能生成几个 token，经过递归自我改进循环后在较小的模型上达到 80+ token/秒，并可运行 Qwen 3.5、Gemma 4 等现代模型。 该项目正处在两个热门趋势的交汇点：面向大模型推理的低成本开放硬件，以及能够设计硬件本身的 AI 智能体——若属实，小型团队无需芯片设计团队也能造出加速器。它还直接卷入了关于“递归自我改进”的争论，因为其卖点在本质上就是让 AI 改进运行 AI 的芯片。 该仓库提供了一个推理引擎（otpu-chat，演示中在 FPGA 卡上运行 LFM2.5-230M），以及用于监控板卡利用率和 DRAM 带宽的工具 otpu-smi；项目围绕两个问题展开：AI 智能体在硬件设计上能走多远，以及它们能否造出运行自身推理的芯片。宣传中的 80+ token/秒 仅适用于较小的模型，而且关于递归自我改进的说法、以及与成熟加速器的性能对比，都缺乏独立验证。

hackernews · fsbonetto · 10月6日 16:23 · [社区讨论](https://news.ycombinator.com/item?id=49980715)

**背景**: AI 加速器（也称 NPU 或深度学习处理器）是专为加速神经网络计算而设计的芯片，最著名的例子是 Google 的 TPU。递归自我改进（RSI）指 AI 系统改写并测试自己的代码以提升自身能力，理论上可能带来智能的快速跃升，一直是 AI 安全讨论的核心议题。在这个项目里，“由 AI 开发”意味着由 AI 智能体生成并迭代硬件设计，而 FPGA 的可重构特性则允许同一块芯片结构针对不同工作负载重新调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/FeSens/openTPU">GitHub - FeSens/openTPU: An open-source AI accelerator ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_processing_unit">Neural processing unit - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论十分活跃但观点分歧：一位软件工程师质疑，既然能降低单次请求成本，前沿实验室为何不直接把模型“烧”进芯片；作者则解释了从 RISC-V 到 OpenTPU 的传承关系，以及从每秒几个 token 提升到 80+ token/秒 的过程。也有人推测顶尖模型在去年年底就已能设计出可运行模型的加速器，并认为更有意思的问题是 AI 能否利用 FPGA 的可重构结构发明全新架构，同时还有人拿递归自我改进的安全风险开玩笑（“长着红色发光眼睛的金属骨架”）。

**标签**: `#OpenTPU`, `#AI accelerators`, `#hardware design`, `#recursive self-improvement`, `#open source`

---

<a id="item-6"></a>
## [派拉蒙 Skydance 完成 1110 亿美元与华纳兄弟探索的合并](https://arstechnica.com/tech-policy/2026/10/paramount-completes-111b-warner-merger-creating-skydance-behemoth/) ⭐️ 8.0/10

派拉蒙 Skydance 已完成与华纳兄弟探索价值 1110 亿美元的合并，将两家公司整合为一个庞大的媒体集团，旗下囊括 CBS、派拉蒙影业、HBO、CNN、华纳兄弟电影制片厂以及探索频道的电视网，并与 Paramount+和 Max 等流媒体服务并列。 这笔交易减少了好莱坞主要制片厂的数量，把美国新闻与娱乐内容生产的巨大份额集中到单一所有者手中，从而加剧了美国长期以来关于媒体整合与反垄断执法的争论。与此同时，在传统制片厂正被 YouTube 等平台夺走观看时长之际，它也重塑了整个竞争格局。 1110 亿美元的交易价格伴随着沉重的债务负担，评论者认为这会限制合并后公司在内容或流媒体上的投入力度。讨论中一个被广泛引用的对比是：YouTube 约占美国电视屏幕总观看时长的 13%，而派拉蒙与华纳两者合计仅约 6%。

hackernews · Mgtyalx · 10月6日 20:33 · [社区讨论](https://news.ycombinator.com/item?id=49983703)

**背景**: 时代华纳历来是大型并购的常客：2001 年 AOL 与其合并成立 AOL 时代华纳，2018 年 AT&T 将其收购，随后又在 2022 年被分拆并与 Discovery 合并，组建了华纳兄弟探索。而派拉蒙此前则被 Skydance Media 收购，该公司由甲骨文联合创始人拉里·埃里森之子大卫·埃里森领导。正是这段历史，让许多观察者认为涉及时代华纳的大型交易一直未能创造价值，也使这次新合并无论在经济效益还是所有权方面都受到审视。

**社区讨论**: 评论者普遍持怀疑态度：多人引用 The Verge 长期以来的观点，认为涉及时代华纳的合并从未成功，并以 AOL 和 AT&T 作为前车之鉴。也有人担忧美国媒体在新所有者手中会变得编辑控制权高度集中，警告合并后公司的债务负担是严重问题，并指出 YouTube 的观看时长份额更大，说明真正的竞争威胁其实来自传统好莱坞之外。

**标签**: `#mergers`, `#media`, `#antitrust`, `#consolidation`, `#Warner Bros Discovery`

---

<a id="item-7"></a>
## [HunyuanImage 3.0（80B）在单张 12–24 GB 显卡上原生运行于 ComfyUI](https://www.reddit.com/r/StableDiffusion/comments/1wzclz5/hunyuanimage_30_80b_running_natively_in_comfyui/) ⭐️ 8.0/10

一位开发者发布了 ComfyUI-HunyuanImage3 节点，为腾讯 80B 参数、每步仅激活 13B 的 HunyuanImage 3.0 混合专家图像模型提供原生 ComfyUI 支持。它不是对腾讯官方管线的封装，而是直接调用标准的 KSampler、VAE Decode 和 ComfyUI 自带的内存管理，把专家权重从系统内存中流式加载，从而在 RTX 3090 上以 4-bit 权重约 29 秒生成约 100 万像素的图像。 这说明 80B 级别的开源权重图像模型已经可以在消费级硬件上本地运行，大幅降低了以往需要数据中心级显存才能使用的大型 MoE 扩散模型的门槛。同时它也验证了 ComfyUI 的内存管理机制可以作为流式加载超大模型的实用平台，并把文生图、指令编辑和多图风格迁移统一到同一套标准工作流中，且无需任何 pip 安装。 权重提供三种格式：4-bit W4A8（44 GB）、int8（76 GB）和 bf16（150 GB，主要用于对比）；作者指出加载 4-bit 文件时 ComfyUI 占用约 50 GB 系统内存，因此真正的门槛是系统内存而非显存，因为专家权重每步都要经 PCIe 传输。在把显存限制为 16 GB 或 12 GB 的 4090 上，每张图分别约需 30 秒和 32 秒；项目需要较新的 ComfyUI 版本，并且作者坦言少数编辑指令失败（雪花几乎看不见、logo 无法去除、改夜景仍然保持白天）。

reddit · r/StableDiffusion · /u/LatentSpacer · 10月6日 19:59

**背景**: HunyuanImage 3.0 是腾讯于 2025 年 9 月发布的开源权重图像生成模型，总参数 80B、每步激活 13B，采用包含 64 个专家的混合专家（MoE）架构。ComfyUI 是一款免费开源的节点式图像与视频生成界面，用户通过连接节点来搭建工作流。MoE 采用条件计算：路由机制每个 token 只激活少数专家，因此计算量接近小模型，但内存占用仍接近超大模型——正因如此，本项目把专家权重常驻系统内存并按步通过 PCIe 流式传输，而不是全部塞进显存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/HunyuanImage-3.0">tencent/ HunyuanImage - 3 . 0 · Hugging Face</a></li>
<li><a href="https://kenerateai.com/model/hunyuan-image">HunyuanImage 3 . 0 — Tencent's 80B Open Image Model | Kenerate AI</a></li>
<li><a href="https://dev.to/michael_hensel/what-is-a-mixture-of-experts-model-and-why-does-it-use-fewer-resources-3jkl">What Is a Mixture of Experts Model and Why Does... - DEV Community</a></li>

</ul>
</details>

**标签**: `#ComfyUI`, `#HunyuanImage`, `#Mixture-of-Experts`, `#Text-to-Image`, `#GPU Inference`

---

<a id="item-8"></a>
## [Hugging Face Diffusers v0.41.0 发布：集成 Qwen-Image 2.1 并启用新发布策略](https://github.com/huggingface/diffusers/releases/tag/v0.41.0) ⭐️ 7.0/10

Hugging Face 发布了 Diffusers v0.41.0，集成了 Qwen-Image 2.1——这是一个统一模型，涵盖文生图、图像编辑、多参考图输入、原生 RGBA 透明输出以及 LoRA 训练，其视觉生成部分拥有 70 亿参数。此次发布还标志着策略转变：从此 Diffusers 采用与 Transformers 相同的理念，将次要版本围绕新模型集成来协调发布，而补丁版本仍专注于修复问题。 Qwen-Image 2.1 将生成与编辑整合在一个仅 70 亿参数的紧凑模型中，使 Diffusers 用户可以通过熟悉的 pipeline API 同时完成两类任务，而不必在多个模型和自定义代码之间来回切换。借鉴自 Transformers 的新发布节奏意味着次要版本将由模型集成驱动，因此下游项目和用户应围绕新模型的可用性而非固定的时间周期来规划升级。 此次发布的其他要点包括：张量并行检查点加载，每个 rank 只读取自己所分片的权重切片，从而降低加载时的内存占用；LTX-2.5 DFR 流水线支持关键帧槽位以及可组合的空间与时间细化；Cosmos 3 支持 SeaCache，并为 ModelOpt FP8 检查点提供 W8A8/W8A16 混合去噪；此外还新增了 Krea 2 和 MiniMax-H3 的单文件加载器。用户需注意破坏性变更：ONNX 支持已被弃用，建议改用 Optimum，同时此前已弃用的 LuminaText2ImgPipeline 和 Lumina2Text2ImgPipeline 别名已被移除。

github · sayakpaul · 10月6日 06:43

**背景**: Diffusers 是 Hugging Face 提供的预训练扩散模型库，涵盖图像、视频和音频，其核心是 DiffusionPipeline API，让用户用几行代码即可运行最先进的模型。Qwen-Image 2.1 是阿里 Qwen 团队开源的统一图像模型，其视觉生成部分采用 32 层 Single-Stream DiT 结构，定位是在生成质量、推理效率和成本之间取得平衡。LoRA（低秩适配）是一种参数高效的微调技术，只训练少量适配器权重而非整个模型；原生 RGBA 输出意味着模型直接生成真正的 alpha 透明通道，而不是依赖事后的背景抠除。在文生图领域，所谓“pipeline”是把模型、调度器和预处理步骤封装在一起的端到端对象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen-Image-2.1 - Hugging Face</a></li>
<li><a href="https://github.com/huggingface/diffusers">GitHub - huggingface/ diffusers : Diffusers : State-of-the-art...</a></li>
<li><a href="https://qwen.ai/blog?id=qwen-image-2.1">Qwen-Image-2.1: Compact, Efficient, and Unified Image Creation</a></li>

</ul>
</details>

**标签**: `#diffusers`, `#huggingface`, `#image-generation`, `#qwen-image`, `#model-release`

---

<a id="item-9"></a>
## [OpenAI Decisions API 进入公测，主打快速分类判断](https://developers.openai.com/api/docs/guides/decisions) ⭐️ 7.0/10

OpenAI 正式将 Decisions API 推向公测，提供一个轻量级接口，直接返回带置信度的“是/否”判断结果，而不是完整生成的文本。它面向的是快速、低成本的分类与决策类任务，而非开放式内容生成。 这次发布标志着行业正走向专用的“系统一”（system-1）式模型，同时价格战也愈发激烈——OpenAI 愿意放弃潜在的输出 token 收入来留住客户。对构建路由、打标签和分类流水线的开发者而言，这带来了更便宜、更快速的推理选择，也助推了“AI 输出是否正在商品化”的更大讨论。 社区评论者指出，其成本与直接用提示词做分类大致相当（约每 100 万 token 0.10 美元），但 Decisions API 号称比 Responses API 快约 10 倍，质量则与像“luna”这样的强模型基本持平。这些数据来自公测期间开发者的经验分享，尚未经过独立验证。

hackernews · chiefstorm · 10月6日 20:57 · [社区讨论](https://news.ycombinator.com/item?id=49984025)

**背景**: Decisions API 返回的是结构化且范围很窄的结果（“是/否”加置信度分数），因此它不同于普通的聊天补全，也不同于仍然会生成完整回复的结构化输出（structured outputs）。由此引发的讨论聚焦于“系统一”（system-1）模型，例如 TypeSafe AI 的 Jev——这类模型在简单判断任务上被优化得远比大型通用大模型更快、更便宜；同时也涉及随着价格下降和开源版本涌现，AI 模型能力正在被商品化的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesel.ai/blog/openai-decisions-api">OpenAI Decisions API explained: how it works and who it's for | eesel AI</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.techpolicy.press/taking-ai-commoditization-seriously/">Taking AI Commoditization Seriously - techpolicy.press</a></li>

</ul>
</details>

**社区讨论**: simonw 等评论者分享了可直接运行的 curl 示例；TSiege 认为这一回应证明了 AI 正在成为商品化市场，系统一模型提供的廉价“是/否/置信度”评分往往已能满足用户所需。Topfi 通过 OpenRouter 对 Jev 和 Mercury Decide 做了初步评测，而 ashu1461 指出在成本和质量上它与基于提示词的分类大致相当，因此真正的优势最终还是体现在速度上。

**标签**: `#openai`, `#api`, `#llm`, `#model-pricing`, `#inference`

---

<a id="item-10"></a>
## [AnyPS5 无模拟器将 PS5 二进制移植到 PC，已映射 87% 系统库](https://github.com/boykopovar/AnyPS5) ⭐️ 7.0/10

开源逆向工程项目 AnyPS5 通过把 PS5 可执行文件重新链接为 Windows/Linux 原生程序，已重新实现约 87% 的主机系统库，完全绕过了传统模拟。据报道，2026 年 9 月底该项目已能让一款商业 PS5 游戏在普通 PC 上显示 Logo 并开始加载主菜单，但在进入可操作界面前崩溃。 这表明兼容层路线最终可能让 PC 玩家原生运行 PS5 游戏，从而削弱主机独占和厂商锁定。它也加剧了游戏保存与平台方法律及商业利益之间的争论，并可能促使索尼等厂商进一步转向仅云端分发。 该项目并不模拟主机硬件，而是把 PS5 可执行文件转换为宿主平台格式，并重新实现动态链接所需的系统库；但项目仍不完整：系统库映射约 87%，当前版本仍会在主菜单阶段崩溃，有报道称崩溃发生在约第 168 帧。由于二进制文件本身属于游戏发行商，分发此类工具很可能仍面临法律风险。

hackernews · Fe2O3 · 10月6日 23:28 · [社区讨论](https://news.ycombinator.com/item?id=49985664)

**背景**: PS5 采用 AMD x86-64 硬件，但其游戏依赖专有的系统库（如 Orbis 操作系统 API）和主机专属的可执行文件格式，因此无法直接在 Windows 或 Linux 上运行。传统模拟器用软件重建主机硬件，计算开销很大；兼容层则通过转译或重新链接，让游戏直接调用宿主操作系统，思路类似 Proton 或 Wine。AnyPS5 正是把这一策略应用到 PS5 上的开源尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/353098/anyps5-project-skips-emulation-entirely-aims-to-port-playstation-5-games-to-pc-directly">AnyPS5 Project Skips Emulation Entirely, Aims to Port ...</a></li>
<li><a href="https://shattered.io/anyps5-skips-emulation-crashes-frame-168-2026/">AnyPS5: PS5 Games on PC Without Emulation [2026]</a></li>
<li><a href="https://windowsforum.com/news/anyps5-loads-ps5-game-menu-but-crashes-before-play-begins.445786/">AnyPS 5 Loads PS 5 Game Menu but Crashes Before Play Begins</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍赞赏这一逆向工程成果及其打破厂商锁定的潜力，但不少人担心它会促使索尼、任天堂和微软进一步转向云游戏。也有人强调法律风险，援引任天堂下架 Yuzu 和 Ryujinx 的先例，建议保留本地 git 镜像；还有人猜测《GTA 6》是否会首日登陆 PC，以及这对软件产业大国可能造成的更广泛经济冲击。

**标签**: `#PlayStation 5`, `#reverse engineering`, `#compatibility layer`, `#game preservation`, `#emulation`

---

<a id="item-11"></a>
## [博客观点：Claude Code 的建议消息功能服务的是模型，而非用户](https://www.zohaib.cc/blog/smartest-claude-code-feature) ⭐️ 7.0/10

一篇发表在 zohaib.cc 上的博客文章认为，Claude Code 的“建议消息”（suggested message）功能——即为用户提议下一条提示词——主要的受益者是模型及其训练数据，而不是坐在终端前的开发者。该文章在 Hacker News 上引发了讨论，达到约 100 分、51 条评论，许多读者在争论这一功能究竟是纯体验优化，还是一种数据收集手段。 这篇文章把一个小小的界面细节上升为关于激励机制的问题：如果某个 AI 编程工具的功能主要是为了产生训练信号，那么开发者的日常工作实际上就变成了无偿的数据标注。它也呼应了专业开发者日益增长的担忧：自己的工作流究竟有多少正被少数几家 AI 厂商收割。 这一说法属于推测而非有据可查的事实——Anthropic 从未把建议消息描述为训练数据机制，而且有评论者指出，只要把任意对话截断到用户发言之前，就可以让模型预测出一条看似合理的用户提问，因此这个显性功能未必是采集训练数据所必需的。同样值得记住的是，Claude Code 在本地终端中运行，直接与模型 API 通信，无需后端服务器或远程代码索引，并且在修改文件或执行命令前会请求用户授权。

hackernews · zed_labs_dev · 10月6日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49981905)

**背景**: Claude Code 是 Anthropic 推出的智能体式编程工具，运行在开发者的终端里，可以读取并修改本地代码库，并在用户批准的前提下执行命令。“建议消息”是该工具给出的、作为开发者下一轮输入候选的短提示词，类似于电子邮件和聊天应用中常见的“建议回复”。大语言模型通过在海量文本（其中包含对话记录）上做“预测下一个 token”的目标来训练，因此“聊天界面是否在暗中塑造自己日后学习的数据”这一问题一直是热门话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://support.claude.com/en/articles/14553413-claude-code-cheatsheet">Claude Code cheatsheet | Claude Help Center</a></li>
<li><a href="https://netquill.com/what-practices-are-beneficial-for-training-ai-models-with-prompts/">What Practices Are Beneficial for Training AI Models With Prompts?</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向怀疑，大致分为两种论点。一派（rcxdude、bugos）质疑其技术前提：只要提示词以“用户发言开始”的标记结尾，“原始”的大模型本来就能生成看似合理的用户提问，而且在“预测发言”与“真实发言”的差异上做训练根本不需要把建议展示给用户；另一派（Cyan488、0xfaded）则表达了对“替你补全句子”式界面的反感，以及对少数私营公司垄断专家开发者行为数据采集的担忧。munchler 还提出一个轻松的观察：这些建议总是全小写，与该评论者自己的输入习惯并不一致。

**标签**: `#Claude Code`, `#LLM`, `#AI training`, `#developer tools`, `#User Experience`

---

<a id="item-12"></a>
## [Gleam 编译器改为直接生成 Erlang 抽象形式，不再输出 Erlang 源码](https://gleam.run/news/gleam-doesnt-compile-to-erlang-source-anymore/) ⭐️ 7.0/10

Gleam 编译器的后端不再先生成 Erlang 源码文本再交给 Erlang 编译器解析，而是直接生成 Erlang 抽象形式(abstract forms)，也就是 Erlang 编译器本身所消费的 AST 表示。这是一个颇为重要的编译器架构变更，在 Hacker News 上引发了 299 分、127 条评论的热烈讨论。 跳过“生成源码再解析”这一额外往返可以缩短编译时间，也让 Gleam 能更直接地接入 Erlang 自身的工具层，例如 parse transform。这在 BEAM 生态中也具有象征意义：Gleam 的后端因此更接近 Elixir 早已采用的同一种中间表示。 Erlang 抽象形式由 Erlang term 规范地构成，标准库提供了用于查看和改写该表示的例程，它同时也是 parse transform 所操作的层面——正是 parse transform 为 qlc 等特性提供了语法糖。Gleam 仍然保留 JavaScript 作为第二个编译目标，因此这一变更只影响 Erlang/BEAM 后端。

hackernews · ingve · 10月6日 08:08 · [社区讨论](https://news.ycombinator.com/item?id=49975619)

**背景**: Gleam 是一门静态类型、函数式、支持并发的编程语言，可编译到 Erlang/BEAM 和 JavaScript，并自带一套类型安全的 OTP 实现——OTP 即 Erlang 的 actor 框架。BEAM 是 Erlang/OTP 的核心虚拟机，负责执行编译后存放在 .beam 文件中的字节码。抽象形式是 Erlang 编译器使用的源码级 AST 格式；自 Erlang/OTP R9C 起，.beam 文件会通过 abstract_code 代码块携带它。由于抽象形式本质上就是普通的 Erlang term，编译器可以直接以编程方式构造它，而无需先打印成文本再重新解析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.erlang.org/doc/apps/erts/absform.html">The Abstract Format — OTP 29.1.1 (erts 17.1)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gleam_(programming_language)">Gleam (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/BEAM_VM">BEAM VM</a></li>

</ul>
</details>

**社区讨论**: 整体氛围非常正面：有评论者详细解释了 Erlang 抽象形式与 parse transform，也有人表达了对 Erlang 运行时的喜爱以及对 Gleam 日渐成熟的欣慰。有用户推荐了 Giacomo 关于 Gleam 与 Rust 的 Twitch 直播，还有人表示自从有了 Lustre 和 Tauri 让 Gleam 可以运行在任何地方后，它已成为自己的默认语言；最主要的期待是希望 Gleam 未来能增加类似 Rust 或 Go 的原生编译目标。

**标签**: `#gleam`, `#erlang`, `#compilers`, `#programming-languages`, `#beam-vm`

---

<a id="item-13"></a>
## [OpenSSH 10.6 修复压缩侧信道问题，并放弃 macOS 沙箱支持](https://www.openssh.org/releasenotes.html#10.6) ⭐️ 7.0/10

OpenSSH 10.6 针对“Crossing The Streams”这一 CRIME 式压缩侧信道攻击加入了缓解措施，该攻击利用了不同会话之间共享的 LZ77 压缩状态；同时由于所依赖的 API 已被移除，该版本在 macOS SDK 27 及更高版本上不再支持沙箱功能。发布说明还指出，OpenSSH 团队目前将改为更频繁地发布版本，以便更快地把缺陷修复交付到用户手中，而不是等到计划中的下一次发布才一次性推出。 OpenSSH 是绝大多数 Linux、BSD 以及嵌入式系统上默认的远程访问实现，因此无论是侧信道漏洞的修复，还是 macOS 沙箱支持的取消，都会影响极其庞大的装机量。发布说明中因应 AI 辅助漏洞发现而转向更频繁发版的表态，也为关键开源项目今后如何处理协同披露释放了一个值得关注的政策信号。 “Crossing The Streams”之所以引人注目，是因为它依赖的是不同 SSH 会话之间共享的压缩状态，而非直接攻破加密本身，因此它属于信息泄露类缺陷，而不是密码学意义上的机密性失效。在 macOS 上，被移除的沙箱是一种需要主动启用、由 API 驱动的机制，因此失去它意味着 sshd 无法再通过该途径限制自身的资源访问。

hackernews · torcete · 10月6日 20:41 · [社区讨论](https://news.ycombinator.com/item?id=49983791)

**背景**: 压缩侧信道攻击并不攻破加密算法本身，而是通过观察被压缩并加密后的响应长度来还原秘密数据——针对 TLS 的经典 CRIME 与 BREACH 攻击正是这一原理，而 SSH 的可选压缩在共享固定状态的密钥数据时会产生类似风险。macOS 的应用沙箱是一套由内核强制执行、需要进程主动进入的访问控制技术（与 iOS 不同），通常通过 Apple 的 Seatbelt API 实现。此外，OpenSSH 的发布说明也反映出整个行业的一个趋势：AI 工具正在加速漏洞发现，其速度已超出传统披露时间线所能承受的范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.encryptionconsulting.com/compression-side-channel-attacks/">Securing Against Compression Side-Channel Attacks</a></li>
<li><a href="https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox">Configuring the macOS App Sandbox - Apple Developer</a></li>
<li><a href="https://www.tenable.com/blog/why-the-approaching-flood-of-vulnerabilities-changes-everything-and-what-to-do-about-it">How AI-driven vulnerability discovery changes everything ...</a></li>

</ul>
</details>

**社区讨论**: 评论的焦点大致集中在三点：tptacek 认为本次最值得关注的是“Crossing The Streams”压缩侧信道的缓解措施，并附上了相关论文链接；FloatArtifact 引用了发布说明中的理由，即由 AI 发现的漏洞正越来越多地被他人独立复现，因此团队决定加快发版节奏。davb 分享了一次非常正面的维护者响应经历——一个非安全性的客户端缺陷在一天内就得到修复；ilaksh 则看到捐赠链接后，对项目的资金状况表示好奇。

**标签**: `#OpenSSH`, `#Security`, `#Side-Channel Attacks`, `#Open Source`, `#Release Notes`

---

<a id="item-14"></a>
## [多伦多 VPN 服务商因合法访问法案计划撤离加拿大](https://citizenlab.ca/toronto-based-vpn-provider-plans-to-quit-canada-over-lawful-access-bill/) ⭐️ 7.0/10

根据 Citizen Lab 发布的一篇文章，一家总部位于多伦多的 VPN 服务商宣布，计划因加拿大的合法访问法案而撤离该国。这一消息在 Hacker News 上引发了一场包含 47 条评论的讨论，焦点是此举对 VPN 服务、加密服务商以及位于加拿大的开源项目意味着什么。 这一决定把长期存在的隐私政策争论变成了具体的商业结果，表明合法访问立法可能直接把安全和加密公司赶出某个司法辖区。这也给使用加拿大境内托管服务的用户，以及在加拿大设有法律实体、治理结构集中的开源项目，带来了令人不安的问题。 该消息没有披露这家服务商的名称、迁往的目的地国家或搬迁时间表，Citizen Lab 的那篇文章是这一说法的主要来源。相关立法涉及“合法访问”，即执法机关和情报机构获取电子服务提供商所掌握信息的权力，加拿大议会文件中也列有一项名为《关于合法访问的法案》。

hackernews · speckx · 10月6日 18:52 · [社区讨论](https://news.ycombinator.com/item?id=49982471)

**背景**: 加拿大围绕合法访问立法的争论已持续多年；此类法案旨在让执法机关和加拿大安全情报局能够从电子服务提供商处获取数据，某些版本还要求具备拦截能力。争议焦点是加密后门，也就是绕过正常认证或加密的故意弱点，因为为警方打造的能力同样可能被犯罪分子或外国政府滥用，1993 年美国失败的 Clipper 芯片计划就是先例。VPN 服务商尤其敏感，因为其核心产品正是加密流量和隐藏的 IP 地址，这与强制拦截要求直接冲突。开源治理在这里同样重要：治理集中、法律实体设在加拿大的项目，可能比镜像广泛分散的项目更容易受到强制命令的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lawful_Access_Act">Lawful Access Act - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Encryption_backdoor">Encryption backdoor</a></li>
<li><a href="https://www.parl.ca/DocumentViewer/en/45-1/bill/C-22/first-reading">Government Bill (House of Commons) C-22 (45-1) - First ...</a></li>

</ul>
</details>

**社区讨论**: 评论者的关注点并不在这家 VPN 服务商本身，而更多担心 OpenBSD：这个项目位于加拿大，其集中的治理结构在他们看来可能使其成为被强制分发带后门镜像或更新的目标，不过分布式镜像也许能降低这种风险。还有人质疑，在其他国家可能出台类似法律的情况下，企业迁往何处才能真正安心，也有人好奇 Tailscale 会受此类规定怎样的影响，另有一位评论者指出，该法案可能已被修订，以明确不要求设置加密后门。

**标签**: `#privacy`, `#encryption`, `#policy/legislation`, `#VPN`, `#open-source-governance`

---

<a id="item-15"></a>
## [FastVideo 的 FastH3 视频模型现已可在单台消费级显卡上运行](https://www.reddit.com/r/StableDiffusion/comments/1wzi858/fastvideos_fasth3_now_runs_on_a_single_consumer/) ⭐️ 7.0/10

FastVideo 发布了 FastH3 的优化版本，这是一个基于 MiniMax-H3 蒸馏而来的文生视频加音频（T2VA）模型，如今可以在单台消费级设备上运行。此次发布同时提供了 Hugging Face 上的开放权重（FastVideo-FastH3-Trim-Comfy）、FastVideo 官网的 cookbook 教程、hao-ai-lab/FastVideo 的 GitHub 仓库，以及 ComfyUI 集成支持。 让高质量的视频加音频生成模型在消费级硬件上运行，降低了买不起多卡集群的爱好者和中小工作室的入门门槛。这也表明少步蒸馏加稀疏注意力优化，正在成为让大型视频扩散模型能在边缘设备部署的标准路径。 FastH3 提供 4 步和 8 步两种版本，其中 8 步检查点通过 8 次 transformer 前向即可生成同步的视频与音频，采用了无需数据的 DMD2 蒸馏以及在 80% 稀疏度下的 VSA-H3 稀疏注意力。这些检查点需要 FastVideo 的 VSA-H3 注意力后端支持，而 MiniMax-H3 还可以选择使用 FlashAttention 4 的 packed-varlen 入口来处理其超长的单序列稠密 DiT 自注意力。

reddit · r/StableDiffusion · /u/fruesome · 10月7日 00:01

**背景**: FastH3 是 MiniMax-H3 的少步蒸馏预览版，而 MiniMax-H3 是一个能够根据文本提示同时生成视频与音频的扩散 Transformer。步数蒸馏把扩散模型通常需要的多次去噪过程压缩到仅几步，这正是让消费级显卡推理变得可行的关键。FastVideo 是一个面向加速视频生成的统一推理与后训练框架，而 ComfyUI 则是广受欢迎的开源节点式界面，用于在本地运行扩散模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://haoailab.com/FastVideo/">FastVideo - haoailab.com</a></li>
<li><a href="https://huggingface.co/FastVideo/FastVideo-FastH3-8-Step-V2">FastVideo-FastH3-8-Step-V2 - Hugging Face</a></li>
<li><a href="https://github.com/hao-ai-lab/FastVideo">GitHub - hao-ai-lab/FastVideo: A unified inference and post ...</a></li>

</ul>
</details>

**标签**: `#video-generation`, `#diffusion-models`, `#model-optimization`, `#comfyui`, `#consumer-gpu-inference`

---

<a id="item-16"></a>
## [欧盟《人工智能法案》将于 12 月 2 日起禁止“脱衣”类 AI 工具](https://www.reddit.com/r/StableDiffusion/comments/1wzfp7m/eu_nudifier_ban/) ⭐️ 7.0/10

根据 Stable Diffusion 社区中一篇被广泛讨论的帖子，自 12 月 2 日起，欧盟《人工智能法案》将禁止“脱衣”（nudify）类工具，使其在欧盟境内成为非法内容。该禁令适用于任何投放欧盟市场、其主要功能是生成未经同意的裸露图像的产品；同时《数字服务法案》将义务扩展至中介方，包括应用商店、托管服务商、域名注册商、支付处理商、CDN 和云服务，罚款最高可达 3500 万欧元或全球营业额的 7%（取较高者）。 该措施把执法重点从单个网站转向支撑它们的整条基础设施链条，意味着谷歌、亚马逊、Cloudflare、苹果、Telegram、GoDaddy、Visa 和万事达等主流服务商都将面临切实的合规压力。对生成式 AI 社区而言，这也提出了一个棘手问题：开源图像模型及其之上的衍生服务要如何在欧盟境内分发。 据称该禁令的适用情形有两种：一是生成未经同意的裸露内容是产品的主要功能；二是这属于可合理预见的结果而提供方未采取适当防护措施。帖文并未给出 12 月 2 日这一日期或具体法律范围的原始出处，因此在据以行动之前，应核对欧盟官方文本以确认具体条款与适用年份。

reddit · r/StableDiffusion · /u/Logical_Benefit2875 · 10月6日 22:04

**背景**: Stable Diffusion 是 2022 年发布的开源潜在扩散文本生成图像模型，其公开权重可在消费级显卡上运行，由此催生了庞大的微调图像与视频工具生态。其中一些工具被改造成“脱衣”类应用，利用图生图和局部重绘（inpainting）技术生成未经同意的私密图像；帖文也提到 Motionmuse、Opengoon 等网站近期被关停。欧盟《人工智能法案》是欧盟基于风险分级管理 AI 系统的法规，而《数字服务法案》则对在线中介平台施加尽职调查与下架义务——两者结合，使监管机构能够针对托管、资助或分发这类工具的平台采取行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stable_Diffusion">Stable Diffusion</a></li>
<li><a href="https://grokipedia.com/page/Stable_Diffusion">Stable Diffusion</a></li>

</ul>
</details>

**标签**: `#EU AI Act`, `#AI regulation`, `#generative AI`, `#content moderation`, `#Stable Diffusion`

---

<a id="item-17"></a>
## [TII 发布 Falcon-Emirati：面向阿联酋方言与文化的定制大模型](https://huggingface.co/blog/tiiuae/falcon-emirati) ⭐️ 6.0/10

技术创新研究院（TII）在 Hugging Face 上发布了 Falcon-Emirati，这是其 Falcon 大语言模型的一个专门微调版本，用于理解阿联酋阿拉伯语方言、当地文化以及日常对话中的细微含义。与大多数依赖现代标准阿拉伯语的阿拉伯语模型不同，此次发布瞄准的是阿联酋本地人日常口语的实际表达方式。 大多数大语言模型的能力都集中在少数高资源语言上，像阿联酋阿拉伯语这样的地区方言长期得不到良好支持；为一个方言专门打造模型，说明文化和语言的本地化可以下沉到次国家层面。这对面向海湾地区的客服、政府聊天机器人和本地化工具等应用具有实际意义，也为阿拉伯语 NLP 研究者提供了在一个主流模型家族内部做方言适配的具体范例。 Falcon-Emirati 通过 Hugging Face 分发，是在 Falcon 家族基础上微调而成，而非从头预训练的模型，因此它在阿联酋方言上的表现很大程度上取决于微调所用方言数据的质量与规模。阿联酋阿拉伯语在词汇、发音和习语上与现代标准阿拉伯语差异明显，这意味着该模型的优势很可能仅限于阿联酋语境下的对话，未必能迁移到其他阿拉伯语方言。

rss · Hugging Face Blog · 10月6日 06:44

**背景**: 阿拉伯语是一种“双言制”语言：现代标准阿拉伯语（MSA）是新闻和官方文件使用的正式书面语，而日常交流则使用阿联酋、埃及、黎凡特等地区方言，这些方言之间往往无法互通。大语言模型的训练数据以高资源语言和正式文本为主，因此对现代标准阿拉伯语的处理能力远好于口语方言。方言适配研究——例如对法语、英语方言采用的持续预训练或语言学规则动态聚合方法——正是希望用较少量低资源方言数据来缩小这一差距。Falcon 是 TII 在阿布扎比开发的开源大模型家族，被定位为面向主权需求的开放替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://falconllm.tii.ae/">Introducing the Technology Innovation Institute’s Falcon Perception...</a></li>
<li><a href="https://alramsa.ae/alramsa-faqs/">How to Learn Emirati Arabic - Al Ramsa FAQs</a></li>
<li><a href="https://arxiv.org/html/2510.22747v2">Low-Resource Dialect Adaptation of Large Language Models ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Arabic NLP`, `#Falcon`, `#Dialect Adaptation`, `#Cultural Alignment`

---

<a id="item-18"></a>
## [OmniChar 的 ComfyUI 工作流为 .char 角色加入一致克隆语音与口型同步](https://www.reddit.com/r/StableDiffusion/comments/1wz42o6/omni_charsame_face_cloths_body_now_with/) ⭐️ 6.0/10

一位 Reddit 创作者宣布，其 OmniChar 的 ComfyUI 工作流此前已能保证角色面部、服装和身体在多轮生成中保持一致，如今只需提供 10 至 30 秒的 mp3 或 wav 语音样本，就能在多段视频生成中实现一致的语音克隆与口型同步。该 ComfyUI 节点已更新，新增可选的语音样本输入，并同步发布了示例工作流（“Build a .char with a voice”“MiniMax H3 with voice”）。 语音一致性一直是 AI 角色流水线中最后缺失的环节之一：即便面部和服装在多段视频里保持稳定，声音一变，角色的整体感就会崩塌。将语音克隆打包进 ComfyUI 中可移植的 .char 格式，使 Stable Diffusion 与 AI 视频创作者拥有了可复用、可分享的角色资产，它有可能演变为跨模型的事实互操作标准。 口型同步并非额外叠加的模块，而是由 MiniMax H3 视频模型自身生成；语音克隆在英语上表现良好，但在非英语语言中可能“胡言乱语”，同时应避免在样本中出现多个说话人的声音。该 ComfyUI 节点目前仍属 nightly 版本，用户需要调整更新设置或直接通过 Git 仓库地址安装；底层 OmniChar 仓库采用 GPLv3 许可，除了支持 krea2 的 .char 外，还提供角色微调等功能。

reddit · r/StableDiffusion · /u/ashishsanu · 10月6日 14:29

**背景**: ComfyUI 是一个开源、基于节点的图形界面，用于搭建扩散模型工作流，可生成图像、视频、音频和 3D 资产。OmniChar 是一种开放的 .char 格式，旨在承载单一角色（包括身份、身体、服装，如今还有声音），使同一文件可以被不同工具和模型加载。MiniMax 是一家总部位于上海的多模态 AI 公司，旗下拥有 Hailuo AI 视频服务以及 MiniMax H3 视频生成模型，本次演示正是用它来生成会说话的角色视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/omnichar/OmniChar">GitHub - omnichar / OmniChar : The open . char format for characters.</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_Group">MiniMax Group</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#ComfyUI`, `#Character Consistency`, `#Voice Cloning`, `#AI Video Generation`

---

<a id="item-19"></a>
## [Forge Neo 扩展让 MiniMax H3 在 16 GB 显存上生成带声音的视频](https://www.reddit.com/r/StableDiffusion/comments/1wz6ulh/i_made_a_forge_neo_extension_for_minimax_h3_text/) ⭐️ 6.0/10

开发者 eduardoabreu81 发布了一个 Forge Neo 扩展 "minimax-h3-forge-neo"，可在 Forge Neo 常规的 txt2img 和 img2img 标签页中运行 MiniMax H3，一次性生成画面与同步立体声，并把 MP4 直接输出到常规结果区。它支持最长 15 秒、24 fps 的文生视频，首帧/尾帧条件控制，最多 9 张参考图（Ref2VA），以及包括 8 步 turbo LoRA 在内的多种 LoRA，且无需修改任何 Forge Neo 文件、也无需额外安装 Python 包。 MiniMax H3 是一个能同时生成视频与原生音频的开放多模态模型，但运行它通常需要另一套繁重流程；该扩展把它并入广泛使用的 Stable Diffusion WebUI Forge/Forge Neo 工作流，让爱好者沿用熟悉的 checkpoint 列表、VAE/文本编码器选择和 Generate 按钮。使其能塞进 16 GB 显卡的显存优化，也切实降低了本地生成“带声音视频”的硬件门槛。 作者在 A40（48 GB）、RTX 4090（24 GB）和 RTX 2000 Ada（16 GB）上做了测试：A40 上 5 秒 960×544 片段在 20 步时约需 3 分钟，使用 turbo LoRA 约 1 分钟，而在所测的 16 GB 显卡上 8 秒片段耗时 27 分钟。系统内存与显存同样重要（使用较小量化文件约需 32 GB，使用 INT8 权重集约需 50 GB），低于 16 GB 的显卡尚未测试，并且需要较新的 Forge Neo（2026 年 10 月 3 日及之后的 neo 分支）。后续计划包括支持视频与音频作为参考，以及姿态、深度和边缘控制。

reddit · r/StableDiffusion · /u/digitalhunters0 · 10月6日 16:19

**背景**: MiniMax H3（又称 Hailuo 3）是一个开放的通用多模态生成模型，能产出带原生口型同步音频的短视频——脚步声、雨声、引擎声、音乐和对白——而非无声视频。Forge Neo 是 Stable Diffusion WebUI Forge 的分支（后者又构建于 Automatic1111 的 WebUI 之上），侧重于资源管理与更快的推理速度，并支持庞大的扩展生态。要在消费级硬件上运行这类模型，通常依赖 W4A8（4 位权重、8 位激活）等量化技术、GGUF 文件以及 INT4 文本编码器，用少量质量换取大幅降低的显存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://theagenttimes.com/articles/w4a8-quantized-minimax-h3-cuts-video-generation-time-5x-on-8-74a53bea">W 4 A 8 Quantized MiniMax-H3 Cuts Video Generation Time 5x on 8GB...</a></li>
<li><a href="https://grokipedia.com/page/Stable_Diffusion_WebUI_Forge">Stable Diffusion WebUI Forge — Grokipedia</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#video generation`, `#MiniMax H3`, `#Forge Neo`, `#generative AI`

---

<a id="item-20"></a>
## [Claude 写剧本，MiniMax H3 与 ComfyUI 渲染 25 个场景的 AI 喜剧短片](https://www.reddit.com/r/StableDiffusion/comments/1wz82c3/and_how_does_that_make_you_feel_an_ai_short/) ⭐️ 6.0/10

Reddit 用户 r/StableDiffusion 上的一位作者展示了一套高度自主的 AI 电影制作流程：Claude 独立完成了故事、五个角色、全部对白以及 25 个场景的剧本，拍出一部 3 分钟的心理医生诊室喜剧；MiniMax H3（Singularity ref2va v1.3 加 8-step 768p turbo LoRA）配合 ComfyUI 视频构建器渲染了所有场景，并自带语音与音效，总渲染时间约 6.3 小时。人类只提供了一段简短的提示词，并在中途对某个不听话的场景做了一次干预。 它说明具备代理能力的 LLM 工作流正与开源视频生成模型融合，把编剧、选角、配音、音效、配乐和质检等整支剧组的工作压缩进一条自动化流水线，这一趋势正在重塑个人创作者和小型工作室的产能边界。对 Stable Diffusion 与 ComfyUI 社区而言，这是一个可复现的具体案例，说明节点图已从单次出图工具演变为真正的生产基础设施。 角色先用 Z-Image（Turbo）生成三视图参考表；H3 采用两遍工作流——先跑 Singularity 模型，第二遍使用 8-step LoRA、4 步、0.35 降噪——并在每个场景中逐字复用同一段角色声音描述，以保证 H3 原生语音的一致性。质检也大幅自动化：用 Whisper 将音频与剧本比对，逐角色检查音高与音色，失败镜头重拍，配乐由 MiniMax Music 3 生成，最终母带归一化到 -14 LUFS，音画同步最差偏差仅 5 毫秒。

reddit · r/StableDiffusion · /u/Cheap_Credit_3957 · 10月6日 17:06

**背景**: MiniMax H3 是一个开放的通用全模态生成模型，可统一理解文本、图像、视频与音频，并在同一次生成中输出原生同步立体声，API 支持最长 15 秒、最高 2K，开源权重在短边原生生成 768p。ComfyUI 是面向生成式 AI 流水线的开源节点式可视化图编辑与执行后端，让创作者能把 H3、Z-Image、Whisper 等模型串联成一套自动化工作流。Z-Image 是为高质量生成和强角色一致性设计的图像基础模型（并有 Turbo 版本），这正是它被用来生成演员参考表的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://design.minimax.io/h3">MiniMax H3 Open: Tutorials, Deployment & Workflows</a></li>
<li><a href="https://github.com/Tongyi-MAI/Z-Image">GitHub - Tongyi-MAI/Z-Image</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#ComfyUI`, `#MiniMax H3`, `#agentic workflows`, `#generative AI filmmaking`

---

<a id="item-21"></a>
## [MiniMax H3 ref2va：在 ComfyUI 中排查动漫视频画质忽好忽坏](https://www.reddit.com/r/StableDiffusion/comments/1wz2ys3/minimax_h3_ref2va_whats_the_next_lever_for_quality/) ⭐️ 6.0/10

一位 Reddit 用户在 r/StableDiffusion 上公开了自己用 MiniMax H3（ref2va）生成 15 秒动漫打斗短片的完整 ComfyUI 工作流，并就下一步该优先调整哪个画质变量寻求建议。其配置包括 int8 基础模型 `minimax_h3_fl2va_int8_convrot.safetensors`、Spectrum v0.2.16、30 步采样与 `res_multistep`/`simple` 采样器、8 张各有明确分工的参考图，以及从 1344×768 经 `MinimaxH3LatentUpscaler3D` 放大到 1920×1088（2 MP、4 步、0.5 去噪）。 这篇帖子是一份少见的、可复现的实战报告，指出了用 MiniMax H3 生成长篇动漫内容时画质究竟在哪里出问题，涵盖同一片段内各镜头画质不一致、地面打击缺乏重量感，以及参考图数量是否过多等疑问。其中的实用结论——例如在提示开头加上“The target video is 2d colored anime.”可防止画面漂移成 3D，以及加快剪切节奏能显著改善打斗的可读性——对所有做多镜头视频扩散的人都直接有用。同时它也揭示了成本现实：在 RTX PRO 6000 上，每 15 秒片段大约需要 28 分钟渲染。 该片段为 362 帧、24fps，一次性生成、未做剪辑，所有切换都写在提示词里；作者表示把 15 秒内的镜头从 4 个增加到 8 个（每段约 1.8 秒），并配合冲击动词和每次击打的物质后果，打斗的观感明显更好。尚未解决的问题有两类：一是低位击打的动作偏软，因此他在考虑 derope 或时间维度上采样是否值得付出生成时开销；二是同一段 15 秒内各镜头质量不均，有些是干净的赛璐璐风格，有些则发软、有塑料感——这可能与 8 张参考图的设置有关，也可能是社区常说的“超过 10 秒就会崩坏”的现象。

reddit · r/StableDiffusion · /u/lajonquillebleu · 10月6日 13:43

**背景**: MiniMax H3 是 MiniMax 推出的视频生成模型系列，其公开权重支持 FL2VA（首尾帧到带音频视频）和 Ref2VA（参考图到视频）等模式，其中参考图可用来控制人物身份、姿态、场景与构图。ComfyUI 是一个开源、基于节点的扩散模型工作流界面，用户把模型、采样器、放大器与自定义节点连成一张图来运行。像 MinimaxH3LatentUpscaler3D 这样的潜空间放大器会在两次采样之间对潜变量重新加噪并放大，从而先用较低分辨率生成、再放大收尾，避免全程承担高分辨率的算力成本。参考图条件在这里很关键，因为该工作流给 8 张图各自指定了明确角色（脸、愤怒表情、打斗姿态、场景、构图参照）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MiniMax-AI/MiniMax-H3/tree/main/Ref2VA">MiniMax-H3/Ref2VA at main · MiniMax-AI/MiniMax-H3 · GitHub</a></li>
<li><a href="https://minimax3.org/minimax-h3-video-model">MiniMax H3 Model Card – Architecture, FL2VA, Ref2VA & 2K Pipeline</a></li>
<li><a href="https://github.com/Tr1dae/ComfyUI-MiniMaxH3_LatentUpscaler">GitHub - Tr1dae/ComfyUI- MiniMaxH 3 _ LatentUpscaler ...</a></li>

</ul>
</details>

**标签**: `#Stable Diffusion`, `#MiniMax H3`, `#ComfyUI`, `#AI video generation`, `#anime generation`

---

