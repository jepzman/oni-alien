"""Hand-drawn SVG helpers (Doodle + icon library) and a tiny code highlighter, shared by every journal."""
import html
import math
import re


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- doodles
class Doodle:
    """Tiny helper for hand-drawn SVG: shapes go in a wobbly group, text stays crisp."""

    def __init__(self, w, h, label, caption="", small=False):
        self.w, self.h, self.label, self.caption, self.small = w, h, label, caption, small
        self.shapes, self.texts, self.defs = [], [], []

    # shapes ------------------------------------------------------
    def raw(self, svg):
        self.shapes.append(svg)
        return self

    def rawtext(self, svg):
        self.texts.append(svg)
        return self

    def box(self, x, y, w, h, label=None, fill="blue", sub=None, stroke="", dash=False, size=None, rx=10, subsize=17):
        cls = f"d f-{fill}" + (f" d-{stroke}" if stroke else "") + (" d-dash" if dash else "")
        self.shapes.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>')
        cx = x + w / 2
        if label:
            ly = y + h / 2 + (7 if not sub else -4)
            fs = f' font-size="{size}"' if size else ""
            tcls = "t-head" + (f" t-{stroke}" if stroke in ("red", "green", "pen") else "")
            self.texts.append(f'<text class="{tcls}" x="{cx:g}" y="{ly:g}" text-anchor="middle"{fs}>{esc(label)}</text>')
        if sub:
            self.texts.append(f'<text class="t" x="{cx:g}" y="{y + h / 2 + 20:g}" text-anchor="middle" font-size="{subsize}">{esc(sub)}</text>')
        return self

    def circle(self, cx, cy, r, fill="paper", stroke="", label=None, sub=None):
        cls = f"d f-{fill}" + (f" d-{stroke}" if stroke else "")
        self.shapes.append(f'<circle class="{cls}" cx="{cx}" cy="{cy}" r="{r}"/>')
        if label:
            self.texts.append(f'<text class="t-head" x="{cx}" y="{cy + (7 if not sub else -4)}" text-anchor="middle">{esc(label)}</text>')
        if sub:
            self.texts.append(f'<text class="t" x="{cx}" y="{cy + 20}" text-anchor="middle" font-size="16">{esc(sub)}</text>')
        return self

    def db(self, cx, y, label=None, w=68, h=40, fill="paper", stroke=""):
        rx = w / 2
        cls = f"d d-thin f-{fill}" + (f" d-{stroke}" if stroke else "")
        self.shapes.append(
            f'<path class="{cls}" d="M{cx - rx:g} {y} v{h} a{rx:g} 9 0 0 0 {w} 0 v-{h}"/>'
            f'<ellipse class="{cls}" cx="{cx}" cy="{y}" rx="{rx:g}" ry="9"/>')
        if label:
            self.texts.append(f'<text class="t t-soft" x="{cx}" y="{y + h + 30}" text-anchor="middle" font-size="16">{esc(label)}</text>')
        return self

    def msgs(self, x, y, n, fill="y", size=18, gap=6, stroke=""):
        """A row of little message envelopes / queue items."""
        for i in range(n):
            xx = x + i * (size + gap)
            cls = f"d d-thin f-{fill}" + (f" d-{stroke}" if stroke else "")
            self.shapes.append(f'<rect class="{cls}" x="{xx}" y="{y}" width="{size}" height="{size * .72:g}" rx="2"/>'
                               f'<path class="d d-thin" d="M{xx} {y} l{size / 2:g} {size * .4:g} l{size / 2:g} -{size * .4:g}"/>')
        return self

    def line(self, d, color="", dash=False, thin=False):
        cls = "d" + (f" d-{color}" if color else "") + (" d-dash" if dash else "") + (" d-thin" if thin else "")
        self.shapes.append(f'<path class="{cls}" d="{d}"/>')
        return self

    def arrow(self, x1, y1, x2, y2, color="", dash=False, label=None, lx=None, ly=None, anchor="middle",
              curve=None, both=False, lcls="t-s"):
        cls = "d" + (f" d-{color}" if color else "") + (" d-dash" if dash else "")
        if curve:
            cx, cy = curve
            d = f"M{x1} {y1} Q{cx} {cy} {x2} {y2}"
            fx, fy = cx, cy
            bx, by = cx, cy
        else:
            d = f"M{x1} {y1} L{x2} {y2}"
            fx, fy, bx, by = x1, y1, x2, y2
        self.shapes.append(f'<path class="{cls}" d="{d}"/>')
        solid = "d" + (f" d-{color}" if color else "")
        self.shapes.append(f'<path class="{solid}" d="{self._head(fx, fy, x2, y2)}"/>')
        if both:
            self.shapes.append(f'<path class="{solid}" d="{self._head(bx, by, x1, y1)}"/>')
        if label:
            if lx is None:
                lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 - 10
            tc = lcls + (f" t-{color}" if color in ("red", "green") else "")
            self.texts.append(f'<text class="{tc}" x="{lx:g}" y="{ly:g}" text-anchor="{anchor}">{esc(label)}</text>')
        return self

    @staticmethod
    def _head(fx, fy, x, y, size=12):
        a = math.atan2(y - fy, x - fx)
        p1 = (x - size * math.cos(a - .45), y - size * math.sin(a - .45))
        p2 = (x - size * math.cos(a + .45), y - size * math.sin(a + .45))
        return f"M{p1[0]:.1f} {p1[1]:.1f} L{x} {y} L{p2[0]:.1f} {p2[1]:.1f}"

    def text(self, x, y, s, cls="t", anchor="middle", size=None):
        fs = f' font-size="{size}"' if size else ""
        self.texts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}"{fs}>{esc(s)}</text>')
        return self

    def note(self, x, y, s, color="", anchor="middle", size=None):
        return self.text(x, y, s, "t-s" + (f" t-{color}" if color else ""), anchor, size)

    def head(self, x, y, s, anchor="middle", size=None, color=""):
        return self.text(x, y, s, "t-head" + (f" t-{color}" if color else ""), anchor, size)

    def icon(self, name, x, y, s=1.0, color="", fill=None):
        body = ICONS[name]
        cls = "d" + (f" d-{color}" if color else "")
        if fill:
            body = body.replace('class="F"', f'class="f-{fill}"')
        body = body.replace('class="F"', 'class="f-paper"')
        self.shapes.append(f'<g transform="translate({x} {y}) scale({s})"><g class="{cls}">{body}</g></g>')
        return self

    def table(self, x, y, name, cols, w=170, fill="y", row=26, hl=(), strike=(), soft=(), stroke="", size=16):
        """A database table drawn as a card: a filled header row, then one line per column.
        hl / strike / soft are indexes of rows to mark green, cross out in red, or grey out."""
        h = 32 + row * len(cols)
        cls = "d d-thin" + (f" d-{stroke}" if stroke else "")
        self.shapes.append(f'<rect class="{cls} f-paper" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>')
        self.shapes.append(f'<path class="{cls} f-{fill}" d="M{x} {y + 4} a4 4 0 0 1 4 -4 h{w - 8} a4 4 0 0 1 4 4 v28 h-{w} z"/>')
        self.texts.append(f'<text class="t-head" x="{x + w / 2:g}" y="{y + 23}" text-anchor="middle" font-size="{size + 1}">{esc(name)}</text>')
        for i, c in enumerate(cols):
            ry = y + 32 + i * row
            if i:
                self.shapes.append(f'<path class="d d-thin d-soft" d="M{x + 6} {ry} h{w - 12}"/>')
            if i in hl:
                self.shapes.append(f'<rect class="f-hl" x="{x + 3}" y="{ry + 2}" width="{w - 6}" height="{row - 4}" rx="2" style="stroke:none"/>')
            tc = "t" + (" t-soft" if i in soft else "") + (" t-red" if i in strike else "")
            self.texts.append(f'<text class="{tc}" x="{x + 10}" y="{ry + row / 2 + 6:g}" font-size="{size}">{esc(c)}</text>')
            if i in strike:
                self.shapes.append(f'<path class="d d-red" d="M{x + 6} {ry + row / 2:g} h{w - 12}"/>')
        return self

    def html(self):
        shapes = "".join(self.shapes)
        texts = "".join(self.texts)
        swipe = "" if self.small else '<p class="swipe">← swipe to see the whole drawing →</p>'
        cap = f"<figcaption>{self.caption}</figcaption>" if self.caption else ""
        cls = "fig fig--small" if self.small else "fig"
        return (f'<figure class="{cls}"><div class="fig-scroll"><svg viewBox="0 0 {self.w} {self.h}" role="img" '
                f'aria-label="{esc(self.label)}"><g class="rough">{shapes}</g>{texts}</svg></div>{swipe}{cap}</figure>')


