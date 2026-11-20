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

# Estilos de efecto del archivo de Figma "FID SDK — Variables" (no están en tokens.css).
SHADOWS = [
    {'name': 'shadow/sm', 'css': '0 1px 4px rgba(12, 12, 13, 0.05)', 'layers': 1},
    {'name': 'shadow/4dp', 'css': '0 0 0 rgba(72, 70, 82, 0.06), 0 1px 2px rgba(72, 70, 82, 0.05), 0 4px 4px rgba(72, 70, 82, 0.05), 0 9px 5px rgba(72, 70, 82, 0.03), 0 15px 6px rgba(72, 70, 82, 0.01), 0 24px 7px rgba(72, 70, 82, 0)', 'layers': 6},
    {'name': 'shadow/elevation-1', 'css': '0 4px 6px rgba(33, 33, 33, 0.04), 0 4px 50px rgba(33, 33, 33, 0.08)', 'layers': 2},
]

read = lambda p: Path(p).read_text(encoding='utf-8')
md = read(PKG / 'DESIGN.md')
tokens = json.loads(read(PKG / 'tokens.json'))


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
        'shadows': SHADOWS, 'svgs': svgs, 'logo': logo_sm,
    }),
    'LOTTIES_JSON': js(lotties),
    **LINKS,
}

out = read(HERE / 'plantilla.html')
for k in sorted(repl, key=len, reverse=True):
    out = out.replace('{{' + k + '}}', repl[k])
left = re.findall(r'\{\{[A-Z_]+\}\}', out)
assert not left, left
OUT.write_text(out, encoding='utf-8')
print(f'OK → {OUT}  ({OUT.stat().st_size / 1024:.0f} KB) · semánticos {len(semantic)} · estilos de texto {len(text_styles)} · reglas {len(rules)} · checklist {len(checklist)}')
