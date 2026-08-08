#!/usr/bin/env python3
"""Build the shared Hall of Fame Studio frosted-glass diagram system."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams"
PROFILE = "buffett"
WIDTH = 1400
HEIGHT = 820

INK = "#f0e5cf"
MUTED = "#b9aa8f"
BRONZE = "#c5a875"
BRONZE_DARK = "#806b4e"
COPPER = "#874139"
CHARCOAL = "#25211c"
DEEP = "#171411"
PARCHMENT = "#eadcc2"
PARCHMENT_INK = "#31271e"
MONO = "Consolas,'Courier New',monospace"
SERIF = "Georgia,'Times New Roman','Microsoft YaHei',serif"
SANS = "'Segoe UI','Microsoft YaHei',sans-serif"


def esc(value: object) -> str:
    return escape(str(value), quote=True)


def svg_text(
    x: float,
    y: float,
    value: object,
    size: float = 18,
    fill: str = INK,
    family: str = SERIF,
    weight: str = "400",
    anchor: str | None = None,
    spacing: float | None = None,
    opacity: float | None = None,
) -> str:
    attrs = [
        f'x="{x}"',
        f'y="{y}"',
        f'fill="{fill}"',
        f'font-family="{family}"',
        f'font-size="{size}"',
        f'font-weight="{weight}"',
    ]
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if spacing is not None:
        attrs.append(f'letter-spacing="{spacing}"')
    if opacity is not None:
        attrs.append(f'opacity="{opacity}"')
    return f'<text {" ".join(attrs)}>{esc(value)}</text>'


def panel(x: float, y: float, w: float, h: float, light: bool = False, accent: bool = False) -> str:
    fill = "url(#glass-light)" if light else "url(#glass)"
    stroke = "url(#edge)" if accent else BRONZE
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.6" stroke-opacity=".78"/>'
        f'<rect x="{x + 9}" y="{y + 9}" width="{w - 18}" height="{h - 18}" rx="16" '
        f'fill="none" stroke="{PARCHMENT}" stroke-opacity=".12"/>'
    )


def line(x1: float, y1: float, x2: float, y2: float, color: str = BRONZE, dashed: bool = False) -> str:
    dash = ' stroke-dasharray="7 8"' if dashed else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.8" opacity=".78"{dash}/>'


def arrow(x1: float, y1: float, x2: float, y2: float, color: str = BRONZE) -> str:
    return (
        f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2" '
        f'stroke-linecap="round" marker-end="url(#arrow)"/>'
    )


def header(label: str, title: str, subtitle: str) -> str:
    return (
        svg_text(70, 52, f"HALL OF FAME STUDIO  /  {label}", 15, BRONZE, MONO, "500", spacing=2.4)
        + svg_text(70, 94, title, 31, INK, SERIF, "700")
        + svg_text(70, 127, subtitle, 18, MUTED, SANS)
    )


def footer(note: str) -> str:
    return svg_text(70, 787, note, 14, MUTED, MONO, "400", spacing=1.1)


def document(label: str, title: str, subtitle: str, body: str, note: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">{esc(title)}</title>
  <desc id="desc">{esc(subtitle)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#171411"/>
      <stop offset=".52" stop-color="#302a22"/>
      <stop offset="1" stop-color="#1f1b17"/>
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#625747" stop-opacity=".58"/>
      <stop offset=".48" stop-color="#332c24" stop-opacity=".78"/>
      <stop offset="1" stop-color="#191612" stop-opacity=".84"/>
    </linearGradient>
    <linearGradient id="glass-light" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#eadcc2" stop-opacity=".92"/>
      <stop offset="1" stop-color="#bfa77b" stop-opacity=".86"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#f1e6cf"/>
      <stop offset=".5" stop-color="#c5a875"/>
      <stop offset="1" stop-color="#6e5a41"/>
    </linearGradient>
    <filter id="grain" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency=".72" numOctaves="2" seed="19" result="noise"/>
      <feColorMatrix in="noise" type="saturate" values="0" result="grain"/>
      <feComponentTransfer in="grain">
        <feFuncA type="table" tableValues="0 .18"/>
      </feComponentTransfer>
      <feBlend in="SourceGraphic" in2="grain" mode="screen"/>
    </filter>
    <filter id="soft-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 0 L10 5 L0 10 Z" fill="{BRONZE}"/>
    </marker>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="26" fill="url(#bg)"/>
  <rect x="24" y="24" width="{WIDTH - 48}" height="{HEIGHT - 48}" rx="20" fill="none" stroke="url(#edge)" stroke-width="1.8" stroke-opacity=".72"/>
  <path d="M48 86V48H86M1314 48H1352V86M48 734V772H86M1314 772H1352V734" fill="none" stroke="{PARCHMENT}" stroke-opacity=".52" stroke-width="1.4"/>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="26" fill="#eadcc2" opacity=".12" filter="url(#grain)"/>
  {header(label, title, subtitle)}
  {body}
  {footer(note)}
</svg>
"""