# Icons are drawn in a ~60×60 box at the origin. class="F" marks a fill that can be recoloured.
ICONS = {
    "envelope": '<rect class="F" x="0" y="10" width="60" height="40" rx="3"/><path d="M0 12 L30 34 L60 12"/>',
    "truck": '<rect class="F" x="0" y="10" width="40" height="30" rx="3"/><path class="F" d="M40 20 h12 l8 10 v10 h-20 z"/><circle class="F" cx="12" cy="44" r="6"/><circle class="F" cx="48" cy="44" r="6"/>',
    "clock": '<circle class="F" cx="30" cy="30" r="26"/><path d="M30 14 V30 H42"/>',
    "lock": '<rect class="F" x="8" y="26" width="44" height="32" rx="4"/><path d="M18 26 v-8 a12 12 0 0 1 24 0 v8 M30 38 v8"/>',
    "key": '<circle class="F" cx="14" cy="30" r="11"/><path d="M25 30 h32 M48 30 v9 M55 30 v6"/>',
    "crown": '<path class="F" d="M4 46 L8 14 L20 30 L30 8 L40 30 L52 14 L56 46 z"/><path d="M4 52 h52"/>',
    "server": '<rect class="F" x="0" y="0" width="58" height="22" rx="3"/><rect class="F" x="0" y="28" width="58" height="22" rx="3"/><path d="M8 11 h14 M8 39 h14"/><circle cx="48" cy="11" r="2"/><circle cx="48" cy="39" r="2"/>',
    "phone": '<rect class="F" x="16" y="0" width="30" height="56" rx="6"/><path d="M26 48 h10"/>',
    "cup": '<path class="F" d="M6 16 h40 v20 a20 20 0 0 1 -40 0 z"/><path d="M46 22 h6 a7 7 0 0 1 0 14 h-7 M14 4 q4 5 0 9 M26 2 q4 5 0 9"/>',
    "bell": '<path class="F" d="M10 44 q0 -30 20 -30 q20 0 20 30 z"/><path d="M4 46 h52 M30 8 v6 M26 50 a4 4 0 0 0 8 0"/>',
    "ledger": '<rect class="F" x="4" y="0" width="52" height="60" rx="3"/><path d="M14 12 h32 M14 22 h32 M14 32 h32 M14 42 h22"/>',
    "parcel": '<rect class="F" x="4" y="14" width="52" height="40" rx="2"/><path d="M4 26 h52 M30 14 v40"/>',
    "ship": '<path class="F" d="M0 30 h80 l-10 22 h-60 z"/><path d="M20 30 v22 M40 30 v22 M60 30 v22 M34 30 v-18 h14 v18"/>',
    "tower": '<path d="M30 60 L22 20 h16 L30 60 M24 40 h12"/><circle class="F" cx="30" cy="14" r="5"/><path d="M18 6 a16 16 0 0 0 0 16 M42 6 a16 16 0 0 1 0 16 M10 0 a26 26 0 0 0 0 28 M50 0 a26 26 0 0 1 0 28"/>',
    "board": '<rect class="F" x="0" y="0" width="70" height="46" rx="3"/><path d="M14 46 v14 M56 46 v14"/><rect x="8" y="8" width="20" height="14" class="F"/><rect x="38" y="10" width="22" height="12" class="F"/><path d="M10 32 h48"/>',
    "turnstile": '<rect class="F" x="0" y="20" width="16" height="40" rx="2"/><path d="M16 34 h30 M16 34 l18 -18 M16 34 l18 18"/><circle class="F" cx="16" cy="34" r="5"/>',
    "bucket": '<path class="F" d="M6 18 h48 l-6 38 h-36 z"/><path d="M6 18 q24 -22 48 0"/><circle class="F" cx="22" cy="34" r="5"/><circle class="F" cx="36" cy="40" r="5"/><circle class="F" cx="28" cy="46" r="5"/>',
    "fridge": '<rect class="F" x="6" y="0" width="44" height="64" rx="5"/><path d="M6 24 h44 M14 8 v10 M14 30 v14"/>',
    "store": '<rect class="F" x="4" y="22" width="60" height="38"/><path class="F" d="M0 22 l8 -16 h52 l8 16 z"/><rect x="26" y="38" width="16" height="22"/>',
    "book": '<path class="F" d="M4 6 h22 a6 6 0 0 1 6 6 v44 a6 6 0 0 0 -6 -6 h-22 z"/><path class="F" d="M60 6 h-22 a6 6 0 0 0 -6 6 v44 a6 6 0 0 1 6 -6 h22 z"/>',
    "copier": '<rect class="F" x="0" y="18" width="60" height="34" rx="4"/><path class="F" d="M8 18 l6 -12 h32 l6 12"/><rect class="F" x="16" y="52" width="28" height="8"/><path d="M10 30 h16"/>',
    "ticket": '<path class="F" d="M0 8 h60 v14 a6 6 0 0 0 0 12 v14 h-60 v-14 a6 6 0 0 0 0 -12 z"/><path d="M42 8 v40" stroke-dasharray="4 4"/>',
    "sidecar": '<circle class="F" cx="12" cy="46" r="10"/><circle class="F" cx="56" cy="46" r="10"/><path d="M12 46 L26 26 h18 l12 20 M26 26 l-4 -10 h-8 M44 26 l6 -10"/><path class="F" d="M66 30 h30 a12 12 0 0 1 0 24 h-30 z"/><circle class="F" cx="84" cy="56" r="7"/>',
    "directory": '<rect class="F" x="0" y="0" width="56" height="60" rx="3"/><path d="M8 12 h28 M8 22 h40 M8 32 h34 M8 42 h40 M8 52 h26"/><rect class="F" x="56" y="6" width="8" height="12"/><rect class="F" x="56" y="22" width="8" height="12"/>',
    "lanes": '<path d="M0 0 v60 M30 0 v60 M60 0 v60 M90 0 v60"/><rect class="F" x="6" y="10" width="18" height="12"/><rect class="F" x="36" y="26" width="18" height="12"/><rect class="F" x="66" y="6" width="18" height="12"/>',
    "baton": '<path class="F" d="M6 50 L46 10 l8 8 L14 58 z"/><path d="M40 16 l8 8"/>',
    "door": '<rect class="F" x="6" y="0" width="44" height="64" rx="2"/><circle cx="40" cy="34" r="3"/>',
    "shield": '<path class="F" d="M30 2 L54 10 v18 c0 16 -10 26 -24 32 c-14 -6 -24 -16 -24 -32 v-18 z"/><path d="M20 30 l7 8 l14 -16"/>',
    "map": '<path class="F" d="M0 8 l20 -6 l20 6 l20 -6 v50 l-20 6 l-20 -6 l-20 6 z"/><path d="M20 2 v50 M40 8 v50"/>',
    "pin": '<path class="F" d="M20 56 C 6 36 0 28 0 20 a20 20 0 0 1 40 0 c0 8 -6 16 -20 36 z"/><circle cx="20" cy="20" r="7"/>',
    "kitchen": '<rect class="F" x="0" y="20" width="70" height="36" rx="3"/><path d="M14 20 v-8 h14 v8 M42 20 v-12 h12 v12 M8 34 h54"/>',
    "menu": '<rect class="F" x="0" y="0" width="48" height="62" rx="3"/><path d="M10 12 h28 M10 22 h20 M10 32 h26 M10 42 h18 M10 52 h24"/>',
    "megaphone": '<path class="F" d="M6 24 h10 l28 -16 v44 l-28 -16 h-10 z"/><path d="M16 36 l4 16 h8 l-4 -16 M52 20 q8 10 0 20"/>',
    "fuse": '<rect class="F" x="0" y="0" width="40" height="60" rx="4"/><rect x="12" y="10" width="16" height="16"/><rect x="12" y="34" width="16" height="16"/>',
    "hourglass": '<path class="F" d="M0 0 h24 M0 34 h24 M3 0 q0 13 9 17 q-9 4 -9 17 M21 0 q0 13 -9 17 q9 4 9 17"/>',
    "check": '<path d="M4 30 l16 18 l36 -40"/>',
    "cross": '<path d="M8 8 L52 52 M52 8 L8 52"/>',
    "calendar": '<rect class="F" x="0" y="8" width="56" height="50" rx="4"/><path d="M0 22 h56 M14 2 v12 M42 2 v12"/><path d="M10 32 h8 M24 32 h8 M38 32 h8 M10 44 h8 M24 44 h8"/>',
}


