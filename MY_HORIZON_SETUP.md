# 我的 Horizon AI 资讯雷达配置

这个仓库已经按“AI 博主信息 + AI 创作者信息”方向做了基础配置。

## 已关注的信息类型

### AI 博主 / 研究者

- Simon Willison
- Lilian Weng
- Chip Huyen
- Eugene Yan
- Jay Alammar
- Sebastian Raschka
- Interconnects
- Latent Space
- The Gradient
- BAIR Blog

### AI 创作者 / 工具项目

- OpenAI News / OpenAI Python / OpenAI Cookbook
- Anthropic SDK / Claude Cookbooks
- Hugging Face Blog / Transformers / smolagents
- Ollama
- vLLM
- LangChain / LangGraph
- LlamaIndex
- Model Context Protocol servers

### 社区趋势

- Hacker News 热门技术新闻
- Reddit: MachineLearning, LocalLLaMA, OpenAI, StableDiffusion

## 必须配置的 GitHub Secret

至少需要配置一个 AI 模型密钥。当前默认使用 DeepSeek：

- `DEEPSEEK_API_KEY`

进入仓库：Settings -> Secrets and variables -> Actions -> New repository secret。

## 可选 Secret

- `HORIZON_WEBHOOK_URL`：飞书/钉钉/Slack 等 Webhook 推送地址。
- `APIFY_TOKEN`：如果以后启用 Twitter/X 抓取，需要这个。
- `OPENAI_API_KEY`、`ANTHROPIC_API_KEY`、`GOOGLE_API_KEY`、`MINIMAX_API_KEY`、`DASHSCOPE_API_KEY`：如果以后切换模型供应商再配置。

## 运行方式

进入 GitHub 仓库的 Actions 页面，选择 `Daily Horizon Summary`，点击 `Run workflow` 手动运行。

仓库也已设置为每天北京时间 07:00 自动运行一次。

## GitHub Pages

第一次 Actions 成功后，会生成 `gh-pages` 分支。然后在仓库 Settings -> Pages 里选择：

- Source: Deploy from a branch
- Branch: `gh-pages`
- Folder: `/ (root)`

之后日报站点会通过 GitHub Pages 发布。

## 后续调整

主要编辑 `data/config.github.json`：

- 新增 RSS：在 `sources.rss` 添加条目。
- 新增 GitHub 创作者动态：在 `sources.github` 添加 `user_events`。
- 新增工具项目 Release：在 `sources.github` 添加 `repo_releases`。
- 调整筛选强度：修改 `filtering.ai_score_threshold`。