#!/usr/bin/env python3
"""Close a copied Six7 manual page with the collaboration credits, as six7.work does.

Usage: python3 tools/credits.py <page.html> ...

The public edition adds the credits here; the app repositories' manuals are not changed.
Each page gets "A collaboration we like.", the Claude, Omarchy and Entangled Forge logos
(linked, hearts between them) and a link to six7.work, after its main column. The logos
are embedded as data: addresses, so the page still opens offline. A page that already has
the credits, or whose layout isn't the one the Six7 manual builder writes, stops the run.
"""
import base64
import html
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGOS = [  # file in assets/credits/, name, link, width in pixels
    ('claude.webp', 'Claude', 'https://www.anthropic.com/claude', 140),
    ('omarchy.svg', 'Omarchy', 'https://omarchy.org/', 120),
    ('entangled-forge.webp', 'Entangled Forge', 'https://www.entangledforge.com/en/perspectives/both-and/', 64),
]
TITLE = 'A collaboration we like.'
TEXT = 'Great tools, good people, and a practical way to build.'
SITE = ('https://six7.work/', 'Six7 · six7.work')
MIME = {'.webp': 'image/webp', '.svg': 'image/svg+xml', '.png': 'image/png'}

STYLE = """
/* Six7 public edition: the collaboration credits that close every page. */
.credits { border-top: 1px solid var(--line); margin-top: 48px; background: var(--paper); }
.credits .wrap { padding-top: 32px; padding-bottom: 40px; }
.credits-title { margin: 0; font: 400 28px/1.15 var(--font-title); letter-spacing: -.01em; color: var(--ink); }
.credits-text { margin: 8px 0 0; color: var(--ink-2); }
.credits-logos { display: flex; align-items: center; gap: 14px; margin: 22px 0 0; }
.credits-logos .credit { display: inline-flex; align-items: center; flex: 0 1 auto; min-width: 0; }
.credits-logos img { display: block; border: 0; border-radius: 0; height: auto; max-width: 100%; }
.credits-logos .heart { flex: none; color: #d92926; font-size: 18px; line-height: 1; }
.credits-site { margin: 22px 0 0; font-weight: 600; }
.credits-site a { color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--ink-3); padding-bottom: 2px; }
.credits-site a:hover { border-bottom-color: var(--ink); }
@media (max-width: 480px) { .credits-logos { gap: 8px; } .credits-logos .heart { font-size: 14px; } }
"""

ANCHOR = '</main></div>'  # where the builder closes the main column, once per language


def footer():
    imgs = []
    for name, alt, href, width in LOGOS:
        f = ROOT / 'assets' / 'credits' / name
        uri = 'data:' + MIME[f.suffix] + ';base64,' + base64.b64encode(f.read_bytes()).decode('ascii')
        imgs.append(f'<a class="credit" href="{html.escape(href)}" target="_blank" rel="noopener noreferrer">'
                    f'<img src="{uri}" alt="{html.escape(alt)}" width="{width}"></a>')
    logos = '<span class="heart" aria-hidden="true">♥</span>'.join(imgs)
    return ('\n<footer class="credits"><div class="wrap">'
            f'<p class="credits-title">{html.escape(TITLE)}</p><p class="credits-text">{html.escape(TEXT)}</p>'
            f'<p class="credits-logos">{logos}</p>'
            f'<p class="credits-site"><a href="{html.escape(SITE[0])}" target="_blank" rel="noopener noreferrer">'
            f'{html.escape(SITE[1])} <span aria-hidden="true">↗</span></a></p>'
            '</div></footer>')


def main(pages):
    block = footer()
    for p in map(pathlib.Path, pages):
        t = p.read_text(encoding='utf-8')
        if 'class="credits"' in t:
            sys.exit(f'{p.name}: already has the credits')
        if t.count('</style>') < 1 or t.count(ANCHOR) < 1:
            sys.exit(f'{p.name}: not the layout the Six7 manual builder writes ({ANCHOR!r} or </style> missing)')
        t = t.replace('</style>', STYLE + '</style>', 1).replace(ANCHOR, ANCHOR + block)
        p.write_text(t, encoding='utf-8')
        print(f'credits added: {p.name}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
