#!/usr/bin/env python3
"""Arma index.html (sistema de diseño del SDK, un solo archivo) desde el paquete FID SDK - Assets.
Uso: python3 build.py [ruta/al/paquete FID SDK - Assets]
"""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent.parent / 'FID SDK - Assets'
OUT = HERE.parent / 'index.html'

LINKS = {
    'LINK_FIGMA_DOCS': 'https://www.figma.com/design/o5RhfPgp35VOEXuybrIL9W/FID-SDK-%E2%80%94-Variables--dev---refactor-?node-id=51-2936',
    'LINK_FIGMA_HANDOFF': 'https://www.figma.com/design/HhP97fjZ3FT8xG1AG411Qj/-Handoff--Portal-Integradores?node-id=847-26060',
    'LINK_DRIVE': 'https://drive.google.com/drive/folders/1ErW-_ImyoMbPjmgqAmvuWtwEqSEJ39Cj',
}

read = lambda p: Path(p).read_text(encoding='utf-8')

# ── Pantallas del SDK con sus tokens (ver pantallas_tokens.py); se arma después de leer tokens.json ──
sys.path.insert(0, str(HERE))
from pantallas_tokens import KEYS, FLOW_PAGES, ESTADOS
md = read(PKG / 'DESIGN.md')
tokens = json.loads(read(PKG / 'tokens.json'))


def tk_val(name, d=None):
    d = tokens if d is None else d
    if isinstance(d, dict):
        if name in d and not isinstance(d[name], dict):
            return str(d[name])
        if name in d and isinstance(d[name], dict) and 'value' in d[name]:
            return str(d[name]['value'])
        for v in d.values():
            r = tk_val(name, v)
            if r:
                return r
    return ''


def tk_corto(name):
    v = tk_val(name)
    return v.split(',')[0].strip().strip("'\"") if ',' in v else v


PANT_SCREENS = json.loads(read(HERE / 'pantallas.json'))


def pant_label(s):
    keys = {k for k, _ in s['spots']}
    base = s['title'] or re.sub(r'^\d+\s*·\s*', '', s['name']) or s['path'].split(' / ')[-1]
    est = next((t for k, t in ESTADOS if k in keys), '') if s['title'] else ''
    return base + (' · ' + est if est else '')


PANT = {}
for pid, flow in FLOW_PAGES:
    lst = []
    for s in [x for x in PANT_SCREENS if x['flow'] == flow]:
        spots = []
        for n, (k, rects) in enumerate(s['spots'], 1):
            nombre, toks, marca, nota = KEYS[k]
            spots.append({'n': n, 'l': nombre, 't': [[t, tk_corto(t)] for t in toks], 'm': marca, 'd': nota, 'big': rects[0][2] >= 504,
                          'r': [[round(x / 840 * 100, 3), round(y / s['h'] * 100, 3), round(w / 840 * 100, 3), round(max(h, 2) / s['h'] * 100, 3)] for x, y, w, h in rects]})
        lst.append({'id': s['id'], 'f': 'pantallas/%s.png' % s['id'].replace(':', '-'), 'h': s['h'], 'sec': s['path'], 'l': pant_label(s), 'spots': spots})
    vistos = {}
    for x in lst:
        vistos[x['l']] = vistos.get(x['l'], 0) + 1
        if vistos[x['l']] > 1:
            x['l'] += ' (%d)' % vistos[x['l']]
    PANT[pid] = lst


