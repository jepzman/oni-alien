#!/usr/bin/env python3
"""Paints the plates (illustrations) for The Darkside of the Corporation, Act II, as SVG.

Style (set by the hand-painted Credit Vampire, content/darkside/art/credit-vampire.svg): a dark room, one hard light
source (often from below), a coloured rim light from behind, skin and cloth texture, film grain and a heavy vignette.
Serious faces; the jokes live in the props. Every id is prefixed per plate so plates never clash on one page.

Usage: python3 scripts/plates.py            (writes content/darkside/art/<slug>.svg, except the hand-made vampire)
"""
from pathlib import Path

ART = Path(__file__).resolve().parent.parent / "content" / "darkside" / "art"
W, H = 800, 500
SERIF = "EB Garamond, Georgia, serif"
FELL = "IM Fell English SC, Georgia, serif"
MONO = "Courier Prime, monospace"
HAND = "Caveat, cursive"
BLACK = "Pirata One, Georgia, serif"


# ---------------------------------------------------------------- shared defs and grade
def common_defs(p):
    blurs = "".join(f'<filter id="{p}-b{n}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{n}"/></filter>'
                    for n in (1, 2, 3, 6, 12, 24))
    return f'''{blurs}
<filter id="{p}-glow" x="-2" y="-2" width="5" height="5"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="{p}-skin" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="3" seed="4"/><feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .35 -.05"/></filter>
<filter id="{p}-cloth" x="0" y="0" width="100%" height="100%"><feTurbulence type="turbulence" baseFrequency=".9 .04" numOctaves="2" seed="9"/><feColorMatrix type="matrix" values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .6  0 0 0 .05 0"/></filter>
<filter id="{p}-grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch" seed="2"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 .2"/></feComponentTransfer></filter>
<radialGradient id="{p}-vig" cx=".5" cy=".48" r=".72"><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".92"/></radialGradient>'''


def grade(p, haze=None):
    h = f'<ellipse cx="{haze[0]}" cy="{haze[1]}" rx="300" ry="220" fill="{haze[2]}" opacity=".06" filter="url(#{p}-b24)"/>' if haze else ""
    return f'{h}<rect width="{W}" height="{H}" fill="url(#{p}-vig)"/><rect width="{W}" height="{H}" filter="url(#{p}-grain)"/>'


def svg(p, label, defs, body):
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">\n<defs>{common_defs(p)}{defs}</defs>\n'
            f'{body}\n{grade(p)}\n</svg>\n')


