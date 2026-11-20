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
from pantallas_tokens import KEYS, FLOW_PAGES, ESTADOS, MEDIDA, RADIO_BOTON, CON_ARO, SIN_RADIO
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


CLIENTE_FIJOS = {'--radius-button', '--font-family-default', '--button-primary-text'}


def es_cliente(tok):
    if tok in CLIENTE_FIJOS or tok.startswith('--accent') or tok.startswith(('.ill-primary', '.lt-primary')):
        return True
    ref = tokens['semantic'].get(tok, {}).get('ref', '')
    return ref.startswith('--accent')


def estilo_texto(medida):
    """'24/32/600' o '14/20/600/u' → (nombre del estilo del paquete o '', texto del valor)."""
    p = medida.split('/')
    fs, lh, w, u = int(p[0]), p[1], int(p[2]), len(p) > 3
    valor = '%d / %s · %d%s' % (fs, lh if lh != 'A' else 'auto', w, ' · subrayado' if u else '')
    for st in text_styles:
        sz, sl = [int(x) for x in st['px'].replace(' ', '').split('/')]
        sw = int(re.match(r'\d+', st['peso']).group())
        su = 'subrayado' in st['peso']
        if sz == fs and sw == w and su == u and (lh == 'A' or int(lh) == sl):
            return st['name'], valor
    return '', valor


RADIOS = [('--radius-sm', 4), ('--radius-md', 8), ('--radius-lg', 12)]


def radio(k, medidas):
    if k in RADIO_BOTON:
        figma = ' · en Figma: %s px' % medidas[0].split('/')[0] if medidas else ''
        return ['Radio', '--radius-button', tk_corto('--radius-button') + figma, True]
    if k in SIN_RADIO or not medidas:
        return None
    r, h = [int(x) for x in medidas[0].split('/')]
    if k in CON_ARO:
        r, h = r - 3, h - 6
    if r * 2 >= h:
        return ['Radio', '--radius-full', tk_corto('--radius-full'), False]
    for tok, v in RADIOS:
        if v == r:
            return ['Radio', tok, tk_corto(tok), False]
    return ['Radio', '', 'Sin token en el paquete · en Figma: %d px' % r, False]


def filas(k, med):
    nombre, base, nota = KEYS[k]
    rows = [[rol, tok, tk_corto(tok), es_cliente(tok)] for rol, tok in base]
    estilos = sorted(med[0], key=lambda m: (-int(m.split('/')[0]), m)) if med else []
    for n, m in enumerate(estilos):
        nm, val = estilo_texto(m)
        rol = 'Tipografía'
        if k == 'tt' and len(estilos) >= 2:
            rol = 'Tipografía del título' if n == 0 else 'Tipografía de la descripción' if n == 1 else 'Tipografía (destacado)'
        rows.append([rol, nm, val if nm else 'Sin estilo en el paquete · ' + val, False])
    if estilos:
        rows.append(['Fuente', '--font-family-default', tk_corto('--font-family-default'), True])
    rr = radio(k, med[1] if med else [])
    if rr and not any(r[0] == 'Radio' for r in rows):
        rows.append(rr)
    return nombre, nota, rows


def variacion(s, grupo, med):
    keys = {k for k, _ in s['spots']}
    for k, t in ESTADOS:
        if k in keys:
            return t
    if not s['title'] and s['name']:
        return re.sub(r'^\d+\s*·\s*', '', s['name'])
    otros = [x for x in grupo if x is not s]
    if 'bp' in keys and any('bp' not in {k for k, _ in x['spots']} for x in otros):
        return 'Completo'
    if 'oc' in keys and med.get('oc', [[]])[0]:
        return 'Código ingresado'
    if 'pc' in keys and '16/24/400' in med.get('pc', [[]])[0]:
        return 'Con clave ingresada'
    return 'Inicial'


