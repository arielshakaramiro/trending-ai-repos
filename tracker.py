#!/usr/bin/env python3
"""
Trending AI Repos Tracker
-------------------------
Records which AI repositories are trending on GitHub every day, then analyzes
each week: which topics are rising and which languages dominate.

  data/trending.csv                   one row per repo per day (all trending repos, AI flagged)
  reports/weekly/YYYY-Www.md          finished weekly analysis
  charts/YYYY-Www-*.png               weekly charts (light + dark)
  README.md                           today's AI repos + week-to-date analysis

Source: github.com/trending (HTML), enriched with topics from the GitHub REST
API. If the trending page can't be parsed, the GitHub Search API is used as a
fallback ("new AI repos gaining stars fast") so a day is never empty.
"""
from __future__ import annotations

import csv
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import MaxNLocator  # noqa: E402

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
DATA = ROOT / "data" / "trending.csv"
WEEKLY_DIR = ROOT / "reports" / "weekly"
CHART_DIR = ROOT / "charts"
README = ROOT / "README.md"
README_START = "<!-- TRACKER_START -->"
README_END = "<!-- TRACKER_END -->"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()
UA = "trending-ai-repos-tracker/1.0 (+https://github.com/arielshakaramiro/trending-ai-repos)"
FIELDS = ["date", "rank", "repo", "description", "language", "stars", "forks", "stars_today",
          "topics", "created_at", "license", "is_ai", "source"]

AI_TOPICS = set(CONFIG["ai_topics"])
AI_RE = re.compile("|".join(CONFIG["ai_keywords"]), re.I)
GENERIC = set(CONFIG["generic_topics"])


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def http_get(url: str, api: bool = False, retries: int = 3) -> str:
    headers = {"User-Agent": UA}
    if api:
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    else:
        headers["Accept"] = "text/html"
    last = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code in (404, 451):
                raise
            last = e
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
        time.sleep(5 * attempt)
    raise RuntimeError(f"GET {url} failed: {last}")


# --------------------------------------------------------------------------- #
# Trending page
# --------------------------------------------------------------------------- #
def to_int(text: str) -> int:
    digits = re.sub(r"[^\d]", "", text or "")
    return int(digits) if digits else 0


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def parse_trending(page: str) -> list[dict]:
    """Parse github.com/trending. Relies only on long-stable anchors."""
    repos = []
    for block in re.findall(r'<article[^>]*class="[^"]*Box-row[^"]*"[^>]*>(.*?)</article>', page, re.S):
        m = re.search(r'<h2[^>]*>.*?<a[^>]*href="/([^"/]+/[^"/?#]+)"', block, re.S)
        if not m:
            continue
        full = m.group(1).strip()
        desc = re.search(r"<p[^>]*>(.*?)</p>", block, re.S)
        lang = re.search(r'itemprop="programmingLanguage"[^>]*>([^<]+)<', block)
        stars = re.search(rf'href="/{re.escape(full)}/stargazers"[^>]*>(.*?)</a>', block, re.S)
        forks = re.search(rf'href="/{re.escape(full)}/(?:forks|network/members)"[^>]*>(.*?)</a>', block, re.S)
        today = re.search(r"([\d,]+)\s+stars?\s+(?:today|this week|this month)", block)
        repos.append({
            "repo": full,
            "description": strip_tags(desc.group(1)) if desc else "",
            "language": lang.group(1).strip() if lang else "",
            "stars": to_int(strip_tags(stars.group(1))) if stars else 0,
            "forks": to_int(strip_tags(forks.group(1))) if forks else 0,
            "stars_today": to_int(today.group(1)) if today else 0,
        })
    return repos


