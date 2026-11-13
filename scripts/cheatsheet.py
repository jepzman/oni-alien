"""Building blocks for the laminated reference cards (cheat sheets).

A cheat sheet lives in content/cheatsheets/<slug>.py and is rendered by scripts/build_notes.py into
public/cheatsheets/<slug>/index.html (plus a PDF built by scripts/build-pdf.mjs).

Helpers:
  Graph   a subway-map git graph (one coloured lane per branch, commits, merges, tags) as inline SVG
  cmd()   a terminal block: one command per line, `# comment` lines and trailing comments dimmed
  box()   one panel on a card (coloured title tab + body)
"""
from html import escape as esc


def mono_w(text, size):
    """Rough width of monospace text (IBM Plex Mono is 0.6 em per character)."""
    return len(text) * size * 0.6


class Graph:
    """lanes: [(key, label, colour class, full)] from top to bottom. colour class is one of
    main / dev / feat / rel / hot / bug; full=True draws the lane across the whole graph (long-lived branches)."""

    def __init__(self, title, lanes, width=880, label_w=112, lane_h=48, pad_top=34, pad_bot=30):
        self.title, self.width, self.label_w, self.lane_h = title, width, label_w, lane_h
        self.pad_top, self.pad_bot = pad_top, pad_bot
        self.lanes = {k: dict(i=i, label=l, cls=c, full=f) for i, (k, l, c, f) in enumerate(lanes)}
        self.commits, self.edges, self.spans, self.marks = {}, [], [], []

    def y(self, lane):
        return self.pad_top + self.lanes[lane]["i"] * self.lane_h

    def c(self, cid, x, lane, tag=None, note=None, merge=False, up=False, ghost=False, cls=None):
        """A commit. note: a short label under the dot (up=True puts it above); tag: a version pill above;
        cls: colour it as another branch (e.g. rebased feature commits sitting on develop)."""
        self.commits[cid] = dict(x=x, lane=lane, tag=tag, note=note, merge=merge, up=up, ghost=ghost, cls=cls)
        return self

    def e(self, a, b, dashed=False):
        """An edge from commit a to commit b (branching off or merging in)."""
        self.edges.append((a, b, dashed))
        return self

    def mark(self, x, lane, text, cls="warn"):
        """A callout bubble next to a lane (e.g. "deploy UAT")."""
        self.marks.append((x, lane, text, cls))
        return self

    def svg(self):
        h = self.pad_top + (len(self.lanes) - 1) * self.lane_h + self.pad_bot
        out = [f'<svg class="gg" viewBox="0 0 {self.width} {h}" role="img" aria-label="{esc(self.title)}">']
        # lanes
        for k, ln in self.lanes.items():
            y = self.y(k)
            xs = [c["x"] for c in self.commits.values() if c["lane"] == k]
            if ln["full"]:
                out.append(f'<path class="lane {ln["cls"]}" d="M{self.label_w + 6} {y} H{self.width - 12}"/>')
                out.append(f'<path class="lane-end {ln["cls"]}" d="M{self.width - 18} {y - 5} L{self.width - 10} {y} L{self.width - 18} {y + 5}"/>')
            else:
                out.append(f'<path class="lane-ghost {ln["cls"]}" d="M{self.label_w + 6} {y} H{self.width - 12}"/>')
                if len(xs) > 1:
                    out.append(f'<path class="lane {ln["cls"]}" d="M{min(xs)} {y} H{max(xs)}"/>')
        # edges
        for a, b, dashed in self.edges:
            ca, cb = self.commits[a], self.commits[b]
            x1, y1, x2, y2 = ca["x"], self.y(ca["lane"]), cb["x"], self.y(cb["lane"])
            # an edge takes the colour of the branch it comes from when merging, of the new branch when branching off
            src = self.lanes[ca["lane"]]
            dst = self.lanes[cb["lane"]]
            cls = dst["cls"] if (not dst["full"] and src["full"]) else src["cls"]
            dash = " dashed" if dashed else ""
            if y1 == y2:
                d = f"M{x1} {y1} H{x2}"
            else:
                dx = min(34, (x2 - x1) * 0.55)
                d = f"M{x1} {y1} C{x1 + dx} {y1} {x2 - dx} {y2} {x2} {y2}"
            out.append(f'<path class="edge {cls}{dash}" d="{d}"/>')
        # commits
        for c in self.commits.values():
            x, y, cls = c["x"], self.y(c["lane"]), c["cls"] or self.lanes[c["lane"]]["cls"]
            if c["merge"]:
                out.append(f'<circle class="dot merge {cls}" cx="{x}" cy="{y}" r="8"/><circle class="hole" cx="{x}" cy="{y}" r="3"/>')
            elif c["ghost"]:
                out.append(f'<circle class="dot ghost {cls}" cx="{x}" cy="{y}" r="6"/>')
            else:
                out.append(f'<circle class="dot {cls}" cx="{x}" cy="{y}" r="6.5"/>')
            if c["tag"]:
                w = mono_w(c["tag"], 11) + 14
                out.append(f'<g class="tag"><rect x="{x - w / 2:.1f}" y="{y - 30}" width="{w:.1f}" height="17" rx="8.5"/>'
                           f'<text x="{x}" y="{y - 17.5}">{esc(c["tag"])}</text></g>')
            if c["note"]:
                ny = y - 13 if c["up"] else y + 22
                out.append(f'<text class="note" x="{x}" y="{ny}">{esc(c["note"])}</text>')
        for x, lane, text, cls in self.marks:
            y = self.y(lane)
            w = mono_w(text, 10.5) + 14
            out.append(f'<g class="callout {cls}"><rect x="{x:.1f}" y="{y - 9}" width="{w:.1f}" height="18" rx="4"/>'
                       f'<text x="{x + 7:.1f}" y="{y + 4}">{esc(text)}</text></g>')
        # lane labels last, so they sit on top
        for k, ln in self.lanes.items():
            y = self.y(k)
            w = mono_w(ln["label"], 11.5) + 14
            out.append(f'<g class="lab {ln["cls"]}"><rect x="4" y="{y - 10.5}" width="{w:.1f}" height="21" rx="5"/>'
                       f'<text x="11" y="{y + 4}">{esc(ln["label"])}</text></g>')
        out.append("</svg>")
        return "".join(out)


def cmd(text, title=None):
    """A terminal block. Lines starting with '#' are comments; '  # ' starts a trailing comment;
    lines starting with '>' are output / outcomes."""
    rows = []
    for line in text.strip("\n").split("\n"):
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            rows.append(f'<span class="c">{esc(s)}</span>')
        elif s.startswith(">"):
            rows.append(f'<span class="o">{esc(s[1:].strip())}</span>')
        else:
            code, _, com = s.partition("  # ")
            row = f'<span class="p" aria-hidden="true">$</span>{esc(code)}'
            if com:
                row += f' <span class="c"># {esc(com)}</span>'
            rows.append(row)
    head = f'<figcaption>{title}</figcaption>' if title else ""
    return f'<figure class="term">{head}<pre><code>' + "\n".join(rows) + "</code></pre></figure>"


def box(title, body, tone="", span="", tag=None):
    """tone: main / dev / feat / rel / hot / bug / warn / ink (title tab colour); span: '' | 'wide' | 'full'."""
    cls = " ".join(x for x in ["box", f"t-{tone}" if tone else "", span] if x)
    t = f'<span class="box-tag">{tag}</span>' if tag else ""
    return f'<section class="{cls}"><h3>{title}{t}</h3>\n<div class="box-in">{body}</div></section>'
