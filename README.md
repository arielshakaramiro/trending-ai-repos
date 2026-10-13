# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-13

8 of 9 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br><sub>Star morluto / rea Reverse engineer anything with agents, from app behavior down to native…</sub> | TypeScript | 45,327 | 180,233 | `agent-skills` `ai-agents` `binary-analysis` `claude-code` |
| 3 | [mksglu/context-mode](https://github.com/mksglu/context-mode)<br><sub>Sponsor Star mksglu / context-mode Context window optimization for AI coding agents. Sandb…</sub> | TypeScript | 246 | 27,662 | `antigravity` `claude` `claude-code` `claude-code-hooks` |
| 4 | [storytold/artcraft](https://github.com/storytold/artcraft)<br><sub>Star storytold / artcraft ArtCraft is an intentional crafting engine for artists, designer…</sub> | Rust | 4,095 | 23,514 | `3d-graphics` `ai` `aivideo` `filmmaking` |
| 5 | [open-webui/open-webui](https://github.com/open-webui/open-webui)<br><sub>Sponsor Star open-webui / open-webui User-friendly AI Interface (Supports Ollama, OpenAI A…</sub> | Python | 157 | 155,435 | `ai` `llm` `llm-ui` `llm-webui` |
| 6 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)<br><sub>Sponsor Star cathrynlavery / diagram-design Editorial diagram design for Claude Code, Code…</sub> | HTML | 2,081 | 53,220 | `agent-skills` `claude-code` `codex` `data-visualization` |
| 7 | [lyogavin/airllm](https://github.com/lyogavin/airllm)<br><sub>Sponsor Star lyogavin / airllm AirLLM 2.8T LLM inference with single 4GB GPU</sub> | Jupyter Notebook | 879 | 37,868 | `chinese-llm` `chinese-nlp` `finetune` `generative-ai` |
| 8 | [microsoft/BitNet](https://github.com/microsoft/BitNet)<br><sub>Star microsoft / BitNet Official inference framework for 1-bit LLMs</sub> | C++ | 97 | 41,058 | – |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)<br><sub>Star Alishahryar1 / free-claude-code Use Claude Code, Codex, VSCode, Pi, and OpenCode (and…</sub> | Python | 626 | 59,682 | – |

### 📊 This week so far · 2026-W42

#### Summary

- **9** distinct AI repos trended over 2 day(s) (last week: 34)
- AI share of all trending slots: **76%** (+2 pts vs last week)
- Dominant language: **Python** (33% of AI repos)

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W42-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W42-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 3 | 33% | 10 |
| TypeScript | 2 | 22% | 5 |
| Rust | 1 | 11% | 2 |
| HTML | 1 | 11% | 1 |
| Jupyter Notebook | 1 | 11% | 0 |
| C++ | 1 | 11% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W42-topics-dark.png"><img alt="Topic movers" src="charts/2026-W42-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `mcp` | 3 |
| `claude-code` | 3 |
| `codex` | 3 |
| `agent-skills` | 2 |
| `binary-analysis` | 1 |
| `cli` | 1 |
| `decompiler` | 1 |
| `ghidra` | 1 |
| `static-analysis` | 1 |
| `ctf` | 1 |
| `ai-agents` | 1 |
| `dsh` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [morluto/rea](https://github.com/morluto/rea) | TypeScript | 2 | 70,926 | 180,233 |
| [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 2 | 7,052 | 23,514 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 2 | 3,164 | 53,220 |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 2 | 1,427 | 37,868 |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 1 | 626 | 59,682 |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | Python | 1 | 315 | 104,680 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 1 | 246 | 27,662 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python | 1 | 157 | 155,435 |
| [microsoft/BitNet](https://github.com/microsoft/BitNet) | C++ | 1 | 97 | 41,058 |

➡️ Last full weekly analysis: [2026-W41](reports/weekly/2026-W41.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 13 day(s) of data · [raw data](data/trending.csv)_
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
