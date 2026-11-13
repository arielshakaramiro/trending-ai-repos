# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-11-13

9 of 13 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)<br><sub>Star GoogleChrome / modern-web-guidance-src Keep your coding agent up to date with the lat…</sub> | TypeScript | 739 | 3,895 | – |
| 2 | [openai/codex-security](https://github.com/openai/codex-security)<br><sub>Star openai / codex-security OpenAI's Codex Security CLI and TypeScript SDK for finding, v…</sub> | TypeScript | 643 | 12,735 | `ai-security` `application-security` `cli` `code-scanning` |
| 6 | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)<br><sub>Star QwenLM / qwen-code An open-source AI coding agent that lives in your terminal.</sub> | TypeScript | 151 | 30,047 | `agentic` `ai` `ai-agent` `ai-coding` |
| 7 | [ashhart/TensorFold](https://github.com/ashhart/TensorFold)<br><sub>Sponsor Star ashhart / TensorFold LLM Inference Engine for Metal, CUDA and Vulkan.</sub> | Zig | 54 | 2,038 | `ai` `ai-tools` `llm` `llm-inference` |
| 9 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)<br><sub>Star addyosmani / agent-skills Production-grade engineering skills for AI coding agents.</sub> | JavaScript | 816 | 116,930 | `agent-skills` `antigravity` `claude-code` `codex` |
| 10 | [meta/astryx](https://github.com/meta/astryx)<br><sub>Star meta / astryx An open source design system that's fully customizable and agent ready</sub> | TypeScript | 1,830 | 27,008 | – |
| 11 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)<br><sub>Star CopilotKit / OpenBot Open-source AI coworkers that each get a computer of their own: …</sub> | TypeScript | 298 | 11,933 | `ag-ui` `agent-governance` `ai-agents` `browser-automation` |
| 12 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)<br><sub>Star Alishahryar1 / free-claude-code Use Claude Code, Codex, Antigravity, VSCode, Pi, and …</sub> | Python | 415 | 69,637 | – |
| 13 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)<br><sub>Star ggml-org / llama.cpp LLM inference in C/C++</sub> | C++ | 176 | 134,774 | `ggml` |

### 📊 This week so far · 2026-W46

#### Summary

- **19** distinct AI repos trended over 5 day(s) (last week: 58)
- AI share of all trending slots: **67%** (-6 pts vs last week)
- Dominant language: **TypeScript** (37% of AI repos)
- Rising topics: `home-assistant` (+2), `home-automation` (+2)
- New this week: `home-automation`, `home-assistant`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W46-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| TypeScript | 7 | 37% | 12 |
| Python | 5 | 26% | 21 |
| Rust | 2 | 11% | 6 |
| Go | 1 | 5% | 1 |
| JavaScript | 1 | 5% | 7 |
| Shell | 1 | 5% | 2 |
| Zig | 1 | 5% | 1 |
| C++ | 1 | 5% | 0 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W46-topics-dark.png"><img alt="Topic movers" src="charts/2026-W46-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `mcp` | 4 |
| `claude-code` | 3 |
| `codex` | 3 |
| `ai-agents` | 2 |
| `agent-skills` | 2 |
| `home-automation` | 2 |
| `home-assistant` | 2 |
| `claude` | 2 |
| `ai-agent` | 2 |
| `cli` | 2 |
| `gpu` | 1 |
| `nvidia` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [meta/astryx](https://github.com/meta/astryx) | TypeScript | 5 | 11,867 | 27,008 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Rust | 4 | 3,219 | 50,119 |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 3 | 3,509 | 192,716 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 3 | 2,068 | 116,930 |
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | Python | 3 | 1,466 | 7,607 |
| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Python | 3 | 1,114 | 20,676 |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | TypeScript | 2 | 3,026 | 20,240 |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | Python | 2 | 784 | 70,900 |
| [openai/codex-security](https://github.com/openai/codex-security) | TypeScript | 2 | 695 | 12,735 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 1 | 1,225 | 321,360 |

➡️ Last full weekly analysis: [2026-W45](reports/weekly/2026-W45.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 44 day(s) of data · [raw data](data/trending.csv)_
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
