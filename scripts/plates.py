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


# ================================================================ Act I plates (three only)
def hidden_thrones():
    p = "ht"
    defs = (f'<radialGradient id="{p}-lamp" cx="0" cy=".2" r="1"><stop offset="0" stop-color="#ffcf8a" stop-opacity=".7"/><stop offset="1" stop-color="#ffcf8a" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-leather" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2a0e0a"/><stop offset=".5" stop-color="#140504"/><stop offset="1" stop-color="#050101"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030305"/>', glowlight(p, 260, 200, 260, 180, "#7a8ab0", .14)]
    # the org chart on the wall
    boxes = [(200, 60, 160, 40, "VP STRATEGIC SYNERGY", True), (60, 150, 120, 30, "Grid Planning", False), (200, 150, 120, 30, "Network Assets", False),
             (340, 150, 120, 30, "Customer Ops", False), (60, 230, 120, 30, "Strategy", False), (200, 230, 120, 30, "Lumen", False), (340, 230, 120, 30, "Finance", False)]
    lines = '<g stroke="#5a6680" stroke-width="1.4" opacity=".6"><path d="M280 100 V128 M120 128 H400 M120 128 V150 M260 128 V150 M400 128 V150 M120 180 V230 M260 180 V230 M400 180 V230"/></g>'
    b.append(lines)
    for x, y, w, h, t, big in boxes:
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#141824" stroke="#5a6680"/>' + text(x + w / 2, y + h / 2 + 4, t, 12 if big else 10, "#b8c4dc", FELL, "middle"))
    b.append('<rect x="420" y="70" width="80" height="22" fill="#141824" stroke="#5a6680" stroke-dasharray="3 3"/>' + text(460, 85, "Chief of Staff", 8.5, "#b8c4dc", FELL, "middle")
             + '<path d="M360 80 H420" stroke="#5a6680" stroke-dasharray="3 3"/>')
    # the red string: every box really runs to the small one
    pins = [(174, 156), (314, 156), (454, 156), (174, 236), (314, 236), (454, 236), (354, 66)]
    b.append('<g stroke="#d4201a" stroke-width="1.3" fill="none" opacity=".9">' + "".join(f'<path d="M{x} {y} Q{(x + 424) / 2} {min(y, 81) - 24} 424 81"/>' for x, y in pins) + "</g>"
             + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#ff3a22" filter="url(#{p}-glow)"/>' for x, y in pins + [(424, 81)]))
    b.append(text(260, 300, "the official map", 13, "#8a96b0", HAND, "middle", 'opacity=".6"') + text(560, 70, "the real one →", 13, "#ff5a4a", HAND, "middle", 'opacity=".7" transform="rotate(-6 560 70)"'))
    # the high-backed chair and Ottoline in it
    b.append(f'<path d="M500 470 L500 150 C500 100 530 80 580 80 C630 80 660 100 660 150 L660 470 Z" fill="url(#{p}-leather)"/>'
             '<g fill="#3a1410" opacity=".6">' + "".join(f'<circle cx="{x}" cy="{y}" r="2.4"/>' for x in (520, 545, 570, 595, 620, 645) for y in (110, 150, 190)) + "</g>"
             f'<path d="M660 150 L660 470" stroke="#ff5a2a" stroke-width="1.4" opacity=".35"/>')
    b.append(f'<path d="M300 0 L460 0 L760 470 L260 470 Z" fill="url(#{p}-lamp)" filter="url(#{p}-b24)" opacity=".5"/>')
    b.append(blouse(p, 580, 233, .78, cardigan="#141016", top="#2a2028", rim="#ffb070", rim_side="left"))
    b.append(face(p, 1, 580, 170, .7, skin=("#1a1210", "#6a5048", "#c8a890"), light="left", light_col="#ffd6a8", rim="#7a8ab0", rim_side="right",
                  eye="violet", glow=False, brows="flat", mouth="smile", hair="bob", hair_col="#08060a", ears="none", lip="#7a2a30"))
    # the desk, a lamp, the mug
    b.append(table(420, "#070505"))
    b.append('<path d="M330 420 L350 300 L370 300" stroke="#1a1410" stroke-width="5" fill="none"/><path d="M350 300 L330 270 L390 262 Z" fill="#1a1410"/>'
             f'<ellipse cx="360" cy="276" rx="22" ry="6" fill="#ffd6a8" filter="url(#{p}-glow)"/>')
    b.append(mug(430, 368, "I'M NOT", "IN CHARGE", "#d8d0c0", "#5a1a1a") + text(452, 412, "(I am)", 6, "#5a1a1a", HAND, "middle"))
    b.append(hand(p, 640, 360, .7, rim="#7a8ab0", light="#ffd6a8", claws=False, pose="claw"))
    return p, "The Map of Hidden Thrones", defs, "".join(b)


def ring_kissing_ritual():
    p = "rk"
    defs = (f'<radialGradient id="{p}-gold" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#ffd27a" stop-opacity=".55"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-throne" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1006"/><stop offset="1" stop-color="#080302"/></linearGradient>'
            f'<radialGradient id="{p}-ring" cx=".35" cy=".35" r=".7"><stop offset="0" stop-color="#fff2b0"/><stop offset=".5" stop-color="#d8a020"/><stop offset="1" stop-color="#5a3a00"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040202"/>', f'<path d="M380 0 L540 0 L700 470 L220 470 Z" fill="url(#{p}-gold)" filter="url(#{p}-b24)"/>']
    # the throne on a dais of A4 boxes
    b.append('<g fill="#d8d2c4" stroke="#8a8270">' + "".join(f'<rect x="{360 + c * 70 - r * 35}" y="{430 - r * 34}" width="70" height="34"/>' for r in range(2) for c in range(3 - r)) + "</g>"
             + "".join(text(395 + c * 70, 452, "A4", 11, "#5a5040", FELL, "middle") for c in range(3)))
    b.append(f'<path d="M380 380 L380 120 C380 60 420 34 470 34 C520 34 560 60 560 120 L560 380 Z" fill="url(#{p}-throne)"/>'
             '<path d="M470 34 l-10 -20 10 6 10 -6 z" fill="#d8a020"/><path d="M380 120 C380 60 420 34 470 34 C520 34 560 60 560 120" stroke="#d8a020" stroke-width="2" fill="none" opacity=".7"/>')
    b.append(suit(p, 1, 470, 202, .82, tie="#a07a10", jacket="#0c0a10", shirt="#6a6070", rim="#ffd27a"))
    b.append(face(p, 1, 470, 150, .62, skin=("#1a1010", "#6a5450", "#c8b0a0"), light="above", light_col="#ffe2a8", rim="#ff3a22",
                  eye="yellow", glow=True, brows="raised", mouth="smile", hair="slick", hair_col="#0a0806", ears="human"))
    # the extended hand with the signet ring
    b.append('<path d="M420 300 C390 310 360 320 334 322" stroke="#0c0a10" stroke-width="22" stroke-linecap="round" fill="none"/>')
    b.append(f'<g transform="rotate(-96 318 322)">{hand(p, 318, 322, .62, rim="#ffd27a", light="#ffe2a8", claws=False, pose="open")}</g>')
    b.append(f'<ellipse cx="300" cy="326" rx="9" ry="7" fill="url(#{p}-ring)" filter="url(#{p}-glow)"/><path d="M298 321 l-3 5 3 0 -2 5 5 -6 -3 0 2 -4z" fill="#5a3a00"/>')
    # nameplate
    b.append('<rect x="400" y="392" width="140" height="22" fill="#2a1a06" stroke="#d8a020"/>' + text(470, 407, "S. VARNISH · VP STRATEGIC SYNERGY", 8, "#ffd27a", FELL, "middle"))
    # the queue of the devoted, bowing, lanyards on
    for k, (x, sc) in enumerate(((286, 1.2), (214, 1.05), (152, .92), (98, .8), (52, .7))):
        bow = 34 if k == 0 else 22
        b.append(f'<g transform="translate({x} 470) scale({sc})"><path d="M-22 0 L-18 -70 C-14 -96 6 -104 24 -96 L30 -60 L24 0 Z" fill="#0a0806"/>'
                 f'<circle cx="{30 + bow * .2}" cy="{-98 + bow}" r="15" fill="#0a0806"/><path d="M14 -90 L22 -60" stroke="#1e3e6a" stroke-width="2"/>'
                 f'<rect x="18" y="-62" width="10" height="13" fill="#c9cfdc" opacity=".8"/>'
                 f'<path d="M-18 -70 C-14 -96 6 -104 24 -96 L30 -60" stroke="#ffd27a" stroke-width="1.6" fill="none" opacity=".75"/>'
                 f'<path d="M{16 + bow * .2} {-110 + bow} a15 15 0 0 1 26 4" stroke="#ffd27a" stroke-width="1.4" fill="none" opacity=".7"/></g>')
    b.append(text(286, 492, "Dorian (first, as always)", 10, "#c9b8a0", HAND, "middle", 'opacity=".6"'))
    # candles
    for x in (360, 600, 640):
        b.append(f'<rect x="{x}" y="{400}" width="12" height="40" fill="#e0d4b0"/><ellipse cx="{x + 6}" cy="394" rx="4" ry="9" fill="#ffd27a" filter="url(#{p}-glow)"/>')
    b.append(text(660, 120, "“Great point,", 16, "#ffd27a", HAND, "middle", 'opacity=".55"') + text(660, 140, "Simon.”", 16, "#ffd27a", HAND, "middle", 'opacity=".55"'))
    return p, "The Ring-Kissing Ritual", defs, "".join(b)


def sacrificial_lamb():
    p = "sl"
    defs = (f'<radialGradient id="{p}-wool" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#fbf8f0"/><stop offset=".6" stop-color="#b8b2a6"/><stop offset="1" stop-color="#3a3630"/></radialGradient>'
            f'<radialGradient id="{p}-cand" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".5"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030202"/>']
    # the screen behind: cheerful, terrible
    b.append('<rect x="250" y="30" width="300" height="130" fill="#14100c" stroke="#2a2018"/>' + text(400, 74, "WELCOME, NEW", 22, "#e8d8b0", BLACK, "middle", 'opacity=".8"')
             + text(400, 102, "PROJECT LEAD! 🎉", 22, "#e8d8b0", BLACK, "middle", 'opacity=".8"') + text(400, 136, "Project Orion · a great opportunity", 11, "#a89878", SERIF, "middle", 'font-style="italic"'))
    # the long table in perspective
    b.append('<path d="M300 250 L500 250 L720 500 L80 500 Z" fill="#0e0907"/><path d="M300 250 L500 250" stroke="#4a3020" stroke-width="1.2"/>')
    # seven hooded figures with candles
    for k, (x, y, sc) in enumerate(((270, 250, .55), (530, 250, .55), (200, 300, .72), (600, 300, .72), (120, 370, .9), (680, 370, .9), (400, 230, .45))):
        b.append(f'<circle cx="{x}" cy="{y - 40 * sc}" r="{70 * sc}" fill="url(#{p}-cand)"/>'
                 f'<g transform="translate({x} {y}) scale({sc})"><path d="M0 -150 C-40 -146 -56 -100 -58 -40 C-60 10 -70 60 -80 120 L80 120 C70 60 60 10 58 -40 C56 -100 40 -146 0 -150 Z" fill="#050303"/>'
                 '<ellipse cx="0" cy="-96" rx="26" ry="32" fill="#000"/>'
                 '<circle cx="-9" cy="-98" r="3" fill="#ff3a22"/><circle cx="9" cy="-98" r="3" fill="#ff3a22"/>'
                 '<rect x="-5" y="-30" width="10" height="34" fill="#e0d4b0"/><ellipse cx="0" cy="-38" rx="4" ry="9" fill="#ffd27a"/>'
                 '<path d="M0 -150 C40 -146 56 -100 58 -40" stroke="#ffb070" stroke-width="2" fill="none" opacity=".35"/></g>')
    b.append(f'<g filter="url(#{p}-glow)" opacity=".8">' + "".join(f'<circle cx="{x}" cy="{y - 38 * sc}" r="{3 * sc + 1}" fill="#ffd27a"/>' for x, y, sc in ((270, 250, .55), (530, 250, .55), (200, 300, .72), (600, 300, .72), (120, 370, .9), (680, 370, .9), (400, 230, .45))) + "</g>")
    # the lamb on the table
    b.append(f'<g transform="translate(400 380)">'
             '<g fill="#1a1612"><rect x="-38" y="20" width="9" height="40" rx="3"/><rect x="-18" y="24" width="9" height="40" rx="3"/><rect x="12" y="24" width="9" height="40" rx="3"/><rect x="30" y="20" width="9" height="40" rx="3"/></g>'
             + "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{p}-wool)"/>' for cx, cy, r in ((-40, 0, 24), (-16, -12, 26), (12, -12, 26), (38, 0, 24), (-26, 16, 22), (0, 12, 26), (26, 16, 22), (0, -22, 22)))
             + '<ellipse cx="-58" cy="-26" rx="18" ry="22" fill="#2a2420"/><ellipse cx="-74" cy="-38" rx="10" ry="5" fill="#2a2420" transform="rotate(-30 -74 -38)"/>'
             '<ellipse cx="-44" cy="-42" rx="10" ry="5" fill="#2a2420" transform="rotate(30 -44 -42)"/>'
             '<circle cx="-64" cy="-30" r="3" fill="#f0e8d8"/><circle cx="-63.4" cy="-30" r="1.6" fill="#000"/><circle cx="-52" cy="-30" r="3" fill="#f0e8d8"/><circle cx="-51.4" cy="-30" r="1.6" fill="#000"/>'
             '<path d="M-66 -38 l6 3 M-50 -38 l-6 3" stroke="#000" stroke-width="1.4"/>'
             '<path d="M-62 -14 L-50 10 L-40 -12" stroke="#1e3e6a" stroke-width="2.4" fill="none"/>'
             '<g transform="rotate(-8 -50 20)"><rect x="-68" y="10" width="40" height="24" fill="#c9cfdc"/><rect x="-68" y="10" width="40" height="7" fill="#6a0d0d"/></g>'
             + text(-48, 30, "PROJECT LEAD", 5.4, "#1b1b22", SERIF, "middle", 'font-weight="700" transform="rotate(-8 -50 20)"') + "</g>")
    # the folder
    b.append('<g transform="rotate(6 540 440)"><rect x="480" y="420" width="130" height="50" fill="#5a3a1a"/><rect x="486" y="426" width="118" height="38" fill="#e8dcc0"/>'
             + text(545, 440, "PROJECT ORION", 9, "#2a1a10", FELL, "middle") + text(545, 452, "18 months late", 7.5, "#7a1010", SERIF, "middle")
             + text(545, 461, "£2.4m over · lead #4", 7.5, "#7a1010", SERIF, "middle") + "</g>")
    b.append(text(170, 486, "“Real visibility for you.”", 13, "#ffcf7a", HAND, "middle", 'opacity=".6"'))
    return p, "The Sacrificial Lamb", defs, "".join(b)


# ================================================================ Act III plates (three only)
def all_seeing_eye():
    p = "ae"
    defs = (f'<radialGradient id="{p}-scr" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#cfe6ff" stop-opacity=".95"/><stop offset="1" stop-color="#6a8ab8"/></radialGradient>'
            f'<radialGradient id="{p}-spill" cx=".2" cy=".6" r=".8"><stop offset="0" stop-color="#bcd6ff" stop-opacity=".45"/><stop offset="1" stop-color="#bcd6ff" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="{p}-loupe" cx=".42" cy=".38" r=".6"><stop offset="0" stop-color="#ffd27a"/><stop offset=".3" stop-color="#ff3a1a"/><stop offset=".75" stop-color="#7a0000"/><stop offset="1" stop-color="#1a0000"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030306"/>']
    # the wall of webcams, each one recording
    for r in range(3):
        for c in range(9):
            x, y = 40 + c * 84, 30 + r * 52
            b.append(f'<g transform="translate({x} {y})"><rect x="-14" y="-10" width="28" height="20" rx="4" fill="#0c0c12" stroke="#1a1a24"/>'
                     f'<circle cx="0" cy="0" r="6" fill="#020203" stroke="#2a2a38"/><circle cx="0" cy="0" r="2.6" fill="#3a5aa0" opacity=".8"/>'
                     f'<circle cx="10" cy="-6" r="1.6" fill="#ff2a20" filter="url(#{p}-glow)"/></g>')
    b.append(f'<rect width="{W}" height="{H}" fill="url(#{p}-spill)"/>')
    # the monitor, Pip's work on it, the sticky note
    b.append('<path d="M40 190 L330 200 L326 380 L46 386 Z" fill="#0a0c12"/>'
             f'<path d="M52 202 L318 210 L314 368 L56 374 Z" fill="url(#{p}-scr)"/>'
             '<g stroke="#4a6a9a" stroke-width="1" opacity=".55">' + "".join(f'<path d="M64 {226 + k * 16} L306 {232 + k * 16}"/>' for k in range(8)) + "</g>"
             '<polyline points="70,350 110,330 150,338 190,300 230,306 270,270 300,262" stroke="#1a3a7a" stroke-width="3" fill="none"/>'
             '<rect x="168" y="388" width="40" height="40" fill="#0a0c12"/>'
             '<g transform="rotate(5 290 210)"><rect x="252" y="176" width="74" height="60" fill="#f0e070"/>'
             + text(289, 194, "UPDATE PLS", 8.5, "#3a2a00", HAND, "middle", 'font-weight="700"') + text(289, 208, "(3rd time", 8, "#3a2a00", HAND, "middle")
             + text(289, 220, "today) — V.", 8, "#3a2a00", HAND, "middle") + "</g>")
    # Pip, from behind, shoulders up
    b.append('<path d="M60 500 C70 440 120 410 180 404 C240 410 290 440 300 500 Z" fill="#040406"/><circle cx="180" cy="372" r="40" fill="#040406"/>'
             '<path d="M140 372 a40 40 0 0 1 60 -36" stroke="#bcd6ff" stroke-width="1.6" fill="none" opacity=".55"/>'
             '<path d="M70 470 C84 432 120 414 160 408" stroke="#bcd6ff" stroke-width="1.4" fill="none" opacity=".45"/>')
    # Victor, leaning in over Pip's shoulder
    b.append(suit(p, 1, 520, 192, .9, tie="#2a3a5a", jacket="#0b0b10", shirt="#5a6478", rim="#bcd6ff", rim_side="left"))
    b.append(face(p, 1, 520, 175, .66, skin=("#0e1018", "#3c4458", "#7a86a0"), light="left", light_col="#cfe6ff", rim="#ff3a22", rim_side="right",
                  eye="red", glow=True, brows="angry", mouth="thin", hair="slick", hair_col="#06060a", ears="human", tilt=-6))
    # the loupe over one eye: an enormous, unblinking eye
    b.append('<g transform="translate(520 175) rotate(-6) scale(.66)">'
             '<path d="M-21 -8 L-60 40 L-70 36" stroke="#1a1a20" stroke-width="5" fill="none"/>'
             '<circle cx="-21" cy="-8" r="28" fill="#cbbab2"/>'
             '<g stroke="#b01414" stroke-width="1" fill="none" opacity=".8"><path d="M-46 -8 l10 -2 6 4 M-46 2 l12 0 M4 -10 l-10 2 M2 4 l-10 -2"/></g>'
             '<circle cx="-21" cy="-8" r="15" fill="url(#ae-loupe)"/><ellipse cx="-21" cy="-8" rx="3" ry="12" fill="#000"/><circle cx="-26" cy="-14" r="3" fill="#fff"/>'
             '<circle cx="-21" cy="-8" r="28" fill="none" stroke="#c9a24a" stroke-width="5"/><circle cx="-21" cy="-8" r="28" fill="#fff" opacity=".07"/>'
             f'<circle cx="-21" cy="-8" r="18" fill="#ff2a14" opacity=".35" filter="url(#{p}-b6)"/></g>')
    b.append(hand(p, 400, 300, .9, flip=True, rim="#ff3a22", light="#cfe6ff", claws=False, pose="point"))
    # the notifications
    for k, (x, y, t) in enumerate(((600, 290, "Any update?"), (612, 336, "Just checking in 🙂"), (580, 382, "Can you share your screen?"), (640, 428, "?"))):
        b.append(f'<g opacity="{.95 - k * .12}"><rect x="{x}" y="{y}" width="{len(t) * 7 + 28}" height="30" rx="6" fill="#1c2030" stroke="#3a4a7a"/>'
                 f'<circle cx="{x + 14}" cy="{y + 15}" r="7" fill="#5a6aa0"/>' + text(x + 26, y + 20, t, 11, "#cfd8f0") + "</g>")
    b.append(text(740, 40, "16:02", 18, "#ff3a22", MONO, "middle", f'filter="url(#{p}-glow)"'))
    return p, "The All-Seeing Eye", defs, "".join(b)


def seagull_overlord():
    p = "so"
    defs = (f'<linearGradient id="{p}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a6a7a"/><stop offset="1" stop-color="#1a2028"/></linearGradient>'
            f'<linearGradient id="{p}-wing" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9aa0aa"/><stop offset=".6" stop-color="#4a4e58"/><stop offset="1" stop-color="#14161c"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#06070a"/>']
    # window wall with a grey seaside sky; gulls circling
    b.append(f'<rect x="0" y="0" width="{W}" height="230" fill="url(#{p}-sky)" opacity=".85"/>'
             '<g stroke="#0a0c10" stroke-width="5">' + "".join(f'<path d="M{x} 0 V230"/>' for x in (130, 270, 530, 670)) + '<path d="M0 230 H800"/></g>')
    for k, (x, y, sc) in enumerate(((90, 60, 1), (210, 110, .8), (600, 50, 1.2), (720, 120, .9), (360, 30, .7), (470, 140, .6))):
        b.append(f'<path d="M{x - 18 * sc} {y} q{9 * sc} {-10 * sc} {18 * sc} 0 q{9 * sc} {-10 * sc} {18 * sc} 0" stroke="#e8ecf0" stroke-width="{2.4 * sc}" fill="none" opacity=".8"/>')
    # the strategy board, decorated by the visit
    b.append('<rect x="40" y="250" width="220" height="150" fill="#d8dcd8"/><rect x="40" y="250" width="220" height="150" fill="#000" opacity=".45"/>'
             + text(150, 276, "LUMEN PLAN v12", 14, "#1a2a4a", FELL, "middle")
             + '<g stroke="#1a2a4a" stroke-width="2" opacity=".7"><path d="M60 300 h80 M60 320 h120 M60 340 h60 M60 360 h140"/><path d="M60 300 l150 70" stroke="#a01818"/></g>'
             + "".join(f'<g fill="#f4f4f0"><ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * .8}"/><path d="M{x - 2} {y} q2 {r * 2.2} 4 0z"/></g>' for x, y, r in ((120, 296, 8), (196, 330, 6), (90, 360, 5), (226, 286, 7)))
             + text(150, 392, "(quick thoughts from Rupert)", 10, "#2a2a2a", HAND, "middle"))
    # papers flying
    for k in range(9):
        x, y, r = 300 + (k * 61) % 460, 230 + (k * 47) % 200, (k * 41) % 80 - 40
        b.append(f'<rect x="{x}" y="{y}" width="26" height="34" fill="#e8e4d8" opacity=".55" transform="rotate({r} {x} {y})"/>')
    # Rupert, coat spread like wings, mid-swoop
    b.append(f'<path d="M500 300 C430 270 360 220 300 230 C340 250 330 262 300 270 C340 280 336 292 306 304 C350 306 350 320 330 334 C380 330 420 330 470 350 Z" fill="url(#{p}-wing)"/>'
             f'<path d="M600 300 C670 270 740 220 790 230 C756 250 766 262 794 270 C756 280 760 292 790 304 C748 306 748 320 768 334 C718 330 678 330 630 350 Z" fill="url(#{p}-wing)"/>'
             '<path d="M300 230 C360 220 430 270 500 300 M790 230 C740 220 670 270 600 300" stroke="#e8ecf0" stroke-width="1.6" fill="none" opacity=".6"/>')
    b.append(suit(p, 1, 550, 229, .82, tie="#e8b020", jacket="#16181e", shirt="#8a96a8", rim="#e8ecf0"))
    b.append(face(p, 1, 550, 180, .66, skin=("#14161c", "#5a5e6a", "#b8bcc8"), light="left", light_col="#e8f0ff", rim="#e8ecf0", rim_side="right",
                  eye="yellow", glow=True, brows="angry", mouth="shout", hair="slick", hair_col="#b8bcc4", ears="human"))
    # sunglasses pushed up on his head
    b.append('<g transform="translate(550 180) scale(.66)"><path d="M-46 -98 Q0 -112 46 -98" stroke="#0a0a0a" stroke-width="4" fill="none"/>'
             '<ellipse cx="-22" cy="-100" rx="18" ry="9" fill="#0a0a0a"/><ellipse cx="22" cy="-100" rx="18" ry="9" fill="#0a0a0a"/>'
             '<path d="M-30 -104 l10 -2" stroke="#fff" stroke-width="2" opacity=".5"/></g>')
    b.append(hand(p, 650, 270, .85, rim="#e8ecf0", light="#e8f0ff", claws=False, pose="point"))
    # flat white, and the departure board
    b.append(table(440, "#08090c"))
    b.append('<g transform="translate(700 392)"><path d="M0 0 L36 0 L32 46 L4 46 Z" fill="#e8e0d0"/><rect x="-2" y="-6" width="40" height="8" rx="2" fill="#3a3028"/>'
             + text(18, 26, "FLAT", 7, "#5a3a20", FELL, "middle") + text(18, 35, "WHITE", 7, "#5a3a20", FELL, "middle") + "</g>")
    b.append('<rect x="60" y="410" width="170" height="40" fill="#0a0a08" stroke="#2a2a20"/>' + text(145, 426, "DEPARTURES", 9, "#c8a030", MONO, "middle")
             + text(145, 442, "14:05  LONDON  ON TIME", 10, "#ffd060", MONO, "middle", f'filter="url(#{p}-glow)"'))
    b.append(text(400, 488, "“I've seen this work in Rotterdam.”", 13, "#e8ecf0", SERIF, "middle", 'font-style="italic" opacity=".6"'))
    return p, "The Seagull Overlord", defs, "".join(b)


def escape_portal():
    p = "ep"
    defs = (f'<radialGradient id="{p}-door" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#fffbe8"/><stop offset=".4" stop-color="#ffe2a0"/><stop offset="1" stop-color="#ffb050"/></radialGradient>'
            f'<linearGradient id="{p}-beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".55"/><stop offset="1" stop-color="#ffe2a0" stop-opacity="0"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030204"/>']
    # the dark throne room on the left: a desk, a crown-shaped shadow, two red eyes
    b.append('<path d="M0 340 L260 340 L260 470 L0 470 Z" fill="#0a0708"/><rect x="40" y="250" width="140" height="90" fill="#0c0a10"/>'
             '<path d="M70 190 L82 160 L96 182 L110 152 L124 182 L138 160 L150 190 Z" fill="#000" stroke="#3a2a10" stroke-width="1"/>'
             '<ellipse cx="110" cy="230" rx="40" ry="46" fill="#000"/>'
             f'<g filter="url(#{p}-glow)"><circle cx="96" cy="226" r="3.4" fill="#ff2a20"/><circle cx="124" cy="226" r="3.4" fill="#ff2a20"/></g>'
             '<path d="M70 280 C60 330 40 380 30 470 L190 470 C180 380 160 330 150 280 Z" fill="#000"/>'
             '<g stroke="#5a5a62" stroke-width="2" fill="none" opacity=".55"><path d="M150 330 C200 350 230 400 250 470"/><path d="M156 330 c6 4 6 10 0 14 c-6 4 -6 10 0 14 c6 4 6 10 0 14"/></g>'
             + text(110, 140, "Victor", 13, "#7a6a6a", HAND, "middle", 'opacity=".55"'))
    # the portal: a door blazing with light, runes on the frame
    b.append(f'<path d="M520 470 L520 110 L680 110 L680 470" fill="#020203"/><rect x="536" y="126" width="128" height="344" fill="url(#{p}-door)" filter="url(#{p}-glow)"/>'
             f'<path d="M536 470 L664 470 L800 500 L300 500 Z" fill="url(#{p}-beam)"/>'
             f'<path d="M536 126 L340 500 M664 126 L800 420" stroke="#ffe2a0" stroke-width="40" opacity=".08" filter="url(#{p}-b12)"/>'
             '<g fill="#c99a43" opacity=".8" font-family="EB Garamond, serif" font-size="12">'
             + "".join(f'<text x="526" y="{140 + k * 28}">{c}</text>' for k, c in enumerate("ᛖᚲᛋᛁᛏᛚᛖᚨᚡᛖᚹᛖ"))
             + "".join(f'<text x="668" y="{140 + k * 28}">{c}</text>' for k, c in enumerate("ᚷᛟᛟᛞᛞᚨᚤᛈᛚᚨᚾ")) + "</g>")
    b.append('<rect x="560" y="70" width="80" height="28" fill="#04140a" stroke="#0a3a1a"/>' + text(600, 90, "EXIT", 18, "#5aff8a", FELL, "middle", f'filter="url(#{p}-glow)"'))
    # Pip, from behind, walking towards it with a box of his things
    b.append('<g transform="translate(600 474) scale(1.15)">'
             '<path d="M-34 0 L-30 -110 C-28 -140 28 -140 30 -110 L34 0 Z" fill="#050406"/>'
             '<circle cx="0" cy="-160" r="24" fill="#050406"/>'
             '<path d="M24 -160 a24 24 0 0 0 -16 -22 M30 -110 L34 0" stroke="#ffe2a0" stroke-width="2" fill="none" opacity=".75"/>'
             '<rect x="-40" y="-110" width="80" height="54" fill="#6a4a2a"/><path d="M-40 -110 L40 -110" stroke="#ffe2a0" stroke-width="1.4" opacity=".6"/>'
             '<path d="M-20 -110 C-24 -130 -10 -140 -6 -126 C-2 -140 12 -136 6 -112" fill="#2a4a1a"/>'
             '<rect x="14" y="-124" width="16" height="16" rx="2" fill="#d8d0c0"/>'
             + text(0, -78, "PIP · DESK", 8, "#2a1a0a", FELL, "middle") + "</g>")
    # the phone on the floor, still glowing
    b.append(f'<g transform="rotate(-12 340 440)"><rect x="310" y="420" width="76" height="40" rx="6" fill="#0a0a0a"/><rect x="314" y="424" width="68" height="32" rx="4" fill="#d8eaff" filter="url(#{p}-glow)"/>'
             + text(348, 436, "Priya:", 7, "#1a2a4a", SERIF, "middle", 'font-weight="700"') + text(348, 448, "no pressure 🙂", 7, "#1a2a4a", SERIF, "middle") + "</g>")
    b.append(text(260, 60, "Floor 9 · 19:40", 14, "#8a7a6a", FELL, "middle", 'letter-spacing="2" opacity=".6"'))
    return p, "The Escape Portal", defs, "".join(b)


# ================================================================ Act I plates, the remaining nine
def by(fy, fs, bs):
    """Body y so that the neck meets the chin: face_y + 85*face_s - 43*body_s."""
    return fy + 85 * fs - 43 * bs


def meeting_before_the_meeting():
    p = "mb1"
    defs = (f'<radialGradient id="{p}-mach" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#ffcf8a" stop-opacity=".7"/><stop offset="1" stop-color="#ffcf8a" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-glass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0c1420"/><stop offset="1" stop-color="#05080e"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040304"/>']
    # behind the glass: the boardroom, empty, already decided
    b.append(f'<rect x="420" y="30" width="360" height="300" fill="url(#{p}-glass)"/><path d="M420 30 V330 M600 30 V330" stroke="#1a2a3a" stroke-width="3"/>'
             '<rect x="470" y="60" width="260" height="110" fill="#1a2436"/>'
             + text(600, 92, "NETWORK INVESTMENT BOARD", 12, "#9ab0d0", FELL, "middle", 'letter-spacing="1.5"')
             + text(600, 116, "Tue 10:00 · item 4", 12, "#9ab0d0", SERIF, "middle")
             + text(600, 146, "APPROVED (pending meeting)", 15, "#7affa0", MONO, "middle", f'filter="url(#{p}-glow)"')
             + '<path d="M440 260 L760 260 L780 320 L420 320 Z" fill="#0a0e14"/>'
             + "".join(f'<rect x="{x}" y="226" width="20" height="34" fill="#06080c"/><rect x="{x - 2}" y="262" width="24" height="8" fill="#c9cfdc" opacity=".55"/>' for x in (470, 530, 590, 650, 710))
             + '<g stroke="#9ab8d0" stroke-width="1" opacity=".15"><path d="M440 40 l90 120 M480 40 l110 150 M640 50 l100 130"/></g>')
    # the coffee machine: where decisions are actually made
    b.append(f'<ellipse cx="300" cy="260" rx="220" ry="190" fill="url(#{p}-mach)" filter="url(#{p}-b12)"/>'
             '<rect x="250" y="150" width="100" height="250" rx="6" fill="#1a1612"/><rect x="262" y="166" width="76" height="46" rx="3" fill="#ffcf8a" opacity=".9"/>'
             + text(300, 184, "FLOOR 27", 8, "#3a2410", MONO, "middle") + text(300, 196, "DECISIONS", 8, "#3a2410", MONO, "middle") + text(300, 207, "DISPENSED HERE", 7, "#3a2410", MONO, "middle")
             + '<rect x="280" y="290" width="40" height="30" fill="#0a0806"/><path d="M290 320 L310 320 L308 344 L292 344 Z" fill="#e8e0d0"/>')
    # Priya and Gareth, leaning in, lit by the machine
    fl, fs = (170, 185), .62
    b.append(blouse(p, fl[0], by(fl[1], fs, .78), .78, cardigan="#1a1418", top="#3a2a34", rim="#ffcf8a", rim_side="right"))
    b.append(face(p, 1, fl[0], fl[1], fs, skin=("#1a1210", "#6a5048", "#c8a890"), light="right", light_col="#ffd8a8", rim="#7a8ab0", rim_side="left",
                  eye="human", glow=False, brows="flat", mouth="thin", hair="bob", hair_col="#0a0608", ears="none", tilt=6, lip="#7a3a3a"))
    fr = (430, 190)
    b.append(suit(p, 1, fr[0], by(fr[1], .62, .8), .8, tie="#2a3a5a", jacket="#0c0c10", shirt="#6a6a70", rim="#ffcf8a", rim_side="left"))
    b.append(face(p, 2, fr[0], fr[1], .62, skin=("#14120e", "#5a4a3c", "#b8a08a"), light="left", light_col="#ffd8a8", rim="#7a8ab0", rim_side="right",
                  eye="human", glow=False, brows="angry", mouth="thin", hair="slick", hair_col="#2a2622", ears="human", tilt=-6))
    b.append(text(140, 60, "Monday · 16:58", 16, "#c9a26a", FELL, "middle", 'letter-spacing="2" opacity=".7"'))
    b.append(text(300, 470, "“Show me first. I'd have said yes.”", 14, "#ffd8a8", HAND, "middle", 'opacity=".65"'))
    return p, "The Meeting Before the Meeting", defs, "".join(b)


def blood_pacts():
    p = "bp"
    defs = f'<radialGradient id="{p}-cand" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".75"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#050302"/>']
    b.append(f'<ellipse cx="400" cy="300" rx="320" ry="220" fill="url(#{p}-cand)" filter="url(#{p}-b12)"/>')
    # Jules across the canteen table, warm, in candlelight
    fj = (520, 150)
    b.append(suit(p, 1, fj[0], by(fj[1], .66, .82), .82, tie="#3a5a3a", jacket="#1a1612", shirt="#8a8070", rim="#ffcf7a", rim_side="left"))
    b.append(face(p, 1, fj[0], fj[1], .66, skin=("#1a120c", "#6a5040", "#d0b090"), light="below", light_col="#ffd8a0", rim="#c86a3a", rim_side="right",
                  eye="human", glow=False, brows="raised", mouth="smile", hair="slick", hair_col="#3a2414", ears="human", lip="#8a4a3a"))
    # the table
    b.append('<path d="M60 330 L740 330 L800 500 L0 500 Z" fill="#1a120a"/><path d="M60 330 L740 330" stroke="#6a4a2a" stroke-width="1.4"/>')
    # a pinky promise across the table, bound with red thread
    b.append('<path d="M120 480 C190 450 260 430 330 420" stroke="#0e0c10" stroke-width="44" stroke-linecap="round" fill="none"/>'
             '<path d="M680 480 C610 450 540 430 470 420" stroke="#14100c" stroke-width="44" stroke-linecap="round" fill="none"/>'
             '<rect x="300" y="384" width="74" height="58" rx="22" fill="#b89878"/><rect x="426" y="384" width="74" height="58" rx="22" fill="#c8a88a"/>'
             '<g stroke="#7a5a44" stroke-width="1.6" fill="none"><path d="M316 396 q6 6 0 12 M332 394 q6 6 0 12 M348 396 q6 6 0 12"/><path d="M484 396 q-6 6 0 12 M468 394 q-6 6 0 12 M452 396 q-6 6 0 12"/></g>'
             '<path d="M368 404 C392 384 410 384 414 398 C416 410 404 414 396 406" stroke="#b89878" stroke-width="12" stroke-linecap="round" fill="none"/>'
             '<path d="M432 404 C408 384 390 384 386 398 C384 410 396 414 404 406" stroke="#c8a88a" stroke-width="12" stroke-linecap="round" fill="none"/>'
             '<path d="M368 404 C392 384 410 384 414 398" stroke="#f0d8bc" stroke-width="2" fill="none" opacity=".6"/>'
             f'<path d="M380 398 C392 410 408 410 420 398 C430 388 420 380 400 386 C380 380 370 388 380 398 Z M400 404 C390 424 372 438 350 452 M400 404 C410 424 428 438 450 452" stroke="#c4161c" stroke-width="2.6" fill="none" filter="url(#{p}-glow)"/>')
    # props: the Ally Garden ledger, a sticky note, two coffees, a candle
    b.append('<g transform="rotate(-6 140 360)"><rect x="70" y="330" width="150" height="100" fill="#d8ccb0"/><path d="M145 330 V430" stroke="#8a7a5a"/>'
             + text(108, 350, "ALLY GARDEN", 9, "#3a2a10", FELL, "middle") + text(108, 366, "Priya · data", 8, "#3a2a10", HAND, "middle")
             + text(108, 380, "Tamsin · macro", 8, "#3a2a10", HAND, "middle") + text(108, 394, "Sam · site visit", 8, "#3a2a10", HAND, "middle")
             + text(183, 350, "WATER", 9, "#3a2a10", FELL, "middle") + text(183, 366, "monthly", 8, "#3a2a10", HAND, "middle") + "</g>")
    b.append('<g transform="rotate(5 640 360)"><rect x="610" y="340" width="64" height="56" fill="#f0e070"/>'
             + text(642, 362, "I OWE", 10, "#3a2a00", HAND, "middle", 'font-weight="700"') + text(642, 378, "YOU ONE", 10, "#3a2a00", HAND, "middle", 'font-weight="700"') + "</g>")
    b.append(f'<rect x="392" y="290" width="16" height="44" fill="#e8dcc0"/><ellipse cx="400" cy="282" rx="6" ry="13" fill="#ffd27a" filter="url(#{p}-glow)"/>')
    b.append(mug(240, 290, "THURSDAY", "LUNCH", "#d8d0c0", "#5a3a20") + mug(520, 290, "HAPPY TO", "HELP", "#d8d0c0", "#5a3a20"))
    b.append(text(400, 492, "“I helped people. Then they remembered.”", 13, "#ffd8a0", HAND, "middle", 'opacity=".6"'))
    return p, "Blood Pacts", defs, "".join(b)


