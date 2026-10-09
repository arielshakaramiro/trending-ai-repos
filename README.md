# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-09

6 of 9 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)<br><sub>Sponsor Star cathrynlavery / diagram-design Editorial diagram design for Claude Code, Code…</sub> | HTML | 1,160 | 47,069 | `agent-skills` `claude-code` `codex` `data-visualization` |
| 3 | [morluto/rea](https://github.com/morluto/rea)<br><sub>Star morluto / rea Reverse engineer anything with agents, from app behavior down to native…</sub> | TypeScript | 7,738 | 32,394 | `agent-skills` `ai-agents` `binary-analysis` `claude-code` |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills)<br><sub>Sponsor Star mattpocock / skills Skills for Real Engineers. Straight from my .agents direc…</sub> | Shell | 1,774 | 281,720 | – |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br><sub>Sponsor Star thedotmack / claude-mem Persistent Context Across Sessions for Every Agent – …</sub> | TypeScript | 670 | 98,772 | `ai` `ai-agents` `ai-memory` `anthropic` |
| 7 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)<br><sub>Star anthropics / knowledge-work-plugins Open source repository of plugins primarily inten…</sub> | Python | 392 | 27,894 | – |
| 8 | [storytold/artcraft](https://github.com/storytold/artcraft)<br><sub>Star storytold / artcraft ArtCraft is an intentional crafting engine for artists, designer…</sub> | Rust | 2,103 | 9,235 | `3d-graphics` `ai` `aivideo` `filmmaking` |

### 📊 This week so far · 2026-W41

#### Summary

- **24** distinct AI repos trended over 5 day(s) (last week: 29)
- AI share of all trending slots: **70%** (-8 pts vs last week)
- Dominant language: **JavaScript** (29% of AI repos)
- Rising topics: `agent` (+2), `claude-code-plugin` (+2), `claude-skills` (+2), `codex` (+2), `macos` (+2)
- New this week: `agent`, `macos`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W41-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| JavaScript | 7 | 29% | 5 |
| Python | 5 | 21% | 8 |
| TypeScript | 4 | 17% | 9 |
| Shell | 2 | 8% | 2 |
| Rust | 2 | 8% | 2 |
| C | 1 | 4% | 1 |
| Cuda | 1 | 4% | 0 |
| HTML | 1 | 4% | 0 |
| Swift | 1 | 4% | 0 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-topics-dark.png"><img alt="Topic movers" src="charts/2026-W41-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 8 |
| `codex` | 6 |
| `claude` | 5 |
| `agent-skills` | 5 |
| `ai-agents` | 4 |
| `developer-tools` | 4 |
| `claude-code-plugin` | 4 |
| `mcp` | 3 |
| `cursor` | 3 |
| `cli` | 3 |
| `claude-skills` | 3 |
| `ai-agent` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 5 | 2,944 | 98,772 |
| [morluto/rea](https://github.com/morluto/rea) | TypeScript | 3 | 15,349 | 32,394 |
| [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | JavaScript | 3 | 4,345 | 7,507 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 3 | 4,066 | 281,720 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 3 | 2,213 | 47,069 |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Python | 3 | 1,139 | 18,162 |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 2 | 2,135 | 92,214 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 2 | 1,787 | 77,943 |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 2 | 1,367 | 158,021 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 2 | 1,013 | 103,092 |

➡️ Last full weekly analysis: [2026-W40](reports/weekly/2026-W40.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 9 day(s) of data · [raw data](data/trending.csv)_
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
