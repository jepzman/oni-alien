#!/usr/bin/env python3
"""Builds Series 3, Jef's Handbooks: long-form books with chapters (see docs/HANDOFF-handbooks.md).

Each book lives in content/handbooks/<key>/:
  - book.py defines BOOK (metadata, parts → chapters, appendices, and which chapters are written)
  - <nn>-<slug>.html is a written chapter's body (plain HTML using the classes in public/assets/book.css)
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
BOOKS = ["cloud-networking", "cloud-identity", "linux"]
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


def link_chapters(html, book):
    done = written(book)

    def repl(m):
        n = int(m.group(1))
        return f'href="{page_name(book, n)}"' if n in done else f'href="index.html#ch{n}"'
    html = re.sub(r'href="#ch(\d+)"', repl, html)
    apps = {a["letter"]: a for a in appendices(book) if a["available"]}

    def arepl(m):
        a = apps.get(m.group(1))
        return f'href="{a["page"]}"' if a else f'href="index.html#app{m.group(1)}"'
    return re.sub(r'href="#app([A-Z])"', arepl, html)


# ---------------------------------------------------------------- appendices
def appendices(book):
    """Each appendix: written by hand (content/…/appendix-<x>-<slug>.html) or generated from the chapters."""
    out = []
    for letter, slug, title, desc in book["appendices"]:
        page = f"appendix-{letter.lower()}-{slug}.html"
        hand = CONTENT / book["key"] / page
        gen = GENERATED.get(slug)
        out.append(dict(letter=letter, slug=slug, title=title, desc=desc, page=page,
                        available=hand.exists() or (gen is not None and bool(written(book))),
                        hand=hand if hand.exists() else None, gen=gen))
    return out


def _strip_tags(html):
    return re.sub(r"<[^>]+>", "", html)


def appendix_opener(letter, title, promise):
    return (f'<header class="opener">\n  <p class="eyebrow">Appendix</p>\n  <p class="chno">{letter}</p>\n'
            f'  <h1>{esc(title)}</h1>\n  <p class="promise">{promise}</p>\n</header>')


def glossary_body(book):
    """Appendix D: every key term from every written chapter, alphabetically, with the chapter it's defined in."""
    seen, rows = set(), []
    for num, f in written(book).items():
        text = (CONTENT / book["key"] / f).read_text(encoding="utf-8")
        for dl in re.findall(r'<dl class="terms">(.*?)</dl>', text, flags=re.S):
            for dt, dd in re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", dl, flags=re.S):
                key = _strip_tags(dt).strip().lower()
                if key in seen:
                    continue
                seen.add(key)
                rows.append((_strip_tags(dt).strip(), dt, dd, num))
    rows.sort(key=lambda r: re.sub(r"[^a-z0-9]", "", r[0].lower()))
    groups = {}
    for plain, dt, dd, num in rows:
        first = plain[0].upper()
        groups.setdefault(first if first.isalpha() else "#", []).append((dt, dd, num))
    parts = [appendix_opener("D", "Glossary", f"All {len(rows)} key terms from the book's chapters, in one place. Each entry links to the chapter that explains it properly.")]
    nav = " · ".join(f'<a href="#gloss-{g}">{g}</a>' for g in groups)
    parts.append(f'<p class="glossary-nav">{nav}</p>')
    for g, items in groups.items():
        lis = "".join(f'<dt>{dt}</dt><dd>{dd} <a class="ref" href="#ch{num}">Ch. {num}</a></dd>' for dt, dd, num in items)
        parts.append(f'<h2 class="sec" id="gloss-{g}"><span class="n"></span>{g}</h2>\n<dl class="terms">{lis}</dl>')
    return "\n".join(parts)


def answers_body(book):
    """Appendix E: every 'check your understanding' question with its answer, chapter by chapter."""
    titles = {c[0]: c[2] for _, c in chapters(book)}
    parts = [appendix_opener("E", "Answers to the exercises", "Every “check your understanding” question in the book, with its worked answer. Try each question in its chapter first; come here to check.")]
    for num, f in written(book).items():
        text = (CONTENT / book["key"] / f).read_text(encoding="utf-8")
        quiz = re.search(r'<ol class="quiz">(.*?)</ol>', text, flags=re.S)
        if not quiz:
            continue
        items = []
        for li in re.findall(r"<li>(.*?)</li>", quiz.group(1), flags=re.S):
            q = re.search(r"<p>(.*?)</p>", li, flags=re.S).group(1)
            q = re.sub(r'\s*<span class="lvl">.*?</span>', "", q)
            a = re.search(r"<details><summary>.*?</summary>(.*?)</details>", li, flags=re.S)
            items.append(f'<li><p class="q">{q}</p>{a.group(1) if a else ""}</li>')
        parts.append(f'<h2 class="sec" id="ans{num}"><span class="n">{num}</span><a href="#ch{num}">{esc(titles[num])}</a></h2>\n'
                     f'<ol class="answers">{"".join(items)}</ol>')
    return "\n".join(parts)


GENERATED = {"glossary": glossary_body, "answers": answers_body}


def appendix_body(book, a):
    if a["hand"]:
        body = a["hand"].read_text(encoding="utf-8")
        body = re.sub(r"^<!--.*?-->\s*", "", body, flags=re.S)
    else:
        body = a["gen"](book)
    return link_chapters(body, book)


