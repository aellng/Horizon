# Horizon 每日速递 - 2026-06-29

> 从 37 条内容中筛选出 12 条重要资讯。

---

## 今日结论

今天最值得继续跟进的信号集中在：AI、LLM、healthcare、Hiring、benchmark。

面向 AI 自媒体创作，可以优先关注以下 3 个方向：
1. **[GLM 5.2 在安全基准测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/)**
2. **[用 Claude Code 获取 MRI 第二意见](https://antoine.fi/mri-analysis-using-claude-code-opus)**
3. **[HackerRank 开源 ATS 揭示简历评分不一致](https://danunparsed.com/p/hackerrank-open-source-ats)**

---
## A 股影响参考

> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。

### 1. AI Agent 与办公软件

- **关联热点**: [GLM 5.2 在安全基准测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/)
- **可能影响**: 企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。
- **示例股票**: 金山办公（688111.SH）、科大讯飞（002230.SZ）

### 2. AI 安全与软件治理

- **关联热点**: [GLM 5.2 在安全基准测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/)
- **可能影响**: Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。
- **示例股票**: 奇安信（688561.SH）、启明星辰（002439.SZ）

### 3. 算力芯片与服务器

- **关联热点**: [HackerRank 开源 ATS 揭示简历评分不一致](https://danunparsed.com/p/hackerrank-open-source-ats)
- **可能影响**: 本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。
- **示例股票**: 寒武纪（688256.SH）、浪潮信息（000977.SZ）、中科曙光（603019.SH）

---

## 最值得发的 3 个选题

### 选题 1：GLM 5.2 在安全基准测试中超越 Claude

**关联新闻**: [GLM 5.2 在安全基准测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/)

**切入角度**: Z.ai 的开源模型 GLM 5.2 在 Semgrep 的网络安全基准测试中取得了与 Anthropic 的 Claude 相竞争的性能，社区报告强调其在日常编程和安全漏洞挖掘中的有效性。 这表明开源模型在安全等专业领域可以媲美专有前沿模型，有望降低开发者和企业的成本并提高可及性。 该基准测试检验模型是否能发现 Mythos 发现的漏洞；一位评论者指出 GLM 5.2 表现不错，但并非最佳开源模型，DeepSeek V4 Pro 和 MiMo 2.5 Pro 最初表现更好。GLM 5.2 以 MIT 许可协议发布，可在 Hugging Face 上获取。

**可延展方向**: GLM 是由中国 AI 公司 Z.ai（原智谱 AI）开发的一系列大语言模型，该公司被认为是中国的‘AI 四小龙’之一，于 2025 年 1 月被美国商务部列入实体清单。Claude 是 Anthropic 公司的 LLM 系列，以注重安全训练著称。开源模型在各类基准测试中正日益挑战专有模型。

---

### 选题 2：用 Claude Code 获取 MRI 第二意见

**关联新闻**: [用 Claude Code 获取 MRI 第二意见](https://antoine.fi/mri-analysis-using-claude-code-opus)

**切入角度**: 一名用户将肩部 MRI 上传到 Claude Code（由 Claude Opus 驱动），并提示 AI 分析图像，获得了与原始放射科医生报告相矛盾、后来与临床结果一致的第二意见。 这一实验展示了使用通用大语言模型进行医疗诊断的潜力和风险，引发了关于 AI 可靠性、信任度以及医患关系在医疗保健中的关键问题。 该分析使用了 Claude Code（一种非为医学影像设计的代理编码工具），并且仅依赖几张静态图像而非完整的 3D MRI 数据集，放射科医生认为这不足以进行可靠解读。

**可延展方向**: Claude Code 是 Anthropic 开发的一种代理编码系统，通过自然语言编辑代码和运行命令；它并非医疗诊断工具。医学影像解读通常需要基于大量标记数据集训练的专业 AI 模型，而像 Claude 这样的通用大语言模型缺乏这一点。用户的实验凸显了随意使用 AI 与经过验证的临床工具之间的差距。

---

### 选题 3：HackerRank 开源 ATS 揭示简历评分不一致

**关联新闻**: [HackerRank 开源 ATS 揭示简历评分不一致](https://danunparsed.com/p/hackerrank-open-source-ats)

**切入角度**: HackerRank 将其使用大语言模型（LLM）评分简历的应聘者跟踪系统（ATS）开源。一次深入测试显示，同一份简历在多次运行时获得不同分数，凸显了其非确定性行为。 这引发了关于 AI 驱动招聘的公平性和可靠性的严重担忧，因为不一致的分数可能导致任意筛选候选人。同时，它也引发了关于使用 LLM 进行简历筛选的合法性和伦理的讨论，特别是在欧盟等地区的反歧视法律下。 评分标准中，开源贡献占 120 分中的 35 分，而技术技能仅占 10 分。作者将同一份简历在 ATS 上运行 100 次，观察到分数变化（例如 90、74、88）。

**可延展方向**: 应聘者跟踪系统（ATS）被雇主用于筛选简历。HackerRank 的开源 ATS 使用 LLM 基于标准对简历进行评估。然而，LLM 具有随机性，即使是相同输入也可能产生不同输出，导致评分非确定。最近的研究记录了基于 LLM 的简历筛选中的偏见问题。

---

1. [年龄验证是走向自动言论归因的一步](#item-1) ⭐️ 9.0/10
2. [Tidal 发布 AI 音乐政策，要求更高标准](#item-2) ⭐️ 8.0/10
3. [HackerRank 开源 ATS 揭示简历评分不一致](#item-3) ⭐️ 8.0/10
4. [GLM 5.2 在安全基准测试中超越 Claude](#item-4) ⭐️ 8.0/10
5. [Pollen CEO 通过伪造 DMCA 通知删除批评文章，谷歌协助](#item-5) ⭐️ 8.0/10
6. [用 Claude Code 获取 MRI 第二意见](#item-6) ⭐️ 8.0/10
7. [黑盒大语言模型的知识蒸馏](#item-7) ⭐️ 8.0/10
8. [Sandia SA3000：用于国防的耐辐射 Intel 8085](#item-8) ⭐️ 7.0/10
9. [逆向工程苹果稀疏映像格式（ASIF）](#item-9) ⭐️ 7.0/10
10. [1960-2026 内存价格历史可视化](#item-10) ⭐️ 7.0/10
11. [Tokenmaxxing 已死，Tokenmaxxing 万岁](#item-11) ⭐️ 7.0/10
12. [可视化纽约公共图书馆 5000 份历史菜单（1880-1920）](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [年龄验证是走向自动言论归因的一步](https://nonogra.ph/age-verification-is-just-a-precursor-to-attribution-of-speech-06-29-2026) ⭐️ 9.0/10

一篇批评性文章指出，年龄验证法律旨在演变为政府控制的身份归因系统，用于所有在线言论，而不仅仅是年龄检查。 如果实施，这种归因可能导致普遍的监控和对言论自由的寒蝉效应，因为每条在线言论都将与真实身份永久关联。 文章和评论者指出，设备认证和强制身份链接的操作系统是同一趋势的一部分，并警告当前欧盟系统可能尚未要求物理身份，但这一趋势令人担忧。

hackernews · arkhiver · 6月29日 03:42 · [社区讨论](https://news.ycombinator.com/item?id=48714529)

**背景**: 年龄验证法律旨在限制未成年人访问某些在线内容，但批评者认为这需要将数字账户与现实身份绑定。自动言论归因是指利用语言模式或元数据识别说话者，一旦身份确立，即可追溯应用到过去的言论上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.54/134148/The-Impact-of-Automatic-Speech-Transcription-on">The Impact of Automatic Speech Transcription on Speaker Attribution | Transactions of the Association for Computational Linguistics | MIT Press</a></li>
<li><a href="https://arxiv.org/abs/2507.08660">[2507.08660] The Impact of Automatic Speech Transcription on Speaker Attribution</a></li>
<li><a href="https://flashpoint.io/blog/guide-to-managed-attribution/">Protecting Your Organization's Digital Identity: A Guide to Managed Attribution | Flashpoint</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意这一批评，有人对比了欧盟保护隐私的年龄证明系统与滑坡论证。其他人强调设备认证和政府批准的操作系统是走向许可制互联网的进一步步骤。

**标签**: `#age verification`, `#privacy`, `#internet governance`, `#identity attribution`, `#surveillance`

---

<a id="item-2"></a>
## [Tidal 发布 AI 音乐政策，要求更高标准](https://tidal.com/ai-policy) ⭐️ 8.0/10

Tidal 宣布将接受 AI 生成的音乐，但会执行更高标准以防止剥削和欺骗听众。 这项政策为大型流媒体平台如何在接纳 AI 内容与保护内容完整性之间取得平衡树立了先例，影响艺术家、企业和听众。 该政策明确禁止 AI 生成的音乐利用个人或团体的音乐、姓名或肖像，欺骗听众或降低服务质量。它不允许用户选择退出 AI 音乐。

hackernews · hn8726 · 6月29日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=48718840)

**背景**: AI 生成的音乐变得越来越普遍，引发了关于版权侵权和真实性的担忧。像 Tidal 这样的流媒体平台正在努力处理这些新内容，同时保持信任和质量。

**社区讨论**: 评论者普遍支持这项政策，认为是一个合理的方法，但有些人对 AI 音乐在小企业中的普及表示不满，并希望有选择退出的功能。一位用户强调了 Tidal 的技术问题和裁员，而另一位用户则希望有一个专门针对人类创作音乐的平台。

**标签**: `#AI`, `#music streaming`, `#policy`, `#copyright`, `#Tidal`

---

<a id="item-3"></a>
## [HackerRank 开源 ATS 揭示简历评分不一致](https://danunparsed.com/p/hackerrank-open-source-ats) ⭐️ 8.0/10

HackerRank 将其使用大语言模型（LLM）评分简历的应聘者跟踪系统（ATS）开源。一次深入测试显示，同一份简历在多次运行时获得不同分数，凸显了其非确定性行为。 这引发了关于 AI 驱动招聘的公平性和可靠性的严重担忧，因为不一致的分数可能导致任意筛选候选人。同时，它也引发了关于使用 LLM 进行简历筛选的合法性和伦理的讨论，特别是在欧盟等地区的反歧视法律下。 评分标准中，开源贡献占 120 分中的 35 分，而技术技能仅占 10 分。作者将同一份简历在 ATS 上运行 100 次，观察到分数变化（例如 90、74、88）。

hackernews · sambellll · 6月29日 01:44 · [社区讨论](https://news.ycombinator.com/item?id=48713832)

**背景**: 应聘者跟踪系统（ATS）被雇主用于筛选简历。HackerRank 的开源 ATS 使用 LLM 基于标准对简历进行评估。然而，LLM 具有随机性，即使是相同输入也可能产生不同输出，导致评分非确定。最近的研究记录了基于 LLM 的简历筛选中的偏见问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danunparsed.com/p/hackerrank-open-source-ats">HackerRank's Open-Source ATS Gave My Resume a Different Score ...</a></li>
<li><a href="https://www.brookings.edu/articles/gender-race-and-intersectional-bias-in-ai-resume-screening-via-language-model-retrieval/">Gender, race, and intersectional bias in AI resume screening via language model retrieval | Brookings</a></li>
<li><a href="https://byteiota.com/hackerrank-ats-open-source-the-hiring-rubric-inside/">HackerRank ATS Open Source: The Hiring Rubric Inside</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，非确定性源于 LLM 的随机性，这可能使该系统在欧盟反歧视法律下违法。一些人将其与旧有的‘我不雇佣不幸运的人’做法相提并论，还有人批评浪费电力，并指出其与旅游网站非确定性定价的相似性。

**标签**: `#AI`, `#Hiring`, `#LLM`, `#Bias`, `#Resume Screening`

---

<a id="item-4"></a>
## [GLM 5.2 在安全基准测试中超越 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

Z.ai 的开源模型 GLM 5.2 在 Semgrep 的网络安全基准测试中取得了与 Anthropic 的 Claude 相竞争的性能，社区报告强调其在日常编程和安全漏洞挖掘中的有效性。 这表明开源模型在安全等专业领域可以媲美专有前沿模型，有望降低开发者和企业的成本并提高可及性。 该基准测试检验模型是否能发现 Mythos 发现的漏洞；一位评论者指出 GLM 5.2 表现不错，但并非最佳开源模型，DeepSeek V4 Pro 和 MiMo 2.5 Pro 最初表现更好。GLM 5.2 以 MIT 许可协议发布，可在 Hugging Face 上获取。

hackernews · jms703 · 6月28日 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: GLM 是由中国 AI 公司 Z.ai（原智谱 AI）开发的一系列大语言模型，该公司被认为是中国的‘AI 四小龙’之一，于 2025 年 1 月被美国商务部列入实体清单。Claude 是 Anthropic 公司的 LLM 系列，以注重安全训练著称。开源模型在各类基准测试中正日益挑战专有模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/ GLM - 5 . 2 · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区讨论意见不一：一些用户称赞 GLM 5.2 是日常编程中性价比高的主力模型，而另一些用户则质疑其长期一致性不如 DeepSeek 等模型。还有猜测认为中国开源实验室可能像电动汽车一样受政府补贴以主导市场。与 Claude 订阅服务的成本比较是一个反复出现的话题。

**标签**: `#AI`, `#LLM`, `#benchmark`, `#security`, `#open-source`

---

<a id="item-5"></a>
## [Pollen CEO 通过伪造 DMCA 通知删除批评文章，谷歌协助](https://blog.pragmaticengineer.com/pollen-tried-to-remove-my-article-about-callum-negus-fancey-and-google-is-assisting-to-it/) ⭐️ 8.0/10

一篇博客文章揭露，创业公司 Pollen 的 CEO Callum Negus-Fancey 与 CTO Wright 向谷歌提交了伪造的 DMCA 删除请求，试图移除一篇批评文章，而谷歌在未充分核实的情况下予以配合。 这一事件凸显了 DMCA 删除流程被滥用于审查和声誉管理的问题，引发了关于平台责任以及要求对索赔进行核实的必要性的关键讨论。 据称，该 DMCA 索赔是虚假的，但谷歌仍将博文从搜索结果中删除，这表明平台在处理未经核实的投诉时可能无意中助长了审查。

hackernews · taubek · 6月29日 09:28 · [社区讨论](https://news.ycombinator.com/item?id=48716902)

**背景**: 《数字千年版权法》(DMCA) 为谷歌等平台提供了安全港，只要它们迅速删除被声称侵权的内容即可免责。然而，该系统容易遭受滥用，因为虚假的删除通知可以在很少核实的情况下提交，从而压制合法言论。

**社区讨论**: 评论者普遍谴责了虚假的 DMCA 索赔，指出斯特赖桑德效应使该文章获得了更多关注。部分人批评谷歌缺乏问责制，并呼吁对删除通知强制要求政府身份验证。

**标签**: `#DMCA`, `#censorship`, `#Google`, `#reputation management`, `#tech policy`

---

<a id="item-6"></a>
## [用 Claude Code 获取 MRI 第二意见](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

一名用户将肩部 MRI 上传到 Claude Code（由 Claude Opus 驱动），并提示 AI 分析图像，获得了与原始放射科医生报告相矛盾、后来与临床结果一致的第二意见。 这一实验展示了使用通用大语言模型进行医疗诊断的潜力和风险，引发了关于 AI 可靠性、信任度以及医患关系在医疗保健中的关键问题。 该分析使用了 Claude Code（一种非为医学影像设计的代理编码工具），并且仅依赖几张静态图像而非完整的 3D MRI 数据集，放射科医生认为这不足以进行可靠解读。

hackernews · engmarketer · 6月28日 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude Code 是 Anthropic 开发的一种代理编码系统，通过自然语言编辑代码和运行命令；它并非医疗诊断工具。医学影像解读通常需要基于大量标记数据集训练的专业 AI 模型，而像 Claude 这样的通用大语言模型缺乏这一点。用户的实验凸显了随意使用 AI 与经过验证的临床工具之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic ...</a></li>

</ul>
</details>

**社区讨论**: 讨论中的放射科医生警告说，由于训练数据有限且使用的是二维快照而非完整三维扫描，AI 的分析不可靠。其他人分享了误诊的个人经历，并表示虽然 AI 可以提供低压力的提问方式，但它无法取代对人类专家的信任。

**标签**: `#AI`, `#healthcare`, `#medical imaging`, `#trust`, `#Claude`

---

<a id="item-7"></a>
## [黑盒大语言模型的知识蒸馏](https://arxiv.org/abs/2401.07013) ⭐️ 8.0/10

一篇 2024 年的综述论文全面回顾了黑盒大语言模型的知识蒸馏技术，其中教师模型的内部结构不可访问。 这项工作很重要，因为它解决了在无法访问参数或嵌入的情况下，将 GPT-4 等专有 LLM 压缩成更小模型的挑战，从而促进更广泛的部署和研究。 该论文聚焦于黑盒蒸馏，即仅能获取教师模型的输出概率或 logits，与白盒方法形成对比。社区讨论提到一篇 2026 年的后续工作，通过生成对抗蒸馏（GAD）在 Qwen 2.5 14B 模型上实现了“GPT-5 级别”性能。

hackernews · babelfish · 6月28日 22:32 · [社区讨论](https://news.ycombinator.com/item?id=48712420)

**背景**: 知识蒸馏是一种模型压缩技术，其中较小的“学生”模型学习模仿较大的“教师”模型。对于大语言模型，传统蒸馏通常需要访问教师模型的内部表示（白盒），而黑盒蒸馏仅使用教师模型的输出，适用于 GPT-4 等专有模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.roboflow.com/what-is-knowledge-distillation/">What is Knowledge Distillation ? A Deep Dive. | Roboflow Blog</a></li>
<li><a href="https://arxiv.org/abs/2402.08219">[2402.08219] BBox-Adapter: Lightweight Adapting for Black-Box Large Language Models</a></li>
<li><a href="https://promptengineering.org/the-black-box-problem-opaque-inner-workings-of-large-language-models/">The Black Box Problem: Opaque Inner Workings of Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 评论者 potus_kushner 指出一篇 2026 年的黑盒策略蒸馏论文，通过生成对抗蒸馏（GAD）方法在 Qwen 2.5 14B 模型上实现了接近 GPT-5 级别的性能。另一位评论者质疑 DPO 相对于纯监督微调的必要性，还有一位评论者引用了关于预训练紧凑模型的相关论文。

**标签**: `#knowledge distillation`, `#large language models`, `#black-box`, `#AI research`

---

<a id="item-8"></a>
## [Sandia SA3000：用于国防的耐辐射 Intel 8085](https://www.cpushack.com/2026/06/03/sandia-national-labs-sa3000-8085-cpu/) ⭐️ 7.0/10

文章详细介绍了 Sandia SA3000，这是 Intel 8085 CPU 的耐辐射版本，专为关键防御系统开发，能够在高辐射剂量下以最小的性能下降幸存。 这次深入探讨揭示了早期耐辐射处理器背后的工程，这些处理器对航空航天和军事应用仍然至关重要，并引发了对历史和现代耐辐射设计的讨论。 SA3000 使用 n-on-n+外延衬底和防护环来防止闩锁效应，能够承受 1×10^6 rad 辐射，性能仅下降 25%。但一些社区成员质疑数据的准确性，认为它是从 1979 年的 DTIC 文档中复制粘贴的。

hackernews · rbanffy · 6月29日 10:20 · [社区讨论](https://news.ycombinator.com/item?id=48717287)

**背景**: 耐辐射电子设备旨在承受高水平的电离辐射，常见于太空和核环境。SA3000 是 Intel 8085 的耐辐射版本，8085 是 20 世纪 70 年代末的 8 位微处理器，用于导弹和卫星等对辐射下可靠性要求极高的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Radiation_hardening">Radiation hardening - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了现代耐辐射 CPU（如使用 IBM POWER 架构的 MOOG BRE440 和 BAE RAD5500）的背景。一位评论者开玩笑地将 SA3000 的性能与 TRS-80 相提并论，另一位批评文章的数据是草率的复制粘贴。还有人对为伽利略探测器制造了 5 万颗 SA3000 CPU 的说法表示怀疑。

**标签**: `#radiation-hardened`, `#vintage CPUs`, `#aerospace`, `#military computing`

---

<a id="item-9"></a>
## [逆向工程苹果稀疏映像格式（ASIF）](https://schamper.dev/dissecting-apples-sparse-image-format-asif/) ⭐️ 7.0/10

一篇关于苹果新型稀疏映像格式（ASIF）的详细逆向工程分析已发布，揭示了其内部结构和性能特征。 这项分析有助于开发者和系统管理员理解 ASIF 与现有格式（如 Qcow2）之间的权衡，从而在 Apple Silicon 上做出关于虚拟机存储和磁盘映像管理的明智决策。 ASIF 在 M4 Pro Mac 上可提供高达 8.3 GB/s 的写入速度，并且由于其结构独立于主机文件系统的能力，主机之间传输效率更高。

hackernews · supermatou · 6月28日 16:10 · [社区讨论](https://news.ycombinator.com/item?id=48708644)

**背景**: 稀疏磁盘映像仅分配实际写入数据的空间，而非最大大小。ASIF 是苹果为虚拟机引入的新型稀疏映像格式，可能取代旧的 sparseimage 格式。它是 macOS Tahoe 的一部分，并针对 Apple Silicon 进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.computerworld.com/article/4007567/wwdc-what-is-apple-sparse-image-format-asif.html">WWDC: What is Apple Sparse Image Format (ASIF)?</a></li>
<li><a href="https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment">VZDiskImageStorageDeviceAttachment - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 评论者将 ASIF 与 Qcow2 进行比较，并指出了权衡：一位用户强调 ASIF 的压缩使得内容在挂载前不透明，这会影响未挂载映像的 Spotlight 索引。另一位分享了一个链接，将 ASIF 与旧的 sparseimage 格式进行了对比。

**标签**: `#file-systems`, `#apple`, `#reverse-engineering`, `#storage-formats`

---

<a id="item-10"></a>
## [1960-2026 内存价格历史可视化](https://dam.stanford.edu/memory-prices.html) ⭐️ 7.0/10

斯坦福大学发布了一个 1960 年至 2026 年内存价格的可视化与分析，展示了每 GB 成本在过去几十年中的急剧下降。 这一历史视角凸显了内存变得极其廉价的过程，为关于现代软件膨胀、通胀调整以及未来定价趋势的讨论提供了背景。 该图表使用对数刻度来比较不同年代，但未进行通胀调整，并指出 1990 年之前的每 GB 定价不现实，因为当时不存在 GB 级系统。数据延伸至预计的 2026 年。

hackernews · vga1 · 6月28日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=48710092)

**背景**: 内存价格遵循摩尔定律和大规模生产带来的指数级下降，但该行业也曾经历价格操纵丑闻（例如 2005-2006 年的 DRAM 卡特尔罚款）。近期趋势显示，由于人工智能等因素导致的需求激增，价格出现波动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DRAM_price_fixing_scandal">DRAM price fixing scandal - Wikipedia</a></li>
<li><a href="https://ourworldindata.org/moores-law">What is Moore ' s Law ? | Our World in Data</a></li>
<li><a href="https://www.trendforce.com/price/dram/dram_spot">DRAM Price Trends | TrendForce</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了关于昂贵内存升级的怀旧轶事，讨论了通胀调整（有人指出调整会使早期价格更高），并将数据与现代软件资源消耗联系起来。其他人推测未来定价，认为 AI 需求可能暂时维持高价位。

**标签**: `#memory`, `#pricing`, `#history`, `#data visualization`, `#hardware`

---

<a id="item-11"></a>
## [Tokenmaxxing 已死，Tokenmaxxing 万岁](https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing) ⭐️ 7.0/10

一篇文章声称，tokenmaxxing（通过增加 token 消耗来提升 AI 输出质量）已从无效转为有效，原因是所谓的“复合正确性”，但社区评论对这一声称的范式转变表示强烈怀疑。 这场辩论之所以重要，是因为 tokenmaxxing 已成为 AI 行业中有争议的生产力指标，其有效性影响公司如何为 AI 工具预算以及评估员工绩效。结果可能推动从基于 token 的指标向基于结果的评估转变。 文章引入了“复合正确性”的概念，即花费更多 token 处理任务能提高获得良好结果的可能性，这与之前的“复合错误”形成对比。然而，评论者指出，现实案例（如一次 5 万美元的 AI 培训）建议不断清除上下文以避免错误，削弱了这一说法。

hackernews · theahura · 6月28日 16:24 · [社区讨论](https://news.ycombinator.com/item?id=48708795)

**背景**: Tokenmaxxing 是指将 AI token 消耗量作为生产力代理指标的做法，类似于软件开发中的“代码行数”度量。像 Meta 和亚马逊这样的公司建立了内部排行榜，根据 token 使用量对员工进行排名，但批评者认为这激励的是浪费性消费而非有价值的产出。文章称当前形势正在变化，但社区意见仍然分歧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/tokenmaxxing-killed-ai-budgets-whats-replacing-it/">Tokenmaxxing Killed AI Budgets — What’s Replacing It</a></li>
<li><a href="https://www.explainx.ai/blog/what-is-tokenmaxxing-ai-workplace-trend-2026">What Is Tokenmaxxing? AI Workplace Trend Explained | explainx ...</a></li>
<li><a href="https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/">The Pulse: ‘Tokenmaxxing’ as a weird new trend - The ...</a></li>

</ul>
</details>

**社区讨论**: 评论者高度怀疑：et1337 回忆了一次昂贵的 AI 培训，其中唯一具体的建议是不断清除上下文，这削弱了复合正确性；baconmania 称 tokenmaxxing 是“高薪经理盲目跟风”，而 aurareturn 则辩护说这是推动员工学习 AI 的临时措施。总体情绪是文章中的乐观尚未得到证实。

**标签**: `#AI-agents`, `#tokenmaxxing`, `#LLM-scaling`, `#community-discussion`, `#critical-analysis`

---

<a id="item-12"></a>
## [可视化纽约公共图书馆 5000 份历史菜单（1880-1920）](https://pudding.cool/2026/06/menu-story/) ⭐️ 6.0/10

Pudding 发布了交互式数据可视化项目，展示了纽约公共图书馆 Buttolph 收藏中 1880 年至 1920 年的 5000 份菜单，揭示了当时的饮食趋势和菜单设计风格。 该数据集为了解美国烹饪史和餐饮文化提供了独特窗口，通过引人入胜的视觉叙事让大众了解历史上的饮食趋势。 Buttolph 收藏包含超过 25,000 份菜单，但本可视化专注于 1880-1920 年间的 5000 份，突出了如 'Boiled' 类别和芹菜作为珍馐的流行。

hackernews · xbryanx · 6月28日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=48707763)

**背景**: Buttolph 收藏由 Frank E. Buttolph 小姐在 1900 年左右为纽约公共图书馆收集，尽管她性格古怪，但在 1924 年去世前积累了约 25,000 份菜单。该收藏现为研究饮食习惯和餐饮文化的重要历史资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digitalcollections.nypl.org/collections/the-buttolph-collection-of-menus">The Buttolph collection of menus - NYPL Digital Collections</a></li>
<li><a href="https://tastecooking.com/getting-lost-in-the-worlds-largest-stack-of-menus/">Getting Lost in the World’s Largest Stack of Menus | TASTE</a></li>
<li><a href="https://www.rochester.edu/in_visible_culture/Issue_14/federman/index.html">Federman | The New York Public Library Menu Collection</a></li>

</ul>
</details>

**社区讨论**: 评论中提到了其他趣闻：德国啤酒垫具有法律文件地位；中式外卖菜单体现了独特的 2000 年代审美；芹菜曾因种植和运输困难而成为奢侈品。

**标签**: `#history`, `#data visualization`, `#datasets`, `#NYPL`, `#food`

---

