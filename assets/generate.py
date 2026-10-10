#!/usr/bin/env python3
"""Generate the profile's SVG assets (hero + project cards), dark & light.

Design system — "audit log": monospace test-runner aesthetic drawn from
driftbench/settledrift (verification, reconciliation, deterministic checks).
Colors are GitHub's own semantic palette so assets feel native on github.com.

Run from repo root:  python3 assets/generate.py
"""
import html
from pathlib import Path

OUT = Path(__file__).parent
MONO = "'SF Mono','Cascadia Code','JetBrains Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(bg="#0D1117", panel="#010409", border="#30363D", fg="#E6EDF3",
                 muted="#8B949E", faint="#484F58", green="#3FB950", amber="#D29922",
                 violet="#A371F7", chipbg="#161B22"),
    "light": dict(bg="#FFFFFF", panel="#F6F8FA", border="#D0D7DE", fg="#1F2328",
                  muted="#656D76", faint="#8C959F", green="#1A7F37", amber="#9A6700",
                  violet="#8250DF", chipbg="#EAEEF2"),
}

STYLE = """
  text { font-family: %(mono)s; }
  .cursor { animation: blink 1.1s steps(1) infinite; }
  @keyframes blink { 50%% { opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { .cursor { animation: none; } }
"""


def esc(s):
    return html.escape(s, quote=True)


def dots(label, status, width=70):
    """ 'label ····· STATUS' padding with middle dots like a test log."""
    n = max(2, width - len(label) - len(status))
    return label + " " + "·" * n + " " + status


def hero(t, name):
    c = THEMES[t]
    W, H = 800, 342
    rows = [
        ("$ ayon --verify --profile github.com/AYON-ARYAN", "cmd", None),
        ("", "", None),
        (dots("ships production systems, not notebooks", "PASS"), "ok", "✓"),
        (dots("ai/ml major · fintech minor · rv university '27", "PASS"), "ok", "✓"),
        (dots("2 industry internships (ai @ broadrange · android @ techpuram)", "PASS"), "ok", "✓"),
        (dots("319 leetcode solved · 166 medium · 35 hard", "PASS"), "ok", "✓"),
        (dots("benchmarks agent reliability — driftbench", "PASS"), "ok", "✓"),
        ("", "", None),
        (dots("open to ai/ml · backend · android internships", "OPEN"), "open", "●"),
    ]
    y0, lh = 118, 22
    lines = []
    for i, (txt, kind, glyph) in enumerate(rows):
        if not txt:
            continue
        y = y0 + i * lh
        delay = 0.25 + i * 0.28
        color = {"cmd": c["fg"], "ok": c["muted"], "open": c["amber"]}[kind]
        g = ""
        if glyph:
            gcol = c["green"] if kind == "ok" else c["amber"]
            g = f'<text x="46" y="{y}" font-size="13" fill="{gcol}">{glyph}</text>'
        body = esc(txt)
        if kind == "ok":
            body = body.replace("PASS", f'</tspan><tspan fill="{c["green"]}" font-weight="600">PASS</tspan><tspan>')
            body = f"<tspan>{body}</tspan>"
        if kind == "open":
            body = body.replace("OPEN", f'</tspan><tspan fill="{c["amber"]}" font-weight="700">OPEN</tspan><tspan>')
            body = f"<tspan>{body}</tspan>"
        x = 46 if kind == "cmd" else 68
        lines.append(
            f'<g>{g}'
            f'<text x="{x}" y="{y}" font-size="13" fill="{color}">{body}</text></g>'
        )
    cursor_y = y0 + (len(rows)) * lh
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img"
  aria-label="Ayon Aryan — AI/ML and backend engineer, RV University 2027, open to internships">
<style>{STYLE % dict(mono=MONO)}</style>
<rect width="{W}" height="{H}" rx="12" fill="{c['bg']}" stroke="{c['border']}"/>
<rect x="1" y="1" width="{W-2}" height="40" rx="11" fill="{c['panel']}"/>
<line x1="1" y1="42" x2="{W-1}" y2="42" stroke="{c['border']}"/>
<circle cx="26" cy="21" r="5.5" fill="#FF5F57"/><circle cx="46" cy="21" r="5.5" fill="#FEBC2E"/><circle cx="66" cy="21" r="5.5" fill="#28C840"/>
<text x="{W/2}" y="26" font-size="12" fill="{c['muted']}" text-anchor="middle">ayon-aryan — verification run</text>
<text x="46" y="84" font-size="26" font-weight="700" fill="{c['fg']}">{esc(name)}</text>
<text x="46" y="84" font-size="26" font-weight="700" fill="{c['violet']}" opacity="0"> </text>
{chr(10).join(lines)}
<g>
  <text x="46" y="{cursor_y}" font-size="13" fill="{c['green']}">5 checks · 5 passed · 0 drift · 1 hiring window open</text>
  <rect class="cursor" x="452" y="{cursor_y-11}" width="7" height="14" fill="{c['green']}"/>
