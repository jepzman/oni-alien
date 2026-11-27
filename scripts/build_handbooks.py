#!/usr/bin/env python3
"""Builds Series 3, Jef's Handbooks: long-form books with chapters (see docs/HANDOFF-handbooks.md).

Each book lives in content/handbooks/<key>/:
  - book.py defines BOOK (metadata, parts → chapters, appendices, and which chapters are written)
  - <nn>-<slug>.html is a written chapter's body (plain HTML using the classes in public/assets/book.css)
  - appendix-<letter>.html is a written appendix's body (same rules); it gets a page, a contents link and a place
    at the end of all.html
Output: public/handbooks/<key>/index.html (title page + contents), all.html (every written chapter, for the PDF)
and one page per written chapter.

Cross-references inside a chapter are written as href="#chN"; they become links to chapter N's page when it is
written, or to its entry on the contents page when it isn't yet.

Run by scripts/build_notes.py (which also puts the books on the landing page and in journals.json for the PDFs),
or alone: python3 scripts/build_handbooks.py [--css-href PATH] [--out DIR]
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
BOOKS = ["cloud-networking", "cloud-identity"]
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


def written(book):
    """Chapter number → file, for every <nn>-<slug>.html in the book's content folder."""
    out = {}
    for f in sorted((CONTENT / book["key"]).glob("[0-9][0-9]-*.html")):
        out[int(f.name[:2])] = f.name
    return out


def written_appendices(book):
    """Appendix letter → file, for every appendix-<letter>.html in the book's content folder."""
    letters = [a[0] for a in book["appendices"]]
    return {a: f"appendix-{a.lower()}.html" for a in letters if (CONTENT / book["key"] / f"appendix-{a.lower()}.html").exists()}


def link_chapters(html, book):
    done, apps = written(book), written_appendices(book)

    def repl(m):
        n = int(m.group(1))
        return f'href="{page_name(book, n)}"' if n in done else f'href="index.html#ch{n}"'

    def repl_app(m):
        a = m.group(1)
        return f'href="{apps[a]}"' if a in apps else f'href="index.html#app{a}"'
    html = re.sub(r'href="#ch(\d+)"', repl, html)
    return re.sub(r'href="#app([A-Z])"', repl_app, html)


def chapter_body(book, num):
    body = (CONTENT / book["key"] / written(book)[num]).read_text(encoding="utf-8")
    body = re.sub(r"^<!--.*?-->\s*", "", body, flags=re.S)
    return link_chapters(body, book)


def appendix_body(book, letter):
    body = (CONTENT / book["key"] / written_appendices(book)[letter]).read_text(encoding="utf-8")
    body = re.sub(r"^<!--.*?-->\s*", "", body, flags=re.S)
    return link_chapters(body, book)


def render_appendix(book, letter, css_href, home):
    title, desc = next((t, d) for a, t, d in book["appendices"] if a == letter)
    return "\n".join([
        head(f"Appendix {letter}: {title} · {book['title']}", desc, css_href, 2),
        runhead(book, f"Appendix {letter}", home),
        '<main class="page">',
        appendix_body(book, letter),
        '</main>',
        colophon(book),
        '</body>', '</html>', ''])


def render_chapter(book, num, css_href, home):
    part, ch = next((p, c) for p, c in chapters(book) if c[0] == num)
    return "\n".join([
        head(f"{ch[2]} · {book['title']}", ch[3], css_href, 2),
        runhead(book, f"Part {part['no']} · Chapter {num}", home),
        '<main class="page">',
        chapter_body(book, num),
        '</main>',
        colophon(book),
        '</body>', '</html>', ''])


def render_all(book, css_href, home):
    """Every written chapter on one page (for the whole-book PDF). Each chapter is an article.sheet."""
    arts = []
    for num in written(book):
        body = chapter_body(book, num)
        body = re.sub(r'<nav class="next".*?</nav>', "", body, flags=re.S)
        arts.append(f'<article class="sheet chapter" id="chapter-{page_name(book, num)[:-5]}">\n{body}\n</article>')
    for letter, fname in written_appendices(book).items():
        body = appendix_body(book, letter)
        body = re.sub(r'<nav class="next".*?</nav>', "", body, flags=re.S)
        arts.append(f'<article class="sheet chapter" id="chapter-{fname[:-5]}">\n{body}\n</article>')
    local = r'href="(\d\d-[a-z0-9-]+|appendix-[a-z])\.html"'
    arts = [re.sub(local, r'href="#chapter-\1"', a) for a in arts]
    return "\n".join([
        head(f"{book['title']} · the whole book", book["promise"], css_href, 2),
        runhead(book, "the whole book", home),
        '<main class="page">',
        f'<header class="opener"><p class="eyebrow">{esc(book["series"])} · Handbook {book["no"]}</p>'
        f'<h1>{esc(book["title"])}</h1><p class="promise">{esc(book["subtitle"])}</p></header>',
        "\n".join(arts),
        '</main>',
        colophon(book),
        '</body>', '</html>', ''])


