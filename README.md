# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-11-07

4 of 18 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 2 | [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)<br><sub>Star NVIDIA / auto-ontology Auto Ontology is a Python framework for building semantic, gra…</sub> | Python | 2,015 | 9,453 | – |
| 10 | [google/skills](https://github.com/google/skills)<br><sub>Star google / skills Agent Skills for Google products and technologies</sub> | Python | 534 | 22,988 | `google` `googlecloud` `skills` |
| 16 | [mattpocock/skills](https://github.com/mattpocock/skills)<br><sub>Sponsor Star mattpocock / skills Skills for Real Engineers. Straight from my .agents direc…</sub> | Shell | 2,070 | 317,022 | – |
| 17 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br><sub>Star cloudflare / security-audit-skill A coding-agent skill for multi-phase security audit…</sub> | JavaScript | 2,548 | 64,548 | – |

### 📊 This week so far · 2026-W45

#### Summary

- **33** distinct AI repos trended over 6 day(s) (last week: 30)
- AI share of all trending slots: **66%** (-17 pts vs last week)
- Dominant language: **Python** (42% of AI repos)
- Rising topics: `mcp` (+3), `transformer` (+3), `accessibility` (+2), `agents` (+2), `automation` (+2)
- New this week: `transformer`, `accessibility`, `model-context-protocol`, `agents`, `moe`, `workflow-automation`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W45-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W45-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 14 | 42% | 7 |
| TypeScript | 6 | 18% | 8 |
| Rust | 5 | 15% | 3 |
| Shell | 2 | 6% | 4 |
| C | 2 | 6% | 0 |
| JavaScript | 2 | 6% | 3 |
| Zig | 1 | 3% | 1 |
| Jupyter Notebook | 1 | 3% | 0 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W45-topics-dark.png"><img alt="Topic movers" src="charts/2026-W45-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `mcp` | 8 |
| `ai-agents` | 7 |
| `claude-code` | 6 |
| `claude` | 4 |
| `codex` | 4 |
| `anthropic` | 3 |
| `rag` | 3 |
| `claude-skills` | 3 |
| `playwright` | 3 |
| `transformer` | 3 |
| `automation` | 3 |
| `browser-automation` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 5 | 7,542 | 317,022 |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | 4 | 10,709 | 17,503 |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Python | 4 | 6,024 | 98,457 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 4 | 5,640 | 113,191 |
| [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | Rust | 4 | 1,592 | 11,684 |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | Python | 3 | 6,744 | 9,453 |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | 3 | 3,528 | 35,031 |
| [anomalyco/hex](https://github.com/anomalyco/hex) | Rust | 2 | 1,589 | 4,809 |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 2 | 1,121 | 39,063 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | TypeScript | 2 | 902 | 140,235 |

➡️ Last full weekly analysis: [2026-W44](reports/weekly/2026-W44.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 38 day(s) of data · [raw data](data/trending.csv)_
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