def fetch_trending() -> tuple[list[dict], str]:
    seen, out = set(), []
    for lang in CONFIG["trending_pages"]:
        path = f"/{urllib.parse.quote(lang)}" if lang else ""
        url = f"https://github.com/trending{path}?since={CONFIG['since']}"
        try:
            rows = parse_trending(http_get(url))
        except Exception as e:  # noqa: BLE001
            print(f"  ! trending page failed ({url}): {e}", file=sys.stderr)
            rows = []
        for r in rows:
            if r["repo"] not in seen:
                seen.add(r["repo"])
                out.append(r)
    if out:
        return out, "trending"
    print("  ! trending page empty or unparseable, using Search API fallback", file=sys.stderr)
    return fetch_fallback(), "search-fallback"


def fetch_fallback() -> list[dict]:
    """New repos with AI topics gaining stars fast, via the official Search API."""
    since = (date.today() - timedelta(days=CONFIG["fallback_days"])).isoformat()
    seen, out = set(), []
    for topic in ("llm", "ai-agents", "machine-learning", "generative-ai", "mcp", "rag"):
        q = f"topic:{topic} created:>={since} stars:>={CONFIG['fallback_min_stars']}"
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
            {"q": q, "sort": "stars", "order": "desc", "per_page": 20})
        try:
            items = json.loads(http_get(url, api=True)).get("items", [])
        except Exception as e:  # noqa: BLE001
            print(f"  ! search failed for {topic}: {e}", file=sys.stderr)
            continue
        for it in items:
            if it["full_name"] in seen:
                continue
            seen.add(it["full_name"])
            out.append({"repo": it["full_name"], "description": it.get("description") or "",
                        "language": it.get("language") or "", "stars": it["stargazers_count"],
                        "forks": it["forks_count"], "stars_today": 0, "_api": it})
        time.sleep(2)  # search API: 30 req/min
    out.sort(key=lambda r: r["stars"], reverse=True)
    return out[:25]


def enrich(repo: dict) -> None:
    info = repo.pop("_api", None)
    if info is None:
        try:
            info = json.loads(http_get(f"https://api.github.com/repos/{repo['repo']}", api=True))
        except Exception as e:  # noqa: BLE001 - keep the row even without topics
            print(f"  ! could not enrich {repo['repo']}: {e}", file=sys.stderr)
            info = {}
    repo["topics"] = " ".join(info.get("topics") or [])
    repo["created_at"] = (info.get("created_at") or "")[:10]
    repo["license"] = ((info.get("license") or {}).get("spdx_id") or "").replace("NOASSERTION", "")
    repo["stars"] = info.get("stargazers_count", repo["stars"])
    repo["forks"] = info.get("forks_count", repo["forks"])
    repo["language"] = repo["language"] or (info.get("language") or "")
    if not repo["description"]:
        repo["description"] = info.get("description") or ""


def is_ai(repo: dict) -> bool:
    topics = set(repo["topics"].split())
    if topics & AI_TOPICS:
        return True
    text = f"{repo['repo'].split('/')[-1].replace('-', ' ')} {repo['description']}"
    return bool(AI_RE.search(text))


# --------------------------------------------------------------------------- #
# Storage
# --------------------------------------------------------------------------- #
def load_rows() -> list[dict]:
    if not DATA.exists():
        return []
    with DATA.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def append_rows(rows: list[dict]) -> None:
    DATA.parent.mkdir(exist_ok=True)
    new = not DATA.exists()
    with DATA.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerows(rows)


# --------------------------------------------------------------------------- #
# Analysis
# --------------------------------------------------------------------------- #
def week_id(d: str) -> str:
    y, w, _ = date.fromisoformat(d).isocalendar()
    return f"{y}-W{w:02d}"


def week_bounds(wid: str) -> tuple[date, date]:
    y, w = wid.split("-W")
    start = date.fromisocalendar(int(y), int(w), 1)
    return start, start + timedelta(days=6)


def prev_week(wid: str) -> str:
    start, _ = week_bounds(wid)
    return week_id((start - timedelta(days=7)).isoformat())


