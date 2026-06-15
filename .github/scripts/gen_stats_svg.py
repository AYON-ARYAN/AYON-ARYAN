#!/usr/bin/env python3
"""Generate a dark-themed GitHub stats card (github-stats.svg).

Computes lifetime stats from the GitHub GraphQL + Search APIs so the numbers
are always accurate (unlike the third-party Vercel widgets, which reported
Total PRs: 0). Run by .github/workflows/metrics.yml.

Env:
  GH_TOKEN  - token with public read access (GITHUB_TOKEN works for public data)
  GH_LOGIN  - target username (default: AYON-ARYAN)
  STATS_OVERRIDE_JSON - optional dict of stats to skip the API (local testing)
"""
import json
import os
import urllib.parse
import urllib.request

API = "https://api.github.com"
LOGIN = os.environ.get("GH_LOGIN", "AYON-ARYAN")
TOKEN = os.environ.get("GH_TOKEN", "")


def _req(url, data=None, headers=None):
    h = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "ayon-stats-card",
    }
    h.update(headers or {})
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=h)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def graphql(query):
    return _req(f"{API}/graphql", {"query": query})["data"]


def search_count(kind, q):
    url = f"{API}/search/{kind}?q={urllib.parse.quote(q)}&per_page=1"
    return _req(url).get("total_count", 0)


def fetch_stats():
    override = os.environ.get("STATS_OVERRIDE_JSON")
    if override:
        return json.loads(override)

    data = graphql(
        """{ user(login: "%s") {
          merged: pullRequests(states: MERGED) { totalCount }
          totalPRs: pullRequests { totalCount }
          openPRs: pullRequests(states: OPEN) { totalCount }
          issues { totalCount }
          followers { totalCount }
          repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST, ISSUE, REPOSITORY]) { totalCount }
          repositories(first: 100, ownerAffiliations: OWNER, isFork: false) { nodes { stargazerCount } }
        } }""" % LOGIN
    )["user"]

    stars = sum(n["stargazerCount"] for n in data["repositories"]["nodes"])
    try:
        commits = search_count("commits", f"author:{LOGIN}")
    except Exception:
        commits = 0

    return {
        "stars": stars,
        "commits": commits,
        "total_prs": data["totalPRs"]["totalCount"],
        "merged_prs": data["merged"]["totalCount"],
        "open_prs": data["openPRs"]["totalCount"],
        "issues": data["issues"]["totalCount"],
        "contributed": data["repositoriesContributedTo"]["totalCount"],
        "followers": data["followers"]["totalCount"],
    }


def render(s):
    rows = [
        ("⭐", "Total Stars", s["stars"]),
        ("\U0001f4e6", "Total Commits", s["commits"]),
        ("\U0001f500", "Total PRs", s["total_prs"]),
        ("✅", "Merged PRs", s["merged_prs"]),
        ("\U0001f53c", "Open PRs", s["open_prs"]),
        ("❗", "Total Issues", s["issues"]),
        ("\U0001f91d", "Contributed to", s["contributed"]),
    ]
    bg, border, accent, label, value = "#0D1117", "#30363d", "#6C63FF", "#8b949e", "#ffffff"
    pad_top, row_h, w = 78, 30, 480
    h = pad_top + row_h * len(rows) + 24

    parts = [
        f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" '
        f'xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="{LOGIN} GitHub statistics">',
        f'<rect x="0.5" y="0.5" rx="10" width="{w-1}" height="{h-1}" fill="{bg}" stroke="{border}"/>',
        f'<text x="32" y="44" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="20" font-weight="700" fill="{value}">{LOGIN}\'s GitHub Stats</text>',
        f'<rect x="32" y="58" width="{w-64}" height="2" rx="1" fill="{accent}" opacity="0.5"/>',
    ]
    for i, (icon, name, num) in enumerate(rows):
        y = pad_top + i * row_h + 18
        parts.append(
            f'<text x="32" y="{y}" font-size="15" font-family="Segoe UI,Helvetica,Arial,sans-serif">'
            f'<tspan>{icon}</tspan>'
            f'<tspan dx="10" fill="{label}">{name}</tspan></text>'
        )
        parts.append(
            f'<text x="{w-32}" y="{y}" text-anchor="end" font-size="15" font-weight="600" '
            f'font-family="Segoe UI,Helvetica,Arial,sans-serif" fill="{value}">{num:,}</text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    stats = fetch_stats()
    print("stats:", json.dumps(stats))
    out = os.environ.get("STATS_OUT", "github-stats.svg")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(stats))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