def ghost_decision():
    p = "gd"
    defs = (f'<linearGradient id="{p}-scr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a6aa0"/><stop offset="1" stop-color="#0a1a2a"/></linearGradient>'
            f'<linearGradient id="{p}-fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ef4ff" stop-opacity=".35"/><stop offset="1" stop-color="#9ef4ff" stop-opacity="0"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#020406"/>']
    # the off-site room: a screen with the deck
    b.append(f'<rect x="230" y="20" width="340" height="150" fill="url(#{p}-scr)"/>' + text(400, 70, "FINAL_v7.pptx", 22, "#e0f0ff", MONO, "middle", f'filter="url(#{p}-glow)"')
             + text(400, 104, "Transition: Grid Analytics → Strategy", 13, "#c0d8f0", SERIF, "middle") + text(400, 134, "(v1–v6 not shared)", 11, "#8aa8c8", SERIF, "middle", 'font-style="italic"'))
    # three ghostly executives at the table, translucent
    for k, (x, y, s) in enumerate(((230, 250, .5), (400, 236, .54), (570, 250, .5))):
        b.append(f'<g opacity=".55">' + suit(p, k + 1, x, by(y, s, .6), .6, tie="#2a4a5a", jacket="#0a1418", shirt="#3a5a6a", rim="#9ef4ff")
                 + face(p, k + 1, x, y, s, skin=("#0a1418", "#3a5a64", "#8ab0ba"), light="above", light_col="#cff6ff", rim="#9ef4ff",
                        eye="cyan", glow=True, brows="flat", mouth="thin", hair="slick" if k != 1 else "bald", hair_col="#0a1418", ears="human", extras=("translucent",)) + "</g>")
        b.append(f'<rect x="{x - 60}" y="{y + 50}" width="120" height="120" fill="url(#{p}-fade)" filter="url(#{p}-b6)"/>')
    # the table, wine, name cards
    b.append('<path d="M100 380 L700 380 L760 500 L40 500 Z" fill="#0a0c10"/><path d="M100 380 L700 380" stroke="#3a5a6a" stroke-width="1"/>')
    for x, n in ((230, "VP"), (400, "DIRECTOR"), (570, "VP")):
        b.append(f'<path d="M{x - 30} 404 L{x + 30} 404 L{x + 26} 392 L{x - 26} 392 Z" fill="#c9cfdc" opacity=".7"/>' + text(x, 402, n, 7, "#1a1a22", FELL, "middle")
                 + f'<path d="M{x + 44} 360 L{x + 54} 360 L{x + 50} 378 L{x + 48} 378 Z" fill="#9ef4ff" opacity=".35"/><path d="M{x + 49} 378 V392" stroke="#9ef4ff" opacity=".35"/>')
    # the empty chair (Marcus's)
    b.append('<rect x="700" y="330" width="44" height="90" fill="#06080a" stroke="#1a2a30"/>' + text(722, 316, "Marcus", 10, "#5a7a8a", HAND, "middle", 'opacity=".7"'))
    # foreground: the phone with the invite
    b.append(f'<g transform="rotate(-8 140 420)"><rect x="90" y="360" width="110" height="130" rx="10" fill="#0a0a0a"/><rect x="96" y="368" width="98" height="114" rx="6" fill="#dceaff" filter="url(#{p}-glow)"/>'
             + text(145, 392, "Calendar", 9, "#1a2a4a", SERIF, "middle", 'font-weight="700"') + text(145, 412, "Transition:", 8, "#1a2a4a", SERIF, "middle")
             + text(145, 424, "Grid Analytics", 8, "#1a2a4a", SERIF, "middle") + text(145, 436, "to Strategy", 8, "#1a2a4a", SERIF, "middle")
             + text(145, 458, "Mon 08:31", 8, "#a01010", MONO, "middle") + "</g>")
    b.append(text(560, 488, "“It came out of the off-site.”", 13, "#9ef4ff", HAND, "middle", 'opacity=".55"'))
    return p, "The Ghost Decision", defs, "".join(b)


