# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-01

15 of 17 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)<br><sub>Star NVIDIA / OpenShell OpenShell is the safe, private runtime for autonomous AI agents.</sub> | Rust | 1,281 | 13,474 | – |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)<br><sub>Star debpalash / VoiceStudio VoiceStudio is the open-source, fully-local ElevenLabs altern…</sub> | Python | 3,483 | 50,919 | `ai` `audiobook` `cuda` `dubbing` |
| 3 | [mvschwarz/openrig](https://github.com/mvschwarz/openrig)<br><sub>Star mvschwarz / openrig Multi-agent harness that runs Claude Code and Codex together as o…</sub> | TypeScript | 624 | 3,262 | `agent-harness` `agent-orchestration` `agent-skills` `ai-coding` |
| 4 | [mksglu/context-mode](https://github.com/mksglu/context-mode)<br><sub>Sponsor Star mksglu / context-mode Context window optimization for AI coding agents. Sandb…</sub> | TypeScript | 90 | 24,615 | `antigravity` `claude` `claude-code` `claude-code-hooks` |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br><sub>Sponsor Star DietrichGebert / ponytail Makes your AI agent think like the laziest senior d…</sub> | JavaScript | 743 | 149,627 | `agent-skills` `ai-agents` `claude` `claude-code` |
| 6 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)<br><sub>Star harry0703 / MoneyPrinterTurbo 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short vi…</sub> | Python | 431 | 127,766 | `ai-video-generator` `content-creation` `ffmpeg` `instagram-reels` |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br><sub>Sponsor Star openclaw / openclaw The AI that really does things. Any OS. Any Platform. The…</sub> | TypeScript | 136 | 391,096 | `ai` `assistant` `crustacean` `molty` |
| 8 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)<br><sub>Star ComposioHQ / awesome-claude-skills A curated list of awesome Claude Skills, resources…</sub> | Python | 123 | 76,256 | `agent-skills` `ai-agents` `antigravity` `automation` |
| 9 | [mattpocock/skills](https://github.com/mattpocock/skills)<br><sub>Sponsor Star mattpocock / skills Skills for Real Engineers. Straight from my .agents direc…</sub> | Shell | 876 | 273,328 | – |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br><sub>Star heygen-com / hyperframes Write HTML. Render video. Built for agents.</sub> | TypeScript | 349 | 54,964 | `ai` `animation` `ffmpeg` `framework` |
| 11 | [firebase/firebase-ios-sdk](https://github.com/firebase/firebase-ios-sdk)<br><sub>Star firebase / firebase-ios-sdk Firebase SDK for Apple App Development</sub> | C++ | 8 | 6,797 | `ai` `analytics` `authentication` `crash-reporting` |
| 12 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)<br><sub>Star modelcontextprotocol / servers Model Context Protocol Servers</sub> | TypeScript | 50 | 90,895 | – |
| 14 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)<br><sub>Star colbymchenry / codegraph Pre-indexed code knowledge graph, auto syncs on code changes…</sub> | C | 118 | 72,709 | – |
| 15 | [t8y2/dbx](https://github.com/t8y2/dbx)<br><sub>Star t8y2 / dbx 25 MB lightweight cross-platform database client for 100+ databases, inclu…</sub> | Rust | 1,138 | 23,535 | `ai` `cli` `clickhouse` `database` |
| 17 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)<br><sub>Sponsor Star VectifyAI / PageIndex 📑 PageIndex: Document Index for Vectorless, Reasoning-b…</sub> | Python | 1,097 | 38,295 | `agentic-ai` `agents` `ai` `ai-agents` |

### 📊 This week so far · 2026-W40

#### Summary

- **15** distinct AI repos trended over 1 day(s)
- AI share of all trending slots: **88%**
- Dominant language: **TypeScript** (33% of AI repos)
- Rising topics: `claude-code` (+4), `mcp` (+4), `agent-skills` (+3), `ai-agents` (+3), `claude` (+3)
- New this week: `claude-code`, `mcp`, `agent-skills`, `claude`, `ai-agents`, `text-to-speech`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W40-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W40-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| TypeScript | 5 | 33% | – |
| Python | 4 | 27% | – |
| Rust | 2 | 13% | – |
| JavaScript | 1 | 7% | – |
| Shell | 1 | 7% | – |
| C++ | 1 | 7% | – |
| C | 1 | 7% | – |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W40-topics-dark.png"><img alt="Topic movers" src="charts/2026-W40-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 4 |
| `mcp` | 4 |
| `agent-skills` | 3 |
| `claude` | 3 |
| `ai-agents` | 3 |
| `text-to-speech` | 2 |
| `tauri` | 2 |
| `codex-cli` | 2 |
| `cli` | 2 |
| `antigravity` | 2 |
| `codex` | 2 |
| `openclaw` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 1 | 3,483 | 50,919 |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Rust | 1 | 1,281 | 13,474 |
| [t8y2/dbx](https://github.com/t8y2/dbx) | Rust | 1 | 1,138 | 23,535 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Python | 1 | 1,097 | 38,295 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 1 | 876 | 273,328 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 1 | 743 | 149,627 |
| [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | TypeScript | 1 | 624 | 3,262 |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Python | 1 | 431 | 127,766 |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | TypeScript | 1 | 349 | 54,964 |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | TypeScript | 1 | 136 | 391,096 |

_Tracking since 2026-10-01 · 1 day(s) of data · [raw data](data/trending.csv)_
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