def analyze(rows: list[dict], wid: str) -> dict:
    this = [r for r in rows if week_id(r["date"]) == wid]
    prev = [r for r in rows if week_id(r["date"]) == prev_week(wid)]
    ai = [r for r in this if r["is_ai"] == "1"]
    ai_prev = [r for r in prev if r["is_ai"] == "1"]

    def distinct(rs):
        latest = {}
        for r in rs:  # latest sighting wins (freshest topics / stars)
            latest[r["repo"]] = r
        return latest

    repos, repos_prev = distinct(ai), distinct(ai_prev)
    days = Counter(r["repo"] for r in ai)
    gained = defaultdict(int)
    for r in ai:
        gained[r["repo"]] += int(r["stars_today"] or 0)

    def lang_counts(rs):
        return Counter((r["language"] or "Unspecified") for r in rs.values())

    def topic_counts(rs):
        c = Counter()
        for r in rs.values():
            c.update(t for t in set(r["topics"].split()) if t not in GENERIC)
        return c

    langs, langs_prev = lang_counts(repos), lang_counts(repos_prev)
    topics, topics_prev = topic_counts(repos), topic_counts(repos_prev)
    movers = sorted(((t, topics[t] - topics_prev.get(t, 0)) for t in set(topics) | set(topics_prev)),
                    key=lambda x: (-x[1], x[0]))
    rising = [(t, d) for t, d in movers if d > 0 and topics[t] >= 2]
    falling = sorted([(t, d) for t, d in movers if d < 0], key=lambda x: (x[1], x[0]))
    new_topics = [t for t, _ in topics.most_common() if topics[t] >= 2 and t not in topics_prev]

    top = sorted(repos.values(), key=lambda r: (-days[r["repo"]], -gained[r["repo"]], r["repo"]))
    all_days = len(this)
    return {
        "week": wid,
        "days_tracked": len({r["date"] for r in this}),
        "ai_repo_days": len(ai),
        "all_repo_days": all_days,
        "ai_share": (len(ai) / all_days) if all_days else 0.0,
        "ai_share_prev": (len(ai_prev) / len(prev)) if prev else None,
        "n_repos": len(repos),
        "n_repos_prev": len(repos_prev),
        "langs": langs,
        "langs_prev": langs_prev,
        "topics": topics,
        "rising": rising,
        "falling": falling,
        "new_topics": new_topics,
        "top": top,
        "days": days,
        "gained": gained,
        "has_prev": bool(prev),
    }


# --------------------------------------------------------------------------- #
# Charts
# --------------------------------------------------------------------------- #
THEMES = {
    "light": {"surface": "#fcfcfb", "text": "#0b0b0b", "text2": "#52514e", "muted": "#898781",
              "grid": "#e1e0d9", "axis": "#c3c2b7", "main": "#2a78d6", "up": "#2a78d6",
              "down": "#e34948", "faint": "#b7d3f6"},
    "dark": {"surface": "#1a1a19", "text": "#ffffff", "text2": "#c3c2b7", "muted": "#898781",
             "grid": "#2c2c2a", "axis": "#383835", "main": "#3987e5", "up": "#3987e5",
             "down": "#e66767", "faint": "#184f95"},
}


