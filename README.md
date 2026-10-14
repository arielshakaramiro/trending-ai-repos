# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-14

7 of 9 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br><sub>Star morluto / rea Reverse engineer anything with agents, from app behavior down to native…</sub> | TypeScript | 54,679 | 219,289 | `agent-skills` `ai-agents` `binary-analysis` `claude-code` |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)<br><sub>Star debpalash / VoiceStudio VoiceStudio is the open-source, fully-local ElevenLabs altern…</sub> | Python | 1,748 | 64,276 | `ai` `audiobook` `cuda` `dubbing` |
| 4 | [mksglu/context-mode](https://github.com/mksglu/context-mode)<br><sub>Sponsor Star mksglu / context-mode Context window optimization for AI coding agents. Sandb…</sub> | TypeScript | 969 | 28,522 | `antigravity` `claude` `claude-code` `claude-code-hooks` |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)<br><sub>Sponsor Star cathrynlavery / diagram-design Editorial diagram design for Claude Code, Code…</sub> | HTML | 1,815 | 54,665 | `agent-skills` `claude-code` `codex` `data-visualization` |
| 6 | [vercel-labs/skills](https://github.com/vercel-labs/skills)<br><sub>Star vercel-labs / skills The open agent skills tool - npx skills</sub> | TypeScript | 190 | 34,729 | – |
| 7 | [lyogavin/airllm](https://github.com/lyogavin/airllm)<br><sub>Sponsor Star lyogavin / airllm AirLLM 2.8T LLM inference with single 4GB GPU</sub> | Jupyter Notebook | 1,001 | 38,499 | `chinese-llm` `chinese-nlp` `finetune` `generative-ai` |
| 8 | [storytold/artcraft](https://github.com/storytold/artcraft)<br><sub>Star storytold / artcraft ArtCraft is an intentional crafting engine for artists, designer…</sub> | Rust | 4,081 | 26,521 | `3d-graphics` `ai` `aivideo` `filmmaking` |

### 📊 This week so far · 2026-W42

#### Summary

- **11** distinct AI repos trended over 3 day(s) (last week: 34)
- AI share of all trending slots: **77%** (+2 pts vs last week)
- Dominant language: **Python** (36% of AI repos)

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W42-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W42-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 4 | 36% | 10 |
| TypeScript | 3 | 27% | 5 |
| Rust | 1 | 9% | 2 |
| HTML | 1 | 9% | 1 |
| Jupyter Notebook | 1 | 9% | 0 |
| C++ | 1 | 9% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W42-topics-dark.png"><img alt="Topic movers" src="charts/2026-W42-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 3 |
| `mcp` | 3 |
| `codex` | 3 |
| `agent-skills` | 2 |
| `developer-tools` | 1 |
| `reverse-engineering` | 1 |
| `ctf` | 1 |
| `dsh-plugin` | 1 |
| `static-analysis` | 1 |
| `ghidra` | 1 |
| `hopper` | 1 |
| `model-context-protocol` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [morluto/rea](https://github.com/morluto/rea) | TypeScript | 3 | 125,605 | 219,289 |
| [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 3 | 11,133 | 26,521 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 3 | 4,979 | 54,665 |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 3 | 2,428 | 38,499 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 2 | 1,215 | 28,522 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 1 | 1,748 | 64,276 |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 1 | 626 | 59,682 |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | Python | 1 | 315 | 104,680 |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | TypeScript | 1 | 190 | 34,729 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python | 1 | 157 | 155,435 |

➡️ Last full weekly analysis: [2026-W41](reports/weekly/2026-W41.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 14 day(s) of data · [raw data](data/trending.csv)_
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