def glowlight(p, x, y, rx, ry, col, op=.5, blur=24):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{col}" opacity="{op}" filter="url(#{p}-b{blur})"/>'


def text(x, y, s, size, fill, family=SERIF, anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'


def rain(p, x0, x1, y0=0, y1=H, op=.2, col="#7f92c0"):
    lines = "".join(f'M{x0 + (k * 37) % (x1 - x0)} {y0 + (k * 71) % (y1 - y0)} l-7 38 ' for k in range(18))
    return f'<path d="{lines}" stroke="{col}" stroke-width=".7" opacity="{op}"/>'


def window(p, x, w, col_top="#060b16", lights=True, pylon=True):
    g = f'<linearGradient id="{p}-night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col_top}"/><stop offset="1" stop-color="#0d0806"/></linearGradient>'
    out = [f'<rect x="{x}" y="0" width="{w}" height="{H}" fill="url(#{p}-night)"/>']
    if lights:
        out.append(f'<g filter="url(#{p}-b3)" opacity=".7">' + "".join(
            f'<circle cx="{x + 14 + (k * 53) % (w - 20)}" cy="{330 + (k * 29) % 60}" r="{2 + k % 3}" fill="{c}"/>'
            for k, c in enumerate(["#ff9a3a", "#ffd38a", "#ff7a3a", "#9ad0e0", "#ffb24a", "#fff"])) + "</g>")
    if pylon:
        px = x + w * .6
        out.append(f'<g stroke="#000" stroke-width="2" fill="none"><path d="M{px - 10} 340 L{px} 150 L{px + 10} 340 M{px - 7} 290 L{px + 7} 290 M{px - 5} 240 L{px + 5} 240 M{px - 7} 290 L{px + 5} 240 L{px - 3} 190 M{px + 7} 290 L{px - 5} 240 L{px + 3} 190 M{px - 24} 182 L{px + 24} 182"/></g>'
                   f'<circle cx="{px}" cy="146" r="2.6" fill="#ff2a20" filter="url(#{p}-glow)"><animate attributeName="opacity" values="1;.1;1" dur="2.4s" repeatCount="indefinite"/></circle>')
    out.append(rain(p, x, x + w))
    out.append(f'<rect x="{x - 6}" y="0" width="8" height="{H}" fill="#020203"/>')
    return g, "".join(out)


# ---------------------------------------------------------------- the painted face
# Template coordinates: face centred on (0, 0), about 116 wide and 226 tall (as the vampire's).
FACE = "M-58 -17 C-62 -77 -34 -111 0 -113 C34 -111 62 -77 58 -17 C57 29 46 63 30 89 C20 105 10 113 0 113 C-10 113 -20 105 -30 89 C-46 63 -57 29 -58 -17 Z"
IRIS = {
    "red": ("#ffd27a", "#ff3a1a", "#9a0000", "#ff2a14"),
    "green": ("#f0fff0", "#7dffb4", "#0a6a3a", "#5dffa0"),
    "yellow": ("#fffbd0", "#ffe14a", "#8a6a00", "#ffd21a"),
    "cyan": ("#ffffff", "#9ef4ff", "#1a6a8a", "#7ae8ff"),
    "milky": ("#f2f0e2", "#cfcbb8", "#8a8676", None),
    "violet": ("#fff0ff", "#d08aff", "#4a0a8a", "#c06aff"),
    "human": ("#c9a27a", "#6a4a2a", "#20140a", None),
}
LIGHT = {  # gradient centre for the key light, lit planes (x, y, rx, ry, opacity), far-side shadow x
    "below": ((.3, .98), [(-30, 45, 20, 30, .5), (0, 99, 26, 12, .55), (0, 55, 13, 7, .55), (-1, 29, 9, 6, .75), (-23, 3, 15, 5, .5), (-32, 19, 12, 6, .45)],
              [(0, -69, 64, 32, .8), (56, -7, 22, 80, .85)]),
    "above": ((.5, 0), [(0, -70, 40, 22, .55), (0, -10, 7, 26, .45), (-28, 18, 14, 8, .4), (28, 18, 14, 8, .3), (0, 70, 10, 5, .3)],
              [(0, 90, 40, 18, .8), (-22, -6, 18, 8, .9), (22, -6, 18, 8, .9), (56, 20, 18, 70, .6)]),
    "left": ((0, .45), [(-34, -40, 22, 40, .55), (-34, 30, 18, 34, .5), (-6, 10, 8, 26, .4)],
             [(48, 0, 30, 100, .9), (0, 95, 40, 16, .6)]),
    "right": ((1, .45), [(34, -40, 22, 40, .55), (34, 30, 18, 34, .5), (6, 10, 8, 26, .4)],
              [(-48, 0, 30, 100, .9), (0, 95, 40, 16, .6)]),
}


def face(p, k, x, y, s=1.0, sx=1.0, skin=("#1c1a22", "#3c3a48", "#5e6072"), light="below", light_col="#d9e6ff", rim="#ff3a22",
         rim_side="right", eye="red", glow=True, brows="angry", mouth="fangs", hair="slick", hair_col="#050407", ears="pointed",
         extras=(), tilt=0, mouth_col="#1a0608", lip="#4a1a22"):
    """A painted head. Returns SVG (defs inline in a <defs> block of its own)."""
    fid = f"{p}-f{k}"
    (gx, gy), lit, shade = LIGHT[light]
    i0, i1, i2, ig = IRIS[eye]
    d = [f'<defs><clipPath id="{fid}-c"><path d="{FACE}"/></clipPath>'
         f'<linearGradient id="{fid}-base" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{skin[0]}"/><stop offset=".55" stop-color="{skin[1]}"/><stop offset="1" stop-color="{skin[2]}"/></linearGradient>'
         f'<radialGradient id="{fid}-key" cx="{gx}" cy="{gy}" r=".85"><stop offset="0" stop-color="{light_col}" stop-opacity=".95"/><stop offset=".45" stop-color="{light_col}" stop-opacity=".4"/><stop offset="1" stop-color="{light_col}" stop-opacity="0"/></radialGradient>'
         f'<radialGradient id="{fid}-iris" cx=".42" cy=".4" r=".6"><stop offset="0" stop-color="{i0}"/><stop offset=".3" stop-color="{i1}"/><stop offset="1" stop-color="{i2}"/></radialGradient></defs>']
    g = [f'<g transform="translate({x} {y}) rotate({tilt}) scale({s * sx} {s})">']
    # ears behind the face
    rimx = 1 if rim_side == "right" else -1
    if ears == "pointed":
        g.append('<path d="M-54 -21 C-68 -41 -80 -65 -86 -99 C-66 -81 -50 -59 -44 -37 C-42 -15 -44 7 -52 19 C-60 7 -60 -9 -54 -21 Z" fill="#2e2d38"/>'
                 '<path d="M54 -21 C68 -41 80 -65 86 -99 C66 -81 50 -59 44 -37 C42 -15 44 7 52 19 C60 7 60 -9 54 -21 Z" fill="#1d1c25"/>'
                 f'<path d="M{86 * rimx} -99 C{80 * rimx} -65 {68 * rimx} -41 {54 * rimx} -21" stroke="{rim}" stroke-width="1.8" fill="none" opacity=".8"/>')
    elif ears == "big":
        g.append('<path d="M-52 -20 C-90 -40 -130 -70 -150 -96 C-120 -90 -82 -64 -48 -46 C-44 -20 -46 6 -52 16 Z" fill="#232a1e"/>'
                 '<path d="M52 -20 C90 -40 130 -70 150 -96 C120 -90 82 -64 48 -46 C44 -20 46 6 52 16 Z" fill="#161a12"/>'
                 '<path d="M-60 -30 C-90 -48 -116 -70 -132 -88" stroke="#0a0c08" stroke-width="3" fill="none" opacity=".7"/>'
                 f'<path d="M{150 * rimx} -96 C{130 * rimx} -70 {90 * rimx} -40 {52 * rimx} -20" stroke="{rim}" stroke-width="1.6" fill="none" opacity=".7"/>')
    elif ears == "human":
        g.append('<path d="M-56 -20 C-70 -24 -72 6 -58 14 Z" fill="#2a2830"/><path d="M56 -20 C70 -24 72 6 58 14 Z" fill="#1a1820"/>'
                 f'<path d="M{70 * rimx} -20 C{72 * rimx} 0 {66 * rimx} 10 {58 * rimx} 14" stroke="{rim}" stroke-width="1.2" fill="none" opacity=".7"/>')
    if hair == "long":
        g.append(f'<path d="M-64 -20 C-70 -90 -36 -128 0 -128 C36 -128 70 -90 64 -20 L74 170 L50 176 C46 110 50 50 54 0 L-54 0 C-50 50 -46 110 -50 176 L-74 170 Z" fill="{hair_col}"/>')
    if hair == "bob":
        g.append(f'<path d="M-66 -20 C-72 -92 -36 -126 0 -126 C36 -126 72 -92 66 -20 L70 70 C62 78 52 78 46 70 L50 0 L-50 0 L-46 70 C-52 78 -62 78 -70 70 Z" fill="{hair_col}"/>')
    # the face and its light
    g.append(f'<path d="{FACE}" fill="url(#{fid}-base)"/><g clip-path="url(#{fid}-c)">'
             f'<rect x="-70" y="-120" width="140" height="240" fill="url(#{fid}-key)"/>'
             f'<g filter="url(#{p}-b6)" fill="{light_col}">' + "".join(f'<ellipse cx="{a}" cy="{b}" rx="{c}" ry="{e}" opacity="{o}"/>' for a, b, c, e, o in lit) + "</g>"
             f'<g filter="url(#{p}-b12)" fill="#050508">' + "".join(f'<ellipse cx="{a}" cy="{b}" rx="{c}" ry="{e}" opacity="{o}"/>' for a, b, c, e, o in shade) + "</g>"
             f'<g filter="url(#{p}-b3)" fill="#050508"><ellipse cx="-22" cy="-15" rx="20" ry="8" opacity=".9"/><ellipse cx="24" cy="-15" rx="20" ry="8" opacity=".95"/></g>'
             f'<path d="M{58 * rimx} -17 C{57 * rimx} 29 {46 * rimx} 63 {30 * rimx} 89 C{20 * rimx} 105 {10 * rimx} 113 0 113" stroke="{rim}" stroke-width="3" fill="none" opacity=".55" filter="url(#{p}-b1)"/>'
             + (f'<g filter="url(#{p}-b6)" fill="{ig}" opacity=".35"><ellipse cx="-20" cy="7" rx="14" ry="8"/><ellipse cx="22" cy="7" rx="14" ry="8"/></g>' if glow and ig else "")
             + ''.join(EXTRA_IN.get(e, "") for e in extras)
             + f'<rect x="-70" y="-120" width="140" height="240" filter="url(#{p}-skin)"/></g>')
    # lines
    g.append(f'<g stroke="#08070b" fill="none" stroke-linecap="round" filter="url(#{p}-b1)">'
             '<path d="M-5 -39 L-7 -21" stroke-width="1.6" opacity=".8"/><path d="M5 -39 L7 -21" stroke-width="1.6" opacity=".8"/>'
             '<path d="M-12 29 C-20 43 -24 55 -22 71" stroke-width="2" opacity=".7"/><path d="M12 29 C20 43 26 55 24 73" stroke-width="2" opacity=".75"/>'
             '<path d="M-34 3 C-26 7 -16 7 -8 3" stroke-width="1" opacity=".5"/><path d="M10 3 C18 7 28 7 36 3" stroke-width="1" opacity=".5"/></g>')
    # eyes
    sclera = "#c7b2aa" if eye != "milky" else "#bdbcae"
    g.append(f'<path d="M-36 -7 Q-22 -17 -8 -9 Q-22 -1 -36 -7 Z" fill="{sclera}"/><path d="M8 -9 Q22 -17 36 -7 Q22 -1 8 -9 Z" fill="{sclera}" opacity=".85"/>'
             '<g stroke="#b01414" stroke-width=".5" fill="none" opacity=".7"><path d="M-35 -7 l6 -1 l3 2 M-9 -9 l-5 1 M9 -9 l5 1 l3 -2 M35 -7 l-5 0"/></g>'
             f'<circle cx="-21" cy="-8" r="5.4" fill="url(#{fid}-iris)"/><circle cx="21" cy="-8" r="5.4" fill="url(#{fid}-iris)"/>')
    if eye == "milky":
        g.append('<circle cx="-21" cy="-8" r="1.2" fill="#3a3a30" opacity=".6"/><circle cx="21" cy="-8" r="1.2" fill="#3a3a30" opacity=".6"/>')
    elif eye == "human":
        g.append('<circle cx="-21" cy="-8" r="2.2" fill="#000"/><circle cx="21" cy="-8" r="2.2" fill="#000"/>')
    else:
        g.append('<ellipse cx="-21" cy="-8" rx="1.2" ry="4" fill="#000"/><ellipse cx="21" cy="-8" rx="1.2" ry="4" fill="#000"/>')
    g.append('<circle cx="-22.4" cy="-9.6" r="1" fill="#fff"/><circle cx="19.6" cy="-9.6" r="1" fill="#fff"/>')
    if glow and ig:
        g.append(f'<g filter="url(#{p}-b3)" fill="{ig}" opacity=".8"><circle cx="-21" cy="-8" r="7"/><circle cx="21" cy="-8" r="7"/></g>')
    g.append('<path d="M-38 -7 Q-22 -19 -6 -9" stroke="#030305" stroke-width="2.4" fill="none"/><path d="M6 -9 Q22 -19 38 -7" stroke="#030305" stroke-width="2.4" fill="none"/>')
    # brows
    bw = {"angry": ("M-46 -27 Q-26 -39 -6 -21", "M46 -27 Q26 -39 6 -21"), "worried": ("M-44 -24 Q-26 -36 -8 -36", "M44 -24 Q26 -36 8 -36"),
          "raised": ("M-44 -32 Q-26 -48 -8 -36", "M44 -32 Q26 -48 8 -36"), "flat": ("M-44 -27 Q-26 -33 -8 -27", "M44 -27 Q26 -33 8 -27"),
          "none": None}[brows]
    if bw:
        g.append(f'<g stroke-linecap="round" fill="none"><path d="{bw[0]}" stroke="#050407" stroke-width="5"/><path d="{bw[1]}" stroke="#050407" stroke-width="5"/></g>')
    # nose
    g.append('<path d="M-6 -11 C-6 7 -10 21 -12 29 C-8 35 8 35 12 29 C10 21 6 7 6 -11" fill="none" stroke="#0a090d" stroke-width="1.2" opacity=".6"/>'
             '<ellipse cx="-7" cy="33" rx="3.4" ry="2" fill="#07060a"/><ellipse cx="7" cy="33" rx="3.4" ry="2" fill="#07060a"/>')
    g.append(MOUTH[mouth].format(m=mouth_col, lip=lip))
    g.append("".join(EXTRA_OUT.get(e, "") for e in extras))
    if hair == "slick":
        g.append(f'<path d="M-62 -31 C-66 -95 -36 -141 0 -143 C36 -141 66 -95 62 -31 C56 -57 46 -77 32 -87 C22 -75 12 -67 0 -49 C-12 -67 -22 -75 -32 -87 C-46 -77 -56 -57 -62 -31 Z" fill="{hair_col}"/>'
                 '<g stroke="#2b2a36" stroke-width=".9" fill="none" opacity=".9"><path d="M-30 -89 C-26 -111 -14 -127 6 -133"/><path d="M-38 -79 C-36 -103 -24 -121 -6 -131"/><path d="M-20 -87 C-14 -107 -2 -119 16 -125"/><path d="M-10 -71 C-6 -95 8 -113 28 -119"/></g>'
                 f'<path d="M{0} -143 C{36 * rimx} -141 {66 * rimx} -95 {62 * rimx} -31" stroke="{rim}" stroke-width="2" fill="none" opacity=".7" filter="url(#{p}-b1)"/>')
    elif hair in ("long", "bob"):
        g.append(f'<path d="M-62 -24 C-60 -88 -30 -122 0 -122 C30 -122 60 -88 62 -24 C50 -60 30 -80 0 -82 C-20 -80 -40 -70 -54 -40 Z" fill="{hair_col}"/>'
                 '<g stroke="#2b2a36" stroke-width=".8" fill="none" opacity=".8"><path d="M-2 -120 C-20 -100 -40 -80 -56 -40"/><path d="M2 -120 C24 -100 44 -80 58 -40"/><path d="M-10 -116 C-30 -96 -46 -70 -58 -30"/></g>'
                 f'<path d="M0 -122 C{30 * rimx} -122 {60 * rimx} -88 {62 * rimx} -24 L{70 * rimx} 70" stroke="{rim}" stroke-width="1.8" fill="none" opacity=".65" filter="url(#{p}-b1)"/>')
    elif hair == "patchy":
        g.append(f'<g fill="{hair_col}"><path d="M-58 -40 C-56 -90 -30 -116 -6 -116 C-20 -100 -40 -80 -50 -40 Z"/><path d="M20 -112 C40 -104 56 -80 58 -46 C50 -70 36 -90 14 -104 Z"/></g>'
                 '<g stroke="#2a2a20" stroke-width="1" fill="none"><path d="M-10 -114 l-6 -14 M0 -113 l2 -16 M8 -112 l6 -12"/></g>')
    elif hair == "bald":
        g.append(f'<path d="M-40 -96 C-20 -112 20 -112 40 -96" stroke="{light_col}" stroke-width="3" opacity=".25" fill="none" filter="url(#{p}-b3)"/>'
                 f'<path d="M0 -113 C34 -111 62 -77 58 -17" stroke="{rim}" stroke-width="2" fill="none" opacity=".6" filter="url(#{p}-b1)"/>')
    g.append("</g>")
    return "".join(d) + "".join(g)


MOUTH = {
    "fangs": ('<path d="M-26 61 Q0 69 28 55" stroke="{m}" stroke-width="3" fill="none" stroke-linecap="round"/>'
              '<path d="M-15 62 L-12 76 L-9 63 Z" fill="#e9e6e0"/><path d="M13 60 L16 74 L19 59 Z" fill="#e9e6e0"/>'),
    "smile": ('<path d="M-26 56 Q0 72 26 56" stroke="{m}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
              '<path d="M-24 57 Q0 70 24 57 Q0 64 -24 57Z" fill="{lip}"/><path d="M-29 53 q-3 4 0 8 M29 53 q3 4 0 8" stroke="{m}" stroke-width="1.4" fill="none"/>'),
    "grin": ('<path d="M-32 52 Q0 88 32 52 Q0 64 -32 52 Z" fill="{m}"/>'
             '<path d="M-29 54 Q0 66 29 54 L27 60 Q0 70 -27 60 Z" fill="#e8e2d4"/>'
             '<path d="M-28 70 Q0 84 28 70 L26 66 Q0 78 -26 66Z" fill="#cfc8b8" opacity=".85"/>'
             '<g stroke="#2a2420" stroke-width=".7"><path d="M-20 56 v8 M-12 58 v9 M-4 59 v9 M4 59 v9 M12 58 v9 M20 56 v8"/></g>'
             '<path d="M-32 52 Q0 64 32 52" stroke="{lip}" stroke-width="3" fill="none"/><path d="M-32 52 Q0 88 32 52" stroke="{lip}" stroke-width="2.4" fill="none"/>'),
    "sharp": ('<path d="M-30 52 Q0 84 30 52 Q0 62 -30 52 Z" fill="{m}"/>'
              '<path d="M-28 54 l4 9 4 -8 4 10 4 -9 4 10 4 -10 4 10 4 -10 4 9 4 -8 4 8 Q0 64 -28 54Z" fill="#e8ffe0"/>'
              '<path d="M-24 74 l4 -8 4 7 4 -8 4 8 4 -8 4 8 4 -8 4 8 4 -7 4 6" stroke="#e8ffe0" stroke-width="1.6" fill="none"/>'),
    "shout": ('<ellipse cx="0" cy="66" rx="24" ry="28" fill="{m}"/><ellipse cx="0" cy="84" rx="13" ry="8" fill="#5a1a20"/>'
              '<path d="M-20 48 Q0 42 20 48 L18 54 Q0 50 -18 54 Z" fill="#d8d0c0"/><path d="M-18 86 Q0 94 18 86 L16 82 Q0 88 -16 82Z" fill="#b8b0a0"/>'
              '<ellipse cx="0" cy="66" rx="24" ry="28" fill="none" stroke="{lip}" stroke-width="2.4"/>'),
    "slack": ('<path d="M-16 56 C-14 82 18 90 20 58 Q2 62 -16 56 Z" fill="{m}"/>'
              '<path d="M-10 58 l2 6 3 -5 M6 59 l2 5 2 -5" stroke="#b8b48a" stroke-width="2" fill="none"/>'
              '<path d="M-16 56 Q2 62 20 58" stroke="{lip}" stroke-width="2" fill="none"/>'),
    "thin": ('<path d="M-24 62 Q0 58 24 62" stroke="{m}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
             '<path d="M-24 62 q-4 3 -5 7 M24 62 q4 3 5 7" stroke="{m}" stroke-width="1.4" fill="none"/>'),
    "wail": ('<path d="M-18 50 C-24 80 -12 112 0 112 C12 112 24 80 18 50 Q0 44 -18 50Z" fill="{m}"/>'
             '<path d="M-18 50 C-24 80 -12 112 0 112 C12 112 24 80 18 50 Q0 44 -18 50Z" fill="none" stroke="{lip}" stroke-width="2"/>'),
}
EXTRA_IN = {
    "rot": ('<g filter="url(#{p}-b3)" fill="#3a4a1a" opacity=".55"><ellipse cx="30" cy="-60" rx="16" ry="10"/><ellipse cx="-36" cy="40" rx="12" ry="16"/></g>'
            '<g fill="#1a1006" opacity=".7"><ellipse cx="34" cy="-58" rx="5" ry="3"/><ellipse cx="-38" cy="44" rx="4" ry="6"/></g>'),
    "blush": '<g fill="#ff5a8a" opacity=".22"><ellipse cx="-34" cy="24" rx="14" ry="8"/><ellipse cx="34" cy="24" rx="14" ry="8"/></g>',
    "cracks": '<g stroke="#000" stroke-width="1.2" fill="none" opacity=".7"><path d="M-40 -80 l10 18 -6 14 12 20 M30 -100 l-8 22 10 12 -4 18 M40 40 l-14 10 4 20"/></g>',
    "translucent": '<rect x="-70" y="40" width="140" height="80" fill="#9ef4ff" opacity=".12"/>',
}
EXTRA_OUT = {
    "tusks": '<path d="M-22 74 C-26 60 -26 44 -20 34 C-18 46 -16 60 -14 72 Z" fill="#e4d8b0"/><path d="M22 74 C26 60 26 44 20 34 C18 46 16 60 14 72 Z" fill="#cfc29a"/>',
    "wrinkles": ('<g stroke="#08070b" stroke-width="1" fill="none" opacity=".6"><path d="M-36 -52 Q0 -58 36 -52 M-30 -62 Q0 -68 30 -62 M-24 -72 Q0 -76 24 -72"/>'
                 '<path d="M-36 3 q-6 4 -12 2 M36 3 q6 4 12 2 M-30 8 q-4 6 -2 12 M30 8 q4 6 2 12"/></g>'),
    "stitches": '<g stroke="#1a1006" stroke-width="1.4" fill="none"><path d="M18 -96 C30 -80 36 -66 40 -50"/><path d="M20 -86 l8 -4 M26 -76 l8 -4 M32 -66 l8 -4 M36 -56 l8 -4"/></g>',
    "glasses": ('<g fill="none" stroke="#c9b06a" stroke-width="2.2"><circle cx="-21" cy="-8" r="14"/><circle cx="21" cy="-8" r="14"/><path d="M-7 -10 Q0 -14 7 -10 M-35 -10 L-56 -16 M35 -10 L56 -16"/></g>'
                '<g fill="#fff" opacity=".22"><path d="M-30 -16 L-18 -20 L-26 2 L-32 0 Z"/><path d="M12 -16 L24 -20 L16 2 L10 0 Z"/></g>'),
    "lipstick": '<path d="M-24 57 Q0 70 24 57 Q0 64 -24 57Z" fill="#c4122a"/>',
}


def fix(p, s):
    return s.replace("{p}", p)


# ---------------------------------------------------------------- bodies (template: neck at (0, 85), shoulders at y≈100)
def suit(p, k, x, y, s=1.0, coat=False, tie="#5a070c", jacket="#0c0c11", shirt="#5a6070", rim="#ff3a22", rim_side="right"):
    r = 1 if rim_side == "right" else -1
    out = [f'<g transform="translate({x} {y}) scale({s})">']
    if coat:
        out.append(f'<path d="M-280 293 C-266 185 -208 123 -110 97 L-68 -11 C-54 19 -42 55 -26 85 L0 153 L26 85 C42 55 54 19 68 -11 L110 97 C210 123 270 185 282 293 Z" fill="#08080c"/>'
                   f'<path d="M{110 * r} 97 C{210 * r} 123 {270 * r} 185 {282 * r} 293" stroke="{rim}" stroke-width="2.4" fill="none" opacity=".45" filter="url(#{p}-b1)"/>')
    else:
        out.append(f'<path d="M-280 293 C-266 185 -208 123 -110 97 C-70 89 -44 83 -26 80 L0 153 L26 80 C44 83 70 89 110 97 C208 123 266 185 282 293 Z" fill="{jacket}"/>'
                   f'<path d="M{110 * r} 97 C{208 * r} 123 {266 * r} 185 {282 * r} 293" stroke="{rim}" stroke-width="2.4" fill="none" opacity=".5" filter="url(#{p}-b1)"/>')
    out.append(f'<path d="M-100 111 C-70 103 -44 93 -26 85 L0 153 L26 85 C44 93 70 103 100 111 L90 293 L-90 293 Z" fill="{jacket}"/>'
               '<path d="M-26 43 L-24 93 L24 93 L26 43 Z" fill="#2a2a34"/>'
               f'<ellipse cx="0" cy="52" rx="30" ry="14" fill="#000" opacity=".75" filter="url(#{p}-b6)"/>'
               f'<path d="M-32 77 L0 155 L32 77 L18 67 L0 97 L-18 67 Z" fill="{shirt}"/>'
               f'<path d="M-9 97 L9 97 L15 111 L6 119 L18 233 L0 263 L-18 233 L-6 119 L-15 111 Z" fill="{tie}"/>'
               '<path d="M-26 85 L0 153 L-30 263 L-64 133 L-80 99 L-50 93 Z" fill="#08080c" stroke="#24242e" stroke-width="1"/>'
               '<path d="M26 85 L0 153 L30 263 L64 133 L80 99 L50 93 Z" fill="#060609" stroke="#1a1a22" stroke-width="1"/>'
               f'<rect x="-280" y="-20" width="562" height="320" filter="url(#{p}-cloth)" opacity=".8" clip-path="url(#{p}-bodyclip{k})"/>'
               '</g>')
    clip = f'<clipPath id="{p}-bodyclip{k}"><path d="M-280 293 C-266 185 -208 123 -110 97 C-70 89 -44 83 -26 80 L0 153 L26 80 C44 83 70 89 110 97 C208 123 266 185 282 293 Z"/></clipPath>'
    return f"<defs>{clip}</defs>" + "".join(out)


def blouse(p, x, y, s=1.0, cardigan="#14121a", top="#3a3440", rim="#ff3a22", rim_side="right", necklace=True):
    r = 1 if rim_side == "right" else -1
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M-26 43 L-24 93 L24 93 L26 43 Z" fill="#2a2a34"/>'
               f'<ellipse cx="0" cy="52" rx="30" ry="14" fill="#000" opacity=".75" filter="url(#{p}-b6)"/>'
            f'<path d="M-230 293 C-220 190 -170 128 -90 105 C-60 96 -40 90 -24 86 C-12 120 12 120 24 86 C40 90 60 96 90 105 C170 128 220 190 232 293 Z" fill="{cardigan}"/>'
            f'<path d="M-60 100 C-40 130 -20 150 0 156 C20 150 40 130 60 100 L50 293 L-50 293 Z" fill="{top}"/>'
            '<path d="M-24 86 C-12 120 12 120 24 86" fill="#4a4858"/>'
            + ('<path d="M-22 90 C-12 118 12 118 22 90" stroke="#c9a24a" stroke-width="1.2" fill="none"/><circle cx="0" cy="116" r="3" fill="#e0b860"/>' if necklace else "")
            + f'<path d="M{90 * r} 105 C{170 * r} 128 {220 * r} 190 {232 * r} 293" stroke="{rim}" stroke-width="2.2" fill="none" opacity=".5" filter="url(#{p}-b1)"/>'
            '</g>')


def hand(p, x, y, s=1.0, flip=False, rim="#ff3a22", light="#9aa8c2", claws=True, skin_dark="#0c0b10", pose="open"):
    """A bony hand seen from the back, fingers up. pose: open | point | claw"""
    sx = -s if flip else s
    fingers = {"open": ["M-18 0 C-22 -24 -26 -44 -30 -62", "M-6 -4 C-6 -30 -6 -52 -6 -72", "M6 -4 C8 -28 10 -50 12 -68", "M18 0 C22 -20 26 -38 30 -52"],
               "point": ["M-6 -4 C-6 -30 -6 -52 -6 -76", "M-16 0 C-20 -10 -16 -18 -8 -18", "M6 -2 C10 -12 16 -12 18 -4", "M18 4 C24 -4 28 -2 28 6"],
               "claw": ["M-18 0 C-26 -24 -34 -40 -28 -58", "M-6 -4 C-10 -30 -14 -50 -4 -70", "M6 -4 C6 -28 4 -48 14 -66", "M18 0 C22 -20 18 -36 28 -50"]}[pose]
    gid = f"{p}-h{x}{y}".replace(".", "")
    tips = []
    for f in fingers:
        last = f.split()[-1], f.split()[-2]
        tx, ty = map(float, f.split()[-2:]) if False else (float(f.split()[-2]), float(f.split()[-1]))
        if claws:
            tips.append(f'<path d="M{tx - 2} {ty} L{tx} {ty - 12} L{tx + 2} {ty} Z" fill="#0b0a10"/>')
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{light}"/><stop offset=".35" stop-color="#2a2a33"/><stop offset="1" stop-color="{skin_dark}"/></linearGradient></defs>'
            f'<g transform="translate({x} {y}) scale({sx} {s})">'
            f'<path d="M-26 50 C-30 26 -28 6 -20 -4 C-8 -10 8 -10 22 -4 C28 8 28 30 24 50 Z" fill="url(#{gid})"/>'
            f'<g stroke="url(#{gid})" stroke-linecap="round" fill="none">' + "".join(f'<path d="{f}" stroke-width="{7.5 - i * .6}"/>' for i, f in enumerate(fingers)) + "</g>"
            '<path d="M-24 30 C-36 22 -42 10 -44 -6" stroke="url(#' + gid + ')" stroke-width="8" stroke-linecap="round" fill="none"/>'
            + "".join(tips)
            + '<g stroke="#15141a" stroke-width="1.2" opacity=".6" fill="none"><path d="M-14 46 L-12 2 M0 48 L-2 0 M12 46 L10 2"/></g>'
            f'<path d="M22 -4 C28 8 28 30 24 50" stroke="{rim}" stroke-width="1.6" fill="none" opacity=".6"/>'
            '</g>')