def _frame(t, title, subtitle, height):
    fig, ax = plt.subplots(figsize=(9, height), dpi=150)
    fig.patch.set_facecolor(t["surface"])
    ax.set_facecolor(t["surface"])
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(t["axis"])
    ax.tick_params(colors=t["text2"], labelsize=9.5, length=0)
    ax.grid(axis="x", color=t["grid"], linewidth=0.8)
    ax.set_axisbelow(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.text(0.03, 1 - 0.18 / height, title, color=t["text"], fontsize=13, fontweight="bold", va="top")
    fig.text(0.03, 1 - 0.50 / height, subtitle, color=t["text2"], fontsize=9.5, va="top")
    return fig, ax


def chart_languages(a: dict, stub: Path) -> None:
    items = a["langs"].most_common(8)
    other = sum(a["langs"].values()) - sum(n for _, n in items)
    if other:
        items.append(("Other", other))
    if not items:
        return
    total = sum(a["langs"].values())
    labels = [k for k, _ in items][::-1]
    vals = [v for _, v in items][::-1]
    prev = [a["langs_prev"].get(k, 0) for k in labels] if a["has_prev"] else None
    height = 1.4 + 0.42 * len(items)
    for mode, t in THEMES.items():
        fig, ax = _frame(t, f"Languages of trending AI repos · {a['week']}",
                         f"Distinct AI repositories by primary language ({total} repos this week)", height)
        y = range(len(labels))
        ax.barh(y, vals, height=0.62, color=t["main"], zorder=3, label="This week")
        if prev:
            # last week as a tick mark, so it never hides behind or over the bar
            ax.scatter(prev, list(y), marker="|", s=420, linewidths=2.2, color=t["text"],
                       zorder=4, label="Last week")
        for i, v in enumerate(vals):
            edge = max(v, prev[i]) if prev else v
            ax.text(edge, i, f"   {v}  ({v / total:.0%})", va="center", color=t["text"], fontsize=9)
        ax.set_yticks(list(y), labels)
        ax.set_xlim(0, max(vals + (prev or [0])) * 1.3)
        ax.tick_params(axis="x", colors=t["muted"])
        if prev:
            leg = ax.legend(loc="lower right", bbox_to_anchor=(1.0, 1.0), ncol=2, frameon=False,
                            fontsize=9, borderaxespad=0.3)
            for txt in leg.get_texts():
                txt.set_color(t["text2"])
        fig.subplots_adjust(left=0.2, right=0.97, top=1 - 0.8 / height, bottom=0.35 / height)
        fig.savefig(stub.with_name(stub.name + ("" if mode == "light" else "-dark") + ".png"),
                    facecolor=t["surface"])
        plt.close(fig)


def chart_topics(a: dict, stub: Path) -> None:
    movers = (a["rising"][:7] + a["falling"][:5]) if a["has_prev"] else []
    if movers:
        items = movers
        title = f"Topic movers · {a['week']}"
        sub = "Change in number of trending AI repos per topic vs last week"
    else:
        items = [(t, n) for t, n in a["topics"].most_common(CONFIG["weekly_top_topics"])]
        title = f"Top topics · {a['week']}"
        sub = ("Number of trending AI repos per topic (no change vs last week)" if a["has_prev"]
               else "Number of trending AI repos per topic (no previous week to compare yet)")
    stub.with_name(stub.name + ".png").unlink(missing_ok=True)
    stub.with_name(stub.name + "-dark.png").unlink(missing_ok=True)
    if not items:
        return
    items = sorted(items, key=lambda x: x[1])
    labels = [k for k, _ in items]
    vals = [v for _, v in items]
    height = 1.4 + 0.42 * len(items)
    for mode, t in THEMES.items():
        fig, ax = _frame(t, title, sub, height)
        colors = [t["up"] if v >= 0 else t["down"] for v in vals]
        ax.barh(range(len(vals)), vals, height=0.62, color=colors, zorder=3)
        for i, v in enumerate(vals):
            label = f"+{v}" if movers and v > 0 else str(v)
            ax.text(v, i, f"  {label}  " if v >= 0 else f"{label}  ", va="center",
                    ha="left" if v >= 0 else "right", color=t["text"], fontsize=9)
        ax.set_yticks(range(len(labels)), labels)
        lo, hi = min(vals + [0]), max(vals + [0])
        pad = max(1, (hi - lo) * 0.25)
        ax.set_xlim(lo - (pad if lo < 0 else 0), hi + pad)
        if lo < 0:
            ax.axvline(0, color=t["axis"], linewidth=1, zorder=4)
        ax.tick_params(axis="x", colors=t["muted"])
        fig.subplots_adjust(left=0.27, right=0.97, top=1 - 0.8 / height, bottom=0.35 / height)
        fig.savefig(stub.with_name(stub.name + ("" if mode == "light" else "-dark") + ".png"),
                    facecolor=t["surface"])
        plt.close(fig)


# --------------------------------------------------------------------------- #
# Markdown
# --------------------------------------------------------------------------- #
def picture(rel_from: Path, stub: str, alt: str) -> str:
    if not (CHART_DIR / f"{stub}.png").exists():
        return ""
    base = os.path.relpath(CHART_DIR, rel_from).replace(os.sep, "/")
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{base}/{stub}-dark.png">'
            f'<img alt="{alt}" src="{base}/{stub}.png"></picture>')


