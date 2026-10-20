# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-20

9 of 12 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)<br><sub>Sponsor Star MadsLorentzen / ai-job-search The job search that runs on your machine. AI jo…</sub> | Python | 3,856 | 58,326 | `ai` `ai-agents` `career` `claude-code` |
| 2 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br><sub>Sponsor Star anomalyco / opencode The open source coding agent.</sub> | TypeScript | 1,311 | 218,151 | – |
| 3 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)<br><sub>Star akitaonrails / ai-memory Solution for long term memory for agent coding CLIs and to f…</sub> | Rust | 666 | 11,580 | – |
| 4 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)<br><sub>Star Comfy-Org / ComfyUI The most powerful and modular diffusion model GUI, api and backen…</sub> | Python | 1,011 | 140,083 | `ai` `comfy` `comfyui` `python` |
| 5 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo)<br><sub>Star ruvnet / ruflo 🌊 The original agent harness. Deploy intelligent multi-player swarms, …</sub> | TypeScript | 564 | 77,393 | `agentic-ai` `agentic-framework` `agentic-workflow` `agents` |
| 6 | [stablyai/orca](https://github.com/stablyai/orca)<br><sub>Star stablyai / orca Orca is the place for working with a fleet of agents (e.g. Grok Bot, …</sub> | TypeScript | 1,590 | 98,706 | `ade` `agent-ide` `ai-agents` `automation` |
| 7 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)<br><sub>Star headroomlabs-ai / headroom Compress tool outputs, logs, files, and RAG chunks before …</sub> | Python | 310 | 76,409 | `agent` `ai` `anthropic` `claude-code` |
| 10 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)<br><sub>Star HKUDS / CLI-Anything "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: htt…</sub> | Python | 606 | 55,434 | – |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code)<br><sub>Star anthropics / claude-code Claude Code is an agentic coding tool that lives in your ter…</sub> | TypeScript | 167 | 152,801 | – |

### 📊 This week so far · 2026-W43

#### Summary

- **12** distinct AI repos trended over 2 day(s) (last week: 27)
- AI share of all trending slots: **76%** (-2 pts vs last week)
- Dominant language: **Python** (50% of AI repos)

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W43-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 6 | 50% | 10 |
| TypeScript | 4 | 33% | 7 |
| Rust | 1 | 8% | 3 |
| Unspecified | 1 | 8% | 0 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-topics-dark.png"><img alt="Topic movers" src="charts/2026-W43-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 4 |
| `ai-agents` | 3 |
| `mcp` | 2 |
| `skills` | 2 |
| `codex` | 2 |
| `resume` | 1 |
| `cv` | 1 |
| `job-application` | 1 |
| `interview-preparation` | 1 |
| `job-hunting` | 1 |
| `job-search` | 1 |
| `career` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 2 | 6,088 | 58,326 |
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 2 | 2,736 | 98,706 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 2 | 2,725 | 218,151 |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 2 | 1,195 | 55,434 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 2 | 1,178 | 11,580 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 2 | 1,165 | 140,083 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 2 | 1,077 | 77,393 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 1 | 2,082 | 76,204 |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 1 | 1,175 | 42,921 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 1 | 310 | 76,409 |

➡️ Last full weekly analysis: [2026-W42](reports/weekly/2026-W42.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 20 day(s) of data · [raw data](data/trending.csv)_
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
