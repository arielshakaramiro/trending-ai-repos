# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-11-09

6 of 9 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 2 | [dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke)<br><sub>Star dsx-ai-factory / nvke NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kub…</sub> | Go | 345 | 977 | `bare-metal` `cluster-api` `gpu` `kubernetes` |
| 3 | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)<br><sub>Sponsor Star milind-soni / OpenMausBot Open-source Grok Bot alternative with a virtual mac…</sub> | TypeScript | 1,439 | 19,023 | `ai-agents` `claude-code` `codex` `computer-use` |
| 4 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)<br><sub>Star anthropics / claude-quickstarts A collection of projects designed to help developers …</sub> | Python | 32 | 19,672 | – |
| 5 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)<br><sub>Star vercel-labs / agent-browser Browser automation CLI for AI agents</sub> | Rust | 815 | 48,025 | – |
| 6 | [meta/astryx](https://github.com/meta/astryx)<br><sub>Star meta / astryx An open source design system that's fully customizable and agent ready</sub> | TypeScript | 875 | 18,021 | – |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br><sub>Star anthropics / skills Public repository for Agent Skills</sub> | Python | 792 | 190,025 | `agent-skills` |

### 📊 This week so far · 2026-W46

#### Summary

- **6** distinct AI repos trended over 1 day(s) (last week: 58)
- AI share of all trending slots: **67%** (-6 pts vs last week)
- No single dominant language: Python, TypeScript tied at 2 repo(s) each

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W46-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| TypeScript | 2 | 33% | 12 |
| Python | 2 | 33% | 21 |
| Go | 1 | 17% | 1 |
| Rust | 1 | 17% | 6 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-topics-dark.png"><img alt="Topic movers" src="charts/2026-W46-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `bare-metal` | 1 |
| `kubernetes` | 1 |
| `gpu` | 1 |
| `nvidia` | 1 |
| `cluster-api` | 1 |
| `electron` | 1 |
| `docker` | 1 |
| `grok` | 1 |
| `grok-bot` | 1 |
| `grok-bot-alternative` | 1 |
| `ai-agents` | 1 |
| `computer-use` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | TypeScript | 1 | 1,439 | 19,023 |
| [meta/astryx](https://github.com/meta/astryx) | TypeScript | 1 | 875 | 18,021 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Rust | 1 | 815 | 48,025 |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 1 | 792 | 190,025 |
| [dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) | Go | 1 | 345 | 977 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Python | 1 | 32 | 19,672 |

➡️ Last full weekly analysis: [2026-W45](reports/weekly/2026-W45.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 40 day(s) of data · [raw data](data/trending.csv)_
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
