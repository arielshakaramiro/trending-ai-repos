# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-11-14

8 of 12 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review)<br><sub>Star alibaba / open-code-review Secure, fast, efficient, battle-tested at Alibaba's scale.…</sub> | Go | 215 | 50,920 | `agent` `agent-skills` `code-review` `code-review-assistant` |
| 2 | [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)<br><sub>Star GoogleChrome / modern-web-guidance-src Keep your coding agent up to date with the lat…</sub> | TypeScript | 1,925 | 5,169 | – |
| 3 | [openai/codex-security](https://github.com/openai/codex-security)<br><sub>Star openai / codex-security OpenAI's Codex Security CLI and TypeScript SDK for finding, v…</sub> | TypeScript | 751 | 13,318 | `ai-security` `application-security` `cli` `code-scanning` |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)<br><sub>Sponsor Star ZhuLinsen / daily_stock_analysis LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本…</sub> | Python | 256 | 71,950 | `a-stock` `ai-agent` `aigc` `llm` |
| 6 | [backnotprop/plannotator](https://github.com/backnotprop/plannotator)<br><sub>Star backnotprop / plannotator The workspace to stay in the loop and on top of agents - sh…</sub> | TypeScript | 108 | 10,600 | `agents` `claude-code` `code-review` `codex` |
| 9 | [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)<br><sub>Star tradermonty / claude-trading-skills Claude Code skills for equity investors and trade…</sub> | Python | 69 | 4,348 | – |
| 11 | [Likely7/Veyra-NRVideo](https://github.com/Likely7/Veyra-NRVideo)<br><sub>Star Likely7 / Veyra-NRVideo Bring PS5 GTA6 to 120FPS with DLSS 5. An advanced Windows vid…</sub> | C++ | 256 | 1,755 | – |
| 12 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)<br><sub>Star ChromeDevTools / chrome-devtools-mcp Chrome DevTools for coding agents</sub> | TypeScript | 67 | 55,763 | `browser` `chrome` `chrome-devtools` `debugging` |

### 📊 This week so far · 2026-W46

#### Summary

- **24** distinct AI repos trended over 6 day(s) (last week: 58)
- AI share of all trending slots: **67%** (-6 pts vs last week)
- Dominant language: **TypeScript** (38% of AI repos)
- Rising topics: `home-assistant` (+2), `home-automation` (+2), `code-review` (+1)
- New this week: `home-automation`, `home-assistant`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W46-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| TypeScript | 9 | 38% | 12 |
| Python | 6 | 25% | 21 |
| Go | 2 | 8% | 1 |
| Rust | 2 | 8% | 6 |
| C++ | 2 | 8% | 0 |
| JavaScript | 1 | 4% | 7 |
| Shell | 1 | 4% | 2 |
| Zig | 1 | 4% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-topics-dark.png"><img alt="Topic movers" src="charts/2026-W46-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `mcp` | 5 |
| `claude-code` | 4 |
| `codex` | 4 |
| `agent-skills` | 3 |
| `ai-agents` | 2 |
| `home-automation` | 2 |
| `home-assistant` | 2 |
| `claude` | 2 |
| `ai-agent` | 2 |
| `skills` | 2 |
| `cli` | 2 |
| `code-review` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [meta/astryx](https://github.com/meta/astryx) | TypeScript | 5 | 11,867 | 27,008 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Rust | 4 | 3,219 | 50,119 |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 3 | 3,509 | 192,716 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 3 | 2,068 | 116,930 |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | Python | 3 | 1,466 | 7,607 |
| [openai/codex-security](https://github.com/openai/codex-security) | TypeScript | 3 | 1,446 | 13,318 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Python | 3 | 1,114 | 20,676 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 3 | 1,040 | 71,950 |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | TypeScript | 2 | 3,026 | 20,240 |
| [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | TypeScript | 2 | 2,664 | 5,169 |

➡️ Last full weekly analysis: [2026-W45](reports/weekly/2026-W45.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 45 day(s) of data · [raw data](data/trending.csv)_
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