def pct_delta(now: float, before: float | None) -> str:
    if before is None:
        return ""
    d = (now - before) * 100
    return f" ({'+' if d >= 0 else ''}{d:.0f} pts vs last week)"


def analysis_md(a: dict, where: Path, heading: str = "##") -> list[str]:
    lines = []
    lead = a["langs"].most_common(1)
    lines += [
        f"{heading} Summary", "",
        f"- **{a['n_repos']}** distinct AI repos trended over {a['days_tracked']} day(s)"
        + (f" (last week: {a['n_repos_prev']})" if a["has_prev"] else ""),
        f"- AI share of all trending slots: **{a['ai_share']:.0%}**{pct_delta(a['ai_share'], a['ai_share_prev'])}",
    ]
    if lead:
        lang, n = lead[0]
        tied = [k for k, v in a["langs"].items() if v == n]
        if len(tied) > 1:
            lines.append(f"- No single dominant language: {', '.join(sorted(tied))} tied at {n} repo(s) each")
        else:
            lines.append(f"- Dominant language: **{lang}** ({n / max(1, a['n_repos']):.0%} of AI repos)")
    if a["rising"]:
        lines.append("- Rising topics: " + ", ".join(f"`{t}` (+{d})" for t, d in a["rising"][:5]))
    if a["new_topics"]:
        lines.append("- New this week: " + ", ".join(f"`{t}`" for t in a["new_topics"][:6]))
    lines += ["", f"{heading} Languages", "",
              picture(where, f"{a['week']}-languages", "Languages of trending AI repos"), "",
              "| Language | Repos | Share | Last week |", "|---|--:|--:|--:|"]
    for lang, n in a["langs"].most_common(10):
        prev = a["langs_prev"].get(lang, 0) if a["has_prev"] else "–"
        lines.append(f"| {lang} | {n} | {n / max(1, a['n_repos']):.0%} | {prev} |")
    lines += ["", f"{heading} Topics", "",
              picture(where, f"{a['week']}-topics", "Topic movers"), "",
              "| Topic | Repos this week |", "|---|--:|"]
    for t, n in a["topics"].most_common(CONFIG["weekly_top_topics"]):
        lines.append(f"| `{t}` | {n} |")
    lines += ["", f"{heading} Most persistent AI repos", "",
              "| Repo | Language | Days trending | Stars gained | Total stars |", "|---|---|--:|--:|--:|"]
    for r in a["top"][: CONFIG["weekly_top_repos"]]:
        lines.append(f"| [{r['repo']}](https://github.com/{r['repo']}) | {r['language'] or '–'} "
                     f"| {a['days'][r['repo']]} | {a['gained'][r['repo']]:,} | {int(r['stars']):,} |")
    lines.append("")
    return lines