</g>
</svg>'''


CARDS = [
    dict(repo="driftbench", title="driftbench", status="BENCHMARK",
         desc=["Do AI coding agents silently break API",
               "contracts? Catches breakage & spec-laundering."],
         tags=["LLM EVAL", "OPENAPI", "PYTHON"]),
    dict(repo="settledrift", title="settledrift", status="100% RUN",
         desc=["Settlement reconciliation agent — deterministic",
               "core + bounded local LLM. 100% on a real run."],
         tags=["FINTECH", "AGENTS", "OLLAMA"]),
    dict(repo="DATABASE-MANAGER", title="database-manager", status="8 ENGINES",
         desc=["Natural language → SQL across 8 DB engines.",
               "Dual-LLM safety pipeline, RBAC, snapshot undo."],
         tags=["TEXT-TO-SQL", "GROQ", "OLLAMA"]),
    dict(repo="graph-rag", title="graph-rag", status="HYBRID RAG",
         desc=["Knowledge graph + FAISS dense retrieval,",
               "fused. Live D3 force-graph visualisation."],
         tags=["RAG", "NETWORKX", "FAISS"]),
    dict(repo="credit-risk-xai", title="credit-risk-xai", status="FAIRNESS",
         desc=["Explainable credit underwriting — SHAP,",
               "FairLearn fairness audits, adverse-action notices."],
         tags=["XAI", "LIGHTGBM", "FAIRLEARN"]),
    dict(repo="GEO_LOCATION_SAVER_APP", title="geo-gps-camera", status="100+ INSTALLS",
         desc=["GPS map camera for Android on the Play Store.",
               "Anti-spoof GPS validation, Compose + CameraX."],
         tags=["ANDROID", "KOTLIN", "COMPOSE"]),
]


def card(t, spec):
    c = THEMES[t]
    W, H = 400, 132
    tag_x, chips = 18, []
    for tag in spec["tags"]:
        w = len(tag) * 6.6 + 16
        chips.append(f'<rect x="{tag_x}" y="{H-34}" width="{w:.0f}" height="20" rx="10" fill="{c["chipbg"]}" stroke="{c["border"]}"/>'
                     f'<text x="{tag_x + w/2:.0f}" y="{H-20}" font-size="9.5" fill="{c["muted"]}" text-anchor="middle" letter-spacing="0.5">{esc(tag)}</text>')
        tag_x += w + 8
    desc = "".join(
        f'<text x="18" y="{66 + i*17}" font-size="11.5" fill="{c["muted"]}">{esc(l)}</text>'
        for i, l in enumerate(spec["desc"]))
    sw = len(spec["status"]) * 6.8 + 14
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(spec['title'])}">
<style>text {{ font-family: {MONO}; }}</style>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="{c['bg']}" stroke="{c['border']}"/>
<rect x="0.5" y="0.5" width="4" height="{H-1}" rx="2" fill="{c['green']}"/>
<text x="18" y="32" font-size="12" fill="{c['green']}">✓</text>
<text x="34" y="32" font-size="15" font-weight="700" fill="{c['fg']}">{esc(spec['title'])}</text>
<rect x="{W-sw-16}" y="18" width="{sw:.0f}" height="19" rx="9.5" fill="none" stroke="{c['amber']}"/>
<text x="{W-16-sw/2:.0f}" y="31" font-size="9" font-weight="600" fill="{c['amber']}" text-anchor="middle" letter-spacing="0.5">{esc(spec['status'])}</text>
{desc}
{''.join(chips)}
</svg>'''


name = "AYON ARYAN"
for t in THEMES:
    (OUT / f"hero-{t}.svg").write_text(hero(t, name))
    for spec in CARDS:
        (OUT / f"card-{spec['repo']}-{t}.svg").write_text(card(t, spec))
print("generated:", len(list(OUT.glob("*.svg"))), "svgs")