# ---------------------------------------------------------------- code highlighter
KEYWORDS = r"\b(const|let|var|async|await|function|return|if|else|for|of|in|new|class|type|export|import|from|throw|try|catch|finally|private|while|interface|true|false|null|undefined|SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|BEGIN|COMMIT|ON|CONFLICT|DO|NOTHING|DELETE|AND|ORDER|BY|LIMIT|FOR|SKIP|LOCKED|RETURNING|CREATE|TABLE|PRIMARY|KEY|JOIN|LEFT|INDEX|ALTER|ADD|DROP|COLUMN|NOT|NULL|DEFAULT|GROUP|PARTITION|RANGE|REFERENCES|UNIQUE|CHECK|VIEW|MATERIALIZED|REFRESH|CONCURRENTLY|WITH|AS|IS|OR|IN|TO|OF|USING|POLICY|ENABLE|ROW|LEVEL|SECURITY|EXISTS|IF|DESC|ASC|INCLUDE|CASE|WHEN|THEN|END|BETWEEN|ALL|def|yield|break|continue|switch|case|default)\b"


def highlight(code: str) -> str:
    out = []
    for line in code.split("\n"):
        parts = re.split(r'(//.*$|--\s.*$|#\s.*$|"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`[^`]*`)', line)
        buf = []
        for i, p in enumerate(parts):
            if not p:
                continue
            e = html.escape(p, quote=False)
            if i % 2 == 1:
                if p.startswith(("//", "--", "#")):
                    buf.append(f'<span class="c">{e}</span>')
                else:
                    buf.append(f'<span class="s">{e}</span>')
            else:
                buf.append(re.sub(KEYWORDS, r'<span class="k">\1</span>', e))
        out.append("".join(buf))
    return "\n".join(out)




