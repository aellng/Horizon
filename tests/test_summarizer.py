"""Unit tests for daily summary rendering."""

import asyncio
from datetime import datetime, timezone

from src.ai.summarizer import DailySummarizer
from src.models import ContentItem, SourceType


def _run_async(coro):
    return asyncio.run(coro)


def _make_item(idx: int) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Important Item {idx}",
        url=f"https://example.com/items/{idx}",
        content="content",
        author="tester",
        published_at=datetime(2026, 4, 25, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 8.0
    item.ai_summary = f"Summary for item {idx}."
    item.ai_tags = ["AI", "News"]
    return item


def test_generate_webhook_overview_lists_items_without_full_details():
    summarizer = DailySummarizer()
    items = [_make_item(1), _make_item(2)]

    result = summarizer.generate_webhook_overview(
        items,
        date="2026-04-25",
        total_fetched=10,
        language="en",
    )

    assert "Selected 2 important items from 10 fetched items" in result
    assert "1. [Important Item 1](https://example.com/items/1)" in result
    assert "2. [Important Item 2](https://example.com/items/2)" in result
    assert "Summary for item 1." not in result


def test_generate_webhook_item_renders_single_item_detail():
    summarizer = DailySummarizer()

    result = summarizer.generate_webhook_item(
        _make_item(1),
        language="en",
        index=1,
        total=2,
    )

    assert result.startswith("Item 1/2")
    assert "## [Important Item 1](https://example.com/items/1)" in result
    assert "Summary for item 1." in result
    assert "**Tags**: `#AI`, `#News`" in result


def test_generate_webhook_item_includes_discussion_link_when_distinct():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = "https://news.ycombinator.com/item?id=1"

    result = summarizer.generate_webhook_item(
        item,
        language="en",
        index=1,
        total=1,
    )

    assert "tester · Apr 25, 08:00 · [Discussion](https://news.ycombinator.com/item?id=1)" in result


def test_generate_webhook_item_omits_discussion_link_when_same_as_item_url():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = item.url

    result = summarizer.generate_webhook_item(
        item,
        language="en",
        index=1,
        total=1,
    )

    assert "[Discussion](https://example.com/items/1)" not in result


def test_generate_webhook_item_uses_localized_discussion_label():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = "https://www.reddit.com/r/python/comments/abc123/test/"

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "[社区讨论](https://www.reddit.com/r/python/comments/abc123/test/)" in result


def test_generate_summary_zh_uses_localized_selection_header_and_numeric_date():
    summarizer = DailySummarizer()
    item = _make_item(1)

    result = _run_async(
        summarizer.generate_summary(
            [item],
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "> 从 10 条内容中筛选出 1 条重要资讯。" in result
    assert "rss · tester · 4月25日 08:00" in result
    assert "From 10 items" not in result
    assert "Apr 25, 08:00" not in result


def test_generate_empty_summary_zh_uses_localized_analyzed_line():
    summarizer = DailySummarizer()

    result = _run_async(
        summarizer.generate_summary(
            [],
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "> 已分析 10 条内容，但没有达到重要性阈值的条目。" in result
    assert "Analyzed 10 items" not in result


def test_generate_summary_zh_adds_creator_conclusion_and_publish_topics():
    summarizer = DailySummarizer()
    items = [_make_item(1), _make_item(2), _make_item(3), _make_item(4)]

    result = _run_async(
        summarizer.generate_summary(
            items,
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "## 今日结论" in result
    assert "## 最值得发的 3 个选题" in result
    assert "### 选题 1：Important Item 1" in result
    assert "**切入角度**: Summary for item 1." in result
    assert "### 选题 3：Important Item 3" in result
    assert "### 选题 4：" not in result


def test_generate_summary_prefers_ai_creator_topics_over_generic_high_score_items():
    summarizer = DailySummarizer()
    generic = _make_item(1)
    generic.title = "Typography Design Update"
    generic.ai_tags = ["typography", "design"]
    creator = _make_item(2)
    creator.title = "Claude Agent Sandbox"
    creator.ai_tags = ["Claude", "AI", "sandboxing"]

    result = _run_async(
        summarizer.generate_summary(
            [generic, creator],
            date="2026-04-25",
            total_fetched=2,
            language="zh",
        )
    )

    assert result.index("### 选题 1：Claude Agent Sandbox") < result.index("### 选题 2：Typography Design Update")


def test_generate_summary_prioritizes_creator_story_then_llm_then_ml_technical_topic():
    summarizer = DailySummarizer()
    ml_technical = _make_item(1)
    ml_technical.title = "PyTorch Debugger"
    ml_technical.ai_tags = ["PyTorch", "machine learning"]
    llm_ecosystem = _make_item(2)
    llm_ecosystem.title = "Local LLM Cost Analysis"
    llm_ecosystem.ai_tags = ["local-llm", "hardware"]
    creator_story = _make_item(3)
    creator_story.title = "Claude Agent Sandbox"
    creator_story.ai_tags = ["Claude", "agent"]

    result = _run_async(
        summarizer.generate_summary(
            [ml_technical, llm_ecosystem, creator_story],
            date="2026-04-25",
            total_fetched=3,
            language="zh",
        )
    )

    assert result.index("### 选题 1：Claude Agent Sandbox") < result.index("### 选题 2：Local LLM Cost Analysis")
    assert result.index("### 选题 2：Local LLM Cost Analysis") < result.index("### 选题 3：PyTorch Debugger")


def test_generate_summary_zh_adds_a_share_research_leads_with_risk_note():
    summarizer = DailySummarizer()
    agent = _make_item(1)
    agent.title = "Claude Agent Sandbox"
    agent.ai_tags = ["Claude", "agent", "sandboxing"]
    local_llm = _make_item(2)
    local_llm.title = "Local LLM Cost Analysis"
    local_llm.ai_tags = ["local-llm", "gpu", "hardware"]

    result = _run_async(
        summarizer.generate_summary(
            [agent, local_llm],
            date="2026-04-25",
            total_fetched=2,
            language="zh",
        )
    )

    assert "## A 股影响参考" in result
    assert "不构成投资建议" in result
    assert "### 1. AI Agent 与办公软件" in result
    assert "金山办公（688111.SH）" in result
    assert "### 2. AI 安全与软件治理" in result
    assert "奇安信（688561.SH）" in result
    assert "### 3. 算力芯片与服务器" in result
    assert "寒武纪（688256.SH）" in result