def table(y=470, col="#050302", edge="#3a2a20"):
    return f'<path d="M0 {y} L800 {y} L800 500 L0 500 Z" fill="{col}"/><path d="M0 {y} L800 {y}" stroke="{edge}" stroke-width="1.2" opacity=".6"/>'


def mug(x, y, line1, line2, fill="#1a1816", ink="#5a4a40", steam=True):
    return (f'<g transform="translate({x} {y})"><rect x="0" y="0" width="44" height="52" rx="4" fill="{fill}"/><path d="M44 12 C58 12 58 38 44 38" stroke="{fill}" stroke-width="6" fill="none"/>'
            + text(22, 20, line1, 6.6, ink, SERIF, "middle", 'font-weight="700"') + text(22, 29, line2, 6.6, ink, SERIF, "middle", 'font-weight="700"')
            + ('<path d="M14 -6 C10 -16 22 -18 18 -30 M30 -6 C26 -16 38 -18 34 -30" stroke="#9aa" stroke-width="1.1" fill="none" opacity=".18"/>' if steam else "")
            + "</g>")


def badge(x, y, name, dept, line3, line4="", rot=-8):
    return (f'<g transform="rotate({rot} {x + 40} {y + 40})"><rect x="{x}" y="{y}" width="80" height="84" rx="4" fill="#c9cfdc"/>'
            f'<rect x="{x}" y="{y}" width="80" height="16" rx="4" fill="#6a0d0d"/>' + text(x + 40, y + 12, "METROVOLT", 9, "#e9dccb", FELL, "middle", 'letter-spacing="1"')
            + f'<rect x="{x + 8}" y="{y + 20}" width="22" height="26" fill="#0e0e14"/>'
            + text(x + 34, y + 30, name, 8.5, "#1b1b22", SERIF, "start", 'font-weight="700"') + text(x + 34, y + 40, dept, 7.5, "#33333d")
            + text(x + 6, y + 60, line3, 6.5, "#40404a") + (text(x + 6, y + 70, line4, 6.5, "#7a0d0d") if line4 else "") + "</g>")