# Icons added for the frontend journal (same ~60×60 convention).
ICONS.update({
    "plate": '<ellipse class="F" cx="34" cy="40" rx="32" ry="12"/><ellipse cx="34" cy="38" rx="20" ry="6"/><path d="M22 34 q6 -14 12 -4 q6 -12 12 2"/>',
    "bento": '<rect class="F" x="0" y="8" width="70" height="48" rx="4"/><path d="M34 8 v48 M34 30 h36"/><circle cx="17" cy="32" r="8"/><path d="M42 18 h20 M42 42 h20"/>',
    "recipe": '<rect class="F" x="0" y="0" width="50" height="62" rx="3"/><path d="M8 12 h34 M8 22 h26 M8 34 h34 M8 44 h30 M8 54 h20"/><circle class="F" cx="44" cy="8" r="6"/>',
    "chassis": '<circle class="F" cx="14" cy="44" r="10"/><circle class="F" cx="66" cy="44" r="10"/><path d="M4 34 h76 M14 34 v10 M66 34 v10 M30 34 v-10 h14 v10 M40 24 l6 -8"/>',
    "newspaper": '<rect class="F" x="0" y="0" width="60" height="62" rx="2"/><path d="M8 12 h44 M8 22 h20 M8 30 h20 M8 38 h20 M8 46 h44 M8 54 h44"/><rect x="34" y="20" width="18" height="20"/>',
    "traffic": '<rect class="F" x="14" y="0" width="30" height="74" rx="8"/><circle cx="29" cy="15" r="8"/><circle cx="29" cy="37" r="8"/><circle cx="29" cy="59" r="8"/><path d="M29 74 v14"/>',
    "lamp": '<path class="F" d="M14 6 h28 l10 26 h-48 z"/><path d="M28 32 v24 M14 58 h28 M44 56 q14 0 14 10"/>',
    "plug": '<rect class="F" x="8" y="18" width="30" height="24" rx="4"/><path d="M16 18 v-10 M30 18 v-10 M23 42 v8 q0 10 20 10 h14"/>',
    "frame": '<rect class="F" x="0" y="0" width="64" height="50" rx="2"/><rect x="8" y="8" width="48" height="34"/><path d="M12 38 l14 -14 l10 10 l8 -6 l10 10"/>',
    "screen": '<rect class="F" x="0" y="0" width="64" height="44" rx="4"/><path d="M24 44 l-4 12 h24 l-4 -12"/><path d="M14 30 l10 -10 l8 8 l14 -14"/>',
    "window": '<rect class="F" x="0" y="0" width="60" height="70" rx="4"/><path d="M30 0 v70 M0 35 h60"/>',
    "palette": '<path class="F" d="M34 2 C 12 2 0 18 0 34 c0 16 14 26 28 24 c8 -1 6 -10 12 -12 c8 -3 22 2 24 -12 C 66 16 52 2 34 2 z"/><circle cx="18" cy="24" r="5"/><circle cx="32" cy="14" r="5"/><circle cx="48" cy="20" r="5"/><circle cx="16" cy="40" r="5"/>',
    "tv": '<rect class="F" x="0" y="10" width="70" height="46" rx="5"/><path d="M24 0 l11 10 l11 -10 M14 62 h42"/><path d="M10 20 h40 v28 h-40 z"/>',
    "tray": '<path class="F" d="M0 20 h70 l-6 16 h-58 z"/><circle class="F" cx="22" cy="12" r="7"/><rect class="F" x="38" y="6" width="16" height="12"/>',
    "curtain": '<path d="M0 0 h80"/><path class="F" d="M2 0 q4 30 -2 60 h22 q-10 -30 0 -60 z"/><path class="F" d="M78 0 q-4 30 2 60 h-22 q10 -30 0 -60 z"/>',
})


