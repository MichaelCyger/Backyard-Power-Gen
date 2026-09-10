#!/usr/bin/env python3
"""Compile chapters 1-9 into Backyard-{VERSION}.pdf."""

import re
from pathlib import Path

import markdown
from weasyprint import CSS as WpCSS
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
VERSION = "1.1"
DATE = "9 September 2026"
AUTHOR = "Michael Cyger"
EMAIL = "michael@cyger.org"
OUTPUT = ROOT / f"Backyard-{VERSION}.pdf"

CHAPTERS = [
    ("1_The-Need.md", "1. The Need"),
    ("2_The-Idea.md", "2. The Idea"),
    ("3_Yard-Safety.md", "3. Yard Safety"),
    ("4_The-House.md", "4. The House"),
    ("5_The-Vault.md", "5. The Vault"),
    ("6_The-Approval.md", "6. The Approval"),
    ("7_The-Swap.md", "7. The Swap"),
    ("8_Vault-Spec.md", "8. Vault Spec"),
    ("9_The-Fuel.md", "9. The Fuel"),
]

CSS = """
@page {
  size: letter;
  margin: 0.85in 0.9in 1.15in 0.9in;
  @top-center {
    content: "Backyard Generating Station  ·  Confidential";
    font-family: Inter, "Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 10pt;
    color: #555;
    letter-spacing: 0.02em;
  }
  @bottom-left {
    content: "Confidential. Not for distribution.  ·  Version """ + VERSION + """  ·  """ + DATE + """  ·  """ + AUTHOR + """";
    font-family: Inter, "Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 8.5pt;
    color: #444;
  }
  @bottom-right {
    content: counter(page);
    font-family: Inter, "Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 11pt;
    color: #333;
  }
}

@page :first {
  margin: 1.4in 1.1in 1.2in 1.1in;
  @top-center { content: none; }
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}

html {
  font-family: Inter, "Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 15pt;
  line-height: 1.5;
  color: #1a1a1a;
  hyphens: none;
}

body {
  margin: 0;
}

.title-page {
  page-break-after: always;
  padding-top: 1.6in;
}

.title-page h1 {
  font-size: 28pt;
  line-height: 1.15;
  font-weight: 700;
  margin: 0 0 0.35em;
  page-break-before: auto;
  border: none;
  padding: 0;
  white-space: nowrap;
}

.title-kicker {
  font-size: 13pt;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #8a2020;
  margin: 0 0 1.1em;
  font-weight: 650;
}

.title-meta {
  font-size: 16pt;
  color: #333;
  margin: 0.25em 0;
}

.title-note {
  margin-top: 2.2em;
  margin-bottom: 0;
  font-size: 14pt;
  max-width: 28em;
  color: #333;
}

.title-author {
  margin-top: 2.2em;
}

.toc {
  page-break-after: always;
}

.toc h1 {
  page-break-before: auto;
}

.toc ol {
  font-size: 16pt;
  line-height: 1.7;
  padding-left: 1.4em;
}

.toc a {
  color: #1a1a1a;
  text-decoration: none;
}

h1 {
  font-size: 24pt;
  line-height: 1.2;
  font-weight: 700;
  margin: 0 0 0.7em;
  padding-top: 0.15em;
  border-bottom: 1.5px solid #ccc;
  padding-bottom: 0.25em;
  page-break-before: always;
  page-break-after: avoid;
}

h2 {
  font-size: 18pt;
  line-height: 1.25;
  font-weight: 650;
  margin: 1.35em 0 0.45em;
  page-break-after: avoid;
  break-after: avoid;
}

h3 {
  font-size: 16pt;
  line-height: 1.3;
  font-weight: 650;
  margin: 1.15em 0 0.35em;
  page-break-after: avoid;
  break-after: avoid;
}

h2 + table, h3 + table, h2 + pre, h3 + pre, h2 + p, h3 + p {
  page-break-before: avoid;
  break-before: avoid;
}

p, li {
  orphans: 3;
  widows: 3;
}

p {
  margin: 0 0 0.75em;
}

ul, ol {
  margin: 0 0 0.85em;
  padding-left: 1.3em;
}

li {
  margin: 0.2em 0;
  page-break-inside: avoid;
  break-inside: avoid;
}

strong {
  font-weight: 650;
}

a {
  color: #0b4f8a;
  text-decoration: underline;
  text-underline-offset: 0.12em;
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 1.4em 0;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 1em 0 1.2em;
  page-break-inside: avoid;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12pt;
  line-height: 1.35;
  margin: 0.9em 0 1.2em;
}

table.captioned, table.wide {
  page-break-inside: avoid;
  break-inside: avoid;
}

table.wide {
  font-size: 10pt;
  line-height: 1.22;
}

table.wide th, table.wide td {
  padding: 0.22em 0.32em;
}

tr.caption-row th {
  border: none;
  background: transparent;
  font-weight: 650;
  padding: 0 0 0.4em;
}

thead {
  display: table-header-group;
}

tr {
  page-break-inside: avoid;
  break-inside: avoid;
}

th, td {
  border: 1px solid #bbb;
  padding: 0.4em 0.5em;
  vertical-align: top;
  text-align: left;
}

th {
  background: #f0f0ee;
  font-weight: 650;
}

pre, code {
  font-family: "SF Mono", Menlo, Consolas, monospace;
}

code {
  font-size: 12.5pt;
}

pre {
  font-size: 11.5pt;
  line-height: 1.4;
  background: #f4f4f2;
  border: 1px solid #ddd;
  padding: 0.75em 0.85em;
  white-space: pre-wrap;
  word-wrap: break-word;
  margin: 0.8em 0 1.1em;
  page-break-inside: avoid;
}

blockquote {
  margin: 0.8em 0 1.1em;
  padding: 0.1em 0 0.1em 0.9em;
  border-left: 3px solid #999;
  color: #222;
}

.keep {
  page-break-inside: avoid;
  break-inside: avoid;
}
"""