def rumour_mill_familiar():
    p = "rm"
    defs = (f'<radialGradient id="{p}-fur" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#4a3a4a"/><stop offset="1" stop-color="#08060a"/></radialGradient>'
            f'<radialGradient id="{p}-lamp" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#f0e0b0" stop-opacity=".35"/><stop offset="1" stop-color="#f0e0b0" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040304"/>', f'<path d="M300 0 L500 0 L640 420 L160 420 Z" fill="url(#{p}-lamp)" filter="url(#{p}-b12)"/>']
    # the kitchen: counter, kettle, the broken coffee machine
    b.append('<rect x="0" y="360" width="800" height="140" fill="#0e0a08"/><path d="M0 360 H800" stroke="#4a3a2a" stroke-width="1.4"/>'
             '<rect x="330" y="220" width="140" height="140" rx="6" fill="#1a1612"/><rect x="346" y="236" width="108" height="40" rx="3" fill="#2a1a10"/>'
             + text(400, 262, "OUT OF ORDER", 11, "#ff5a3a", MONO, "middle", f'filter="url(#{p}-glow)"')
             + '<rect x="380" y="300" width="40" height="30" fill="#0a0806"/>')
    # the familiar, perched on the machine
    b.append(f'<g transform="translate(400 212)">'
             f'<path d="M-40 6 C-46 -30 -20 -54 0 -54 C20 -54 46 -30 40 6 Z" fill="url(#{p}-fur)"/>'
             '<path d="M-30 -40 L-46 -86 L-14 -52 Z M30 -40 L46 -86 L14 -52 Z" fill="#0a080c"/>'
             '<path d="M-30 -44 L-40 -76 M30 -44 L40 -76" stroke="#6a4a5a" stroke-width="1.4"/>'
             '<path d="M40 0 C70 -6 80 -40 62 -56 C56 -62 48 -58 52 -50" stroke="#0a080c" stroke-width="7" fill="none" stroke-linecap="round"/>'
             f'<g filter="url(#{p}-glow)"><ellipse cx="-14" cy="-28" rx="8" ry="10" fill="#ffd21a"/><ellipse cx="14" cy="-28" rx="8" ry="10" fill="#ffd21a"/></g>'
             '<ellipse cx="-14" cy="-28" rx="2" ry="8" fill="#000"/><ellipse cx="14" cy="-28" rx="2" ry="8" fill="#000"/>'
             '<path d="M-10 -10 Q0 -2 10 -10" stroke="#ffd21a" stroke-width="1.2" fill="none" opacity=".7"/>'
             '<path d="M-6 -8 l2 5 2 -4 2 4 2 -5" stroke="#e8e0d0" stroke-width="1" fill="none"/>'
             '<path d="M-40 6 C-46 -30 -20 -54 0 -54" stroke="#c8a0ff" stroke-width="1.2" fill="none" opacity=".4"/></g>')
    # the rumour, growing as it travels
    bubbles = [(250, 150, 11, "Marcus looked stressed", .95), (560, 110, 13, "Marcus is devastated", .9), (190, 70, 15, "Grid Planning is closing", .85),
               (600, 30, 17, "WE'RE ALL REDUNDANT", .8)]
    for k, (x, y, sz, t, op) in enumerate(bubbles):
        w = len(t) * sz * .55 + 30
        b.append(f'<g opacity="{op}"><rect x="{x - w / 2}" y="{y - sz - 8}" width="{w}" height="{sz + 20}" rx="14" fill="#e8e2d4"/>'
                 + text(x, y + 4, t, sz, "#2a1a1a", SERIF if k < 3 else BLACK, "middle", 'font-style="italic"' if k < 3 else "") + "</g>")
    b.append('<g stroke="#e8e2d4" stroke-width="1.4" fill="none" opacity=".4" stroke-dasharray="4 4"><path d="M380 180 C340 170 300 168 270 162 M290 140 C380 120 470 110 520 112 M500 100 C400 90 300 84 260 78 M260 60 C380 40 480 36 540 34"/></g>')
    # whispering colleagues in silhouette
    for x, sc in ((90, 1), (160, .9), (650, 1), (720, .9)):
        b.append(f'<g transform="translate({x} 470) scale({sc})"><circle cx="0" cy="-120" r="22" fill="#020203"/><path d="M-36 0 L-32 -84 C-26 -100 26 -100 32 -84 L36 0 Z" fill="#020203"/>'
                 f'<path d="M-22 -120 a22 22 0 0 1 32 -18" stroke="#f0e0b0" stroke-width="1.2" fill="none" opacity=".4"/></g>')
    b.append(text(400, 470, "Wednesday · 09:10 to 15:00", 13, "#c9b090", FELL, "middle", 'letter-spacing="2" opacity=".6"'))
    return p, "The Rumour Mill Familiar", defs, "".join(b)