# Icons added for the data journal (same ~60×60 convention).
ICONS.update({
    "cabinet": '<rect class="F" x="4" y="0" width="52" height="64" rx="3"/><path d="M4 21 h52 M4 42 h52"/><rect x="22" y="8" width="16" height="6"/><rect x="22" y="29" width="16" height="6"/><rect x="22" y="50" width="16" height="6"/>',
    "cards": '<path class="F" d="M0 22 h64 v38 h-64 z"/><path class="F" d="M6 22 v-16 h52 v16"/><path d="M14 6 v-6 h12 v6 M6 14 h52"/>',
    "stamp": '<path class="F" d="M22 4 h16 v18 q0 6 8 8 h8 v12 h-48 v-12 h8 q8 -2 8 -8 z"/><path d="M4 50 h52"/>',
    "receipt": '<path class="F" d="M6 0 h48 v62 l-8 -6 l-8 6 l-8 -6 l-8 6 l-8 -6 l-8 6 z"/><path d="M14 12 h32 M14 22 h24 M14 32 h32 M14 42 h18"/>',
    "tag": '<path class="F" d="M2 18 L18 2 h40 v32 h-40 z"/><circle cx="14" cy="18" r="4"/><path d="M28 14 h22 M28 24 h16"/>',
    "bin": '<path class="F" d="M8 14 h44 l-5 46 h-34 z"/><path d="M2 14 h56 M22 14 v-8 h16 v8 M22 24 v28 M38 24 v28"/>',
    "box": '<path class="F" d="M4 18 l26 -12 l26 12 v32 l-26 12 l-26 -12 z"/><path d="M4 18 l26 12 l26 -12 M30 30 v32"/>',
    "pool": '<path class="F" d="M0 20 h70 v30 h-70 z"/><path d="M6 30 q6 -6 12 0 q6 6 12 0 q6 -6 12 0 q6 6 12 0 q6 -6 12 0 M10 20 v-16 h8 M52 20 v-16 h8"/>',
    "star": '<path class="F" d="M30 2 l8 18 l20 2 l-15 13 l5 20 l-18 -11 l-18 11 l5 -20 l-15 -13 l20 -2 z"/>',
    "bricks": '<rect class="F" x="0" y="0" width="70" height="48"/><path d="M0 16 h70 M0 32 h70 M24 0 v16 M50 0 v16 M12 16 v16 M38 16 v16 M62 16 v16 M24 32 v16 M50 32 v16"/>',
    "camera": '<rect class="F" x="0" y="14" width="64" height="40" rx="5"/><path d="M20 14 l6 -8 h12 l6 8"/><circle class="F" cx="32" cy="34" r="11"/>',
})

