"""Building blocks for the laminated reference cards (cheat sheets).

A cheat sheet lives in content/cheatsheets/<slug>.py and is rendered by scripts/build_notes.py into
public/cheatsheets/<slug>/index.html (plus a PDF built by scripts/build-pdf.mjs).

Helpers:
  Graph   a subway-map git graph (one coloured lane per branch, commits, merges, tags) as inline SVG
  cmd()   a terminal block: one command per line, `# comment` lines and trailing comments dimmed
  box()   one panel on a card (coloured title tab + body)
"""
from html import escape as esc
from zlib import crc32


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


class Diagram:
    """A box-and-arrow diagram (architecture maps, flowcharts). Tones: main / dev / feat / bug / rel / hot / warn / ink.
    node styles: "fill" (filled title + subtitle), "soft" (outlined), "ghost" (dashed, faded), "chip" (small, one line)."""

    def __init__(self, title, width=880, height=300):
        self.title, self.width, self.height = title, width, height
        self.items, self.nodes, self.arrows, self.texts = [], {}, [], []

    def group(self, gid, x, y, w, h, label, tone="ink"):
        self.nodes[gid] = (x, y, w, h)
        self.items.append(f'<g class="grp t-{tone}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>'
                          f'<text x="{x + 10}" y="{y + 16}">{esc(label)}</text></g>')
        return self

    def node(self, nid, x, y, w, h, label, sub=None, tone="ink", style="fill"):
        self.nodes[nid] = (x, y, w, h)
        cx = x + w / 2
        if sub:
            ty, sy = y + h / 2 - 3, y + h / 2 + 12
        else:
            ty, sy = y + h / 2 + 4.5, None
        s = [f'<g class="nd {style} t-{tone}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7"/>',
             f'<text class="nl" x="{cx}" y="{ty}">{esc(label)}</text>']
        if sub:
            s.append(f'<text class="ns" x="{cx}" y="{sy}">{esc(sub)}</text>')
        s.append("</g>")
        self.items.append("".join(s))
        return self

    def raw(self, fragment):
        """Hand-written SVG (e.g. Venn diagrams), drawn with the nodes."""
        self.items.append(fragment)
        return self

    def text(self, x, y, txt, cls="dt", anchor="start"):
        self.texts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{esc(txt)}</text>')
        return self

    def _pt(self, nid, side):
        x, y, w, h = self.nodes[nid]
        return {"r": (x + w, y + h / 2), "l": (x, y + h / 2), "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[side]

    def arrow(self, a, b, label=None, sides="rl", dashed=False, tone="ink", lx=None, ly=None, both=False):
        (x1, y1), (x2, y2) = self._pt(a, sides[0]), self._pt(b, sides[1])
        if sides in ("rl", "lr"):
            dx = (x2 - x1) * 0.5
            d = f"M{x1} {y1} C{x1 + dx} {y1} {x2 - dx} {y2} {x2} {y2}"
        elif sides in ("tb", "bt"):
            dy = (y2 - y1) * 0.5
            d = f"M{x1} {y1} C{x1} {y1 + dy} {x2} {y2 - dy} {x2} {y2}"
        else:
            d = f"M{x1} {y1} L{x2} {y2}"
        dash = " dashed" if dashed else ""
        start = f' marker-start="url(#ah-{tone})"' if both else ""
        self.arrows.append(f'<path class="ar t-{tone}{dash}" d="{d}" marker-end="url(#ah-{tone})"{start}/>')
        if label:
            mx = lx if lx is not None else (x1 + x2) / 2
            my = ly if ly is not None else (y1 + y2) / 2 - 5
            self.arrows.append(f'<text class="al" x="{mx}" y="{my}">{esc(label)}</text>')
        return self

    def svg(self):
        tones = ["main", "dev", "feat", "bug", "rel", "hot", "warn", "ink"]
        marks = "".join(f'<marker id="ah-{t}" class="t-{t}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                        f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z"/></marker>' for t in tones)
        # marker ids must be unique per page when several diagrams share it
        uid = crc32(self.title.encode()) % 100000
        body = "".join(self.items) + "".join(self.arrows) + "".join(self.texts)
        marks = marks.replace('id="ah-', f'id="ah{uid}-')
        body = body.replace("url(#ah-", f"url(#ah{uid}-")
        return (f'<svg class="gg dg" viewBox="0 0 {self.width} {self.height}" role="img" aria-label="{esc(self.title)}">'
                f"<defs>{marks}</defs>{body}</svg>")


def code(text, title=None):
    """A plain code card (YAML, Dockerfile, SQL): no prompts; '#' and '--' comments dimmed."""
    rows = []
    for line in text.strip("\n").split("\n"):
        mark = "  -- " if "  -- " in line else "  # "
        body, sep, com = line.partition(mark)
        if line.lstrip().startswith(("#", "--")):
            rows.append(f'<span class="c">{esc(line)}</span>')
        else:
            rows.append(esc(body) + (f' <span class="c">{mark.strip()} {esc(com)}</span>' if sep else ""))
    head = f'<figcaption>{title}</figcaption>' if title else ""
    return f'<figure class="term plain">{head}<pre><code>' + "\n".join(rows) + "</code></pre></figure>"