def cc_inquisition():
    p = "cc"
    defs = (f'<radialGradient id="{p}-spot" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#fff0d0" stop-opacity=".55"/><stop offset="1" stop-color="#fff0d0" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-robe" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a0a08"/><stop offset="1" stop-color="#050101"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040202"/>']
    # the tribunal bench and fourteen witnesses (the CC line)
    b.append('<path d="M60 250 L740 250 L740 300 L60 300 Z" fill="#1a0c08"/><path d="M60 250 H740" stroke="#7a3a1a" stroke-width="1.6"/>')
    for k in range(14):
        x = 80 + k * 49 + (24 if k > 6 else 0) - (0 if k > 6 else 0)
        if 330 < x < 470:
            continue
        b.append(f'<g transform="translate({x} 250)"><circle cx="0" cy="-34" r="14" fill="#0a0606"/><path d="M-20 0 L-16 -18 C-12 -24 12 -24 16 -18 L20 0 Z" fill="#0a0606"/>'
                 f'<rect x="-9" y="-58" width="18" height="12" rx="2" fill="#e8e2d4" opacity=".85"/><path d="M-9 -58 L0 -51 L9 -58" stroke="#8a7a6a" fill="none"/>'
                 f'<circle cx="-4" cy="-35" r="1.6" fill="#ff3a22"/><circle cx="4" cy="-35" r="1.6" fill="#ff3a22"/></g>')
    # the Inquisitor: Gareth, hooded, centre
    b.append(f'<path d="M400 60 C340 64 322 120 318 190 C316 240 300 280 290 300 L510 300 C500 280 484 240 482 190 C478 120 460 64 400 60 Z" fill="url(#{p}-robe)"/>')
    b.append(face(p, 1, 400, 160, .5, skin=("#140c0a", "#4a3a34", "#9a8478"), light="below", light_col="#ffd8b0", rim="#ff3a22",
                  eye="red", glow=True, brows="angry", mouth="thin", hair="bald", ears="none"))
    b.append(f'<path d="M400 76 C350 80 334 122 340 176 C350 140 370 116 400 112 C430 116 450 140 460 176 C466 122 450 80 400 76 Z" fill="#0a0302"/>'
             f'<path d="M400 60 C460 64 478 120 482 190" stroke="#ff3a22" stroke-width="1.6" fill="none" opacity=".5"/>')
    # the projected email header
    b.append('<rect x="150" y="320" width="500" height="70" fill="#0c0a08" stroke="#5a3a1a"/>'
             + text(170, 342, "Subject: RE: RE: RE: RE: RE: Asset data question", 11, "#e8d8b8", MONO)
             + text(170, 360, "CC: Marcus Bell; Lord Varnish; FAC-ALL; Floor Warden (+10)", 11, "#ff8a6a", MONO)
             + text(170, 378, "“Looping in leadership for visibility…”", 11, "#c9b8a0", MONO))
    # Pip, small, in the spotlight, on a spreadsheet cell
    b.append(f'<path d="M340 0 L460 0 L520 500 L280 500 Z" fill="url(#{p}-spot)" opacity=".5" filter="url(#{p}-b12)"/>'
             f'<ellipse cx="400" cy="486" rx="90" ry="16" fill="#fff0d0" opacity=".35" filter="url(#{p}-b6)"/>'
             '<g transform="translate(400 476)"><rect x="-60" y="0" width="120" height="22" fill="#e8e8e0" stroke="#5a5a50"/>'
             + text(0, 15, "in_service_date", 11, "#1a1a1a", MONO, "middle")
             + '<circle cx="0" cy="-62" r="15" fill="#2a2420"/><path d="M-22 0 L-18 -42 C-14 -52 14 -52 18 -42 L22 0 Z" fill="#2a2420"/>'
             '<path d="M-15 -62 a15 15 0 0 1 30 0 M-18 -42 C-14 -52 14 -52 18 -42" stroke="#fff0d0" stroke-width="2" fill="none" opacity=".85"/>'
             '<path d="M-22 0 L-18 -42 M22 0 L18 -42" stroke="#fff0d0" stroke-width="1.2" opacity=".5"/></g>')
    b.append(text(400, 314, "Witnesses: 14 · Issues: 1 spreadsheet column", 12, "#c9b8a0", FELL, "middle", 'letter-spacing="1" opacity=".6"'))
    return p, "The CC Inquisition", defs, "".join(b)


