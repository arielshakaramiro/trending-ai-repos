# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-23

6 of 9 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 2 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)<br><sub>Star anthropics / knowledge-work-plugins Open source repository of plugins primarily inten…</sub> | Python | 303 | 31,791 | – |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br><sub>Sponsor Star DietrichGebert / ponytail Makes your AI agent think like the laziest senior d…</sub> | JavaScript | 1,948 | 173,995 | `agent-skills` `ai-agents` `claude` `claude-code` |
| 4 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br><sub>Star cloudflare / security-audit-skill A coding-agent skill for multi-phase security audit…</sub> | JavaScript | 2,979 | 40,204 | – |
| 5 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br><sub>Star Graphify-Labs / graphify Turn any codebase, with its docs, SQL schemas, configs, and …</sub> | Python | 1,408 | 133,336 | `ai-agents` `antigravity` `ast` `claude-code` |
| 6 | [supabase/supabase](https://github.com/supabase/supabase)<br><sub>Sponsor Star supabase / supabase The Postgres development platform. Supabase gives you a d…</sub> | TypeScript | 693 | 113,607 | `ai` `alternative` `auth` `database` |
| 8 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)<br><sub>Sponsor Star luongnv89 / claude-howto A visual, example-driven guide to Claude Code — from…</sub> | Python | 177 | 43,546 | `claude-code` `guide` `tutorial` |

### 📊 This week so far · 2026-W43

#### Summary

- **23** distinct AI repos trended over 5 day(s) (last week: 27)
- AI share of all trending slots: **82%** (+4 pts vs last week)
- Dominant language: **Python** (48% of AI repos)
- Rising topics: `cursor` (+3), `postgresql` (+3), `claude-code-plugin` (+2), `cursor-rules` (+2), `langchain` (+2)
- New this week: `cursor`, `postgresql`, `pytorch`, `langchain`, `claude-code-plugin`, `cursor-rules`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W43-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 11 | 48% | 10 |
| TypeScript | 6 | 26% | 7 |
| JavaScript | 2 | 9% | 1 |
| Rust | 1 | 4% | 3 |
| Unspecified | 1 | 4% | 0 |
| Shell | 1 | 4% | 1 |
| Go | 1 | 4% | 2 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-topics-dark.png"><img alt="Topic movers" src="charts/2026-W43-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 8 |
| `ai-agents` | 6 |
| `mcp` | 4 |
| `codex` | 4 |
| `skills` | 3 |
| `claude` | 3 |
| `cursor` | 3 |
| `postgresql` | 3 |
| `job-search` | 2 |
| `career` | 2 |
| `multi-agent` | 2 |
| `agentic-ai` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 4 | 5,842 | 101,811 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 4 | 3,310 | 141,738 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 3 | 9,949 | 61,499 |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 3 | 6,703 | 40,204 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 3 | 5,235 | 173,995 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 3 | 3,965 | 219,234 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 3 | 3,643 | 133,336 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 3 | 1,761 | 77,993 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 3 | 1,464 | 12,537 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 3 | 1,333 | 77,411 |

➡️ Last full weekly analysis: [2026-W42](reports/weekly/2026-W42.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 23 day(s) of data · [raw data](data/trending.csv)_
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