def render_appendix(book, a, css_href, home):
    return "\n".join([
        head(f"Appendix {a['letter']}: {a['title']} · {book['title']}", a["desc"], css_href, 2),
        runhead(book, f"Appendix {a['letter']}", home),
        '<main class="page">',
        appendix_body(book, a),
        f'<nav class="next" aria-label="Chapters"><div><span>Contents</span><a href="index.html">{esc(book["title"])}</a></div></nav>',
        '</main>',
        colophon(book),
        '</body>', '</html>', ''])


def chapter_body(book, num):
    body = (CONTENT / book["key"] / written(book)[num]).read_text(encoding="utf-8")
    body = re.sub(r"^<!--.*?-->\s*", "", body, flags=re.S)
    return link_chapters(body, book)


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
        body = re.sub(r'href="(\d\d-[a-z0-9-]+)\.html"', r'href="#chapter-\1"', body)
        body = re.sub(r'href="(appendix-[a-z]-[a-z0-9-]+)\.html"', r'href="#\1"', body)
        body = re.sub(r'<nav class="next".*?</nav>', "", body, flags=re.S)
        arts.append(f'<article class="sheet chapter" id="chapter-{page_name(book, num)[:-5]}">\n{body}\n</article>')
    for a in appendices(book):
        if a["available"]:
            body = appendix_body(book, a)
            body = re.sub(r'href="(\d\d-[a-z0-9-]+)\.html"', r'href="#chapter-\1"', body)
            body = re.sub(r'href="(appendix-[a-z]-[a-z0-9-]+)\.html"', r'href="#\1"', body)
            arts.append(f'<article class="sheet chapter" id="{a["page"][:-5]}">\n{body}\n</article>')
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


def start_html(book, done, complete, pdf):
    """The 'where to start' line of a contents page; an unstarted book (no chapter written yet) says so instead."""
    if not done:
        nxt = f' The first to be written is <a href="#ch{book["next"]}">Chapter {book["next"]}</a>.' if book.get("next") else ""
        return (f'<p>This book is being written. No chapters are finished yet; the contents below show every planned '
                f'chapter and the topics it will cover.{nxt}</p>')
    return (f'<p>Start at <a href="{page_name(book, min(done))}">Chapter {min(done)}</a>, or <a href="all.html">read '
            f'{"the whole book" if complete else "every written chapter"} on one page</a> (also as a <a href="{pdf}">PDF</a>).'
            f'{"" if complete else " Chapters marked “coming” are planned; the topics they will cover are listed."}</p>')


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
    apps = "\n".join(
        (f'      <li id="app{a["letter"]}"><span class="cn">{a["letter"]}</span><div><h3><a href="{a["page"]}">{esc(a["title"])}</a></h3><p>{esc(a["desc"])}</p></div></li>'
         if a["available"] else
         f'      <li id="app{a["letter"]}" class="planned"><span class="cn">{a["letter"]}</span><div><h3>{esc(a["title"])}<span class="badge badge--soon">coming</span></h3><p>{esc(a["desc"])}</p></div></li>')
        for a in appendices(book))
    n_apps = sum(1 for a in appendices(book) if a["available"])
    complete = len(done) == n_ch and n_apps == len(book["appendices"])
    pdf = f'pdf/{book["key"]}-handbook.pdf'
    return "\n".join([
        head(f"{book['title']} · {book['series']}", book["promise"], css_href, 2),
        runhead(book, f"{n_ch} chapters · {n_apps} appendices" if complete else f"{len(done)} of {n_ch} chapters written", home),
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
{start_html(book, done, complete, pdf)}
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
        if done:  # an unstarted book has only its contents page: no whole-book page, PDF or journals entry yet
            (out / "all.html").write_text(render_all(book, css, home), encoding="utf-8")
        for num in done:
            (out / page_name(book, num)).write_text(render_chapter(book, num, css, home), encoding="utf-8")
        apps = [a for a in appendices(book) if a["available"]]
        for a in apps:
            (out / a["page"]).write_text(render_appendix(book, a, css, home), encoding="utf-8")
        print(f"[handbooks/{key}] index + {len(done)} chapter(s) + {len(apps)} appendices")
        books.append(dict(book, written=done, n_chapters=sum(1 for _ in chapters(book))))
        if not done:
            continue
        base = f"handbooks/{key}"
        listing.append(dict(key=base, title=book["title"], all=f"{base}/all.html", pdf=f"{base}/pdf/{key}-handbook.pdf",
                            notes=[dict(num=n, slug=page_name(book, n)[3:-5], title=next(c[2] for _, c in chapters(book) if c[0] == n),
                                        page=f"{base}/{page_name(book, n)}", pdf=f"{base}/pdf/{page_name(book, n)[:-5]}.pdf")
                                   for n in done]
                                  + [dict(num=100 + i, slug=a["page"][:-5], title=f"Appendix {a['letter']}: {a['title']}",
                                          page=f"{base}/{a['page']}", pdf=f"{base}/pdf/{a['page'][:-5]}.pdf")
                                     for i, a in enumerate(apps)]))
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