def method_lens(profile: dict) -> str:
    method = profile["method"]
    body = [panel(70, 180, 270, 500), panel(390, 180, 520, 500), panel(970, 180, 360, 500, light=True, accent=True)]
    body.append(svg_text(105, 225, method["input_label"], 15, BRONZE, MONO, "600", spacing=1.8))
    for index, item in enumerate(method["input_items"]):
        body.append(svg_text(105, 278 + index * 48, item, 21, INK, SERIF, "600"))
    body.append(svg_text(105, 580, method["input_note"], 16, MUTED, SANS))
    if method.get("input_note2"):
        body.append(svg_text(105, 606, method["input_note2"], 16, MUTED, SANS))
    body.append(arrow(350, 430, 380, 430))
    body.append(svg_text(425, 225, "ORDER OF OPERATIONS / 顺序", 15, BRONZE, MONO, "600", spacing=1.6))
    for index, (title, subtitle) in enumerate(method["steps"]):
        y = 260 + index * 92
        body.append(f'<rect x="420" y="{y}" width="460" height="72" rx="16" fill="#211c17" fill-opacity=".78" stroke="{BRONZE}" stroke-opacity=".52"/>')
        body.append(f'<circle cx="457" cy="{y + 36}" r="18" fill="{COPPER}" opacity=".92"/>')
        body.append(svg_text(457, y + 42, index + 1, 16, INK, MONO, "700", "middle"))
        body.append(svg_text(495, y + 31, title, 19, INK, SERIF, "700"))
        body.append(svg_text(495, y + 55, subtitle, 15, MUTED, SANS))
    body.append(arrow(920, 430, 960, 430))
    body.append(svg_text(1005, 225, method["output_label"], 15, COPPER, MONO, "700", spacing=1.8))
    body.append(svg_text(1005, 300, method["output_title"], 24, PARCHMENT_INK, SERIF, "700"))
    body.append(svg_text(1005, 338, method["output_subtitle"], 17, "#675440", SANS))
    for index, item in enumerate(method["output_items"]):
        body.append(svg_text(1005, 408 + index * 42, f"—  {item}", 18, PARCHMENT_INK, SERIF))
    body.append(line(1005, 578, 1287, 578, COPPER))
    body.append(svg_text(1005, 616, method["output_note"], 15, "#675440", SANS))
    return document(
        profile["label"],
        method["title"],
        method["subtitle"],
        "".join(body),
        method["footer"],
    )