# ================================================================ the plates
def meeting_lich():
    p = "ml"
    defs = (f'<radialGradient id="{p}-pend" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#bfffd8" stop-opacity=".55"/><stop offset=".5" stop-color="#3a8a6a" stop-opacity=".15"/><stop offset="1" stop-color="#3a8a6a" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-robe" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14181a"/><stop offset="1" stop-color="#020303"/></linearGradient>'
            f'<radialGradient id="{p}-bone" cx=".45" cy=".25" r=".8"><stop offset="0" stop-color="#e8e6d4"/><stop offset=".5" stop-color="#8f9a8a"/><stop offset="1" stop-color="#1a201c"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#020303"/>']
    # the wall: a calendar where every slot is taken, a clock with no hands
    b.append(f'<g opacity=".5"><rect x="40" y="60" width="150" height="120" fill="#0a100e" stroke="#2a4a3c"/>'
             + "".join(f'<rect x="{44 + c * 29}" y="{78 + r * 20}" width="26" height="17" fill="#2a5a46" opacity="{.4 + (r * c) % 3 * .2}"/>' for r in range(5) for c in range(5))
             + text(115, 74, "NOVEMBER", 10, "#5a8a76", FELL, "middle", 'letter-spacing="2"') + "</g>")
    b.append(f'<circle cx="660" cy="110" r="44" fill="#060908" stroke="#2a4a3c" stroke-width="3"/>'
             + "".join(f'<path d="M{660 + 36 * __import__("math").cos(a * 0.5236):.1f} {110 + 36 * __import__("math").sin(a * 0.5236):.1f} l0 0" stroke="#5a8a76" stroke-width="3" stroke-linecap="round"/>' for a in range(12))
             + '<line x1="660" y1="110" x2="660" y2="80" stroke="#9fd8bf" stroke-width="2"><animateTransform attributeName="transform" type="rotate" from="0 660 110" to="360 660 110" dur="3s" repeatCount="indefinite"/></line>'
             '<line x1="660" y1="110" x2="684" y2="110" stroke="#9fd8bf" stroke-width="3"><animateTransform attributeName="transform" type="rotate" from="0 660 110" to="360 660 110" dur="30s" repeatCount="indefinite"/></line>')
    # pendant light cone
    b.append(f'<path d="M370 0 L430 0 L620 470 L180 470 Z" fill="url(#{p}-pend)" filter="url(#{p}-b12)"/>')
    b.append('<path d="M380 0 L420 0 L414 18 L386 18 Z" fill="#0a0f0d"/><ellipse cx="400" cy="20" rx="22" ry="5" fill="#dfffee" filter="url(#ml-glow)"/>')
    # the lich: hood and robe
    b.append(f'<path d="M400 60 C320 70 300 150 296 250 C292 330 270 400 240 470 L560 470 C530 400 508 330 504 250 C500 150 480 70 400 60 Z" fill="url(#{p}-robe)"/>')
    b.append(f'<rect x="230" y="60" width="340" height="420" filter="url(#{p}-cloth)" opacity=".7"/>')
    b.append(f'<path d="M400 60 C320 70 300 150 296 250" stroke="#7affc0" stroke-width="1.6" fill="none" opacity=".35" filter="url(#{p}-b1)"/>')
    # the skull under the hood
    b.append(f'<path d="M400 110 C366 110 350 140 352 176 C354 204 366 222 378 232 L378 250 L422 250 L422 232 C434 222 446 204 448 176 C450 140 434 110 400 110 Z" fill="url(#{p}-bone)"/>')
    b.append(f'<path d="M400 96 C340 100 320 150 330 214 C340 170 360 140 400 132 C440 140 460 170 470 214 C480 150 460 100 400 96 Z" fill="#020303"/>')
    b.append('<g fill="#000"><path d="M368 168 C366 156 378 150 390 158 C394 170 386 182 374 182 C368 180 368 174 368 168 Z"/><path d="M432 168 C434 156 422 150 410 158 C406 170 414 182 426 182 C432 180 432 174 432 168 Z"/>'
             '<path d="M400 190 L393 208 L407 208 Z"/></g>')
    b.append(f'<g filter="url(#{p}-glow)"><circle cx="380" cy="168" r="4" fill="#9effc8"/><circle cx="420" cy="168" r="4" fill="#9effc8"/></g>')
    b.append('<g stroke="#1a201c" stroke-width="1.4"><path d="M380 222 h40 M384 222 v14 M392 222 v16 M400 222 v16 M408 222 v16 M416 222 v14 M380 236 h40"/></g>'
             '<path d="M358 140 l12 10 -4 12" stroke="#1a201c" stroke-width="1" fill="none"/>')
    # lanyard with a visitor badge
    b.append('<path d="M378 250 L400 300 L422 250" stroke="#1e3e6a" stroke-width="3" fill="none"/>' + badge(360, 296, "THE LICH", "Alignment", "ORGANISER OF 112", "MEETINGS", rot=0))
    # the long table and bony hands steepled on a binder
    b.append('<path d="M150 400 L650 400 L800 500 L0 500 Z" fill="#0a0d0c"/><path d="M150 400 L650 400" stroke="#3a6a5a" stroke-width="1" opacity=".6"/>')
    b.append('<rect x="340" y="404" width="120" height="26" fill="#1a1c22" transform="skewX(-10)"/>' + text(406, 422, "AGENDA: TBD", 10, "#7a8a86", FELL, "middle"))
    b.append(f'<g stroke="url(#{p}-bone)" stroke-width="4" stroke-linecap="round" fill="none"><path d="M370 400 L392 362 M378 402 L396 364 M386 404 L398 368"/><path d="M430 400 L408 362 M422 402 L404 364 M414 404 L402 368"/></g>')
    # empty chairs, cobwebs
    for cx, sc in ((210, 1), (590, -1), (110, 1.25), (690, -1.25)):
        b.append(f'<g transform="translate({cx} 420) scale({sc} {abs(sc)})"><path d="M-22 -50 L22 -50 L26 60 L-26 60 Z" fill="#050706"/><path d="M-22 -50 L4 -24 M-22 -38 C-10 -38 -4 -44 -2 -50 M-22 -26 C-6 -28 4 -38 8 -50" stroke="#a8b8b0" stroke-width=".6" fill="none" opacity=".5"/></g>')
    b.append(text(400, 470, "WEEKLY SYNC ON THE SYNCS · MEETING #112 · RECURRING, NO END DATE", 11, "#4a7a66", FELL, "middle", 'letter-spacing="1.5"'))
    return p, "The Meeting Lich", defs, "".join(b)


