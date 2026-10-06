# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-06

7 of 13 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br><sub>Sponsor Star thedotmack / claude-mem Persistent Context Across Sessions for Every Agent – …</sub> | TypeScript | 534 | 96,796 | `ai` `ai-agents` `ai-memory` `anthropic` |
| 3 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)<br><sub>Star earthtojake / text-to-cad Give your agent CAD superpowers.</sub> | Python | 437 | 17,624 | `agents` `ai-agents` `cad` `mechanical-engineering` |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)<br><sub>Star Panniantong / Agent-Reach Give your AI agent eyes to see the entire internet. Read & …</sub> | Python | 1,155 | 92,214 | `agent-infrastructure` `ai-agent` `ai-search` `automation` |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)<br><sub>Sponsor Star calesthio / OpenMontage World's first open-source, agentic video production s…</sub> | Python | 742 | 64,344 | `agent` `agentic-ai` `ai` `claude` |
| 9 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym)<br><sub>Sponsor Star DuarteSantos8 / openGym Self-hosted gym & body-weight tracker — plan routines…</sub> | JavaScript | 1,433 | 4,676 | `bodyweight` `docker` `fitness` `fitness-tracker` |
| 10 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os)<br><sub>Star cloudflare / cloudflare-os Agent workspace built on Cloudflare Workers for creating d…</sub> | TypeScript | 101 | 11,127 | – |
| 12 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)<br><sub>Sponsor Star msitarzewski / agency-agents A complete AI agency at your fingertips - From f…</sub> | Shell | 744 | 157,471 | – |

### 📊 This week so far · 2026-W41

#### Summary

- **14** distinct AI repos trended over 2 day(s) (last week: 29)
- AI share of all trending slots: **62%** (-16 pts vs last week)
- Dominant language: **JavaScript** (43% of AI repos)
- Rising topics: `agentic-ai` (+1), `claude-code-plugin` (+1), `claude-skills` (+1)

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W41-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| JavaScript | 6 | 43% | 5 |
| Python | 3 | 21% | 8 |
| TypeScript | 3 | 21% | 9 |
| C | 1 | 7% | 1 |
| Shell | 1 | 7% | 2 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-topics-dark.png"><img alt="Topic movers" src="charts/2026-W41-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude` | 5 |
| `claude-code` | 5 |
| `codex` | 3 |
| `ai-agents` | 3 |
| `claude-code-plugin` | 3 |
| `agent-skills` | 3 |
| `cursor` | 3 |
| `developer-tools` | 2 |
| `mcp` | 2 |
| `agentic-ai` | 2 |
| `anthropic` | 2 |
| `claude-skills` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 2 | 2,135 | 92,214 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 2 | 1,162 | 96,796 |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 2 | 987 | 64,344 |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Python | 2 | 520 | 17,624 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 1 | 1,894 | 155,347 |
| [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | JavaScript | 1 | 1,433 | 4,676 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 1 | 1,171 | 76,630 |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 1 | 744 | 157,471 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 1 | 336 | 101,342 |
| [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude) | JavaScript | 1 | 232 | 1,248 |

➡️ Last full weekly analysis: [2026-W40](reports/weekly/2026-W40.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 6 day(s) of data · [raw data](data/trending.csv)_
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
