#!/usr/bin/env python3
"""Builds Series 3, Jef's Handbooks: long-form books with chapters (see docs/HANDOFF-handbooks.md).

Each book lives in content/handbooks/<key>/:
  - book.py defines BOOK (metadata, parts → chapters, appendices, and which chapters are written)
  - <nn>-<slug>.html is a written chapter's body (plain HTML using the classes in public/assets/book.css)
Output: public/handbooks/<key>/index.html (title page + contents) and one page per written chapter.

Cross-references inside a chapter are written as href="#chN"; they become links to chapter N's page when it is
written, or to its entry on the contents page when it isn't yet.

Usage: python3 scripts/build_handbooks.py [--css-href PATH] [--out DIR]
  (the two options build a copy with another stylesheet path, e.g. for a standalone preview)
"""
import argparse
import hashlib
import importlib.util
import re
import sys
from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
CONTENT = ROOT / "content" / "handbooks"
AUTHOR = "Jefrey Romel Tagunicar"
BOOKS = ["cloud-networking"]
FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800&"
         "family=JetBrains+Mono:wght@400;600&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap")


def load_book(key):
    spec = importlib.util.spec_from_file_location(f"book_{key.replace('-', '_')}", CONTENT / key / "book.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BOOK


def chapters(book):
    for part in book["parts"]:
        for ch in part["chapters"]:
            yield part, ch


def page_name(book, num):
    slug = next(ch[1] for _, ch in chapters(book) if ch[0] == num)
    return f"{num:02d}-{slug}.html"


def default_css_href(depth):
    digest = hashlib.sha256((PUBLIC / "assets" / "book.css").read_bytes()).hexdigest()[:10]
    return "../" * depth + f"assets/book.css?v={digest}"


def head(title, desc, css_href, depth):
    icon = "../" * depth + "assets/favicon.svg"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{css_href}">
<link rel="icon" href="{icon}" type="image/svg+xml">
</head>
<body class="handbook">'''


def runhead(book, right, home):
    draft = ' · <span class="draft">draft for review</span>' if book.get("draft") else ""
    return (f'<header class="runhead"><span><a href="{home}">{esc(book["series"])} · {book["no"]}</a> · '
            f'<a href="index.html">{esc(book["title"])}</a>{draft}</span><span>{right}</span></header>')


def colophon(book):
    return (f'<footer class="colophon"><span>{esc(book["series"])} · Handbook {book["no"]} · {esc(book["title"])}</span>'
            f'<span>by {AUTHOR}</span></footer>')


def link_chapters(html, book):
    written = book["files"]

    def repl(m):
        n = int(m.group(1))
        return f'href="{page_name(book, n)}"' if n in written else f'href="index.html#ch{n}"'
    return re.sub(r'href="#ch(\d+)"', repl, html)


def render_chapter(book, num, css_href, home):
    part, ch = next((p, c) for p, c in chapters(book) if c[0] == num)
    body = (CONTENT / book["key"] / book["files"][num]).read_text(encoding="utf-8")
    body = re.sub(r"^<!--.*?-->\s*", "", body, flags=re.S)
    body = link_chapters(body, book)
    return "\n".join([
        head(f"{ch[2]} · {book['title']}", ch[3], css_href, 2),
        runhead(book, f"Part {part['no']} · Chapter {num}", home),
        '<main class="page">',
        body,
        '</main>',
        colophon(book),
        '</body>', '</html>', ''])


def render_index(book, css_href, home):
    written = book["files"]
    n_ch = sum(1 for _ in chapters(book))
    parts_html = []
    for part in book["parts"]:
        items = []
        for num, slug, title, summary, covers in part["chapters"]:
            if num in written:
                t = f'<a href="{page_name(book, num)}">{esc(title)}</a><span class="badge">sample chapter</span>'
            else:
                t = esc(title)
            items.append(f'''      <li id="ch{num}"><span class="cn">{num}</span><div>
        <h3>{t}</h3>
        <p>{esc(summary)}</p>
        <p class="covers">{esc(covers)}</p>
      </div></li>''')
        parts_html.append(f'''  <section class="toc-part" aria-labelledby="part-{part['no']}">
    <header><span class="pn">Part {part['no']}</span><h2 id="part-{part['no']}">{esc(part['title'])}</h2><p>{esc(part['blurb'])}</p></header>
    <ol class="toc-ch">
{chr(10).join(items)}
    </ol>
  </section>''')
    apps = "\n".join(f'      <li id="app{a}"><span class="cn">{a}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>'
                     for a, t, d in book["appendices"])
    sample = page_name(book, next(iter(written)))
    return "\n".join([
        head(f"{book['title']} · {book['series']}", book["promise"], css_href, 2),
        runhead(book, f"{n_ch} chapters · {len(book['parts'])} parts", home),
        '<main class="page">',
        f'''<header class="opener">
  <p class="eyebrow">{esc(book['series'])} · Handbook {book['no']}</p>
  <h1>{esc(book['title'])}</h1>
  <p class="promise">{esc(book['subtitle'])}</p>
</header>
<section class="chapter-card" aria-label="About this book">
  <div><h2>Who it's for</h2><p>{esc(book['audience'])}</p></div>
  <div><h2>How it's built</h2><p>{esc(book['promise'])}</p></div>
  <div><h2>The running example</h2><p>{book['example']}</p></div>
</section>
<p>Start with <a href="{sample}">the sample chapter</a> to see the format. Planned chapters are listed with the topics they cover.</p>
<h2 class="sec" id="contents"><span class="n">§</span>Contents</h2>''',
        "\n".join(parts_html),
        f'''  <section class="toc-part" aria-labelledby="appendices">
    <header><span class="pn">Back</span><h2 id="appendices">Appendices</h2><p>Reference material to keep open while you work.</p></header>
    <ol class="toc-ch">
{apps}
    </ol>
  </section>''',
        '</main>',
        colophon(book),
        '</body>', '</html>', ''])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--css-href", help="stylesheet href to use instead of ../../assets/book.css?v=…")
    ap.add_argument("--home", default="../../index.html", help="link for the series name in the running header")
    ap.add_argument("--out", help="output folder instead of public/handbooks/<key>/")
    args = ap.parse_args()
    for key in BOOKS:
        book = load_book(key)
        out = Path(args.out) if args.out else PUBLIC / "handbooks" / key
        out.mkdir(parents=True, exist_ok=True)
        css = args.css_href or default_css_href(2)
        (out / "index.html").write_text(render_index(book, css, args.home), encoding="utf-8")
        for num in book["files"]:
            (out / page_name(book, num)).write_text(render_chapter(book, num, css, args.home), encoding="utf-8")
        print(f"{key}: index + {len(book['files'])} chapter(s) → {out}")


if __name__ == "__main__":
    sys.exit(main())