def gaslight_wraith():
    p = "gw"
    defs = (f'<radialGradient id="{p}-lamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd27a" stop-opacity=".9"/><stop offset=".4" stop-color="#ff8a2a" stop-opacity=".3"/><stop offset="1" stop-color="#ff8a2a" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-mist" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b8f0ff" stop-opacity=".55"/><stop offset="1" stop-color="#b8f0ff" stop-opacity="0"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#020406"/>']
    # the lift: steel doors half open, floor indicator 13
    b.append('<rect x="140" y="20" width="520" height="460" fill="#06090c"/><rect x="150" y="60" width="250" height="420" fill="#0c1116"/><rect x="400" y="60" width="250" height="420" fill="#0a0e12"/>'
             '<path d="M400 60 V480" stroke="#000" stroke-width="3"/><g stroke="#1e2830" stroke-width="1" opacity=".7"><path d="M160 60 V480 M640 60 V480"/></g>')
    b.append('<rect x="370" y="26" width="60" height="26" fill="#000" stroke="#2a2a2a"/>' + text(400, 46, "13", 20, "#ff3a22", MONO, "middle", f'filter="url(#{p}-glow)"'))
    # the wraith: translucent, long hair, dissolving into mist
    b.append(f'<path d="M320 300 C300 380 280 440 250 500 L560 500 C520 440 500 380 480 300 Z" fill="url(#{p}-mist)" filter="url(#{p}-b6)"/>')
    b.append(f'<g opacity=".88">{blouse(p, 400, 192, .8, cardigan="#0c1a22", top="#1a2a34", rim="#7ae8ff", rim_side="left", necklace=False)}</g>')
    b.append(f'<rect x="200" y="320" width="400" height="180" fill="url(#{p}-mist)" opacity=".7" filter="url(#{p}-b12)"/>')
    b.append(face(p, 1, 400, 160, .78, skin=("#0a1418", "#3a5a64", "#7aa0aa"), light="left", light_col="#ffd9a0", rim="#7ae8ff", rim_side="right",
                  eye="cyan", brows="raised", mouth="smile", hair="long", hair_col="#03080a", ears="none", extras=("translucent",)))
    # wisps
    b.append(f'<g stroke="#b8f0ff" stroke-width="1.4" fill="none" opacity=".35" filter="url(#{p}-b2)"><path d="M300 300 C260 260 280 220 250 180"/><path d="M500 300 C540 250 520 210 560 170"/><path d="M330 420 C300 400 290 360 260 350"/></g>')
    # the gas lamp she holds up
    b.append(f'<circle cx="250" cy="250" r="110" fill="url(#{p}-lamp)"/>'
             '<path d="M250 170 L250 196" stroke="#2a1a0a" stroke-width="2"/><path d="M236 196 L264 196 L268 206 L232 206 Z" fill="#2a1a0a"/>'
             '<path d="M236 206 C230 230 232 262 240 276 L260 276 C268 262 270 230 264 206 Z" fill="#ffd27a" opacity=".55"/>'
             f'<ellipse cx="250" cy="244" rx="7" ry="13" fill="#fff4c0" filter="url(#{p}-glow)"/>'
             '<path d="M236 206 C230 230 232 262 240 276 L260 276 C268 262 270 230 264 206" fill="none" stroke="#2a1a0a" stroke-width="2"/>'
             '<path d="M232 276 L268 276 L262 288 L238 288 Z" fill="#2a1a0a"/>')
    b.append(hand(p, 290, 300, .7, flip=True, rim="#7ae8ff", light="#ffd9a0", claws=False, pose="claw"))
    # the shredder eating a sticky note
    b.append('<rect x="520" y="400" width="120" height="70" fill="#0e0e10"/><rect x="530" y="396" width="100" height="8" fill="#000"/>'
             '<g transform="rotate(-6 580 380)"><rect x="552" y="350" width="56" height="48" fill="#e8d84a"/>'
             + text(556, 368, "PAUSE THE", 7.5, "#3a2a00", HAND) + text(556, 380, "SUBSTATION", 7.5, "#3a2a00", HAND) + text(556, 392, "— R.", 7.5, "#3a2a00", HAND) + "</g>"
             '<g stroke="#e8d84a" stroke-width="2" opacity=".7"><path d="M560 404 v14 M568 404 v18 M576 404 v12 M584 404 v20 M592 404 v14 M600 404 v16"/></g>'
             + text(580, 450, "SHRED-O-MATIC", 8, "#3a3a40", FELL, "middle"))
    b.append(text(400, 478, "I NEVER SAID THAT", 12, "#7ae8ff", FELL, "middle", 'letter-spacing="4" opacity=".45"'))
    return p, "The Gaslight Wraith", defs, "".join(b)


def bulldozer_ogre():
    p = "bo"
    defs = f'<radialGradient id="{p}-tube" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#e8fff4" stop-opacity=".22"/><stop offset="1" stop-color="#e8fff4" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#050405"/>']
    # whiteboard covered in his scrawl
    b.append('<rect x="30" y="40" width="300" height="200" fill="#9a9a96"/><rect x="30" y="40" width="300" height="200" fill="#000" opacity=".78"/>'
             '<g stroke="#a01818" stroke-width="3" fill="none" stroke-linecap="round" opacity=".85"><path d="M50 80 l60 -8 M50 100 l90 4 M60 130 c40 -20 80 30 120 -10 M200 70 l80 60 M280 70 l-80 60 M60 180 l200 -6"/><circle cx="240" cy="190" r="26"/></g>'
             + text(70, 220, "MY PLAN!!!", 20, "#a01818", HAND, "start", 'font-weight="700" opacity=".9"'))
    b.append(f'<path d="M260 0 L540 0 L700 480 L100 480 Z" fill="url(#{p}-tube)" filter="url(#{p}-b12)"/><rect x="330" y="0" width="140" height="8" fill="#e8fff4" filter="url(#{p}-glow)"/>')
    # exit sign red glow
    b.append('<rect x="660" y="40" width="70" height="26" fill="#1a0000"/>' + text(695, 59, "EXIT", 16, "#ff3a22", FELL, "middle", f'filter="url(#{p}-glow)"') + glowlight(p, 700, 80, 120, 90, "#ff2a14", .25))
    # the ogre: huge shoulders, small head, jabbing finger
    b.append(f'<g>{suit(p, 1, 420, 170, 1.35, tie="#3a3a10", jacket="#101014", shirt="#6a6a70", rim="#ff3a22")}</g>')
    b.append(face(p, 1, 420, 175, .62, sx=1.25, skin=("#1a1a12", "#4a4a3a", "#7a7a62"), light="above", light_col="#e8fff4", rim="#ff3a22",
                  eye="yellow", brows="angry", mouth="shout", hair="bald", ears="human", extras=("tusks",)))
    # the jabbing hand, and a crushed talking stick
    b.append(hand(p, 610, 300, 1.15, flip=False, rim="#ff3a22", light="#e8fff4", claws=False, pose="point"))
    b.append('<g transform="rotate(-30 230 380)"><rect x="200" y="370" width="90" height="10" rx="5" fill="#6a4a2a"/><path d="M240 368 l6 -8 4 10 6 -6" stroke="#d8c09a" stroke-width="1.4" fill="none"/></g>')
    b.append(hand(p, 230, 400, 1, flip=True, rim="#ff3a22", light="#e8fff4", claws=False, pose="claw"))
    b.append(text(196, 350, "TALKING STICK", 8, "#c9a26a", FELL, "start", 'transform="rotate(-30 230 380)"'))
    # tiny colleagues, hands half raised
    b.append(table(440, "#060506"))
    for k, cx in enumerate((90, 160, 650, 720)):
        b.append(f'<g transform="translate({cx} 440)"><circle cx="0" cy="-26" r="13" fill="#0c0c10"/><path d="M-20 0 Q0 -18 20 0 Z" fill="#0c0c10"/>'
                 + (f'<path d="M12 -6 L18 -36" stroke="#0c0c10" stroke-width="5" stroke-linecap="round"/>' if k % 2 == 0 else "")
                 + f'<path d="M-13 -26 a13 13 0 0 1 26 0" stroke="#e8fff4" stroke-width="1" fill="none" opacity=".35"/></g>')
    b.append(text(400, 490, "“SORRY, JUST TO JUMP IN—” (he is not sorry)", 12, "#c9b8a0", SERIF, "middle", 'font-style="italic" opacity=".7"'))
    return p, "The Bulldozer Ogre", defs, "".join(b)