def turf_wars():
    p = "tw"
    defs = (f'<linearGradient id="{p}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14080a"/><stop offset=".6" stop-color="#2a0e0a"/><stop offset="1" stop-color="#060304"/></linearGradient>'
            f'<radialGradient id="{p}-lant" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".7"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="url(#{p}-sky)"/>', glowlight(p, 400, 300, 380, 120, "#ff3a10", .15)]
    b.append('<circle cx="400" cy="80" r="36" fill="#e8d0b0" opacity=".8" filter="url(#tw-b2)"/>')
    # four towers, each with a banner
    towers = [(70, 110, 140, "CUSTOMER OPS", "#3a5aa0"), (190, 160, 110, "LUMEN", "#7a5aa0"), (610, 160, 110, "GRID PLANNING", "#3a8a5a"), (730, 110, 140, "NETWORK ASSETS", "#a05a3a")]
    for x, top, w, name, col in towers:
        b.append(f'<g><rect x="{x - w / 2}" y="{top}" width="{w}" height="{420 - top}" fill="#050304"/>'
                 + "".join(f'<rect x="{x - w / 2 + 8 + c * 22}" y="{top + 16 + r * 26}" width="10" height="14" fill="#ffcf7a" opacity="{.15 + ((r * 7 + c * 3) % 5) * .12}"/>'
                           for r in range((420 - top - 30) // 26) for c in range(int((w - 16) // 22)))
                 + f'<path d="M{x} {top} V{top - 50}" stroke="#2a2020" stroke-width="2"/><path d="M{x} {top - 50} L{x + 46} {top - 42} L{x} {top - 30} Z" fill="{col}"/>'
                 + text(x + 18, top - 38, name, 6, "#fff", FELL, "middle") + "</g>")
    # no-man's-land: silent meters like grave markers, barbed wire, a red LED on each
    b.append('<path d="M0 420 L800 420 L800 500 L0 500 Z" fill="#0a0604"/>')
    b.append('<path d="M240 432 q10 -8 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" stroke="#4a3a30" stroke-width="1.4" fill="none"/>'
             '<g stroke="#4a3a30" stroke-width="1.4">' + "".join(f'<path d="M{x} 426 l4 6 M{x + 4} 426 l-4 6"/>' for x in range(250, 560, 20)) + "</g>")
    for k in range(16):
        x, y = 260 + (k * 37) % 290, 440 + (k * 13) % 50
        b.append(f'<g transform="translate({x} {y})"><rect x="-6" y="-16" width="12" height="16" fill="#2a2420"/><circle cx="0" cy="-10" r="2" fill="#ff2a14" filter="url(#{p}-glow)"/></g>')
    # Pip with a lantern, alone in the gap
    b.append(f'<circle cx="420" cy="380" r="60" fill="url(#{p}-lant)"/>'
             '<g transform="translate(400 420)"><circle cx="0" cy="-74" r="11" fill="#060304"/><path d="M-14 0 L-12 -56 C-8 -64 8 -64 12 -56 L14 0 Z" fill="#060304"/>'
             '<path d="M12 -50 L24 -38" stroke="#060304" stroke-width="4"/><rect x="18" y="-38" width="12" height="16" fill="#ffd27a"/></g>')
    b.append(text(400, 160, "11,400 meters · 63 days · owner: none", 14, "#ffcf7a", FELL, "middle", 'letter-spacing="2" opacity=".8"'))
    return p, "The Turf Wars of the Two Towers", defs, "".join(b)


def empire_builder():
    p = "eb"
    defs = (f'<radialGradient id="{p}-gold" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd27a" stop-opacity=".6"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="{p}-coin" cx=".35" cy=".35" r=".7"><stop offset="0" stop-color="#fff2b0"/><stop offset=".5" stop-color="#d8a020"/><stop offset="1" stop-color="#5a3a00"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#050302"/>']
    # the wall: “Our Expanding Footprint”, his colour spreading across the map
    b.append('<rect x="40" y="30" width="300" height="200" fill="#0e0c0a" stroke="#3a2a1a"/>' + text(190, 54, "OUR EXPANDING FOOTPRINT", 11, "#d8a020", FELL, "middle", 'letter-spacing="1.5"')
             + '<path d="M60 210 C80 150 120 120 160 140 C200 100 260 90 320 120 L320 210 Z" fill="#a05a1a" opacity=".55"/>'
             + '<path d="M60 210 C70 180 100 170 120 180" fill="none" stroke="#3a5aa0" stroke-width="2" opacity=".6"/>'
             + text(110, 196, "2024: 40", 9, "#e8d8b8", SERIF) + text(250, 160, "2026: 112", 13, "#ffe2a0", SERIF, "middle", 'font-weight="700"'))
    # the dragon's shadow behind him, thrown on a wall lit by the hoard
    b.append(glowlight(p, 540, 160, 260, 170, "#c87a2a", .45))
    b.append(f'<path d="M520 260 C470 180 400 140 360 60 C420 90 450 100 470 130 C470 90 490 60 520 40 C530 90 540 120 560 140 C590 100 640 80 700 70 C660 120 640 160 600 230 Z" fill="#000" opacity=".85" filter="url(#{p}-b6)"/>'
             '<path d="M560 150 L590 120 L586 150 Z" fill="#000" opacity=".8"/>')
    b.append(f'<ellipse cx="540" cy="400" rx="260" ry="120" fill="url(#{p}-gold)" filter="url(#{p}-b12)"/>')
    # Gareth
    fg = (540, 170)
    b.append(suit(p, 1, fg[0], by(fg[1], .66, .9), .9, tie="#8a6a10", jacket="#14100c", shirt="#7a7060", rim="#ffd27a", rim_side="left"))
    b.append(face(p, 1, fg[0], fg[1], .66, skin=("#1a120c", "#6a5040", "#c8a888"), light="below", light_col="#ffe2a0", rim="#ff6a2a", rim_side="right",
                  eye="yellow", glow=True, brows="flat", mouth="smile", hair="slick", hair_col="#6a6058", ears="human"))
    # the hoard: a pile of staff badges like gold coins
    b.append(table(400, "#0c0806"))
    for k in range(38):
        x = 360 + (k * 29) % 360 + (k % 3) * 4
        y = 470 - (k % 5) * 12 - (abs(540 - x) < 120) * ((k * 7) % 30)
        b.append(f'<g transform="translate({x} {y}) rotate({(k * 37) % 50 - 25})"><rect x="-11" y="-14" width="22" height="28" rx="2" fill="url(#{p}-coin)"/><rect x="-11" y="-14" width="22" height="6" fill="#7a0d0d" opacity=".8"/></g>')
    b.append(hand(p, 660, 380, .8, rim="#ffd27a", light="#ffe2a0", claws=True, pose="claw"))
    b.append('<rect x="80" y="380" width="150" height="40" fill="#1a1410" stroke="#d8a020"/>' + text(155, 396, "CENTRE OF EXCELLENCE", 8, "#d8a020", FELL, "middle")
             + text(155, 410, "for Asset Intelligence", 8, "#c9b090", SERIF, "middle", 'font-style="italic"'))
    b.append(text(155, 450, "excellent at: (TBC)", 11, "#c9b090", HAND, "middle", 'opacity=".65"'))
    return p, "The Empire Builder", defs, "".join(b)


def chosen_one():
    p = "co"
    defs = f'<linearGradient id="{p}-beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff4d8" stop-opacity=".75"/><stop offset="1" stop-color="#fff4d8" stop-opacity=".08"/></linearGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#030304"/>']
    # the programme board
    b.append('<rect x="560" y="40" width="200" height="90" fill="#0c0c10" stroke="#3a3a4a"/>' + text(660, 68, "HIGH POTENTIAL", 12, "#d8c090", FELL, "middle", 'letter-spacing="1.5"')
             + text(660, 86, "PROGRAMME", 12, "#d8c090", FELL, "middle", 'letter-spacing="1.5"') + text(660, 112, "places: 1 · applications: none", 10, "#9a8a70", SERIF, "middle", 'font-style="italic"'))
    # the spotlight on Jules
    b.append(f'<path d="M270 0 L350 0 L440 500 L180 500 Z" fill="url(#{p}-beam)" filter="url(#{p}-b6)"/>')
    fj = (310, 190)
    b.append(blouse(p, fj[0], by(fj[1], .68, .86), .86, cardigan="#3a3022", top="#6a5a42", rim="#fff4d8", necklace=False))
    b.append(face(p, 1, fj[0], fj[1], .68, skin=("#2a2018", "#8a7060", "#e8d0b8"), light="above", light_col="#fff4d8", rim="#ffd27a", rim_side="left",
                  eye="human", glow=False, brows="raised", mouth="smile", hair="slick", hair_col="#3a2414", ears="human", lip="#8a4a3a"))
    b.append(f'<g filter="url(#{p}-glow)" opacity=".8"><ellipse cx="310" cy="88" rx="56" ry="10" fill="none" stroke="#ffe2a0" stroke-width="2.4"/></g>')
    # Pip, beside the beam, in the dark
    fp = (520, 220)
    b.append(suit(p, 1, fp[0], by(fp[1], .64, .82), .82, tie="#2a2a3a", jacket="#08080c", shirt="#3a3a44", rim="#5a5a6a", rim_side="left"))
    b.append(face(p, 2, fp[0], fp[1], .64, skin=("#08080c", "#24242c", "#4a4a56"), light="left", light_col="#c8c0a8", rim="#5a5a6a", rim_side="left",
                  eye="human", glow=False, brows="worried", mouth="thin", hair="slick", hair_col="#050505", ears="human"))
    # the coffee Jules offers across the line of light
    b.append('<g transform="translate(408 330)"><path d="M0 0 L30 0 L27 40 L3 40 Z" fill="#e8e0d0"/><rect x="-2" y="-6" width="34" height="7" rx="2" fill="#3a3028"/>'
             '<path d="M10 -10 C6 -20 16 -22 12 -32" stroke="#fff" stroke-width="1" fill="none" opacity=".3"/></g>')
    b.append(hand(p, 380, 390, .7, flip=True, rim="#fff4d8", light="#fff4d8", claws=False, pose="claw"))
    b.append(text(160, 470, "“ask Jules”", 18, "#ffe2a0", HAND, "middle", 'opacity=".75"') + text(600, 470, "(nobody ever said “ask Pip”)", 12, "#8a8a9a", HAND, "middle", 'opacity=".6"'))
    return p, "The Chosen One", defs, "".join(b)


def plausible_silence():
    p = "ps"
    defs = f'<radialGradient id="{p}-pend" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#f0e8d0" stop-opacity=".5"/><stop offset="1" stop-color="#f0e8d0" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#040304"/>']
    b.append('<rect x="250" y="20" width="300" height="90" fill="#0e0e12" stroke="#2a2a34"/>' + text(400, 52, "EFFICIENCY OPPORTUNITIES", 14, "#c8c0a8", FELL, "middle", 'letter-spacing="1.5"')
             + text(400, 80, "(volunteers?)", 13, "#9a9080", SERIF, "middle", 'font-style="italic"'))
    b.append(text(700, 60, "14:22", 22, "#ff3a22", MONO, "middle", f'filter="url(#{p}-glow)"'))
    b.append(f'<path d="M330 110 L470 110 L640 470 L160 470 Z" fill="url(#{p}-pend)" filter="url(#{p}-b12)"/>')
    # Lord Varnish asks the room
    fv = (400, 190)
    b.append(suit(p, 1, fv[0], by(fv[1], .56, .72), .72, tie="#a07a10", jacket="#0c0a10", shirt="#5a5868", rim="#ffd27a"))
    b.append(face(p, 1, fv[0], fv[1], .56, skin=("#1a1010", "#6a5450", "#c8b0a0"), light="above", light_col="#f0e8d0", rim="#ff3a22",
                  eye="yellow", glow=True, brows="raised", mouth="thin", hair="slick", hair_col="#0a0806", ears="human"))
    # the table and the silent managers: eyes down, mouths shut
    b.append('<path d="M120 330 L680 330 L760 500 L40 500 Z" fill="#0c0a08"/><path d="M120 330 H680" stroke="#4a3a2a" stroke-width="1.2"/>')
    for k, (x, y, sc) in enumerate(((150, 330, 1), (250, 320, .9), (550, 320, .9), (650, 330, 1))):
        b.append(f'<g transform="translate({x} {y}) scale({sc})"><circle cx="0" cy="-60" r="24" fill="#030203"/><path d="M-34 0 L-30 -34 C-24 -44 24 -44 30 -34 L34 0 Z" fill="#030203"/>'
                 f'<path d="M-12 -62 q6 4 12 0 M2 -62 q6 4 12 0" stroke="#5a5a62" stroke-width="1.4" fill="none"/>'
                 f'<path d="M-24 -60 a24 24 0 0 1 36 -20" stroke="#f0e8d0" stroke-width="1.2" fill="none" opacity=".4"/></g>')
    b.append(text(150, 352, "studying pen", 9, "#8a8070", HAND, "middle", 'opacity=".7"') + text(250, 340, "laptop", 9, "#8a8070", HAND, "middle", 'opacity=".7"')
             + text(550, 340, "ceiling (CFO)", 9, "#8a8070", HAND, "middle", 'opacity=".7"') + text(650, 352, "window", 9, "#8a8070", HAND, "middle", 'opacity=".7"'))
    # Pip, foreground, the only one speaking
    b.append('<g transform="translate(400 500)"><circle cx="0" cy="-92" r="30" fill="#060406"/><path d="M-60 0 L-54 -50 C-46 -64 46 -64 54 -50 L60 0 Z" fill="#060406"/>'
             '<path d="M-30 -92 a30 30 0 0 1 44 -24" stroke="#f0e8d0" stroke-width="1.6" fill="none" opacity=".6"/></g>')
    b.append('<g opacity=".95"><rect x="430" y="370" width="300" height="46" rx="18" fill="#f0e8d0"/><path d="M440 412 L420 432 L462 414 Z" fill="#f0e8d0"/>'
             + text(580, 399, "“Grid Planning could probably—”", 14, "#2a1a1a", SERIF, "middle", 'font-style="italic"') + "</g>")
    b.append('<g transform="rotate(-4 640 300)"><rect x="590" y="270" width="96" height="40" fill="#e8e0c8"/>' + text(638, 288, "CFO notes:", 8, "#3a2a1a", HAND, "middle")
             + text(638, 302, "Grid Planning −12%", 9, "#a01010", HAND, "middle", 'font-weight="700"') + "</g>")
    return p, "The Art of Plausible Silence", defs, "".join(b)


# ================================================================ Act III plates, the remaining nine
def absent_lord():
    p = "al"
    defs = (f'<linearGradient id="{p}-gate" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a2a3a"/><stop offset="1" stop-color="#05080c"/></linearGradient>'
            f'<radialGradient id="{p}-ph" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#cfe0ff" stop-opacity=".7"/><stop offset="1" stop-color="#cfe0ff" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030304"/>']
    # left: his office at The Grid, abandoned
    b.append('<rect x="20" y="260" width="300" height="20" fill="#14100c"/><rect x="40" y="280" width="12" height="160" fill="#0c0806"/><rect x="290" y="280" width="12" height="160" fill="#0c0806"/>'
             '<path d="M110 260 L110 170 C110 150 210 150 210 170 L210 260 Z" fill="#0a0808"/>'
             '<g stroke="#b8b8b0" stroke-width=".7" fill="none" opacity=".45"><path d="M110 170 L150 210 M110 196 C130 196 140 186 144 170 M110 220 C140 216 160 196 168 170 M210 170 L176 206"/></g>')
    for k in range(9):
        b.append(f'<rect x="{230 + (k % 3) * 4}" y="{246 - k * 7}" width="70" height="7" fill="#e8e4d8" opacity="{.5 + (k % 2) * .2}" transform="rotate({(k * 7) % 9 - 4} 260 {246 - k * 7})"/>')
    b.append(text(265, 168, "412 unread", 11, "#ff5a3a", MONO, "middle", f'filter="url(#{p}-glow)"'))
    b.append('<rect x="40" y="40" width="240" height="100" fill="#0c0a10" stroke="#2a2a34"/>' + text(160, 60, "CALENDAR · Oct → Feb", 10, "#9a9aa8", FELL, "middle")
             + "".join(f'<rect x="{50 + c * 32}" y="{70 + r * 14}" width="28" height="11" fill="#5a2a7a" opacity="{.6 + (r + c) % 3 * .12}"/>' for r in range(4) for c in range(7))
             + text(160, 132, "travelling", 9, "#c8a0ff", HAND, "middle"))
    # right: the airport gate, and Benedict, half there
    b.append(f'<rect x="400" y="0" width="400" height="500" fill="url(#{p}-gate)"/><rect x="420" y="30" width="200" height="56" fill="#0a0a08" stroke="#2a2a20"/>'
             + text(520, 52, "GATE 22 · BOARDING", 12, "#ffd060", MONO, "middle", f'filter="url(#{p}-glow)"') + text(520, 74, "ZURICH · DELAYED", 11, "#ff8a3a", MONO, "middle"))
    b.append(f'<g opacity=".7">{suit(p, 1, 620, by(190, .62, .8), .8, coat=True, tie="#3a2a5a", jacket="#0c0c14", shirt="#5a6070", rim="#9ab8ff")}'
             + face(p, 1, 620, 190, .62, skin=("#0c0e18", "#3a4458", "#8090b0"), light="below", light_col="#cfe0ff", rim="#9ab8ff",
                    eye="human", glow=False, brows="flat", mouth="thin", hair="slick", hair_col="#6a6a72", ears="human") + "</g>")
    b.append(f'<circle cx="590" cy="340" r="60" fill="url(#{p}-ph)"/><rect x="574" y="318" width="32" height="50" rx="5" fill="#dceaff" filter="url(#{p}-glow)"/>'
             + text(590, 340, "DECIDE", 6, "#1a2a4a", MONO, "middle") + text(590, 350, "BY THU?", 6, "#1a2a4a", MONO, "middle"))
    b.append(f'<rect x="400" y="0" width="4" height="500" fill="#000"/>')
    b.append(text(600, 470, "In the building: 9 days of 120", 13, "#9ab8ff", FELL, "middle", 'letter-spacing="1" opacity=".7"'))
    return p, "The Absent Lord", defs, "".join(b)