def evidence_chain(profile: dict) -> str:
    evidence = profile["evidence"]
    body = []
    positions = [(70, 185), (500, 185), (930, 185), (70, 425), (500, 425), (930, 425)]
    for index, (x, y) in enumerate(positions):
        card = evidence["cards"][index]
        body.append(panel(x, y, 370, 170, accent=index in (0, 5)))
        body.append(svg_text(x + 30, y + 36, card["label"], 14, BRONZE, MONO, "600", spacing=1.5))
        value_size = 32 if len(str(card["value"])) > 5 else 38
        body.append(svg_text(x + 30, y + 94, card["value"], value_size, INK, SERIF, "700"))
        body.append(svg_text(x + 205, y + 86, card["line1"], 17, INK, SANS))
        body.append(svg_text(x + 205, y + 116, card["line2"], 15, MUTED, SANS))
        if index < len(positions) - 1:
            next_x, next_y = positions[index + 1]
            if next_y == y:
                body.append(arrow(x + 380, y + 85, next_x - 12, next_y + 85))
            else:
                body.append(arrow(x + 185, y + 180, x + 185, next_y - 12))
    body.append(svg_text(70, 660, evidence["closing"], 19, INK, SERIF, "600"))
    body.append(svg_text(70, 697, evidence["closing_zh"], 16, MUTED, SANS))
    return document(profile["label"], evidence["title"], evidence["subtitle"], "".join(body), evidence["footer"])


def capability_clusters(profile: dict) -> str:
    capabilities = profile["capabilities"]
    body = []
    positions = [(70, 180), (830, 180), (70, 505), (830, 505)]
    for index, (x, y) in enumerate(positions):
        cluster = capabilities["clusters"][index]
        body.append(panel(x, y, 500, 235))
        body.append(svg_text(x + 32, y + 43, cluster["label"], 14, BRONZE, MONO, "600", spacing=1.35))
        for item_index, item in enumerate(cluster["items"]):
            body.append(svg_text(x + 32, y + 95 + item_index * 35, item, 18, INK, SERIF, "600" if item_index == 0 else "400"))
    body.append(line(570, 297, 630, 390, BRONZE_DARK, True))
    body.append(line(830, 297, 770, 390, BRONZE_DARK, True))
    body.append(line(570, 622, 630, 525, BRONZE_DARK, True))
    body.append(line(830, 622, 770, 525, BRONZE_DARK, True))
    body.append(panel(515, 365, 370, 145, light=True, accent=True))
    body.append(svg_text(700, 410, capabilities["core"][0], 18, COPPER, MONO, "700", "middle", 1.7))
    body.append(svg_text(700, 450, capabilities["core"][1], 28, PARCHMENT_INK, SERIF, "700", "middle"))
    body.append(svg_text(700, 480, capabilities["core"][2], 15, "#675440", SANS, "400", "middle"))
    return document(profile["label"], capabilities["title"], capabilities["subtitle"], "".join(body), capabilities["footer"])


def mode_router(profile: dict) -> str:
    modes = profile["modes"]
    body = []
    positions = [70, 395, 720, 1045]
    for index, x in enumerate(positions):
        mode = modes[index]
        body.append(panel(x, 185, 285, 455, accent=index == 3))
        body.append(svg_text(x + 28, 230, mode["label"], 14, COPPER if index == 3 else BRONZE, MONO, "700", spacing=1.5))
        body.append(svg_text(x + 28, 294, mode["title"], 25, INK, SERIF, "700"))
        for line_index, value in enumerate(mode["lines"]):
            body.append(svg_text(x + 28, 352 + line_index * 32, value, 16, MUTED, SANS))
        body.append(line(x + 28, 470, x + 257, 470, COPPER if index == 3 else BRONZE_DARK))
        body.append(svg_text(x + 28, 520, mode["rule"], 16, INK, SERIF, "600"))
        body.append(svg_text(x + 28, 566, mode["bound"], 15, MUTED, SANS))
        body.append(svg_text(x + 28, 595, mode["bound2"], 15, MUTED, SANS))
    return document(profile["label"], modes[0]["diagram_title"], modes[0]["diagram_subtitle"], "".join(body), modes[0]["footer"])