def passive_aggressive_poltergeist():
    p = "pp"
    defs = (f'<radialGradient id="{p}-fridge" cx="0" cy=".5" r="1"><stop offset="0" stop-color="#e0f0ff" stop-opacity=".7"/><stop offset="1" stop-color="#e0f0ff" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-ghost" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8f4ff" stop-opacity=".55"/><stop offset="1" stop-color="#e8f4ff" stop-opacity="0"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030406"/>']
    # the office kitchen at night: an open fridge spills cold light
    b.append('<rect x="40" y="80" width="150" height="380" fill="#0a0c10"/><rect x="50" y="90" width="130" height="300" fill="#cfe0f0" opacity=".85"/>'
             '<g stroke="#8aa0b8" stroke-width="2"><path d="M50 160 H180 M50 230 H180 M50 300 H180"/></g>'
             '<rect x="70" y="240" width="24" height="56" fill="#6a8aaa"/><rect x="110" y="250" width="40" height="46" fill="#aa6a3a"/>'
             '<g transform="rotate(-4 120 200)"><rect x="96" y="186" width="56" height="34" fill="#f0e070"/>' + text(124, 200, "THIS IS", 7, "#3a2a00", HAND, "middle") + text(124, 211, "NOT YOURS", 7, "#3a2a00", HAND, "middle") + "</g>"
             f'<path d="M190 90 L520 0 L800 0 L800 500 L190 500 Z" fill="url(#{p}-fridge)" opacity=".5" filter="url(#{p}-b12)"/>')
    # the laminated sign, glowing
    b.append('<g transform="rotate(3 600 120)"><rect x="500" y="60" width="210" height="120" fill="#f4f2ea"/><rect x="504" y="64" width="202" height="112" fill="none" stroke="#c03030" stroke-width="2"/>'
             + text(605, 96, "PLEASE WASH", 22, "#a01010", BLACK, "middle") + text(605, 124, "YOUR MUG", 22, "#a01010", BLACK, "middle")
             + text(605, 152, "AS PER POLICY (attached again) :)", 10, "#333", SERIF, "middle", 'font-style="italic"') + "</g>")
    # the poltergeist: a sheet of light with a polite, terrible smile
    b.append(f'<path d="M330 120 C270 130 260 210 262 290 C264 360 246 420 230 470 L300 450 L330 480 L370 448 L410 480 L450 448 L490 476 L520 450 C500 400 488 340 490 280 C492 200 470 130 410 120 Z" fill="url(#{p}-ghost)" filter="url(#{p}-b3)"/>')
    b.append(face(p, 1, 372, 220, .62, skin=("#2a3442", "#7a8a9a", "#c8d4e0"), light="left", light_col="#e0f0ff", rim="#7ab0ff", rim_side="right",
                  eye="milky", glow=False, brows="raised", mouth="smile", hair="bob", hair_col="#0a0c12", ears="none", extras=("blush",)))
    # floating things: mugs, envelopes, a CC
    for k, (x, y, r) in enumerate(((210, 140, -20), (620, 260, 25), (560, 370, -10))):
        b.append(f'<g transform="rotate({r} {x} {y})">{mug(x - 22, y - 26, "PER MY", "LAST EMAIL", "#d8d2c4", "#5a1a1a", False)}</g>')
    for k, (x, y) in enumerate(((180, 330), (640, 200), (250, 60), (690, 380))):
        b.append(f'<g transform="translate({x} {y}) rotate({(k * 23) % 40 - 20})" opacity=".85"><rect x="-22" y="-14" width="44" height="28" fill="#e8eef8"/><path d="M-22 -14 L0 4 L22 -14" stroke="#8a9ab0" fill="none"/>'
                 + (text(0, 24, "CC: your manager", 6.5, "#c9d4e4", SERIF, "middle") if k == 1 else "") + "</g>")
    b.append(f'<g stroke="#e0f0ff" stroke-width="1" opacity=".25" fill="none" filter="url(#{p}-b1)"><path d="M200 160 c10 -10 20 -10 30 0"/><path d="M600 290 c-10 10 -20 10 -30 0"/></g>')
    b.append(table(470, "#08090c"))
    b.append(text(400, 492, "“Kind regards” (20% kind)", 12, "#c9d4e4", SERIF, "middle", 'font-style="italic" opacity=".6"'))
    return p, "The Passive-Aggressive Poltergeist", defs, "".join(b)


def coasting_zombie():
    p = "cz"
    defs = f'<radialGradient id="{p}-mon" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#bfffd0" stop-opacity=".6"/><stop offset="1" stop-color="#bfffd0" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#030503"/>']
    # a calendar still on March, a dead plant
    b.append('<rect x="60" y="60" width="110" height="130" fill="#0c100c"/><rect x="60" y="60" width="110" height="26" fill="#3a0a0a"/>'
             + text(115, 79, "MARCH", 14, "#b8a890", FELL, "middle") + text(115, 140, "4", 46, "#4a5a48", BLACK, "middle")
             + text(115, 178, "(it is November)", 9, "#6a7a68", HAND, "middle"))
    b.append('<path d="M640 360 L690 360 L684 420 L646 420 Z" fill="#1a120c"/><g stroke="#3a3020" stroke-width="2" fill="none"><path d="M664 360 C660 320 640 300 620 300 M666 360 C670 330 690 316 704 330 M665 360 C664 340 668 316 660 296"/></g>'
             '<g fill="#3a3020"><path d="M620 300 l-6 6 8 2 Z M704 330 l6 6 -8 2 Z"/></g>')
    # the monitor, back to us, green glow on him
    b.append(f'<ellipse cx="420" cy="260" rx="260" ry="200" fill="url(#{p}-mon)" filter="url(#{p}-b24)"/>')
    b.append(suit(p, 1, 410, 186, 1.05, tie="#2a3a1a", jacket="#121610", shirt="#4a5440", rim="#7aff9a"))
    b.append(face(p, 1, 410, 170, .72, skin=("#10160c", "#3a4a2c", "#6a7a52"), light="below", light_col="#c8ffd8", rim="#7aff9a", rim_side="right",
                  eye="milky", glow=False, brows="flat", mouth="slack", hair="patchy", hair_col="#0a0c08", ears="human", extras=("rot", "stitches"), tilt=-8))
    # headset
    b.append('<path d="M350 120 C350 70 470 70 470 120" stroke="#0a0a0a" stroke-width="6" fill="none"/><rect x="340" y="120" width="16" height="30" rx="6" fill="#0a0a0a"/><path d="M350 150 C350 190 370 210 390 214" stroke="#0a0a0a" stroke-width="3" fill="none"/>')
    # the desk, keyboard with cobwebs, a progress bar on a second screen facing us
    b.append(table(420, "#070806"))
    b.append('<rect x="520" y="300" width="160" height="110" fill="#050605" stroke="#1a1a18" stroke-width="3"/>'
             '<rect x="536" y="350" width="128" height="14" fill="#0a0c0a" stroke="#2a4a2a"/><rect x="537" y="351" width="19" height="12" fill="#5aff7a" opacity=".85"/>'
             + text(600, 340, "ASSET CLEAN-UP", 9, "#7aff9a", MONO, "middle") + text(600, 382, "15% · in progress", 9, "#7aff9a", MONO, "middle")
             + text(600, 396, "since 4 March", 8, "#4a8a5a", MONO, "middle"))
    b.append('<rect x="250" y="430" width="200" height="30" fill="#0a0c0a" transform="skewX(-14)"/><path d="M260 432 L330 458 M300 432 L270 458 M262 445 C290 440 310 446 330 440" stroke="#b8c0b0" stroke-width=".7" fill="none" opacity=".5"/>')
    b.append(mug(150, 400, "IN", "PROGRESS", "#1c1f1a", "#5a6a50"))
    return p, "The Coasting Zombie", defs, "".join(b)