def weather_tyrant():
    p = "wt"
    defs = (f'<linearGradient id="{p}-split" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a2a10"/><stop offset=".48" stop-color="#2a1a0a"/><stop offset=".52" stop-color="#0a0e18"/><stop offset="1" stop-color="#04060c"/></linearGradient>'
            f'<radialGradient id="{p}-sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd27a" stop-opacity=".9"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="url(#{p}-split)"/>']
    b.append(f'<circle cx="170" cy="100" r="110" fill="url(#{p}-sun)"/><circle cx="170" cy="100" r="32" fill="#ffe2a0"/>')
    b.append(f'<g fill="#1a2030"><ellipse cx="600" cy="80" rx="140" ry="50"/><ellipse cx="520" cy="96" rx="80" ry="40"/><ellipse cx="690" cy="100" rx="90" ry="40"/></g>'
             f'<path d="M600 120 L580 170 L600 172 L572 230" stroke="#e8f0ff" stroke-width="3" fill="none" filter="url(#{p}-glow)"/>'
             + rain(p, 440, 800, 130, 480, .35, "#9ab0d8"))
    # Gareth, split down the middle
    b.append(suit(p, 1, 400, by(190, .74, .95), .95, tie="#3a3a5a", jacket="#0e0e14", shirt="#6a6a70", rim="#9ab0d8"))
    b.append(face(p, 1, 400, 190, .74, skin=("#14100c", "#5a4a3c", "#d0b090"), light="left", light_col="#ffe2a0", rim="#9ab0d8", rim_side="right",
                  eye="yellow", glow=True, brows="angry", mouth="thin", hair="slick", hair_col="#4a4440", ears="human"))
    # left: pastries; right: a junior under an umbrella
    b.append('<path d="M120 430 L280 430" stroke="#5a4a2a" stroke-width="2"/>' + "".join(f'<ellipse cx="{x}" cy="420" rx="18" ry="10" fill="#c8843a"/><path d="M{x - 10} 418 c6 -6 14 -6 20 0" stroke="#f0d090" fill="none"/>' for x in (150, 195, 240)))
    b.append(text(195, 455, "Monday ☀️  “pastries, anyone?”", 13, "#ffe2a0", HAND, "middle", 'opacity=".8"'))
    b.append('<g transform="translate(650 470)"><path d="M-40 -90 Q0 -130 40 -90 Z" fill="#2a3a5a"/><path d="M0 -90 V-40" stroke="#1a1a1a" stroke-width="2"/>'
             '<circle cx="0" cy="-56" r="10" fill="#040406"/><path d="M-14 0 L-10 -44 C-6 -50 6 -50 10 -44 L14 0 Z" fill="#040406"/></g>')
    b.append(text(620, 488, "Tuesday ⛈️  “unacceptable”", 13, "#9ab0d8", HAND, "middle", 'opacity=".8"'))
    b.append('<rect x="20" y="20" width="130" height="34" rx="8" fill="#14141a" stroke="#3a3a4a"/>' + text(85, 42, "#☀️ / ⛈️  (12)", 11, "#c8c8d8", SERIF, "middle"))
    return p, "The Weather Tyrant", defs, "".join(b)


def conflict_phantom():
    p = "cph"
    defs = (f'<linearGradient id="{p}-fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".5" stop-color="#000" stop-opacity=".2"/><stop offset="1" stop-color="#000" stop-opacity="1"/></linearGradient>'
            f'<radialGradient id="{p}-warm" cx=".4" cy=".4" r=".6"><stop offset="0" stop-color="#ffcf9a" stop-opacity=".45"/><stop offset="1" stop-color="#ffcf9a" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#050405"/>', f'<rect width="{W}" height="{H}" fill="url(#{p}-warm)"/>']
    # the door he's drifting through
    b.append('<rect x="560" y="80" width="150" height="400" fill="#0a0a0c" stroke="#2a2a30" stroke-width="4"/><rect x="560" y="80" width="150" height="400" fill="#cfe0ff" opacity=".08"/>'
             + text(635, 66, "MEETING ROOM 9C · “quick chat?”", 10, "#8a8a9a", FELL, "middle"))
    # Marcus: kind face, body dissolving into fog towards the door
    b.append(f'<g>{suit(p, 1, 470, by(180, .7, .9), .9, tie="#5a3a2a", jacket="#1a1614", shirt="#8a8070", rim="#ffcf9a", rim_side="left")}'
             + face(p, 1, 470, 180, .7, skin=("#1a120e", "#6a5044", "#d8b8a0"), light="left", light_col="#ffd8b0", rim="#9ab0d8", rim_side="right",
                    eye="human", glow=False, brows="worried", mouth="smile", hair="slick", hair_col="#3a2a20", ears="human", lip="#8a4a3a") + "</g>")
    b.append(f'<rect x="380" y="0" width="420" height="500" fill="url(#{p}-fade)"/>')
    b.append(f'<g fill="#cfd8e8" opacity=".25" filter="url(#{p}-b6)"><ellipse cx="560" cy="300" rx="60" ry="120"/><ellipse cx="620" cy="260" rx="40" ry="90"/></g>')
    # Pip, approaching with a question
    b.append('<g transform="translate(200 470)"><circle cx="0" cy="-150" r="22" fill="#08070a"/><path d="M-34 0 L-30 -110 C-24 -126 24 -126 30 -110 L34 0 Z" fill="#08070a"/>'
             '<path d="M-22 -150 a22 22 0 0 1 36 -16" stroke="#ffcf9a" stroke-width="1.4" fill="none" opacity=".6"/>'
             '<g transform="rotate(-8 40 -110)"><rect x="24" y="-140" width="70" height="56" fill="#f0e070"/></g></g>'
             + text(258, 352, "honest", 9, "#3a2a00", HAND, "middle", 'transform="rotate(-8 258 352)"') + text(258, 366, "feedback?", 9, "#3a2a00", HAND, "middle", 'transform="rotate(-8 258 366)"'))
    b.append(mug(300, 420, "YOU'RE DOING", "GREAT!", "#d8d0c0", "#3a5a3a"))
    # Neville asleep in the background
    b.append('<g opacity=".7"><rect x="40" y="250" width="110" height="70" fill="#0c0c0e"/><circle cx="95" cy="232" r="14" fill="#0a0a0c"/>' + text(95, 296, "in progress", 9, "#7aff9a", MONO, "middle") + "</g>")
    b.append(text(95, 210, "z z", 12, "#7a7a8a", HAND, "middle", 'opacity=".6"'))
    b.append(text(400, 488, "“You're doing great!” (changes the subject to football)", 12, "#ffd8b0", SERIF, "middle", 'font-style="italic" opacity=".65"'))
    return p, "The Conflict Phantom", defs, "".join(b)


def credit_taking_crown():
    p = "ctc"
    defs = (f'<radialGradient id="{p}-stage" cx=".5" cy=".3" r=".6"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".5"/><stop offset="1" stop-color="#ffe2a0" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff0b0"/><stop offset=".5" stop-color="#d8a020"/><stop offset="1" stop-color="#6a4a00"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040304"/>', f'<rect width="{W}" height="{H}" fill="url(#{p}-stage)"/>']
    # the post behind him
    b.append('<rect x="520" y="40" width="250" height="150" rx="8" fill="#0e1420" stroke="#2a3a5a"/>' + text(540, 66, "Victor Kraal · Head of Grid Analytics", 10, "#c8d8f0", SERIF)
             + text(540, 92, "The power of data-driven leadership.", 11, "#e8f0ff", SERIF, "start", 'font-weight="700"')
             + text(540, 112, "My team delivered a step-change…", 10, "#a8b8d0", SERIF) + text(540, 170, "👍 412   💬 38   ↗ 17", 13, "#7ab0ff", SERIF))
    # Victor, crowned, lifting the chart
    fv = (360, 200)
    b.append(suit(p, 1, fv[0], by(fv[1], .7, .9), .9, tie="#a07a10", jacket="#0c0c12", shirt="#6a6a78", rim="#ffe2a0"))
    b.append(face(p, 1, fv[0], fv[1], .7, skin=("#14100e", "#5a4c48", "#c8b0a0"), light="above", light_col="#ffe8b8", rim="#ff3a22",
                  eye="red", glow=True, brows="raised", mouth="smile", hair="slick", hair_col="#06060a", ears="human"))
    b.append(f'<path d="M318 112 L326 82 L342 104 L360 72 L378 104 L394 82 L402 112 Z" fill="url(#{p}-gold)" stroke="#5a3a00" stroke-width="1"/>'
             f'<circle cx="360" cy="96" r="4" fill="#c4161c" filter="url(#{p}-glow)"/>')
    b.append('<g transform="rotate(-6 200 230)"><rect x="120" y="170" width="160" height="110" fill="#e8e8e0" stroke="#3a3a3a"/>'
             '<polyline points="134,262 160,250 184,254 208,228 232,232 256,204 270,200" stroke="#1a3a7a" stroke-width="3" fill="none"/>'
             + text(200, 188, "Q1 FORECAST (±1.5%)", 9, "#1a1a1a", FELL, "middle") + text(200, 276, "model: P.", 7, "#8a8a8a", HAND, "middle") + "</g>")
    b.append(hand(p, 250, 300, .8, flip=True, rim="#ffe2a0", light="#ffe8b8", claws=False, pose="open"))
    # Pip, behind, holding the laptop that made it
    b.append('<g transform="translate(640 470)"><circle cx="0" cy="-130" r="20" fill="#08070a"/><path d="M-30 0 L-26 -96 C-20 -110 20 -110 26 -96 L30 0 Z" fill="#08070a"/>'
             '<rect x="-34" y="-82" width="68" height="44" fill="#1a2030"/><rect x="-30" y="-78" width="60" height="36" fill="#9ab8ff" opacity=".6"/></g>')
    b.append(text(640, 492, "(Pip's mum liked it)", 11, "#8a9ab0", HAND, "middle", 'opacity=".7"'))
    b.append(text(220, 470, "“…using an approach I introduced.”", 14, "#ffe2a0", SERIF, "middle", 'font-style="italic" opacity=".7"'))
    return p, "The Credit-Taking Crown", defs, "".join(b)


def new_lord_arrives():
    p = "nl"
    defs = f'<linearGradient id="{p}-door" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff4d8"/><stop offset="1" stop-color="#e8c890"/></linearGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#040406"/>']
    # the doorway, light spilling in
    b.append(f'<rect x="300" y="40" width="200" height="420" fill="url(#{p}-door)"/><path d="M300 460 L500 460 L700 500 L100 500 Z" fill="#fff4d8" opacity=".25" filter="url(#{p}-b6)"/>')
    # Victor in the doorway, carrying the operating model
    fv = (400, 170)
    b.append(suit(p, 1, fv[0], by(fv[1], .64, .82), .82, tie="#2a3a5a", jacket="#0b0b10", shirt="#5a6478", rim="#fff4d8"))
    b.append(face(p, 1, fv[0], fv[1], .64, skin=("#0e1018", "#3c4458", "#7a86a0"), light="below", light_col="#fff4d8", rim="#fff4d8",
                  eye="human", glow=False, brows="worried", mouth="thin", hair="slick", hair_col="#06060a", ears="human"))
    b.append('<g transform="rotate(-4 400 360)"><rect x="330" y="320" width="140" height="90" fill="#1a2a4a"/><rect x="330" y="320" width="140" height="18" fill="#c8a040"/>'
             + text(400, 333, "OPERATING MODEL", 9, "#1a1a1a", FELL, "middle") + text(400, 360, "v1 · 47 slides", 12, "#e8f0ff", SERIF, "middle")
             + text(400, 382, "GAOM · DART · THE SPINE", 9, "#9ab8ff", MONO, "middle") + "</g>")
    # the three camps
    for k, (x, label, pose) in enumerate(((120, "the eager", "up"), (220, "the eager", "up"), (590, "the sceptical", "arms"), (690, "the sceptical", "arms"))):
        arm = '<path d="M14 -70 L22 -110" stroke="#06060a" stroke-width="6" stroke-linecap="round"/>' if pose == "up" else '<path d="M-22 -60 L22 -60" stroke="#121218" stroke-width="10" stroke-linecap="round"/>'
        b.append(f'<g transform="translate({x} 470)"><circle cx="0" cy="-102" r="16" fill="#16161e"/><path d="M-26 0 L-22 -74 C-16 -86 16 -86 22 -74 L26 0 Z" fill="#16161e"/>{arm.replace("#06060a", "#16161e")}'
                 f'<path d="M-16 -102 a16 16 0 0 1 32 0 M-22 -74 C-16 -86 16 -86 22 -74" stroke="#fff4d8" stroke-width="1.6" fill="none" opacity=".8"/></g>')
    b.append(text(170, 340, "the eager", 12, "#c8b890", HAND, "middle", 'opacity=".7"') + text(640, 340, "the sceptical", 12, "#c8b890", HAND, "middle", 'opacity=".7"'))
    b.append('<rect x="40" y="60" width="120" height="80" fill="#0c0c10" stroke="#2a2a34"/>' + text(100, 96, "camera off", 10, "#6a6a7a", SERIF, "middle", 'font-style="italic"')
             + text(100, 114, "(the invisible)", 9, "#6a6a7a", HAND, "middle") + '<path d="M70 120 l60 -40 M70 80 l60 40" stroke="#3a3a4a"/>')
    b.append(text(660, 80, "Day 1 · 09:00", 16, "#c8b890", FELL, "middle", 'letter-spacing="2" opacity=".7"'))
    return p, "The New Lord Arrives", defs, "".join(b)


def ritual_circle_one_to_one():
    p = "rc"
    defs = f'<radialGradient id="{p}-doc" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#cfe6ff" stop-opacity=".6"/><stop offset="1" stop-color="#cfe6ff" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#040305"/>']
    # cancelled invites on the wall
    for k, (x, y, r) in enumerate(((60, 50, -8), (160, 90, 6), (620, 60, 5), (700, 120, -6), (90, 170, 4))):
        b.append(f'<g transform="rotate({r} {x + 40} {y + 20})" opacity=".55"><rect x="{x}" y="{y}" width="90" height="40" fill="#d8d4c8"/>' + text(x + 45, y + 16, "1:1 · Thu 15:00", 8, "#2a2a2a", SERIF, "middle")
                 + text(x + 45, y + 32, "CANCELLED", 11, "#a01010", FELL, "middle", 'font-weight="700"') + "</g>")
    # the summoning circle on the floor
    b.append('<ellipse cx="400" cy="410" rx="300" ry="70" fill="none" stroke="#c4161c" stroke-width="2.4" opacity=".75"/><ellipse cx="400" cy="410" rx="270" ry="58" fill="none" stroke="#c4161c" stroke-width="1" opacity=".6"/>'
             '<path d="M140 410 L660 410 M400 352 L400 468 M210 368 L590 452 M590 368 L210 452" stroke="#c4161c" stroke-width=".8" opacity=".4"/>')
    for x, y in ((120, 410), (680, 410), (240, 360), (560, 360), (240, 460), (560, 460)):
        b.append(f'<rect x="{x - 4}" y="{y - 22}" width="8" height="22" fill="#e0d4b0"/><ellipse cx="{x}" cy="{y - 26}" rx="3.4" ry="7" fill="#ffd27a" filter="url(#{p}-glow)"/>')
    # two chairs facing, two silhouettes
    for x, flip in ((260, 1), (540, -1)):
        b.append(f'<g transform="translate({x} 420) scale({flip} 1)"><path d="M-30 0 L-30 -60 L-40 -130 L-14 -130 L-6 -60 L30 -60 L30 0" stroke="#1a1418" stroke-width="6" fill="none"/>'
                 f'<circle cx="2" cy="-150" r="20" fill="#1a141c"/><path d="M-26 -60 L-20 -120 C-14 -132 18 -132 24 -120 L28 -60 Z" fill="#1a141c"/>'
                 f'<path d="M-18 -150 a20 20 0 0 1 40 0 M-20 -120 C-14 -132 18 -132 24 -120 L28 -60" stroke="#ffcf7a" stroke-width="1.8" fill="none" opacity=".85"/></g>')
    b.append(text(260, 470, "Pip", 13, "#c9b090", HAND, "middle", 'opacity=".7"') + text(540, 470, "Victor", 13, "#c9b090", HAND, "middle", 'opacity=".7"'))
    # the shared doc, floating between them
    b.append(f'<ellipse cx="400" cy="200" rx="160" ry="120" fill="url(#{p}-doc)"/><g transform="translate(320 120)"><rect width="160" height="170" rx="4" fill="#e8f0ff" filter="url(#{p}-glow)"/>'
             + text(80, 22, "1:1 · Thu 23 Jan", 10, "#1a2a4a", SERIF, "middle", 'font-weight="700"')
             + text(10, 46, "STATUS (read, don't discuss) ✔", 8, "#4a5a7a", MONO) + text(10, 66, "DECISIONS: scenario A/B", 8, "#1a2a4a", MONO)
             + text(10, 84, "BLOCKERS: substation data", 8, "#1a2a4a", MONO) + text(10, 102, "FEEDBACK: the board pack?", 8, "#1a2a4a", MONO)
             + text(10, 120, "FOR ME: level 5", 8, "#a01010", MONO) + text(10, 150, "ended at 14 min ✨", 9, "#3a7a3a", HAND) + "</g>")
    return p, "The Ritual Circle of the 1:1", defs, "".join(b)