def quality_loop(profile: dict) -> str:
    quality = profile["quality"]
    body = [
        panel(70, 245, 250, 190, light=True),
        panel(380, 190, 570, 300),
        panel(1020, 205, 300, 125, light=True, accent=True),
        panel(1020, 380, 300, 125, accent=True),
        arrow(330, 340, 365, 340),
        arrow(965, 268, 1005, 268),
        arrow(965, 425, 1005, 425, COPPER),
        f'<path d="M1170 530 C1170 615 655 620 655 520" fill="none" stroke="{COPPER}" stroke-width="1.8" stroke-dasharray="8 8" marker-end="url(#arrow)"/>',
    ]
    body.append(svg_text(195, 290, "DRAFT", 15, COPPER, MONO, "700", "middle", 1.5))
    body.append(svg_text(195, 350, "Answer", 28, PARCHMENT_INK, SERIF, "700", "middle"))
    body.append(svg_text(195, 386, "method + relationship", 15, "#675440", SANS, "400", "middle"))
    body.append(svg_text(420, 235, quality["label"], 15, BRONZE, MONO, "700", spacing=1.7))
    for index, check in enumerate(quality["checks"]):
        body.append(svg_text(420, 290 + index * 38, f"✓  {check}", 17, INK, SERIF))
    body.append(svg_text(1170, 250, "CLEAR", 14, COPPER, MONO, "700", "middle", 1.4))
    body.append(svg_text(1170, 294, "Release", 28, PARCHMENT_INK, SERIF, "700", "middle"))
    body.append(svg_text(1170, 425, "VIOLATION", 14, COPPER, MONO, "700", "middle", 1.4))
    body.append(svg_text(1170, 469, "Revise or fallback", 22, INK, SERIF, "700", "middle"))
    return document(profile["label"], quality["title"], quality["subtitle"], "".join(body), quality["footer"])


def studio_network(profile: dict) -> str:
    network = profile["network"]
    body = [
        panel(70, 190, 320, 390),
        panel(515, 175, 370, 420, light=True, accent=True),
        panel(1010, 175, 320, 420),
        panel(300, 650, 800, 78, light=True),
        arrow(400, 385, 495, 385),
        arrow(905, 385, 990, 385),
    ]
    body.append(svg_text(105, 235, "DIRECT USE / 单独使用", 14, BRONZE, MONO, "700", spacing=1.45))
    body.append(svg_text(105, 305, network["direct_title"], 25, INK, SERIF, "700"))
    for index, item in enumerate(network["direct_items"]):
        body.append(svg_text(105, 370 + index * 42, f"—  {item}", 17, MUTED, SANS))
    body.append(svg_text(700, 235, network["agent_label"], 15, COPPER, MONO, "700", "middle", 1.6))
    body.append(svg_text(700, 315, network["agent_title"], 29, PARCHMENT_INK, SERIF, "700", "middle"))
    body.append(svg_text(700, 355, network["agent_subtitle"], 17, "#675440", SANS, "400", "middle"))
    body.append(line(595, 392, 805, 392, COPPER))
    body.append(svg_text(700, 440, "ONE DISTINCT POINT OF VIEW", 14, "#675440", MONO, "700", "middle", 1.2))
    body.append(svg_text(700, 480, network["agent_note"], 14, PARCHMENT_INK, SERIF, "600", "middle"))
    body.append(svg_text(1045, 220, "STUDIO NETWORK / 网络", 14, BRONZE, MONO, "700", spacing=1.45))
    for index, item in enumerate(network["studio_items"]):
        y = 290 + index * 62
        body.append(f'<rect x="1045" y="{y}" width="250" height="42" rx="12" fill="#211c17" fill-opacity=".74" stroke="{BRONZE}" stroke-opacity=".5"/>')
        body.append(svg_text(1065, y + 27, item[0], 16, INK, SERIF, "600"))
        body.append(svg_text(1280, y + 27, item[1], 13, MUTED, MONO, "400", "end"))
    body.append(svg_text(700, 682, network["footer_label"], 15, COPPER, MONO, "700", "middle", 1.5))
    body.append(svg_text(700, 713, network["footer_text"], 18, PARCHMENT_INK, SERIF, "700", "middle"))
    return document(profile["label"], network["title"], network["subtitle"], "".join(body), network["note"])


