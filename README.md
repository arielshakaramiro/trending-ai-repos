# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-11-10

9 of 11 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [anthropics/skills](https://github.com/anthropics/skills)<br><sub>Star anthropics / skills Public repository for Agent Skills</sub> | Python | 1,038 | 191,592 | `agent-skills` |
| 2 | [meta/astryx](https://github.com/meta/astryx)<br><sub>Star meta / astryx An open source design system that's fully customizable and agent ready</sub> | TypeScript | 3,278 | 21,157 | – |
| 5 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)<br><sub>Star anthropics / claude-quickstarts A collection of projects designed to help developers …</sub> | Python | 551 | 20,209 | – |
| 6 | [garrytan/gbrain](https://github.com/garrytan/gbrain)<br><sub>Star garrytan / gbrain Garry's Opinionated OpenClaw/Hermes Agent Brain</sub> | TypeScript | 216 | 32,369 | – |
| 7 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)<br><sub>Star vercel-labs / agent-browser Browser automation CLI for AI agents</sub> | Rust | 916 | 48,823 | – |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView)<br><sub>Star ruvnet / RuView π RuView turns commodity WiFi signals into real-time spatial intellig…</sub> | Rust | 172 | 103,747 | `claude` `claude-code` `esp32` `firmware` |
| 9 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)<br><sub>Star ZhuLinsen / daily_stock_analysis LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LL…</sub> | Python | 506 | 69,396 | `a-stock` `ai-agent` `aigc` `llm` |
| 10 | [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)<br><sub>Star homeassistant-ai / ha-mcp Configure and automate Home Assistant with Claude, ChatGPT,…</sub> | Python | 31 | 6,268 | `ai` `claude` `hacs` `home-assistant` |
| 11 | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)<br><sub>Sponsor Star milind-soni / OpenMausBot Open-source Grok Bot alternative with a virtual mac…</sub> | TypeScript | 1,587 | 20,240 | `ai-agents` `claude-code` `codex` `computer-use` |

### 📊 This week so far · 2026-W46

#### Summary

- **10** distinct AI repos trended over 2 day(s) (last week: 58)
- AI share of all trending slots: **75%** (+2 pts vs last week)
- Dominant language: **Python** (40% of AI repos)
- Rising topics: `home-assistant` (+2), `home-automation` (+2)
- New this week: `home-assistant`, `home-automation`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W46-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 4 | 40% | 21 |
| TypeScript | 3 | 30% | 12 |
| Rust | 2 | 20% | 6 |
| Go | 1 | 10% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-topics-dark.png"><img alt="Topic movers" src="charts/2026-W46-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 2 |
| `claude` | 2 |
| `home-assistant` | 2 |
| `mcp` | 2 |
| `home-automation` | 2 |
| `nvidia` | 1 |
| `kubernetes` | 1 |
| `bare-metal` | 1 |
| `gpu` | 1 |
| `cluster-api` | 1 |
| `computer-use` | 1 |
| `grok-bot-alternative` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [meta/astryx](https://github.com/meta/astryx) | TypeScript | 2 | 4,153 | 21,157 |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | TypeScript | 2 | 3,026 | 20,240 |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 2 | 1,830 | 191,592 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Rust | 2 | 1,731 | 48,823 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Python | 2 | 583 | 20,209 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 1 | 506 | 69,396 |
| [dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) | Go | 1 | 345 | 977 |
| [garrytan/gbrain](https://github.com/garrytan/gbrain) | TypeScript | 1 | 216 | 32,369 |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 1 | 172 | 103,747 |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | Python | 1 | 31 | 6,268 |

➡️ Last full weekly analysis: [2026-W45](reports/weekly/2026-W45.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 41 day(s) of data · [raw data](data/trending.csv)_
<!-- TRACKER_END -->

## How it works

```
github.com/trending ──► GitHub API (topics, license, created) ──► AI classifier ──► data/trending.csv
                                                                                        │
                                              reports/weekly/YYYY-Www.md + charts ◄─────┘
```

1. **Collect.** Reads the daily [GitHub trending](https://github.com/trending) list (all languages) and records rank, stars, stars gained today, and language for every repository.
2. **Enrich.** Fetches each repository's topics, creation date and license from the GitHub REST API.
3. **Classify.** A repo counts as AI if it carries an AI topic (`llm`, `ai-agents`, `rag`, `mcp`, `computer-vision`, ...) or its name and description match AI keywords. All trending repos are stored, so the AI share of trending can be measured too.
4. **Analyze weekly.** For each finished ISO week (Monday–Sunday):
   - **Languages**: distinct AI repos per primary language, with last week for comparison
   - **Topics**: repos per topic, plus *movers* (biggest gains and drops vs last week) and topics that are new this week. Generic tags like `ai` or `python` are left out, so the movement shows what people are actually building.
   - **Most persistent repos**: AI repos that stayed on the trending list the most days, with stars gained
5. **Fallback.** If GitHub changes the trending page and it can no longer be parsed, the run falls back to the official Search API (new repos with AI topics gaining stars fast) and marks those rows as `search-fallback`, so a day is never empty.

## Data

`data/trending.csv`, one row per repository per day:

| Column | Meaning |
|--------|---------|
| `date`, `rank` | Day (WIB) and position on the trending list |
| `repo` | `owner/name` |
| `description`, `language`, `topics`, `license`, `created_at` | Repository metadata |
| `stars`, `forks`, `stars_today` | Totals and stars gained that day |
| `is_ai` | `1` if classified as AI-related |
| `source` | `trending` or `search-fallback` |

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/arielshakaramiro/trending-ai-repos/main/data/trending.csv")
ai = df[df.is_ai == 1]
ai.groupby("language").repo.nunique().sort_values(ascending=False).head(10)
```

## Setup

1. Push this repository to GitHub. No secrets are needed: the workflow uses the built-in `GITHUB_TOKEN` for API calls.
2. **Actions → Daily Trending Snapshot → Run workflow** for the first run.

The first full weekly report appears on the Monday after the first complete week of data. Until then, the live view above shows the week-to-date analysis.

## Run locally

```bash
pip install -r requirements.txt
export GITHUB_TOKEN=ghp_...   # optional, raises the API rate limit
python tracker.py
```

## Customize

`config.json`:

- `ai_topics` / `ai_keywords`: what counts as AI
- `generic_topics`: tags ignored in topic analysis
- `trending_pages`: `[""]` is the all-languages list. Adding e.g. `"python"` also reads that language's list, which finds more repos but skews the language analysis toward the languages you add.
- `since`: `daily`, `weekly` or `monthly`

## License

MIT. Repository data comes from GitHub; each listed project keeps its own license.