def skip_level_seance():
    p = "sl3"
    defs = (f'<radialGradient id="{p}-smoke" cx=".5" cy=".6" r=".6"><stop offset="0" stop-color="#bcd6ff" stop-opacity=".45"/><stop offset="1" stop-color="#bcd6ff" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="{p}-cand" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".6"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#030304"/>', f'<ellipse cx="400" cy="380" rx="300" ry="140" fill="url(#{p}-cand)"/>']
    # the summoned director, in smoke
    b.append(f'<ellipse cx="400" cy="200" rx="180" ry="170" fill="url(#{p}-smoke)" filter="url(#{p}-b6)"/>')
    b.append(f'<g opacity=".7">{face(p, 1, 400, 170, .66, skin=("#0c1018", "#4a5a74", "#a8bcd8"), light="above", light_col="#e0ecff", rim="#bcd6ff", eye="cyan", glow=True, brows="raised", mouth="thin", hair="slick", hair_col="#6a6a72", ears="human", extras=("translucent",))}</g>')
    b.append(f'<path d="M340 250 C330 300 360 330 400 340 C440 330 470 300 460 250" fill="#bcd6ff" opacity=".2" filter="url(#{p}-b6)"/>')
    b.append(text(400, 40, "“Have you raised these with Victor?”", 15, "#bcd6ff", SERIF, "middle", 'font-style="italic" opacity=".8"'))
    # the séance table: a board of letters, a list of eleven grievances
    b.append('<ellipse cx="400" cy="420" rx="260" ry="50" fill="#140c08"/><ellipse cx="400" cy="414" rx="250" ry="44" fill="#1e140c"/>'
             '<rect x="330" y="394" width="140" height="40" rx="6" fill="#c8b08a"/>' + text(400, 410, "OPEN DOOR", 10, "#3a2010", FELL, "middle", 'letter-spacing="2"')
             + text(400, 426, "POLICY", 10, "#3a2010", FELL, "middle", 'letter-spacing="2"'))
    b.append('<g transform="rotate(8 560 410)"><rect x="520" y="380" width="80" height="60" fill="#e8e0c8"/>' + text(560, 394, "PROBLEMS", 7, "#3a2a1a", FELL, "middle")
             + "".join(text(528, 404 + k * 3.4, f"{k + 1}. …", 3, "#5a4a3a") for k in range(11)) + "</g>")
    for x in (180, 620):
        b.append(f'<rect x="{x - 4}" y="378" width="8" height="26" fill="#e0d4b0"/><ellipse cx="{x}" cy="374" rx="3.4" ry="8" fill="#ffd27a" filter="url(#{p}-glow)"/>')
    # Pip's hands on the table
    b.append(hand(p, 330, 470, .7, flip=True, rim="#ffcf7a", light="#ffd8a0", claws=False, pose="open") + hand(p, 470, 470, .7, rim="#ffcf7a", light="#ffd8a0", claws=False, pose="open"))
    # Victor, watching through the door crack
    b.append('<rect x="700" y="60" width="90" height="400" fill="#0a0a0c"/><rect x="700" y="60" width="10" height="400" fill="#cfe0ff" opacity=".2"/>'
             f'<g filter="url(#{p}-glow)"><circle cx="716" cy="200" r="3" fill="#ff2a20"/><circle cx="730" cy="200" r="3" fill="#ff2a20"/></g>' + text(740, 480, "Victor knew by 17:30", 10, "#8a8a9a", HAND, "middle", 'opacity=".7"'))
    return p, "The Skip-Level Séance", defs, "".join(b)


def puppet_king():
    p = "pk"
    defs = (f'<linearGradient id="{p}-gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff0b0"/><stop offset=".5" stop-color="#d8a020"/><stop offset="1" stop-color="#6a4a00"/></linearGradient>'
            f'<radialGradient id="{p}-spot" cx=".5" cy=".4" r=".6"><stop offset="0" stop-color="#e8d8ff" stop-opacity=".35"/><stop offset="1" stop-color="#e8d8ff" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040306"/>', f'<rect width="{W}" height="{H}" fill="url(#{p}-spot)"/>']
    # the hand above, holding the control bar, and a teacup
    b.append('<path d="M240 40 L560 40" stroke="#6a4a2a" stroke-width="10" stroke-linecap="round"/><path d="M400 20 L400 60" stroke="#6a4a2a" stroke-width="8"/>'
             '<path d="M380 0 C384 14 416 14 420 0" fill="#c8b0a0"/>'
             '<g transform="translate(600 40)"><path d="M-14 0 L14 0 L10 16 L-10 16 Z" fill="#e8e0d0"/><path d="M14 4 C22 4 22 12 14 12" stroke="#e8e0d0" stroke-width="2" fill="none"/><ellipse cx="0" cy="22" rx="20" ry="4" fill="#e8e0d0"/></g>'
             + text(640, 80, "(Ottoline)", 11, "#c8b8d8", HAND, "middle", 'opacity=".7"'))
    # the strings
    b.append('<g stroke="#e8e0f0" stroke-width=".9" opacity=".7"><path d="M250 40 L300 300 M330 40 L360 130 M470 40 L440 130 M550 40 L500 300 M400 60 L400 70"/></g>')
    # Victor, crowned, on a small throne, limbs on strings
    b.append('<path d="M310 470 L310 280 C310 240 490 240 490 280 L490 470 Z" fill="#1a0e10"/>')
    fv = (400, 180)
    b.append(suit(p, 1, fv[0], by(fv[1], .62, .78), .78, tie="#2a3a5a", jacket="#0b0b10", shirt="#5a6478", rim="#e8d8ff"))
    b.append(face(p, 1, fv[0], fv[1], .62, skin=("#0e1018", "#3c4458", "#7a86a0"), light="above", light_col="#e8d8ff", rim="#c4161c",
                  eye="human", glow=False, brows="worried", mouth="thin", hair="slick", hair_col="#06060a", ears="human"))
    b.append(f'<path d="M370 104 L376 84 L388 98 L400 78 L412 98 L424 84 L430 104 Z" fill="url(#{p}-gold)"/>')
    b.append(hand(p, 300, 320, .7, flip=True, rim="#e8d8ff", light="#e8d8ff", claws=False, pose="open") + hand(p, 500, 320, .7, rim="#e8d8ff", light="#e8d8ff", claws=False, pose="open"))
    b.append('<g transform="rotate(-6 150 300)"><rect x="80" y="270" width="150" height="56" fill="#e8e0c8"/>' + text(155, 292, "LEAVE IT WITH ME", 11, "#3a2a1a", FELL, "middle")
             + text(155, 314, "(× 4)", 11, "#7a1010", HAND, "middle") + "</g>")
    b.append(f'<g transform="rotate(10 640 340)"><rect x="580" y="300" width="130" height="70" fill="none" stroke="#c4161c" stroke-width="3"/>'
             + text(645, 326, "APPROVAL LIMIT", 10, "#c4161c", FELL, "middle") + text(645, 352, "£5,000", 20, "#c4161c", BLACK, "middle") + "</g>")
    b.append(text(400, 492, "Head of Grid Analytics. Can approve: biscuits.", 13, "#c8b8d8", SERIF, "middle", 'font-style="italic" opacity=".65"'))
    return p, "The Puppet King", defs, "".join(b)


def friend_became_boss():
    p = "fb"
    defs = f'<radialGradient id="{p}-cafe" cx=".5" cy=".4" r=".7"><stop offset="0" stop-color="#ffcf9a" stop-opacity=".45"/><stop offset="1" stop-color="#ffcf9a" stop-opacity="0"/></radialGradient>'
    b = [f'<rect width="{W}" height="{H}" fill="#050403"/>', f'<rect width="{W}" height="{H}" fill="url(#{p}-cafe)"/>']
    b.append(text(400, 46, "Friday 10 January · 08:30", 15, "#c9a87a", FELL, "middle", 'letter-spacing="2" opacity=".7"'))
    # Jules (left) with the new lanyard; Pip (right)
    fj, fp = (230, 200), (570, 205)
    b.append(blouse(p, fj[0], by(fj[1], .62, .8), .8, cardigan="#3a2a1a", top="#6a5a42", rim="#ffcf9a", rim_side="right", necklace=False))
    b.append(face(p, 1, fj[0], fj[1], .62, skin=("#1a120c", "#6a5040", "#d0b090"), light="right", light_col="#ffd8a8", rim="#ffcf9a", rim_side="left",
                  eye="human", glow=False, brows="worried", mouth="smile", hair="slick", hair_col="#3a2414", ears="human", lip="#8a4a3a"))
    b.append('<path d="M206 250 L230 300 L254 250" stroke="#c4161c" stroke-width="3" fill="none"/><rect x="216" y="298" width="30" height="20" rx="2" fill="#e8e0c8"/>'
             + text(231, 311, "TEAM LEAD", 4.6, "#7a1010", FELL, "middle"))
    b.append(suit(p, 2, fp[0], by(fp[1], .62, .8), .8, tie="#2a3a4a", jacket="#121014", shirt="#7a7068", rim="#ffcf9a", rim_side="left"))
    b.append(face(p, 2, fp[0], fp[1], .62, skin=("#14100c", "#5a4a3c", "#c8a888"), light="left", light_col="#ffd8a8", rim="#ffcf9a", rim_side="right",
                  eye="human", glow=False, brows="flat", mouth="thin", hair="slick", hair_col="#08060a", ears="human"))
    # the empty third chair: the job they both wanted
    b.append('<g opacity=".5"><path d="M370 470 L370 360 L360 270 L440 270 L430 360 L430 470" stroke="#3a2a20" stroke-width="5" fill="none"/>'
             '<ellipse cx="400" cy="300" rx="34" ry="44" fill="#cfd8e8" opacity=".25" filter="url(#fb-b6)"/></g>'
             + text(400, 256, "the job you both wanted", 11, "#a8b8c8", HAND, "middle", 'opacity=".7"'))
    # the table: two coffees and the napkin of rules
    b.append('<path d="M120 400 L680 400 L720 500 L80 500 Z" fill="#1a120c"/><path d="M120 400 H680" stroke="#5a3a24"/>')
    b.append(mug(260, 360, "TEAM", "LEAD", "#d8d0c0", "#5a1a1a") + mug(500, 360, "I ♥ PIE", "CHARTS (NOT)", "#d8d0c0", "#2a3a5a"))
    b.append('<g transform="rotate(-3 400 440)"><rect x="330" y="410" width="140" height="70" fill="#f0ece0"/>'
             + text(400, 426, "THE NEW RULES", 8, "#3a2a1a", FELL, "middle") + text(338, 442, "work at work", 8, "#3a2a1a", HAND)
             + text(338, 456, "no pub moaning", 8, "#3a2a1a", HAND) + text(338, 470, "check in: 3 months", 8, "#3a2a1a", HAND) + "</g>")
    b.append(text(400, 494, "“I wanted it, I'm a bit gutted, and I'm glad it's you.”", 12, "#ffd8a8", SERIF, "middle", 'font-style="italic" opacity=".65"'))
    return p, "The Friend Who Became Your Boss", defs, "".join(b)