# Icons added for the testing journal (same ~60×60 convention).
ICONS.update({
    "flask": '<path class="F" d="M22 2 h16 M24 2 v20 L6 54 a4 4 0 0 0 4 6 h40 a4 4 0 0 0 4 -6 L36 22 v-20"/><path d="M12 44 h36"/>',
    "magnifier": '<circle class="F" cx="24" cy="24" r="20"/><path d="M38 38 L58 58"/>',
    "dice": '<rect class="F" x="2" y="2" width="52" height="52" rx="8"/><circle cx="16" cy="16" r="4"/><circle cx="28" cy="28" r="4"/><circle cx="40" cy="40" r="4"/>',
    "pyramid": '<path class="F" d="M40 2 L78 66 h-76 z"/><path d="M17 40 h46 M28 22 h24"/>',
    "dummy": '<circle class="F" cx="30" cy="10" r="9"/><rect class="F" x="16" y="22" width="28" height="26" rx="4"/><path d="M16 26 l-12 14 M44 26 l12 14 M22 48 v14 M38 48 v14"/><circle cx="26" cy="9" r="2"/><path d="M34 6 l4 4 M38 6 l-4 4"/>',
    "mirror": '<ellipse class="F" cx="30" cy="26" rx="22" ry="26"/><path d="M30 52 v10 M18 62 h24 M20 14 l8 -6"/>',
    "handshake": '<path class="F" d="M0 20 h14 l10 -6 h10 l14 10 l12 0 v20 h-12 l-14 10 h-10 l-10 -6 h-14 z"/><path d="M24 14 l12 12 M30 34 l6 6 M36 30 l6 6"/>',
    "stopwatch": '<circle class="F" cx="30" cy="34" r="24"/><path d="M24 4 h12 M30 4 v6 M30 34 l10 -10 M50 14 l4 -4"/>',
})