def doppelganger():
    p = "dg"
    defs = (f'<linearGradient id="{p}-glass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0a1218"/><stop offset="1" stop-color="#05080c"/></linearGradient>'
            f'<radialGradient id="{p}-warm" cx=".3" cy=".6" r=".6"><stop offset="0" stop-color="#ffb070" stop-opacity=".35"/><stop offset="1" stop-color="#ffb070" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040304"/>', f'<rect width="{W}" height="{H}" fill="url(#{p}-warm)"/>']
    # the glass wall of a meeting room; behind it, her reflection is something else
    b.append(f'<rect x="430" y="20" width="360" height="460" fill="url(#{p}-glass)"/><path d="M430 20 V480 M610 20 V480" stroke="#1a2a34" stroke-width="3"/>'
             '<g stroke="#9ab8d0" stroke-width="1" opacity=".18"><path d="M450 40 l120 160 M480 40 l140 190 M640 60 l120 160"/></g>')
    b.append('<g opacity=".72">' + blouse(p, 610, 199, .82, cardigan="#0c1018", top="#1a1c28", rim="#7ab0ff", rim_side="right", necklace=False)
             + face(p, 2, 610, 170, .75, skin=("#06080e", "#2a3446", "#5a6a86"), light="right", light_col="#9ab8ff", rim="#7ab0ff",
                    eye="violet", brows="angry", mouth="sharp", hair="bob", hair_col="#020306", ears="pointed") + "</g>")
    b.append(hand(p, 690, 330, .9, rim="#7ab0ff", light="#9ab8ff", pose="claw"))
    b.append('<g transform="rotate(-20 700 250)"><path d="M696 160 L704 160 L708 250 L692 250 Z" fill="#c8d4e4"/><path d="M696 160 L700 140 L704 160 Z" fill="#e8f0ff"/><rect x="690" y="250" width="20" height="40" rx="3" fill="#1a0a0a"/></g>')
    b.append(text(610, 470, "“some people feel…”", 12, "#9ab8ff", HAND, "middle", 'opacity=".55"'))
    # in front: Saskia, warm and lovely, buns
    b.append(blouse(p, 240, 194, .9, cardigan="#3a2418", top="#6a4a3a", rim="#ffb070", rim_side="left"))
    b.append(face(p, 1, 240, 165, .8, skin=("#2a1a14", "#8a6a5a", "#d8b8a0"), light="left", light_col="#ffd8b0", rim="#ffb070", rim_side="left",
                  eye="human", glow=False, brows="raised", mouth="smile", hair="bob", hair_col="#2a160c", ears="none", lip="#a04a4a", mouth_col="#3a1010"))
    b.append('<ellipse cx="300" cy="400" rx="90" ry="20" fill="#d8d0c0"/><ellipse cx="300" cy="396" rx="84" ry="16" fill="#efe8dc"/>')
    for x, y in ((260, 384), (300, 380), (340, 386), (282, 370), (320, 370)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="18" ry="11" fill="#a8642a"/><path d="M{x - 10} {y - 2} c6 -6 14 -6 20 0" stroke="#e8c890" stroke-width="1.2" fill="none"/>')
    b.append(text(300, 440, "cardamom buns, for you ♥", 13, "#ffd8b0", HAND, "middle", 'opacity=".7"'))
    return p, "The Doppelgänger", defs, "".join(b)


def martyr_banshee():
    p = "mb"
    defs = f'<radialGradient id="{p}-scr" cx=".5" cy="1" r="1"><stop offset="0" stop-color="#cfe0ff" stop-opacity=".6"/><stop offset="1" stop-color="#cfe0ff" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#03030a"/>']
    wg, wb = window(p, 600, 200, "#05081a", lights=False, pylon=False)
    defs += wg
    b.append(wb + '<circle cx="700" cy="80" r="26" fill="#e8e6d0" opacity=".75" filter="url(#mb-b2)"/>')
    b.append(text(120, 70, "23:58", 34, "#ff3a22", MONO, "middle", f'filter="url(#{p}-glow)"'))
    # papers swirling
    for k in range(14):
        x, y, r = 80 + (k * 97) % 640, 60 + (k * 61) % 330, (k * 37) % 70 - 35
        if x < 220 and y < 110:
            continue
        col = "#e8e4d8" if k % 3 else "#f0e070"
        b.append(f'<rect x="{x}" y="{y}" width="{30 if k % 3 else 22}" height="{38 if k % 3 else 22}" fill="{col}" opacity=".55" transform="rotate({r} {x} {y})"/>')
    b.append(f'<ellipse cx="400" cy="420" rx="300" ry="160" fill="url(#{p}-scr)" filter="url(#{p}-b12)"/>')
    # the banshee: long hair streaming, mouth wide
    b.append(f'<path d="M330 120 C230 100 160 160 120 120 C170 200 240 190 300 220 Z M470 120 C570 100 640 160 680 120 C630 200 560 190 500 220 Z" fill="#05050a"/>'
             f'<path d="M120 120 C170 200 240 190 300 220" stroke="#9ab0ff" stroke-width="1.2" fill="none" opacity=".5"/>')
    b.append(blouse(p, 400, 199, .9, cardigan="#0e0e18", top="#1e1e2c", rim="#9ab0ff", rim_side="right"))
    b.append(face(p, 1, 400, 175, .74, skin=("#0c0c16", "#3a3c52", "#7a80a0"), light="below", light_col="#cfe0ff", rim="#9ab0ff",
                  eye="cyan", brows="worried", mouth="wail", hair="long", hair_col="#05050a", ears="none"))
    # hands to her head
    b.append(hand(p, 300, 170, .85, flip=True, rim="#9ab0ff", light="#cfe0ff", claws=True, pose="claw"))
    b.append(hand(p, 500, 170, .85, rim="#9ab0ff", light="#cfe0ff", claws=True, pose="claw"))
    # laptop with 400 unread and her status
    b.append(table(440, "#05050a"))
    b.append('<path d="M250 440 L270 360 L530 360 L550 440 Z" fill="#0a0c12"/><rect x="290" y="372" width="220" height="56" fill="#cfe0ff" opacity=".85"/>'
             + text(400, 392, "Inbox (412)", 13, "#1a2a4a", SERIF, "middle", 'font-weight="700"') + text(400, 412, "status: drowning 🫠", 11, "#1a2a4a", SERIF, "middle")
             + text(400, 424, "help offered: 3 · help accepted: 0", 8, "#4a5a7a", SERIF, "middle"))
    return p, "The Martyr Banshee", defs, "".join(b)


def know_it_all_basilisk():
    p = "kb"
    defs = (f'<linearGradient id="{p}-scale" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a5a2a"/><stop offset=".5" stop-color="#14220e"/><stop offset="1" stop-color="#050804"/></linearGradient>'
            f'<pattern id="{p}-scales" width="12" height="10" patternUnits="userSpaceOnUse"><path d="M0 10 Q6 0 12 10" stroke="#000" stroke-width="1" fill="none" opacity=".5"/></pattern>'
            f'<radialGradient id="{p}-stone" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#a8a49a"/><stop offset="1" stop-color="#2a2824"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030503"/>', glowlight(p, 400, 220, 280, 200, "#5aff6a", .12)]
    # bookshelf of old physics
    for k in range(10):
        b.append(f'<rect x="{40 + k * 22}" y="{70 + (k % 3) * 6}" width="18" height="{110 - (k % 3) * 6}" fill="{["#2a1410", "#14202a", "#2a2410"][k % 3]}"/>'
                 + text(49 + k * 22, 170, "1987" if k % 2 else "PHYS", 6, "#8a7a5a", FELL, "middle", f'transform="rotate(-90 {49 + k * 22} 170)"'))
    b.append('<rect x="30" y="180" width="240" height="8" fill="#1a120a"/>')
    # the serpent's coils
    b.append(f'<path d="M120 470 C120 400 260 380 400 400 C560 420 680 400 680 340 C680 280 560 270 480 300 C420 322 420 360 470 360" stroke="url(#{p}-scale)" stroke-width="64" fill="none" stroke-linecap="round"/>'
             f'<path d="M120 470 C120 400 260 380 400 400 C560 420 680 400 680 340 C680 280 560 270 480 300 C420 322 420 360 470 360" stroke="url(#{p}-scales)" stroke-width="64" fill="none" stroke-linecap="round"/>'
             '<path d="M140 440 C160 404 260 390 400 408 C560 428 670 410 676 350" stroke="#9aff8a" stroke-width="1.4" fill="none" opacity=".4"/>')
    # the neck rises into a human-ish head with glasses and a lanyard
    b.append(f'<path d="M470 360 C520 320 520 250 470 180" stroke="url(#{p}-scale)" stroke-width="56" fill="none" stroke-linecap="round"/>')
    b.append('<path d="M450 250 L470 300 L490 250" stroke="#1e3e6a" stroke-width="3" fill="none"/>' + badge(434, 296, "DR. L. ASHE", "Principal Eng.", "RIGHT SINCE 2011", "", rot=6))
    b.append(face(p, 1, 470, 150, .66, skin=("#0a1408", "#2e4a24", "#6a8a52"), light="above", light_col="#c8ffb8", rim="#9aff8a", rim_side="left",
                  eye="yellow", brows="flat", mouth="thin", hair="bald", ears="none", extras=("glasses",)))
    b.append('<path d="M470 196 l-4 18 M466 214 l-6 6 M466 214 l6 6" stroke="#c0304a" stroke-width="2" fill="none"/>')
    b.append(f'<g filter="url(#{p}-glow)" opacity=".6"><path d="M456 148 L300 250" stroke="#ffe14a" stroke-width="2"/><path d="M484 148 L320 262" stroke="#ffe14a" stroke-width="2"/></g>')
    # Pip, turned to stone, laptop still open
    b.append(f'<g transform="translate(250 300)"><path d="M-50 160 C-48 90 -30 60 0 56 C30 60 48 90 50 160 Z" fill="url(#{p}-stone)"/>'
             f'<circle cx="0" cy="20" r="34" fill="url(#{p}-stone)"/><path d="M-14 16 h8 M8 16 h8 M-8 36 q8 -4 16 0" stroke="#3a3830" stroke-width="2"/>'
             '<path d="M-40 96 L40 96 L48 120 L-48 120 Z" fill="#6a665e"/><path d="M-36 76 L36 76 L40 96 L-40 96 Z" fill="#8a867c"/>'
             '<g stroke="#1a1814" stroke-width="1" fill="none" opacity=".7"><path d="M-20 -6 l8 14 -4 10 M18 40 l10 30 -6 16 M-30 110 l14 -8"/></g></g>'
             + text(250, 492, "Pip, with an idea (former)", 12, "#c8c4b0", SERIF, "middle", 'font-style="italic" opacity=".6"'))
    b.append(text(640, 60, "“That won't work. Next.”", 15, "#c8ffb8", HAND, "middle", 'opacity=".6"'))
    return p, "The Know-It-All Basilisk", defs, "".join(b)


