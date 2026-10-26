# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-26

8 of 11 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [makecindy/cindy](https://github.com/makecindy/cindy)<br><sub>Star makecindy / cindy Consider it done. The open-source AI agent that works out of the bo…</sub> | TypeScript | 675 | 5,351 | `agent` `ai-agent` `ai-assistant` `android` |
| 2 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark)<br><sub>Star Nutlope / hallmark Anti-AI-slop design skill for Claude Code, Cursor, and Codex.</sub> | CSS | 1,317 | 34,587 | – |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)<br><sub>Sponsor Star debpalash / VoiceStudio VoiceStudio is the open-source, fully-local ElevenLab…</sub> | Python | 1,592 | 87,484 | `ai` `audiobook` `cuda` `dubbing` |
| 4 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable)<br><sub>Star pbakaus / impeccable The design language that makes your AI harness better at design.</sub> | Rust | 1,092 | 88,162 | – |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)<br><sub>Star TauricResearch / TradingAgents TradingAgents: Multi-Agents LLM Financial Trading Fram…</sub> | Python | 381 | 114,996 | `agent` `finance` `llm` `multiagent` |
| 8 | [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)<br><sub>Star JetBrains / thinkrail Vibe code with pi in a lightweight, real IDE that customises it…</sub> | TypeScript | 51 | 2,114 | `agent` `agent-skills` `agentic-ai` `agentic-workflow` |
| 10 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br><sub>Star cloudflare / security-audit-skill A coding-agent skill for multi-phase security audit…</sub> | JavaScript | 2,878 | 47,463 | – |
| 11 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)<br><sub>Star AgriciDaniel / claude-seo Universal SEO skill for Claude Code. 26 sub-skills + 19 sub…</sub> | Python | 197 | 21,389 | `ai` `ai-seo` `claude-code` `claude-code-skill` |

### 📊 This week so far · 2026-W44

#### Summary

- **8** distinct AI repos trended over 1 day(s) (last week: 31)
- AI share of all trending slots: **73%** (-7 pts vs last week)
- Dominant language: **Python** (38% of AI repos)
- Rising topics: `agent` (+1)

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W44-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W44-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 3 | 38% | 14 |
| TypeScript | 2 | 25% | 8 |
| CSS | 1 | 12% | 1 |
| Rust | 1 | 12% | 3 |
| JavaScript | 1 | 12% | 2 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W44-topics-dark.png"><img alt="Topic movers" src="charts/2026-W44-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `agent` | 3 |
| `claude-code` | 2 |
| `ai-agent` | 1 |
| `codex` | 1 |
| `ios` | 1 |
| `react-native` | 1 |
| `electron` | 1 |
| `ai-assistant` | 1 |
| `macos` | 1 |
| `windows` | 1 |
| `android` | 1 |
| `omnivoice-studio` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 1 | 2,878 | 47,463 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 1 | 1,592 | 87,484 |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | CSS | 1 | 1,317 | 34,587 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Rust | 1 | 1,092 | 88,162 |
| [makecindy/cindy](https://github.com/makecindy/cindy) | TypeScript | 1 | 675 | 5,351 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Python | 1 | 381 | 114,996 |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | Python | 1 | 197 | 21,389 |
| [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) | TypeScript | 1 | 51 | 2,114 |

➡️ Last full weekly analysis: [2026-W43](reports/weekly/2026-W43.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 26 day(s) of data · [raw data](data/trending.csv)_
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