# Icons added for the security journal (same ~60×60 convention).
ICONS.update({
    "badge": '<rect class="F" x="4" y="6" width="52" height="56" rx="4"/><circle cx="30" cy="26" r="9"/><path d="M16 50 q14 -16 28 0 M22 6 v-4 h16 v4"/>',
    "vault": '<rect class="F" x="2" y="2" width="58" height="58" rx="4"/><circle class="F" cx="31" cy="31" r="16"/><path d="M31 15 v32 M15 31 h32 M2 18 h-2 M2 44 h-2"/>',
    "guard": '<circle class="F" cx="30" cy="14" r="10"/><path class="F" d="M10 10 h40 l-4 -8 h-32 z"/><rect class="F" x="14" y="26" width="32" height="28" rx="4"/><path d="M14 30 l-10 16 M46 30 l10 16 M22 54 v10 M38 54 v10 M26 36 h8"/>',
    "eye": '<path class="F" d="M2 30 q28 -30 56 0 q-28 30 -56 0 z"/><circle cx="30" cy="30" r="9"/>',
    "castle": '<path class="F" d="M4 64 v-40 h8 v8 h8 v-8 h8 v8 h8 v-8 h8 v8 h8 v-8 h8 v40 z"/><path d="M28 64 v-14 a6 6 0 0 1 12 0 v14"/>',
    "keycard": '<rect class="F" x="2" y="10" width="58" height="40" rx="5"/><rect x="10" y="20" width="14" height="12"/><path d="M32 22 h20 M32 30 h14 M10 40 h42"/>',
    "fingerprint": '<path d="M30 58 c-10 -8 -14 -20 -12 -30 a12 12 0 0 1 24 0 c0 8 -2 14 -6 20 M22 54 c-6 -8 -10 -18 -8 -28 a16 16 0 0 1 32 0 M30 50 c-4 -8 -6 -14 -4 -22 a4 4 0 0 1 8 0 c0 6 -2 10 -4 14"/>',
    "seal": '<circle class="F" cx="30" cy="26" r="20"/><path d="M18 42 l-6 20 l10 -6 l6 8 l2 -18 M42 42 l6 20 l-10 -6 l-6 8 l-2 -18 M22 26 l6 6 l12 -12"/>',
})