def flow_page(pid, flow):
    e = lambda t: html.escape(str(t))
    lst = PANT[pid]
    groups = []
    for i, s in enumerate(lst):
        if not groups or groups[-1][0] != s['sec']:
            groups.append((s['sec'], []))
        groups[-1][1].append((i, s))
    opts = ''.join('<optgroup label="%s">%s</optgroup>' % (e(g), ''.join('<option value="%d">%s</option>' % (i, e(s['l'])) for i, s in items)) for g, items in groups)
    thumbs = ''.join('<button type="button" data-i="%d"><span class="im"><img loading="lazy" src="%s" width="840" height="%d" alt=""></span><span class="cap"><b>%s</b><small>%s</small></span></button>' % (i, s['f'], s['h'], e(s['l']), e(s['sec'])) for i, s in enumerate(lst))
    n = len(lst)
    return ('<section class="page" id="pg-%s" data-title="%s" data-g="Tokens en las pantallas" data-desc="%s" hidden>\n <div class="panel" data-tab="resumen" data-label="Resumen">\n'
            '<p>Las pantallas de desktop del flujo, exportadas de Figma (archivo “FID SDK — Variables”, página Flujo) sin el header, que lo pone el integrador. Elegí una pantalla y pasá el mouse por cada parte para ver qué token la pinta. Los tokens son los del paquete (<code>DESIGN.md</code>), que es lo que tenés que usar en código.</p>\n'
            '<div class="note"><b>Los componentes de Figma todavía usan variables viejas</b>En Figma, estas pantallas siguen vinculadas a variables de la librería anterior (por ejemplo <code>Primitves/brand/700 main</code>). Para código, usá los tokens que se ven acá.</div>\n'
            '<h2 id="%s-visor">Pantalla</h2>\n<div class="pviewer" data-p="%s"><div class="pvbar"><div class="ctrl"><label for="%s-sel">Pantalla</label><select id="%s-sel">%s</select></div><div class="pvnav"><button type="button" data-d="-1">Anterior</button><span class="pvcount"></span><button type="button" data-d="1">Siguiente</button></div></div>'
            '<p class="pvsec small muted"></p><div class="ptwrap"><div class="ptimg"><img alt="" src="%s" width="840" height="%d"></div><ol class="ptlist"></ol></div></div>\n'
            '<h2 id="%s-todas">Todas las pantallas</h2>\n<div class="pthumbs">%s</div>\n </div>\n</section>\n') % (
        pid, e(flow), e('%d %s del flujo, exportadas de Figma, con el token que se aplica en cada parte.' % (n, 'pantalla' if n == 1 else 'pantallas')),
        pid, pid, pid, pid, opts, lst[0]['f'], lst[0]['h'], pid, thumbs)


FIG_HTML = ''.join(flow_page(pid, flow) for pid, flow in FLOW_PAGES)


def section(title_start, until=None):
    i = md.index(title_start)
    j = md.index(until, i + 1) if until else len(md)
    return md[i:j]


def code_blocks(text, lang):
    return re.findall(r'```' + lang + r'\n(.*?)```', text, re.S)


def hl(code):
    out = html.escape(code, quote=False)
    out = re.sub(r'(/\*.*?\*/)', r'<span class="tk-c">\1</span>', out, flags=re.S)
    out = re.sub(r'(?m)(^|\s)(//.*)$', r'\1<span class="tk-c">\2</span>', out)
    out = re.sub(r'(&lt;!--.*?--&gt;)', r'<span class="tk-c">\1</span>', out, flags=re.S)
    return out.rstrip('\n')


def inline_md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)


uso = {}
for line in section('## 5 · Catálogo', '## 6 ·').splitlines():
    m = re.match(r'\|\s*`(--[a-z0-9-]+)`\s*\|(.*)\|\s*$', line)
    if m:
        cells = [c.strip() for c in m.group(2).split('|')]
        if cells and cells[-1] and cells[-1] not in ('sí', 'no', '**sí**'):
            uso[m.group(1)] = cells[-1].replace('`', '')

STATE_ES = {'error': 'error', 'success': 'éxito', 'warning': 'advertencia', 'info': 'información'}
PART_ES = {'bg': 'fondo', 'border': 'borde', 'text': 'texto', 'icon': 'ícono', 'surface': 'superficie'}
BTN_ES = {'primary': 'primario', 'secondary': 'secundario', 'tertiary': 'terciario', 'danger': 'de peligro', 'disabled': 'deshabilitado'}


def make_uso(name):
    if name in uso:
        return uso[name]
    m = re.match(r'--feedback-(\w+)-(\w+)', name)
    if m:
        return f'Estado de {STATE_ES.get(m.group(1), m.group(1))}: {PART_ES.get(m.group(2), m.group(2))}'
    m = re.match(r'--button-(\w+)-(.+)', name)
    if m:
        part = m.group(2).replace('bg-hover', 'fondo en hover').replace('-hover', ' en hover').replace('bg', 'fondo').replace('border', 'borde').replace('text', 'texto')
        return f'Botón {BTN_ES.get(m.group(1), m.group(1))}: {part}'
    m = re.match(r'--accent-(\d+)', name)
    if m:
        return f'Escala de marca, paso {m.group(1)}'
    return ''


semantic = []
for name, t in tokens['semantic'].items():
    ref = t.get('ref') or ''
    brand = ('accent-' in ref) or name.startswith('--accent-') or name == '--button-primary-text'
    semantic.append({'name': name, 'value': t['value'], 'ref': ref, 'uso': make_uso(name), 'brand': brand})