# Match one element only. A DOTALL (p).*?(p) still backtracks across
# later paragraphs until it finds a table, which wrapped half a chapter.
_P = r"<p>(?:(?!</p>).)*</p>"
_H = r"<h[23][^>]*>(?:(?!</h[23]>).)*</h[23]>"
_TABLE = r"<table(?:(?!</table>).)*</table>"
_PRE = r"<pre(?:(?!</pre>).)*</pre>"


def _plain(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html).strip()


def _p_inner(p_html: str) -> str:
    return re.sub(r"^<p>|</p>$", "", p_html, flags=re.DOTALL).strip()


def _table_cols(table: str) -> int:
    head = table.split("</tr>", 1)[0]
    return head.count("<th>") + head.count("<td>")


def keep_together(html: str) -> str:
    """Glue captions, headings, and intro lines to the table or pre they introduce."""

    def _caption(match: re.Match) -> str:
        p, table = match.group(1), match.group(2)
        inner = _p_inner(p)
        text = _plain(inner)
        bold = bool(re.fullmatch(r"<strong>.*</strong>\s*", inner, flags=re.DOTALL))
        if len(text) <= 140 or (bold and len(text) <= 220):
            cols = _table_cols(table)
            kind = "wide" if cols >= 4 else "captioned"
            table = table.replace("<table", f'<table class="{kind}"', 1)
            row = f'<tr class="caption-row"><th colspan="{cols}">{inner}</th></tr>'
            if "<thead>" in table:
                table = table.replace("<thead>", f"<thead>{row}", 1)
            else:
                table = table.replace(
                    f'<table class="{kind}">',
                    f'<table class="{kind}"><thead>{row}</thead>',
                    1,
                )
            return table
        return match.group(0)

    html = re.sub(rf"({_P})\s*({_TABLE})", _caption, html, flags=re.DOTALL)

    def _wrap(match: re.Match) -> str:
        return f'<div class="keep">{match.group(0)}</div>'

    html = re.sub(rf"({_H})\s*({_TABLE})", _wrap, html, flags=re.DOTALL)

    def _wrap_intro(match: re.Match) -> str:
        p, table = match.group(1), match.group(2)
        if len(_plain(p)) <= 420:
            return f'<div class="keep">{p}{table}</div>'
        return p + table

    html = re.sub(rf"({_P})\s*({_TABLE})", _wrap_intro, html, flags=re.DOTALL)
    html = re.sub(rf"({_P})\s*({_PRE})", _wrap, html, flags=re.DOTALL)
    html = re.sub(
        rf"(<h2>[^<]*What this chapter covered</h2>(?:\s*{_P})+)",
        r'<div class="keep">\1</div>',
        html,
    )
    html = html.replace("take-back", "take\u2011back")
    return html


def rewrite_heading(text: str, title: str) -> str:
    lines = text.splitlines()
    if not lines:
        return f"# {title}\n"
    if lines[0].startswith("# "):
        lines[0] = f"# {title}"
    # Chapter 2 opens with a duplicate "The idea" heading.
    if title.endswith("The Idea") and len(lines) > 2 and lines[2].strip().lower() == "## the idea":
        del lines[2]
        if len(lines) > 2 and lines[2] == "":
            del lines[2]
    return "\n".join(lines)


def main() -> None:
    parts = [
        '<div class="title-page">',
        '<p class="title-kicker">Confidential. Not for distribution.</p>',
        "<h1>Backyard Generating Station</h1>",
        '<p class="title-meta">Version {0}</p>'.format(VERSION),
        '<p class="title-meta">{0}</p>'.format(DATE),
        (
            '<p class="title-note">One house. One backyard generating station. '
            "Electricity and heat, day and night, for 100 years.</p>"
        ),
        '<p class="title-meta title-author">{0}</p>'.format(AUTHOR),
        '<p class="title-meta">{0}</p>'.format(EMAIL),
        "</div>",
        '<div class="toc"><h1>Contents</h1><ol>',
    ]
    for i, (_, title) in enumerate(CHAPTERS, start=1):
        parts.append(f'<li><a href="#chapter-{i}">{title.split(". ", 1)[1]}</a></li>')
    parts.append("</ol></div>")

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "smarty"]
    )
    for i, (filename, title) in enumerate(CHAPTERS, start=1):
        raw = (ROOT / filename).read_text(encoding="utf-8")
        raw = rewrite_heading(raw, title)
        html = keep_together(md.convert(raw))
        md.reset()
        parts.append(f'<section id="chapter-{i}">{html}</section>')

    document = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>"
        + "\n".join(parts)
        + "</body></html>"
    )
    HTML(string=document, base_url=str(ROOT)).write_pdf(
        OUTPUT, stylesheets=[WpCSS(string=CSS)]
    )
    stale = ROOT / "Backyard.pdf"
    if stale.exists():
        stale.unlink()
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