PROFILE_DATA = {
    "buffett": {
        "label": "AGENT 002  /  WARREN BUFFETT",
        "method": {
            "title": "Calm is not passivity. It is a better order of operations.",
            "subtitle": "平静不是被动，而是把判断重新排成更好的顺序",
            "input_label": "INPUT / 热点输入",
            "input_items": ["Urgency", "Social proof", "Headline noise", "Sunk cost", "Leverage", "Permanent loss"],
            "input_note": "A decision arrives hot.",
            "input_note2": "The bar stays high.",
            "steps": [
                ("What is known?", "Facts · estimates · inferences · unknowns"),
                ("What can cause permanent loss?", "Impairment · leverage · forced sale · trust"),
                ("What can be made reversible?", "Stage · cap · test · preserve liquidity"),
                ("What is the next-best use?", "Capital · time · attention · reputation"),
            ],
            "output_label": "OUTPUT / 可检验决策",
            "output_title": "Durable decision",
            "output_subtitle": "经得起复核的决定",
            "output_items": ["explicit downside", "preserved options", "named alternative", "falsifier + review"],
            "output_note": "owner · patience · margin of safety",
            "footer": "VOLATILITY IS NOT THE SAME AS PERMANENT LOSS · PATIENCE STILL REQUIRES A REVIEW DATE",
        },
        "evidence": {
            "title": "The method is compiled from evidence, not borrowed from a reputation",
            "subtitle": "方法从证据逐层编译，而不是借用名声临场表演",
            "cards": [
                {"label": "01 · SOURCE", "value": "46", "line1": "documented records", "line2": "documented-real-person"},
                {"label": "02 · OBSERVE", "value": "56", "line1": "atomic moments", "line2": "different contexts"},
                {"label": "03 · CLAIM", "value": "11", "line1": "bounded claims", "line2": "counterevidence included"},
                {"label": "04 · RUNTIME", "value": "Rules", "line1": "modes + restraints", "line2": "method and shadow"},
                {"label": "05 · TEST", "value": "12", "line1": "package checks", "line2": "offline contract suite"},
                {"label": "06 · OBSERVE", "value": "Behavior", "line1": "decision behavior", "line2": "reviewable outputs"},
            ],
            "closing": "A missing fact stays missing; it never becomes a confident transaction.",
            "closing_zh": "缺失的事实保持缺失，不会被包装成自信的交易结论。",
            "footer": "SOURCE → OBSERVATION → CLAIM → RUNTIME RULE → TEST → OBSERVED BEHAVIOR",
        },
        "capabilities": {
            "title": "The person chooses the tools. The tools do not replace the owner judgment.",
            "subtitle": "人物选择工具，工具不能反过来替代所有者判断",
            "core": ["WARREN BUFFETT", "LONG-TERM OWNER", "steady · candid · option-preserving"],
            "clusters": [
                {"label": "BUSINESS QUALITY · 3", "items": ["Analyze Business Quality", "Map Economic Moat", "Evaluate Management Stewardship"]},
                {"label": "ECONOMICS + VALUE · 3", "items": ["Normalize Owner Earnings", "Estimate Intrinsic Value", "Demand Margin of Safety"]},
                {"label": "CAPITAL + DOWNSIDE · 4", "items": ["Allocate Capital", "Weigh Opportunity Cost", "Stress-test Downside + Leverage", "Construct Concentrated Portfolio"]},
                {"label": "JUDGMENT + COMMUNICATION · 2", "items": ["Assess Circle of Competence", "Communicate with Owner Candor", "Boundaries that keep helping."]},
            ],
            "footer": "12 CALLABLE SKILLS · EACH HAS AN ARTIFACT, STOP CONDITION, FAILURE MODE, AND SELF-REVIEW",
        },
        "modes": [
            {"diagram_title": "One person. Four different kinds of help.", "diagram_subtitle": "人格核心始终在线，变化的是工作方法与 Skill 边界", "label": "RELATIONAL / 关系", "title": "See the person.", "lines": ["Ordinary conversation", "vulnerability · uncertainty"], "rule": "0 hard Skills", "bound": "No memo.", "bound2": "Stay at the table.", "footer": "SKILL ACTIVATION CHANGES THE METHOD, NEVER THE HUMAN RELATIONSHIP"},
            {"diagram_title": "", "diagram_subtitle": "", "label": "EXPLORATORY / 探索", "title": "Contribute first.", "lines": ["Ideas · unfamiliar fields", "learning · vague plans"], "rule": "0 by default", "bound": "Give 2–3 concrete starts.", "bound2": "Ask one real question.", "footer": ""},
            {"diagram_title": "", "diagram_subtitle": "", "label": "TASK / 任务", "title": "Make the artifact.", "lines": ["Analysis · comparison", "decision · owner memo"], "rule": "1–3 routed Skills", "bound": "Named output.", "bound2": "STOP + self-review.", "footer": ""},
            {"diagram_title": "", "diagram_subtitle": "", "label": "HIGH-STAKES / 高风险", "title": "Protect survival.", "lines": ["Specific securities", "major capital · irreversible acts"], "rule": "VERIFY FIRST", "bound": "Current evidence + review.", "bound2": "No promise. No transaction.", "footer": ""},
        ],
        "quality": {
            "title": "A good voice is not enough. The decision must survive inspection.",
            "subtitle": "声音好听还不够，决定必须经得起检查",
            "label": "BUFFETT QUALITY GATE",
            "checks": ["facts, estimates, unknowns separated", "no fabricated memory or current holdings", "no competence-based social exit", "no cheap reassurance or guaranteed return", "required artifact, downside, review, STOP"],
            "footer": "REPAIR THE RESPONSIBLE UPSTREAM RULE · DO NOT POLISH A BROKEN CLAIM",
        },
        "network": {
            "title": "Standalone when you need one mind. Composable when the work needs a team.",
            "subtitle": "需要一个判断时单独工作，需要协作时进入受治理的圆桌",
            "direct_title": "Warren Buffett",
            "direct_items": ["one Agent", "long-term owner lens", "open-source package"],
            "agent_label": "AGENT 002",
            "agent_title": "DEEP AGENT",
            "agent_subtitle": "长期所有者与资本配置伙伴",
            "agent_note": "A distinct judgment system, not a quote machine.",
            "studio_items": [["Talent Market", "dossier"], ["Persona Chat", "fingerprint"], ["Project Team", "review"], ["Proof System", "revision"]],
            "footer_label": "ROUND TABLE / 共同项目目标",
            "footer_text": "contribute → disagree → review → reintegrate",
            "note": "ONE AGENT ENTERS THE STUDIO WITHOUT LOSING ITS EVIDENCE, METHOD, OR BOUNDARIES",
        },
    },
}


def main() -> None:
    profile = PROFILE_DATA[PROFILE]
    OUT.mkdir(parents=True, exist_ok=True)
    diagrams = {
        "01-method-lens.svg": method_lens(profile),
        "02-evidence-chain.svg": evidence_chain(profile),
        "03-capability-clusters.svg": capability_clusters(profile),
        "04-mode-router.svg": mode_router(profile),
        "05-quality-loop.svg": quality_loop(profile),
        "06-studio-network.svg": studio_network(profile),
    }
    for stale in OUT.glob("*.svg"):
        if stale.name not in diagrams:
            stale.unlink()
    for name, content in diagrams.items():
        (OUT / name).write_text(content, encoding="utf-8", newline="\n")
        print(f"Built assets/diagrams/{name}")


if __name__ == "__main__":
    main()