text_styles = []
for line in section('Estilos de texto, de mayor', '## 6 ·').splitlines():
    m = re.match(r'\|\s*`(text/[^`]+)`\s*\|\s*([\d]+\s*/\s*[\d]+)\s*\|\s*(.+?)\s*\|', line)
    if m:
        text_styles.append({'name': m.group(1), 'px': m.group(2), 'peso': m.group(3)})

checklist = [inline_md(l[6:].strip()) for l in section('## 10 ·').splitlines() if l.startswith('- [ ] ')]
rules = [inline_md(re.sub(r' \(sección 4\)', '', re.sub(r'^\d+\.\s*', '', l.strip())).replace('en los casos de la tabla de la sección 5', 'en los casos del catálogo de tokens')) for l in section('## 2 ·', '## 3 ·').splitlines() if re.match(r'^\d+\.\s', l.strip())]

apply_js = code_blocks(section('## 4 ·', '## 5 ·'), 'js')[0]
apply_only = 'var RADII' + apply_js.split('var RADII', 1)[1]
apply_only = apply_only.split('function luminance')[0] + 'function applyBranding' + apply_only.split('function applyBranding', 1)[1]
a11y_js = apply_js.split('function applyBranding')[0].strip()
a11y_js = 'function luminance' + a11y_js.split('function luminance', 1)[1]
recetas = code_blocks(section('## 6 ·', '## 7 ·'), 'css')[0]


def cut(a, b=None):
    i = recetas.index(a)
    j = recetas.index(b) if b else len(recetas)
    return recetas[i:j].strip('\n')


accent_css = read(PKG / 'css/accent-from-primary.css')
accent_css = accent_css[accent_css.index('.sdk-frame {'):]
icons_css = read(PKG / 'css/icons.css').split('*/', 1)[1].strip()
tint_js = read(PKG / 'js/tint-lottie.js')
tint_js = tint_js[tint_js.index('function lottiePrimaryClass'):]

package_css = '\n'.join(read(PKG / 'css' / f) for f in ('tokens.css', 'accent-from-primary.css', 'illustrations.css', 'icons.css'))
svgs = {n: read(PKG / 'illustrations' / f'{n}.svg') for n in ('ill-onboarding', 'ill-sms', 'ill-email', 'error-x')}
lotties = {n: json.loads(read(PKG / 'lottie' / f'{n}.json')) for n in ('face-scan', 'card-skeleton', 'verification', 'success-check')}
logo = read(PKG / 'fixed/logo-fid.svg').strip()
logo_sm = re.sub(r'width="46" height="32"', 'width="22" height="15"', logo, count=1)
sample_json = json.dumps({'--button-primary-bg': tokens['semantic']['--button-primary-bg']}, ensure_ascii=False, indent=2)


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


repl = {
    'PACKAGE_CSS': package_css,
    'LOGO_FID': logo,
    'CODE_APPLY': hl(apply_only),
    'CODE_A11Y': hl(a11y_js),
    'CODE_ACCENT': hl(accent_css),
    'CODE_JSON': hl(sample_json),
    'CODE_BTN': hl(cut('.sdk-btn {', '.sdk-checkbox')),
    'CODE_CTRL': hl(cut('.sdk-checkbox', '.sdk-link')),
    'CODE_MISC': hl(cut('.sdk-link')),
    'CODE_ICONS': hl(icons_css),
    'CODE_TINT': hl(tint_js),
    'LOTTIE_LIB': read(HERE / 'lottie.min.js').replace('</script', '<\\/script'),
    'DATA_JSON': js({
        'semantic': semantic,
        'primitive': {k: v['value'] for k, v in tokens['primitive'].items()},
        'size': {k: v['value'] for k, v in tokens['size'].items()},
        'textStyles': text_styles, 'checklist': checklist, 'rules': rules,
        'svgs': svgs, 'logo': logo_sm, 'pant': PANT,
    }),
    'LOTTIES_JSON': js(lotties),
    'FIGMA_PAGES': FIG_HTML,
    **LINKS,
}

out = read(HERE / 'plantilla.html')
for k in sorted(repl, key=len, reverse=True):
    out = out.replace('{{' + k + '}}', repl[k])
left = re.findall(r'\{\{[A-Z_]+\}\}', out)
assert not left, left
OUT.write_text(out, encoding='utf-8')
print(f'OK → {OUT}  ({OUT.stat().st_size / 1024:.0f} KB) · semánticos {len(semantic)} · estilos de texto {len(text_styles)} · reglas {len(rules)} · checklist {len(checklist)}')