# Icons added for the cloud & devops journal (same ~60×60 convention).
ICONS.update({
    "cloud": '<path class="F" d="M14 52 a12 12 0 0 1 0 -24 a16 16 0 0 1 30 -8 a12 12 0 0 1 18 14 a9 9 0 0 1 -4 18 z"/>',
    "rocket": '<path class="F" d="M30 2 q14 12 12 36 h-24 q-2 -24 12 -36 z"/><circle cx="30" cy="22" r="5"/><path class="F" d="M18 30 l-10 14 h10 M42 30 l10 14 h-10"/><path d="M24 44 l-2 12 M30 44 v14 M36 44 l2 12"/>',
    "gear": '<circle class="F" cx="30" cy="30" r="18"/><circle cx="30" cy="30" r="7"/><path d="M30 4 v8 M30 48 v8 M4 30 h8 M48 30 h8 M12 12 l6 6 M42 42 l6 6 M48 12 l-6 6 M12 48 l6 -6"/>',
    "gauge": '<path class="F" d="M4 44 a26 26 0 0 1 52 0 z"/><path d="M30 44 l14 -18 M10 36 l4 -2 M30 20 v4 M50 36 l-4 -2"/><circle cx="30" cy="44" r="3"/>',
    "flag": '<path d="M8 2 v60"/><path class="F" d="M8 4 h40 l-8 12 l8 12 h-40 z"/>',
    "switch": '<rect class="F" x="2" y="16" width="56" height="28" rx="14"/><circle class="F" cx="44" cy="30" r="10"/>',
    "container": '<rect class="F" x="2" y="10" width="66" height="40" rx="2"/><path d="M12 10 v40 M22 10 v40 M32 10 v40 M42 10 v40 M52 10 v40 M62 10 v40"/>',
    "coins": '<ellipse class="F" cx="24" cy="46" rx="20" ry="8"/><ellipse class="F" cx="24" cy="36" rx="20" ry="8"/><ellipse class="F" cx="36" cy="22" rx="20" ry="8"/>',
})