def doom_prophet():
    p = "dp"
    defs = f'<linearGradient id="{p}-robe" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a0c0a"/><stop offset="1" stop-color="#030101"/></linearGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#050101"/>']
    # the control room wall: screens of alarms
    for r in range(3):
        for c in range(6):
            x, y = 30 + c * 128, 30 + r * 78
            on = (r * 6 + c) % 4 != 1
            b.append(f'<rect x="{x}" y="{y}" width="118" height="68" fill="{"#3a0604" if on else "#0a0404"}" stroke="#1a0a08"/>'
                     + (f'<path d="M{x + 8} {y + 50} l14 -10 12 6 14 -24 12 14 14 -6 12 8 14 -16" stroke="#ff4a2a" stroke-width="1.6" fill="none"/>' + text(x + 59, y + 18, "ALARM", 9, "#ff6a4a", MONO, "middle") if on else ""))
    b.append(glowlight(p, 400, 120, 420, 140, "#ff2010", .35))
    # the prophet: hooded, wrinkled, one finger raised
    b.append(f'<path d="M400 90 C320 96 300 170 296 260 C292 340 270 410 240 480 L560 480 C530 410 508 340 504 260 C500 170 480 96 400 90 Z" fill="url(#{p}-robe)"/>'
             f'<rect x="240" y="90" width="320" height="400" filter="url(#{p}-cloth)" opacity=".7"/>'
             f'<path d="M400 90 C480 96 500 170 504 260" stroke="#ff4a2a" stroke-width="2" fill="none" opacity=".5" filter="url(#{p}-b1)"/>')
    b.append(face(p, 1, 400, 225, .68, skin=("#140806", "#4a3028", "#8a6a5a"), light="below", light_col="#ffd8b0", rim="#ff4a2a",
                  eye="red", glow=True, brows="worried", mouth="thin", hair="bald", ears="human", extras=("wrinkles",)))
    b.append(f'<path d="M400 120 C340 124 316 180 322 250 C334 200 360 168 400 160 C440 168 466 200 478 250 C484 180 460 124 400 120 Z" fill="#050101"/>')
    # beard
    b.append('<path d="M370 280 C372 330 386 370 400 390 C414 370 428 330 430 280 C416 300 384 300 370 280 Z" fill="#8a8078" opacity=".75"/>'
             '<g stroke="#4a4038" stroke-width=".8" fill="none"><path d="M380 300 l6 60 M392 304 l4 70 M408 304 l-4 70 M420 300 l-6 60"/></g>')
    b.append(hand(p, 540, 300, .95, rim="#ff4a2a", light="#ffd8b0", claws=False, pose="point"))
    # the dusty printout
    b.append('<g transform="rotate(-8 250 380)"><rect x="190" y="330" width="120" height="150" fill="#d8d0b8"/><rect x="190" y="330" width="120" height="150" fill="#3a2010" opacity=".3"/>'
             + text(250, 352, "INCIDENT REPORT", 9, "#2a1a10", FELL, "middle") + text(250, 372, "2014", 20, "#7a1010", BLACK, "middle")
             + "".join(f'<path d="M202 {388 + k * 9} h{70 + (k * 13) % 30}" stroke="#5a4a3a" stroke-width="1.4"/>' for k in range(8)) + "</g>")
    b.append(hand(p, 260, 420, .8, flip=True, rim="#ff4a2a", light="#ffd8b0", claws=False, pose="claw"))
    # candles on the console
    b.append(table(460, "#080302"))
    for x in (110, 150, 650, 690):
        b.append(f'<rect x="{x}" y="{430}" width="12" height="30" fill="#d8c8a0"/><ellipse cx="{x + 6}" cy="424" rx="4" ry="8" fill="#ffd27a" filter="url(#{p}-glow)"/>')
    b.append(text(400, 492, "“We tried that in 2014.”", 13, "#ffd8b0", SERIF, "middle", 'font-style="italic" opacity=".65"'))
    return p, "The Doom Prophet", defs, "".join(b)


def toxic_positivity_siren():
    p = "tp"
    defs = (f'<linearGradient id="{p}-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a2a3a" stop-opacity=".9"/><stop offset="1" stop-color="#020a10"/></linearGradient>'
            f'<radialGradient id="{p}-neon" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ff4ad0" stop-opacity=".45"/><stop offset="1" stop-color="#ff4ad0" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040208"/>']
    b.append(f'<ellipse cx="400" cy="60" rx="380" ry="120" fill="url(#{p}-neon)"/>')
    b.append(text(400, 58, "GOOD VIBES ONLY", 38, "#ffd0f4", BLACK, "middle", f'filter="url(#{p}-glow)" letter-spacing="3"'))
    b.append(text(400, 58, "GOOD VIBES ONLY", 38, "none", BLACK, "middle", 'stroke="#ff4ad0" stroke-width="1.2" letter-spacing="3"'))
    # balloons, one deflating
    for x, y, c in ((110, 170, "#ff4a8a"), (160, 140, "#ffd04a"), (680, 160, "#4ad0ff"), (720, 210, "#ff4a8a")):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="27" fill="{c}" opacity=".7"/><path d="M{x} {y + 27} C{x - 6} {y + 70} {x + 8} {y + 110} {x} {y + 160}" stroke="#aaa" stroke-width=".8" fill="none" opacity=".5"/>')
    b.append('<path d="M700 260 c10 -6 18 2 12 10 c-8 10 -20 4 -12 -10z" fill="#ffd04a" opacity=".5"/>')
    # the siren
    b.append(blouse(p, 400, 219, .9, cardigan="#2a0a24", top="#ff4ad0", rim="#ff4ad0", rim_side="left"))
    b.append(face(p, 1, 400, 195, .74, skin=("#1a0814", "#6a3a5a", "#e0a8c8"), light="above", light_col="#ffd0f4", rim="#4ad0ff",
                  eye="violet", brows="raised", mouth="grin", hair="long", hair_col="#1a0418", ears="none", extras=("blush", "lipstick")))
    # the gong and mallet
    b.append(f'<circle cx="620" cy="300" r="70" fill="#8a6a1a"/><circle cx="620" cy="300" r="60" fill="#c8a03a"/><circle cx="620" cy="300" r="20" fill="#a07a1a"/>'
             '<path d="M548 220 L692 220 M560 220 L560 380 M680 220 L680 380" stroke="#2a1a0a" stroke-width="6"/>' + text(620, 306, "JOY", 14, "#4a2a0a", BLACK, "middle"))
    b.append(hand(p, 520, 290, .9, rim="#4ad0ff", light="#ffd0f4", claws=True, pose="claw"))
    b.append('<path d="M520 240 L580 300" stroke="#4a2a0a" stroke-width="5"/><circle cx="584" cy="304" r="10" fill="#ff4ad0"/>')
    # the office is flooding
    b.append(f'<path d="M0 400 Q100 390 200 402 T400 398 T600 404 T800 396 L800 500 L0 500 Z" fill="url(#{p}-water)"/>'
             '<path d="M0 400 Q100 390 200 402 T400 398 T600 404 T800 396" stroke="#7ad8ff" stroke-width="1.4" fill="none" opacity=".5"/>')
    for k, (x, y, r) in enumerate(((120, 430, 10), (300, 450, -16), (560, 440, 8), (690, 460, -6))):
        b.append(f'<rect x="{x}" y="{y}" width="40" height="28" fill="#e8e4d8" opacity=".45" transform="rotate({r} {x} {y})"/>')
    b.append(f'<g transform="rotate(-12 200 420)"><rect x="150" y="410" width="110" height="24" fill="#d8d0c0" opacity=".7"/>' + text(205, 427, "Q4 RISKS", 11, "#3a2a2a", FELL, "middle") + "</g>")
    b.append(text(400, 490, "“Let's reframe the iceberg as a growth opportunity 🚀”", 12, "#ffd0f4", SERIF, "middle", 'font-style="italic" opacity=".6"'))
    return p, "The Toxic Positivity Siren", defs, "".join(b)


def boundary_goblin():
    p = "bg"
    defs = f'<radialGradient id="{p}-phone" cx=".5" cy="1" r="1"><stop offset="0" stop-color="#b9ffd9" stop-opacity=".7"/><stop offset="1" stop-color="#b9ffd9" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#03040a"/>']
    wg, wb = window(p, 560, 220, "#05081a", lights=True, pylon=True)
    defs += wg
    b.append(wb + '<circle cx="640" cy="70" r="22" fill="#e8e6c0" opacity=".8"/><circle cx="648" cy="64" r="20" fill="#060b18"/>')
    # bed, sleeper
    b.append('<path d="M20 330 L520 330 L540 480 L0 480 Z" fill="#0c0e1a"/><path d="M30 330 C120 270 330 280 470 310 L520 330 Z" fill="#161a2c"/>'
             '<ellipse cx="80" cy="314" rx="40" ry="20" fill="#1c2238"/>' + text(120, 260, "z z z", 20, "#5a64a0", HAND, "middle", 'opacity=".6"'))
    b.append(text(70, 90, "23:47", 34, "#ff3a22", MONO, "middle", f'filter="url(#{p}-glow)"'))
    # the goblin crouched at the foot of the bed
    b.append('<path d="M300 480 C290 400 310 330 380 300 C450 290 500 330 510 400 C516 440 510 480 506 480 Z" fill="#050604"/>'
             '<path d="M380 300 C450 290 500 330 510 400" stroke="#9aa3d6" stroke-width="1.6" fill="none" opacity=".5"/>')
    b.append(f'<ellipse cx="400" cy="300" rx="160" ry="150" fill="url(#{p}-phone)" filter="url(#{p}-b12)"/>')
    b.append(face(p, 1, 410, 230, .7, sx=1.15, skin=("#0a1008", "#2a3a22", "#6a8a5a"), light="below", light_col="#c8ffe0", rim="#9aa3d6", rim_side="right",
                  eye="yellow", brows="raised", mouth="sharp", hair="bald", ears="big"))
    # the phone
    b.append(hand(p, 360, 380, .8, flip=True, rim="#9aa3d6", light="#c8ffe0", pose="claw"))
    b.append(f'<g transform="rotate(-10 400 360)"><rect x="372" y="320" width="56" height="96" rx="7" fill="#0a0a0a"/><rect x="376" y="326" width="48" height="84" rx="4" fill="#d8fff0" filter="url(#{p}-glow)"/>'
             '<rect x="380" y="336" width="40" height="20" rx="4" fill="#ffffff"/>' + text(400, 349, "quick q 🙂", 7, "#0a2a1c", MONO, "middle")
             + '<rect x="380" y="360" width="40" height="14" rx="4" fill="#ffffff"/>' + text(400, 370, "no rush", 7, "#0a2a1c", MONO, "middle")
             + '<rect x="380" y="378" width="18" height="14" rx="4" fill="#ffffff"/>' + text(389, 388, "?", 8, "#0a2a1c", MONO, "middle")
             + text(400, 404, "23:47", 7, "#a00", MONO, "middle") + "</g>")
    b.append(hand(p, 450, 380, .8, rim="#9aa3d6", light="#c8ffe0", pose="claw"))
    return p, "The Boundary Goblin", defs, "".join(b)


PLATES = {
    "meeting-lich": meeting_lich, "gaslight-wraith": gaslight_wraith, "bulldozer-ogre": bulldozer_ogre,
    "passive-aggressive-poltergeist": passive_aggressive_poltergeist, "coasting-zombie": coasting_zombie,
    "doppelganger": doppelganger, "martyr-banshee": martyr_banshee, "know-it-all-basilisk": know_it_all_basilisk,
    "doom-prophet": doom_prophet, "toxic-positivity-siren": toxic_positivity_siren, "boundary-goblin": boundary_goblin,
}


def main():
    ART.mkdir(parents=True, exist_ok=True)
    for slug, fn in PLATES.items():
        p, label, defs, body = fn()
        (ART / f"{slug}.svg").write_text(fix(p, svg(p, label, defs, body)), encoding="utf-8")
    print(f"wrote {len(PLATES)} plates")


if __name__ == "__main__":
    main()
