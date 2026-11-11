# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-11-11

7 of 12 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [meta/astryx](https://github.com/meta/astryx)<br><sub>Star meta / astryx An open source design system that's fully customizable and agent ready</sub> | TypeScript | 3,108 | 23,877 | – |
| 2 | [anthropics/skills](https://github.com/anthropics/skills)<br><sub>Star anthropics / skills Public repository for Agent Skills</sub> | Python | 1,679 | 192,716 | `agent-skills` |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)<br><sub>Star addyosmani / agent-skills Production-grade engineering skills for AI coding agents.</sub> | JavaScript | 465 | 115,456 | `agent-skills` `antigravity` `claude-code` `codex` |
| 4 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)<br><sub>Star anthropics / claude-quickstarts A collection of projects designed to help developers …</sub> | Python | 531 | 20,676 | – |
| 7 | [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)<br><sub>Star homeassistant-ai / ha-mcp Configure and automate Home Assistant with Claude, ChatGPT,…</sub> | Python | 790 | 6,893 | `ai` `claude` `hacs` `home-assistant` |
| 8 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)<br><sub>Star vercel-labs / agent-browser Browser automation CLI for AI agents</sub> | Rust | 780 | 49,500 | – |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills)<br><sub>Sponsor Star mattpocock / skills Skills for Real Engineers. Straight from my .agents direc…</sub> | Shell | 1,225 | 321,360 | – |

### 📊 This week so far · 2026-W46

#### Summary

- **12** distinct AI repos trended over 3 day(s) (last week: 58)
- AI share of all trending slots: **69%** (-4 pts vs last week)
- Dominant language: **Python** (33% of AI repos)
- Rising topics: `home-assistant` (+2), `home-automation` (+2)
- New this week: `home-assistant`, `home-automation`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W46-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 4 | 33% | 21 |
| TypeScript | 3 | 25% | 12 |
| Rust | 2 | 17% | 6 |
| Go | 1 | 8% | 1 |
| JavaScript | 1 | 8% | 7 |
| Shell | 1 | 8% | 2 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-topics-dark.png"><img alt="Topic movers" src="charts/2026-W46-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 3 |
| `codex` | 2 |
| `agent-skills` | 2 |
| `claude` | 2 |
| `home-assistant` | 2 |
| `mcp` | 2 |
| `home-automation` | 2 |
| `gpu` | 1 |
| `nvidia` | 1 |
| `kubernetes` | 1 |
| `cluster-api` | 1 |
| `bare-metal` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [meta/astryx](https://github.com/meta/astryx) | TypeScript | 3 | 7,261 | 23,877 |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 3 | 3,509 | 192,716 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Rust | 3 | 2,511 | 49,500 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Python | 3 | 1,114 | 20,676 |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | TypeScript | 2 | 3,026 | 20,240 |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | Python | 2 | 821 | 6,893 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 1 | 1,225 | 321,360 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 1 | 506 | 69,396 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 1 | 465 | 115,456 |
| [dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) | Go | 1 | 345 | 977 |

➡️ Last full weekly analysis: [2026-W45](reports/weekly/2026-W45.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 42 day(s) of data · [raw data](data/trending.csv)_
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