def write_weekly(rows: list[dict], wid: str) -> Path:
    a = analyze(rows, wid)
    CHART_DIR.mkdir(exist_ok=True)
    chart_languages(a, CHART_DIR / f"{wid}-languages")
    chart_topics(a, CHART_DIR / f"{wid}-topics")
    start, end = week_bounds(wid)
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    path = WEEKLY_DIR / f"{wid}.md"
    lines = [f"# Trending AI repos · {wid}", "", f"{start:%d %b %Y} – {end:%d %b %Y}", "",
             *analysis_md(a, WEEKLY_DIR)]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def update_readme(rows: list[dict], today: str, today_rows: list[dict], latest_report: Path | None) -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    if README_START not in text or README_END not in text:
        return
    ai_today = [r for r in today_rows if r["is_ai"] == "1"]
    src = today_rows[0]["source"] if today_rows else "trending"
    note = " _(trending page unavailable today, showing fast-rising new AI repos instead)_" \
        if src == "search-fallback" else ""
    block = [README_START, f"### 🔥 AI repos trending today · {today}", "",
             f"{len(ai_today)} of {len(today_rows)} trending repositories are AI-related.{note}", "",
             "| # | Repo | Language | ⭐ today | ⭐ total | Topics |", "|--:|---|---|--:|--:|---|"]
    for r in ai_today:
        topics = " ".join(f"`{t}`" for t in r["topics"].split()[:4]) or "–"
        desc = r["description"][:90] + ("…" if len(r["description"]) > 90 else "")
        desc = desc.replace("|", "\\|").replace("<", "&lt;")
        block.append(f"| {r['rank']} | [{r['repo']}](https://github.com/{r['repo']})<br><sub>{desc}</sub> "
                     f"| {r['language'] or '–'} | {int(r['stars_today'] or 0):,} | {int(r['stars']):,} | {topics} |")
    wid = week_id(today)
    a = analyze(rows, wid)
    chart_languages(a, CHART_DIR / f"{wid}-languages")
    chart_topics(a, CHART_DIR / f"{wid}-topics")
    block += ["", f"### 📊 This week so far · {wid}", ""]
    block += analysis_md(a, ROOT, heading="####")
    if latest_report:
        block += [f"➡️ Last full weekly analysis: [{latest_report.stem}]"
                  f"({latest_report.relative_to(ROOT).as_posix()}) · "
                  f"[all reports](reports/weekly)", ""]
    days = len({r['date'] for r in rows})
    block += [f"_Tracking since {min(r['date'] for r in rows)} · {days} day(s) of data · "
              f"[raw data](data/trending.csv)_", README_END]
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), re.S)
    README.write_text(pattern.sub(lambda _: "\n".join(block), text), encoding="utf-8")


def prune_charts(keep_weeks: set[str]) -> None:
    """Keep charts only for finished weekly reports and the current week."""
    for f in CHART_DIR.glob("*-W*-*.png"):
        if f.name[:8] not in keep_weeks:
            f.unlink()


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    today = datetime.now(ZoneInfo(CONFIG["timezone"])).strftime("%Y-%m-%d")
    rows = load_rows()

    if any(r["date"] == today for r in rows):
        print(f"Already recorded {today}.")
        today_rows = [r for r in rows if r["date"] == today]
    else:
        print("Fetching trending repositories")
        repos, source = fetch_trending()
        print(f"  {len(repos)} repos from {source}")
        if not repos:
            print("Nothing fetched. Skipping.", file=sys.stderr)
            return 1
        today_rows = []
        for i, r in enumerate(repos, 1):
            enrich(r)
            today_rows.append({
                "date": today, "rank": i, "repo": r["repo"], "description": r["description"],
                "language": r["language"], "stars": r["stars"], "forks": r["forks"],
                "stars_today": r["stars_today"], "topics": r["topics"], "created_at": r["created_at"],
                "license": r["license"], "is_ai": "1" if is_ai(r) else "0", "source": source,
            })
            time.sleep(0.3)
        append_rows(today_rows)
        rows = load_rows()
        today_rows = [r for r in rows if r["date"] == today]
        print(f"  {sum(r['is_ai'] == '1' for r in today_rows)} AI-related")

    # Finish every completed week that has data but no report yet.
    this_week = week_id(today)
    weeks = sorted({week_id(r["date"]) for r in rows})
    for wid in weeks:
        if wid < this_week and not (WEEKLY_DIR / f"{wid}.md").exists():
            print(f"Writing weekly report {wid}")
            write_weekly(rows, wid)
    reports = sorted(WEEKLY_DIR.glob("*.md")) if WEEKLY_DIR.exists() else []
    CHART_DIR.mkdir(exist_ok=True)
    update_readme(rows, today, today_rows, reports[-1] if reports else None)
    prune_charts({p.stem for p in reports} | {this_week})
    print("README updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