def pantallas_build():
    screens = json.loads(read(HERE / 'pantallas.json'))
    medidas = json.loads(read(HERE / 'pantallas_medidas.json'))
    e = lambda t: html.escape(str(t))
    pant, pages = {}, []
    for pid, flow in FLOW_PAGES:
        grupos = []
        for s in [x for x in screens if x['flow'] == flow]:
            titulo = s['title'] or s['path'].split(' / ')[-1]
            sec = re.sub(r' / Error$', '', s['path'])
            ilu = any(k == 'il' for k, _ in s['spots'])
            g = next((g for g in grupos if g['t'] == titulo and g['sec'] == sec and g['il'] == ilu), None)
            if not g:
                g = {'t': titulo, 'sec': sec, 'il': ilu, 'v': []}
                grupos.append(g)
            g['v'].append(s)
        data = []
        for g in grupos:
            vs, vistos = [], {}
            for s in g['v']:
                med = medidas.get(s['id'], {})
                lab = variacion(s, g['v'], med)
                vistos[lab] = vistos.get(lab, 0) + 1
                if vistos[lab] > 1:
                    lab = 'Otra versión' if vistos[lab] == 2 else 'Otra versión (%d)' % (vistos[lab] - 1)
                spots = []
                for n, (k, rects) in enumerate(s['spots'], 1):
                    nombre, nota, rows = filas(k, med.get(MEDIDA.get(k, k)))
                    spots.append({'n': n, 'l': nombre, 'd': nota, 'rows': rows, 'big': rects[0][2] >= 504,
                                  'r': [[round(x / 840 * 100, 3), round(y / s['h'] * 100, 3), round(w / 840 * 100, 3), round(max(h, 2) / s['h'] * 100, 3)] for x, y, w, h in rects]})
                vs.append({'l': lab, 'f': 'pantallas/%s.png' % s['id'].replace(':', '-'), 'h': s['h'], 'spots': spots})
            iguales = [x for x in grupos if x['t'] == g['t']]
            t = g['t'] if len(iguales) == 1 else '%s (%s)' % (g['t'], 'con ilustración' if g['il'] else 'sin ilustración') if len({x['il'] for x in iguales}) > 1 and len({x['sec'] for x in iguales}) == 1 else g['t']
            data.append({'t': t, 'sec': g['sec'], 'v': vs})
        pant[pid] = data
        n = sum(len(g['v']) for g in data)
        h = ['<section class="page" id="pg-%s" data-title="%s" data-g="Tokens en las pantallas" data-desc="%s" hidden>' % (pid, e(flow), e('%d pantallas y %d variaciones del flujo, exportadas de Figma, con los tokens de cada parte.' % (len(data), n))),
             ' <div class="panel" data-tab="resumen" data-label="Resumen">',
             '<p>Las pantallas de desktop del flujo, exportadas de Figma (archivo “FID SDK — Variables”, página Flujo) sin el header, que lo pone el integrador. Elegí la variación de cada pantalla y pasá el mouse por cada parte: a la derecha ves sus tokens separados por función (fondo, borde, texto, tipografía, fuente y radio). Los tokens son los del paquete (<code>DESIGN.md</code>), que es lo que tenés que usar en código.</p>',
             '<div class="note"><b>Los componentes de Figma todavía usan variables viejas</b>En Figma, estas pantallas siguen vinculadas a variables de la librería anterior (por ejemplo <code>Primitves/brand/700 main</code>). Para código, usá los tokens que se ven acá. Cuando un valor de Figma no tiene token en el paquete, se marca como “Sin token”.</div>']
        for gi, g in enumerate(data):
            v0 = g['v'][0]
            seg = ''
            if len(g['v']) > 1:
                seg = '<div class="pvseg" role="group" aria-label="Variación de la pantalla">%s</div>' % ''.join(
                    '<button type="button" data-v="%d" aria-pressed="%s">%s</button>' % (vi, 'true' if vi == 0 else 'false', e(v['l'])) for vi, v in enumerate(g['v']))
            h.append('<div class="pgroup" data-p="%s" data-g="%d"><h2 id="%s-%d">%s</h2><p class="small muted pgsec">Figma: %s%s</p>%s<div class="ptwrap"><div class="ptimg"><img loading="lazy" alt="Pantalla: %s" src="%s" width="840" height="%d"></div><ol class="ptlist"></ol></div></div>' % (
                pid, gi, pid, gi + 1, e(g['t']), e(g['sec']), (' · %d variaciones' % len(g['v'])) if len(g['v']) > 1 else '', seg, e(g['t']), v0['f'], v0['h']))
        h.append(' </div>\n</section>\n')
        pages.append('\n'.join(h))
    return ''.join(pages), pant




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


FIG_HTML, PANT = pantallas_build()
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
