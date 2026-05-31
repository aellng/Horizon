"""Daily summary generation — pure programmatic rendering."""

import re
from typing import List, Dict

from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"
_CREATOR_TOPIC_SIGNAL_GROUPS = (
    ("agent", "claude", "gpt", "codex", "prompt", "vibe coding", "image generation"),
    ("llm", "qwen", "stable diffusion", "flux"),
    ("machine learning", "pytorch"),
)
_A_SHARE_THEME_RULES = (
    {
        "name": "AI Agent 与办公软件",
        "signals": ("agent", "claude", "codex", "gpt", "office", "wps", "productivity"),
        "impact": "企业级 AI Agent 落地、办公软件智能化和软件订阅模式变化，可能提升 AI 应用层与办公软件方向的市场关注度。",
        "stocks": ("金山办公（688111.SH）", "科大讯飞（002230.SZ）"),
    },
    {
        "name": "AI 安全与软件治理",
        "signals": ("sandbox", "sandboxing", "security", "安全", "gvisor", "bubblewrap", "seatbelt"),
        "impact": "Agent 权限隔离、数据泄露防护和企业安全治理成为落地前提，可能增加网络安全与安全服务方向的讨论热度。",
        "stocks": ("奇安信（688561.SH）", "启明星辰（002439.SZ）"),
    },
    {
        "name": "算力芯片与服务器",
        "signals": ("llm", "local-llm", "gpu", "inference", "qwen", "quantization", "nvidia", "server", "算力"),
        "impact": "本地模型部署、推理成本和算力效率讨论升温，可能使市场继续关注 AI 芯片、服务器与算力基础设施。",
        "stocks": ("寒武纪（688256.SH）", "浪潮信息（000977.SZ）", "中科曙光（603019.SH）"),
    },
    {
        "name": "AI 创作工具",
        "signals": ("stable diffusion", "flux", "prompt", "image generation", "audio ai", "creative tools"),
        "impact": "图像、视频、音频与提示工程工具迭代，可能提升 AI 内容生产和创意软件方向的关注度。",
        "stocks": ("万兴科技（300624.SZ）", "昆仑万维（300418.SZ）"),
    },
)


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "daily_conclusion": "Today's Conclusion",
        "publish_topics": "{count} Topics Worth Publishing",
        "focus_intro": "Today's most valuable signals are concentrated in: {topics}.",
        "follow_up_intro": "For content creation, prioritize these {count} directions:",
        "topic": "Topic {index}",
        "related_news": "Related news",
        "angle": "Suggested angle",
        "extension": "Further direction",
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "daily_conclusion": "今日结论",
        "publish_topics": "最值得发的 {count} 个选题",
        "focus_intro": "今天最值得继续跟进的信号集中在：{topics}。",
        "follow_up_intro": "面向 AI 自媒体创作，可以优先关注以下 {count} 个方向：",
        "topic": "选题 {index}",
        "related_news": "关联新闻",
        "angle": "切入角度",
        "extension": "可延展方向",
        "a_share_analysis": "A 股影响参考",
        "related_signal": "关联热点",
        "possible_impact": "可能影响",
        "example_stocks": "示例股票",
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        # TOC
        toc_entries = []
        for i, item in enumerate(items):
            _t = item.metadata.get(f"title_{language}") or item.title
            t = str(_t).replace("[", "(").replace("]", ")")
            if language == "zh":
                t = _pangu(t)
            score = item.ai_score or "?"
            toc_entries.append(f"{i + 1}. [{t}](#item-{i + 1}) \u2b50\ufe0f {score}/10")
        toc = "\n".join(toc_entries) + "\n\n---\n\n"

        parts = [self._format_item(item, labels, language, i + 1) for i, item in enumerate(items)]

        editorial = self._format_editorial_sections(items, labels, language)

        return header + editorial + toc + "".join(parts)

    def _format_editorial_sections(self, items: List[ContentItem], labels: dict, language: str) -> str:
        """Render a compact creator-oriented conclusion and publishing shortlist."""
        selected = self._select_publish_topics(items)
        tags = []
        max_tags = max((len(item.ai_tags) for item in selected), default=0)
        for tag_index in range(max_tags):
            for item in selected:
                if tag_index >= len(item.ai_tags):
                    continue
                tag = item.ai_tags[tag_index]
                if tag not in tags:
                    tags.append(tag)
        focus = "、".join(tags[:5]) if language == "zh" else ", ".join(tags[:5])
        if not focus:
            focus = "AI 行业动态" if language == "zh" else "AI industry developments"

        conclusion = [
            f"## {labels['daily_conclusion']}",
            "",
            labels["focus_intro"].format(topics=focus),
            "",
            labels["follow_up_intro"].format(count=len(selected)),
        ]
        topic_sections = [
            f"## {labels['publish_topics'].format(count=len(selected))}",
            "",
        ]

        for index, item in enumerate(selected, start=1):
            title = str(item.metadata.get(f"title_{language}") or item.title)
            summary = (
                item.metadata.get(f"detailed_summary_{language}")
                or item.metadata.get("detailed_summary")
                or item.ai_summary
                or title
            )
            background = item.metadata.get(f"background_{language}") or item.metadata.get("background") or ""
            if language == "zh":
                title = _pangu(title)
                summary = _pangu(summary)
                background = _pangu(background)

            conclusion.append(f"{index}. **[{title}]({item.url})**")
            topic_sections += [
                f"### {labels['topic'].format(index=index)}：{title}" if language == "zh"
                else f"### {labels['topic'].format(index=index)}: {title}",
                "",
                f"**{labels['related_news']}**: [{title}]({item.url})",
                "",
                f"**{labels['angle']}**: {summary}",
            ]
            if background:
                topic_sections += ["", f"**{labels['extension']}**: {background}"]
            topic_sections += ["", "---", ""]

        financial_analysis = self._format_a_share_analysis(items, labels, language)
        return "\n".join(conclusion + ["", "---", ""]) + financial_analysis + "\n".join(topic_sections) + "\n"

    def _format_a_share_analysis(self, items: List[ContentItem], labels: dict, language: str) -> str:
        """Render A-share research leads for Chinese creator briefings."""
        if language != "zh":
            return ""

        matched_themes = []
        for theme in _A_SHARE_THEME_RULES:
            related_item = next(
                (
                    item
                    for item in items
                    if any(signal in self._item_search_text(item) for signal in theme["signals"])
                ),
                None,
            )
            if related_item:
                matched_themes.append((theme, related_item))
            if len(matched_themes) == 3:
                break

        if not matched_themes:
            return ""

        lines = [
            f"## {labels['a_share_analysis']}",
            "",
            "> 仅作内容研究线索，不构成投资建议。热点相关性不等于股价必然上涨，请结合上市公司公告、业绩、估值与市场风险自行判断。",
            "",
        ]
        for index, (theme, item) in enumerate(matched_themes, start=1):
            title = _pangu(str(item.metadata.get("title_zh") or item.title))
            lines += [
                f"### {index}. {theme['name']}",
                "",
                f"- **{labels['related_signal']}**: [{title}]({item.url})",
                f"- **{labels['possible_impact']}**: {theme['impact']}",
                f"- **{labels['example_stocks']}**: {'、'.join(theme['stocks'])}",
                "",
            ]
        return "\n".join(lines + ["---", ""]) + "\n"

    def _item_search_text(self, item: ContentItem) -> str:
        """Build normalized text used for deterministic topic matching."""
        metadata = item.metadata
        parts = [
            item.title,
            item.ai_summary or "",
            *item.ai_tags,
            str(metadata.get("title_zh") or ""),
            str(metadata.get("detailed_summary_zh") or metadata.get("detailed_summary") or ""),
            str(metadata.get("background_zh") or metadata.get("background") or ""),
        ]
        return " ".join(parts).casefold()

    def _select_publish_topics(self, items: List[ContentItem]) -> List[ContentItem]:
        """Prefer AI-related items for the creator shortlist, then fill by score."""
        creator_item_groups = [[] for _ in _CREATOR_TOPIC_SIGNAL_GROUPS]
        general_ai_items = []
        other_items = []
        for item in items:
            searchable = " ".join([item.title, *item.ai_tags]).casefold()
            creator_group = next(
                (
                    group_index
                    for group_index, signals in enumerate(_CREATOR_TOPIC_SIGNAL_GROUPS)
                    if any(
                        re.search(rf"(?<![a-z0-9]){re.escape(signal)}(?![a-z0-9])", searchable)
                        for signal in signals
                    )
                ),
                None,
            )
            is_general_ai_topic = re.search(r"(?<![a-z0-9])ai(?![a-z0-9])", searchable)
            if creator_group is not None:
                creator_item_groups[creator_group].append(item)
            elif is_general_ai_topic:
                general_ai_items.append(item)
            else:
                other_items.append(item)
        creator_items = [item for group in creator_item_groups for item in group]
        return (creator_items + general_ai_items + other_items)[:3]

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        entries = []
        for i, item in enumerate(items, start=1):
            title = str(item.metadata.get(f"title_{language}") or item.title).replace("[", "(").replace("]", ")")
            if language == "zh":
                title = _pangu(title)
            score = item.ai_score or "?"
            entries.append(f"{i}. [{title}]({item.url}) \u2b50\ufe0f {score}/10")

        return header + "\n".join(entries)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            discussion_url = str(discussion_url)
            if discussion_url != url:
                source_line += f' · [{labels["discussion"]}]({discussion_url})'

        lines = [
            f'<a id="item-{index}"></a>',
            f"## [{title}]({url}) \u2b50\ufe0f {score}/10",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