def render_index(book, css_href, home):
    done = written(book)
    n_ch = sum(1 for _ in chapters(book))
    parts_html = []
    for part in book["parts"]:
        items = []
        for num, slug, title, summary, covers in part["chapters"]:
            if num in done:
                t, cls = f'<a href="{page_name(book, num)}">{esc(title)}</a>', ""
            elif num == book.get("next"):
                t, cls = f'{esc(title)}<span class="badge badge--soon">next up</span>', ' class="planned"'
            else:
                t, cls = f'{esc(title)}<span class="badge badge--soon">coming</span>', ' class="planned"'
            items.append(f'''      <li id="ch{num}"{cls}><span class="cn">{num}</span><div>
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
    done_apps = written_appendices(book)
    apps = "\n".join(
        f'      <li id="app{a}"><span class="cn">{a}</span><div><h3><a href="{done_apps[a]}">{esc(t)}</a></h3><p>{esc(d)}</p></div></li>'
        if a in done_apps else
        f'      <li id="app{a}" class="planned"><span class="cn">{a}</span><div><h3>{esc(t)}<span class="badge badge--soon">coming</span></h3><p>{esc(d)}</p></div></li>'
        for a, t, d in book["appendices"])
    pdf = f'pdf/{book["key"]}-handbook.pdf'
    if done:
        start = (f'<p>Start at <a href="{page_name(book, min(done))}">Chapter {min(done)}</a>, or <a href="all.html">read every '
                 f'written chapter on one page</a> (also as a <a href="{pdf}">PDF</a>). Chapters marked “coming” are planned; '
                 f'the topics they\'ll cover are listed.</p>')
    else:
        nxt = f' The first to be written is <a href="#ch{book["next"]}">Chapter {book["next"]}</a>.' if book.get("next") else ""
        start = (f'<p>This book is being written. No chapters are finished yet; the contents below show every planned '
                 f'chapter and the topics it will cover.{nxt}</p>')
    return "\n".join([
        head(f"{book['title']} · {book['series']}", book["promise"], css_href, 2),
        runhead(book, f"{len(done)} of {n_ch} chapters written", home),
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
{start}
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


def build(out_root=None, css_href=None, home="../../index.html"):
    """Render every handbook; return (books, journals.json entries) for scripts/build_notes.py."""
    books, listing = [], []
    for key in BOOKS:
        book = load_book(key)
        done = written(book)
        out = Path(out_root) / key if out_root else PUBLIC / "handbooks" / key
        out.mkdir(parents=True, exist_ok=True)
        css = css_href or default_css_href(2)
        (out / "index.html").write_text(render_index(book, css, home), encoding="utf-8")
        if done:  # an unstarted book has only its contents page: no whole-book page or PDF yet
            (out / "all.html").write_text(render_all(book, css, home), encoding="utf-8")
        for num in done:
            (out / page_name(book, num)).write_text(render_chapter(book, num, css, home), encoding="utf-8")
        apps = written_appendices(book)
        for letter, fname in apps.items():
            (out / fname).write_text(render_appendix(book, letter, css, home), encoding="utf-8")
        print(f"[handbooks/{key}] index + {len(done)} chapter(s)" + (f" + {len(apps)} appendix(es)" if apps else ""))
        books.append(dict(book, written=done, n_chapters=sum(1 for _ in chapters(book))))
        if not done:
            continue
        base = f"handbooks/{key}"
        listing.append(dict(key=base, title=book["title"], all=f"{base}/all.html", pdf=f"{base}/pdf/{key}-handbook.pdf",
                            notes=[dict(num=n, slug=page_name(book, n)[3:-5], title=next(c[2] for _, c in chapters(book) if c[0] == n),
                                        page=f"{base}/{page_name(book, n)}", pdf=f"{base}/pdf/{page_name(book, n)[:-5]}.pdf")
                                   for n in done]
                                  + [dict(num=a, slug=f[:-5], title=f"Appendix {a}: " + next(t for x, t, _ in book["appendices"] if x == a),
                                          page=f"{base}/{f}", pdf=f"{base}/pdf/{f[:-5]}.pdf")
                                     for a, f in apps.items()]))
    return books, listing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--css-href", help="stylesheet href to use instead of ../../assets/book.css?v=…")
    ap.add_argument("--home", default="../../index.html", help="link for the series name in the running header")
    ap.add_argument("--out", help="output root instead of public/handbooks/")
    args = ap.parse_args()
    build(args.out, args.css_href, args.home)


if __name__ == "__main__":
    sys.exit(main())