# ================================================================ Act V plates (three flagships)
def reading_the_omens():
    p = "ro"
    defs = (f'<linearGradient id="{p}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0a1a"/><stop offset="1" stop-color="#1a0e14"/></linearGradient>'
            f'<radialGradient id="{p}-mon" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#cfe0ff" stop-opacity=".55"/><stop offset="1" stop-color="#cfe0ff" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#040306"/>']
    # the window: a night sky with a comet, and a raven on the sill
    b.append(f'<rect x="500" y="20" width="280" height="250" fill="url(#{p}-sky)"/><path d="M640 20 V270 M500 145 H780" stroke="#06060a" stroke-width="6"/>'
             f'<path d="M560 70 L700 40" stroke="#ffe2b0" stroke-width="2" opacity=".6" filter="url(#{p}-b2)"/><circle cx="702" cy="40" r="5" fill="#fff4e0" filter="url(#{p}-glow)"/>'
             '<g transform="translate(560 262)"><path d="M0 0 C-6 -20 10 -34 26 -30 C40 -26 46 -12 40 0 Z" fill="#020203"/><path d="M26 -30 L40 -36 L30 -26 Z" fill="#020203"/>'
             '<circle cx="28" cy="-24" r="2" fill="#ffd21a"/><path d="M4 0 L-4 10 M14 0 L10 10" stroke="#020203" stroke-width="2"/></g>')
    # the poster and the visitor badges
    b.append('<g transform="rotate(-3 140 110)"><rect x="40" y="40" width="200" height="130" fill="#d8d0bc"/>' + text(140, 74, "LEADERSHIP OFF-SITE", 13, "#2a2418", FELL, "middle")
             + text(140, 96, "March 2027 · Lisbon", 11, "#4a4030", SERIF, "middle") + "</g>"
             '<g transform="rotate(-14 140 130)"><rect x="60" y="110" width="160" height="34" fill="none" stroke="#b01414" stroke-width="3"/>'
             + text(140, 134, "POSTPONED", 20, "#b01414", BLACK, "middle") + "</g>")
    for k, x in enumerate((300, 340, 380)):
        b.append(f'<g transform="translate({x} {200 + k * 6}) rotate({k * 8 - 8})"><path d="M0 -40 L0 0" stroke="#3a5aa0" stroke-width="2"/><rect x="-16" y="0" width="32" height="40" rx="2" fill="#e8e8f0"/>'
                 f'<rect x="-16" y="0" width="32" height="9" fill="#1a1a2a"/>' + text(0, 7, "VEXMOOR", 4.6, "#e8e8f0", FELL, "middle") + text(0, 26, "VISITOR", 5, "#3a3a4a", SERIF, "middle") + text(0, 34, "8 weeks", 4.6, "#a01010", SERIF, "middle") + "</g>")
    # Tamsin at her desk, lit by the booking on her screen
    b.append(f'<ellipse cx="380" cy="360" rx="220" ry="160" fill="url(#{p}-mon)" filter="url(#{p}-b12)"/>')
    ft = (400, 250)
    b.append(blouse(p, ft[0], by(ft[1], .6, .78), .78, cardigan="#14121a", top="#2a2a3a", rim="#cfe0ff", rim_side="left"))
    b.append(face(p, 1, ft[0], ft[1], .6, skin=("#0e1018", "#4a5068", "#a8b0c8"), light="below", light_col="#cfe0ff", rim="#c4161c", rim_side="right",
                  eye="human", glow=False, brows="flat", mouth="thin", hair="bob", hair_col="#0a0608", ears="none"))
    b.append(table(400, "#0a0806"))
    b.append(f'<path d="M560 400 L580 300 L760 296 L770 400 Z" fill="#0c0e14"/><rect x="590" y="310" width="164" height="80" fill="#dceaff" filter="url(#{p}-glow)"/>'
             + text(672, 330, "ROOM BOOKING", 9, "#1a2a4a", FELL, "middle") + text(672, 350, "G1 (ground floor)", 9, "#1a2a4a", SERIF, "middle")
             + text(672, 366, "1–5 June · all day", 9, "#1a2a4a", SERIF, "middle") + text(672, 382, "HR", 12, "#a01010", MONO, "middle", 'font-weight="700"'))
    b.append(text(170, 470, "“No plans to make large-scale changes at this time.”", 12, "#c8b8d8", SERIF, "middle", 'font-style="italic" opacity=".65"'))
    return p, "Reading the Omens", defs, "".join(b)


def calendar_invite():
    p = "ci"
    defs = (f'<radialGradient id="{p}-tube" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#eaf6f0" stop-opacity=".55"/><stop offset="1" stop-color="#eaf6f0" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{p}-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1e20"/><stop offset="1" stop-color="#08090a"/></linearGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="url(#{p}-wall)"/>']
    b.append('<rect x="340" y="8" width="120" height="6" fill="#eaf6f0" opacity=".9"/>' + f'<path d="M300 14 L500 14 L700 470 L100 470 Z" fill="url(#{p}-tube)" filter="url(#{p}-b12)"/>')
    b.append('<rect x="40" y="40" width="130" height="34" fill="#0a0c0c" stroke="#2a3030"/>' + text(105, 62, "ROOM 4B · G", 13, "#9ab0a8", FELL, "middle", 'letter-spacing="2"'))
    b.append('<circle cx="700" cy="70" r="34" fill="#0c0e0e" stroke="#3a4a44" stroke-width="2"/><path d="M700 70 L700 46 M700 70 L716 76" stroke="#cfe6dc" stroke-width="2.4"/>' + text(700, 124, "10:14", 13, "#cfe6dc", MONO, "middle"))
    # Marcus
    fm = (400, 190)
    b.append(suit(p, 1, fm[0], by(fm[1], .7, .9), .9, tie="#5a3a2a", jacket="#1a1614", shirt="#8a8070", rim="#eaf6f0"))
    b.append(face(p, 1, fm[0], fm[1], .7, skin=("#14100e", "#5a4a42", "#c8b0a0"), light="above", light_col="#eaf6f0", rim="#7a8a90",
                  eye="human", glow=False, brows="worried", mouth="thin", hair="slick", hair_col="#4a3a30", ears="human", extras=("wrinkles",)))
    # the table: water, tissues, the envelope, the agreement, the pen
    b.append('<path d="M60 380 L740 380 L800 500 L0 500 Z" fill="#141412"/><path d="M60 380 H740" stroke="#4a4a40" stroke-width="1.2"/>')
    b.append('<path d="M160 330 L184 330 L180 380 L164 380 Z" fill="#cfe6f0" opacity=".45"/><rect x="230" y="346" width="70" height="34" fill="#e8e8e0"/><path d="M250 346 C256 330 274 330 280 346" fill="#fff" opacity=".9"/>'
             + text(265, 368, "TISSUES", 8, "#6a6a60", FELL, "middle"))
    b.append('<g transform="rotate(-4 400 440)"><rect x="320" y="400" width="170" height="90" fill="#f0ece0"/>' + text(405, 420, "SETTLEMENT AGREEMENT", 9, "#2a2a2a", FELL, "middle")
             + "".join(f'<path d="M332 {432 + k * 8} h{140 - (k * 17) % 40}" stroke="#8a8a80" stroke-width="1.4"/>' for k in range(5))
             + '<path d="M360 482 H460" stroke="#2a2a2a"/>' + text(352, 480, "✕", 9, "#a01010", SERIF) + "</g>")
    b.append('<g transform="rotate(-30 520 420)"><rect x="470" y="414" width="90" height="7" rx="3" fill="#1a1a2a"/><path d="M560 414 L572 417 L560 421 Z" fill="#c9a24a"/></g>')
    b.append('<g transform="rotate(5 610 430)"><rect x="560" y="400" width="120" height="70" fill="#d8ccb0"/>' + text(620, 434, "PRIVATE &amp;", 9, "#3a2a1a", FELL, "middle") + text(620, 448, "CONFIDENTIAL", 9, "#3a2a1a", FELL, "middle") + "</g>")
    # the two across the table: backs to us, in silhouette
    for x in (130, 670):
        b.append(f'<g transform="translate({x} 500)"><circle cx="0" cy="-150" r="30" fill="#030404"/><path d="M-70 0 L-62 -96 C-50 -118 50 -118 62 -96 L70 0 Z" fill="#030404"/>'
                 f'<path d="M-30 -150 a30 30 0 0 1 60 0" stroke="#eaf6f0" stroke-width="1.6" fill="none" opacity=".55"/></g>')
    b.append(text(130, 330, "HR", 12, "#7a8a90", HAND, "middle", 'opacity=".7"') + text(670, 330, "Rupert (reading)", 12, "#7a8a90", HAND, "middle", 'opacity=".7"'))
    b.append(text(400, 32, "Quick catch-up · 15 min", 14, "#cfe6dc", SERIF, "middle", 'font-style="italic" opacity=".7"'))
    return p, "The Day of the Calendar Invite", defs, "".join(b)


def ghost_ship():
    p = "gs"
    defs = (f'<linearGradient id="{p}-sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a2a36"/><stop offset="1" stop-color="#020a0e"/></linearGradient>'
            f'<radialGradient id="{p}-scr" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#bcd6ff" stop-opacity=".6"/><stop offset="1" stop-color="#bcd6ff" stop-opacity="0"/></radialGradient>')
    b = [f'<rect width="{W}" height="{H}" fill="#03050a"/>', '<circle cx="120" cy="80" r="30" fill="#d8dcc8" opacity=".7" filter="url(#gs-b2)"/>']
    # the office floor, listing, sliding into the sea
    b.append('<g transform="rotate(-7 400 300)"><rect x="60" y="250" width="720" height="16" fill="#1a1612"/>'
             + "".join(f'<rect x="{x}" y="{200 if k % 2 else 210}" width="70" height="50" fill="#0c0a08"/><rect x="{x + 20}" y="{186 if k % 2 else 196}" width="30" height="14" fill="#0a0c10"/>' for k, x in enumerate((120, 260, 600)))
             + '<rect x="660" y="120" width="110" height="130" fill="#0a0a0c" stroke="#2a2a30"/>' + text(715, 150, "B. CRANE", 9, "#7a7a8a", FELL, "middle")
             + text(715, 190, "travelling", 11, "#c8a0ff", HAND, "middle") + text(715, 210, "(permanently)", 9, "#8a7a9a", HAND, "middle") + "</g>")
    # the screen: Strategy 2028 Vision, to empty chairs
    b.append(f'<ellipse cx="300" cy="140" rx="200" ry="110" fill="url(#{p}-scr)"/><g transform="rotate(-7 300 140)"><rect x="200" y="70" width="200" height="110" fill="#1a2a44"/>'
             + text(300, 108, "STRATEGY", 15, "#e0ecff", BLACK, "middle") + text(300, 132, "2028 VISION", 15, "#e0ecff", BLACK, "middle") + text(300, 160, "slide 1 of 40", 9, "#9ab0d0", SERIF, "middle") + "</g>")
    # Dorian at a ship's wheel, presenting to nobody
    fd = (470, 210)
    b.append(suit(p, 1, fd[0], by(fd[1], .52, .66), .66, tie="#5a070c", jacket="#0c0c11", shirt="#5a6070", rim="#bcd6ff"))
    b.append(face(p, 1, fd[0], fd[1], .52, skin=("#0e1018", "#3c4458", "#8a96b0"), light="left", light_col="#bcd6ff", rim="#ff3a22",
                  eye="red", glow=True, brows="raised", mouth="fangs", hair="slick", hair_col="#050407", ears="pointed"))
    b.append('<g transform="translate(470 360)"><circle r="44" fill="none" stroke="#5a3a1a" stroke-width="7"/><circle r="10" fill="#5a3a1a"/>'
             + "".join(f'<path d="M0 0 L{60 * __import__("math").cos(a * 0.7854):.1f} {60 * __import__("math").sin(a * 0.7854):.1f}" stroke="#5a3a1a" stroke-width="5" stroke-linecap="round"/>' for a in range(8)) + "</g>")
    # the sea rising, and the lifeboat rowing away
    b.append(f'<path d="M0 380 Q100 368 200 382 T400 378 T600 386 T800 374 L800 500 L0 500 Z" fill="url(#{p}-sea)"/>'
             '<path d="M0 380 Q100 368 200 382 T400 378 T600 386 T800 374" stroke="#7ad8ff" stroke-width="1.4" fill="none" opacity=".4"/>')
    for k, (x, y, r) in enumerate(((560, 420, 20), (640, 440, -14), (360, 452, 8))):
        b.append(f'<g transform="rotate({r} {x} {y})"><rect x="{x - 24}" y="{y - 10}" width="48" height="14" fill="#1a1612"/><rect x="{x - 18}" y="{y - 30}" width="36" height="20" fill="#0c0a08"/></g>')
    b.append('<g transform="translate(140 430)"><path d="M-70 0 Q0 26 70 0 L56 -14 L-56 -14 Z" fill="#3a2a1a"/><path d="M-56 -14 L56 -14" stroke="#c9a24a"/>'
             + text(0, -2, "LIFEBOAT · OFFICERS ONLY", 6, "#e8d8b8", FELL, "middle")
             + '<circle cx="-10" cy="-32" r="10" fill="#030304"/><path d="M-24 -14 L-20 -40 C-16 -46 0 -46 4 -40 L8 -14 Z" fill="#030304"/>'
             + '<path d="M4 -30 L40 -6 M-24 -30 L-60 -6" stroke="#5a3a1a" stroke-width="3"/>'
             + '<rect x="-14" y="-28" width="9" height="11" fill="#e8e8f0"/>' + text(-9.5, -21, "V", 5, "#1a1a2a", FELL, "middle") + "</g>")
    b.append(text(140, 476, "Victor (to Vexmoor)", 11, "#9ab0c0", HAND, "middle", 'opacity=".7"'))
    b.append(text(640, 492, "Attendees: 3 (one is collecting the projector)", 11, "#bcd6ff", SERIF, "middle", 'font-style="italic" opacity=".6"'))
    return p, "The Ghost Ship", defs, "".join(b)


PLATES = {
    "meeting-lich": meeting_lich, "gaslight-wraith": gaslight_wraith, "bulldozer-ogre": bulldozer_ogre,
    "passive-aggressive-poltergeist": passive_aggressive_poltergeist, "coasting-zombie": coasting_zombie,
    "doppelganger": doppelganger, "martyr-banshee": martyr_banshee, "know-it-all-basilisk": know_it_all_basilisk,
    "doom-prophet": doom_prophet, "toxic-positivity-siren": toxic_positivity_siren, "boundary-goblin": boundary_goblin,
    "hidden-thrones": hidden_thrones, "ring-kissing-ritual": ring_kissing_ritual, "sacrificial-lamb": sacrificial_lamb,
    "meeting-before-the-meeting": meeting_before_the_meeting, "blood-pacts": blood_pacts, "ghost-decision": ghost_decision,
    "rumour-mill-familiar": rumour_mill_familiar, "cc-inquisition": cc_inquisition, "turf-wars": turf_wars,
    "empire-builder": empire_builder, "chosen-one": chosen_one, "plausible-silence": plausible_silence,
    "absent-lord": absent_lord, "weather-tyrant": weather_tyrant, "conflict-phantom": conflict_phantom,
    "credit-taking-crown": credit_taking_crown, "new-lord-arrives": new_lord_arrives, "ritual-circle-one-to-one": ritual_circle_one_to_one,
    "skip-level-seance": skip_level_seance, "puppet-king": puppet_king, "friend-became-boss": friend_became_boss,
    "reading-the-omens": reading_the_omens, "calendar-invite": calendar_invite, "ghost-ship": ghost_ship,
    "all-seeing-eye": all_seeing_eye, "seagull-overlord": seagull_overlord, "escape-portal": escape_portal,
}


def main():
    ART.mkdir(parents=True, exist_ok=True)
    for slug, fn in PLATES.items():
        p, label, defs, body = fn()
        (ART / f"{slug}.svg").write_text(fix(p, svg(p, label, defs, body)), encoding="utf-8")
    print(f"wrote {len(PLATES)} plates")


if __name__ == "__main__":
    main()
