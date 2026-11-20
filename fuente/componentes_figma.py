# Datos exportados de Figma "FID SDK — Variables" (página Flujo 8:2).
# Solo están las variantes que las pantallas del SDK usan directamente (instancias de primer nivel,
# no las que van anidadas dentro de otro componente). Se excluyeron íconos sueltos (icons firmador,
# Icons, "icons "), placeholders (Image swapper, replace) y piezas de documentación (Note, LayoutSidebar).
# Todas las celdas salen de una misma hoja exportada a 2x; x, y, w, h son px a 1x dentro de esa hoja.
# Cada celda: (etiqueta, propiedades en Figma, set de Figma, x, y, w, h, usos, pantallas, variables vinculadas)

F, O, A, E = 'Firmar documento', 'Olvidé mi clave de firma', 'Flujo Alta', 'Errores'
TODAS = [F, O, A, E]
B = 'Primitves/brand/700 main'
W = 'Color/Key Colors/white'
N90 = 'Color/Primitives/Neutral/neutral90'
N30 = 'Color/Primitives/Neutral/neutral30'
DIS = 'Color/Buttons/Disabled/color-interactive-disabled'
ODIS = 'Color/Buttons/Disabled/color-on-interactive-disabled'
BGD = 'Backgrounds/White-Dark/color-bg-default'
TXD = 'Texts/color-text-default'
STD = 'Strokes/color-strokes-default'
PW_F = 'state=default, density=default, theme=light'

SHEETS = [
 dict(key='button', cells=[
  ('Outline · Default · Small', 'Variant=Outline, State=Default, Size=Small, on Dark=False, has Text=True', '8:3', 925, 40, 117, 36, 125, TODAS, [N90, N30]),
  ('Secondary Button · Default · xsm', 'Type=Secondary Button, Status=Default, Size=xsm', '8:1029', 1082, 40, 102, 34, 96, [F, O, A], [BGD, STD, TXD]),
  ('Outline · Default · Large', 'Variant=Outline, State=Default, Size=Large, on Dark=False, has Text=True', '8:3', 1224, 40, 256, 48, 82, TODAS, [N90, N30]),
  ('Primary · Default · Large', 'Variant=Primary, State=Default, Size=Large, on Dark=False, has Text=True', '8:3', 40, 148, 256, 48, 68, TODAS, [B, W]),
  ('Primary · Disabled · Large', 'Variant=Primary, State=Disabled, Size=Large, on Dark=False, has Text=True', '8:3', 336, 148, 256, 48, 53, [F, O, A], [DIS, ODIS]),
  ('Outline · Disabled · Large', 'Variant=Outline, State=Disabled, Size=Large, on Dark=False, has Text=True', '8:3', 632, 148, 256, 48, 38, [F, O, A], ['Color/Buttons/Disabled/color-interactive-outline', ODIS]),
 ]),
 dict(key='button-small', cells=[
  ('Tertiary · Default', 'Variant=Tertiary, State=Default, on Dark=False, Icon=False, Text=True, is Loading=false', '8:49', 1016, 148, 70, 36, 48, [F, O], []),
 ]),
 dict(key='button-icon', cells=[
  ('Default · Md', 'Type=Default, State=Default, Size=Md', '8:1298', 928, 148, 48, 48, 96, [F, O, A], [BGD, TXD, 'Feedback/Error/color-error-bg-alert']),
 ]),
 dict(key='chip', cells=[
  ('Única', '—', '8:10675', 938, 332, 137, 35, 8, [F], []),
 ]),
 dict(key='dropdown', cells=[
  ('Default', 'State=Default', '8:838', 40, 408, 354, 102, 96, [F, O, A], [TXD, 'Backgrounds/White-Dark/color-bg-inputs', STD, 'Texts/color-text-subtle']),
 ]),
 dict(key='input-password', cells=[
  ('default (8:14113)', 'state=default, density=default, theme=light', '8:14113', 697, 1708, 297, 231, 12, [O, A], []),
  ('Filled (8:14113)', 'state=Filled, density=default, theme=light', '8:14113', 1034, 1708, 297, 231, 12, [O, A], [TXD]),
  ('default (8:1804)', 'state=default, density=default, theme=light', '8:1804', 40, 1978, 297, 231, 4, [F, O], []),
  ('error (8:14113)', 'state=error, density=default, theme=light', '8:14113', 377, 1978, 297, 228, 4, [O, A], []),
  ('typing (8:14113)', 'state=typing, density=default, theme=light', '8:14113', 714, 1978, 297, 231, 4, [O, A], []),
  ('focused (8:1804)', 'state=focused, density=default, theme=light', '8:1804', 1051, 1978, 297, 231, 2, [F], []),
  ('Filled (8:1804)', 'state=Filled, density=default, theme=light', '8:1804', 40, 2249, 297, 231, 2, [F], [TXD]),
 ]),
 dict(key='input-otp', cells=[
  ('default · 6 dígitos', 'state=default, digits=6', '8:9319', 353, 1708, 304, 102, 18, [F, A], []),
 ]),
 dict(key='otp-cell', cells=[
  ('default · lg', 'state=default, size=lg', '8:9240', 1120, 1236, 72, 72, 44, [F, A], []),
  ('filled · lg', 'state=filled, size=lg', '8:9240', 1232, 1236, 72, 72, 24, [F, A], []),
  ('success · lg', 'state=success, size=lg', '8:9240', 1344, 1236, 72, 72, 24, [F, A], []),
  ('error · lg', 'state=error, size=lg', '8:9240', 1456, 1236, 72, 72, 12, [A], ['red/700']),
  ('typing · lg', 'state=typing, size=lg', '8:9240', 40, 1348, 72, 72, 4, [F, A], []),
 ]),
 dict(key='helper-text', cells=[
  ('default (8:9506)', 'type=default, theme=light', '8:9506', 1008, 1604, 81, 18, 18, [F, A], []),
  ('default (8:9305)', 'type=default', '8:9305', 1128, 1604, 81, 18, 14, [F, A], []),
  ('default (8:1725)', 'type=default, theme=light', '8:1725', 1248, 1604, 81, 18, 8, [F, O], []),
  ('error (8:9305)', 'type=error', '8:9305', 1368, 1604, 96, 18, 2, [A], []),
  ('success (8:9305)', 'type=success', '8:9305', 40, 1708, 111, 18, 2, [A], []),
 ]),
 dict(key='requirement-list', cells=[
  ('default', 'type=default, theme=light', '8:1748', 191, 1708, 123, 18, 32, [F, O], []),
 ]),
 dict(key='checkmark', cells=[
  ('Default (Larger)', 'State=Default (Larger)', '8:2465', 468, 1604, 24, 24, 20, [F, O, A], []),
  ('Selected (Larger)', 'State=Selected (Larger)', '8:2465', 532, 1604, 24, 24, 6, [O, A], []),
 ]),
 dict(key='radio', cells=[
  ('No seleccionado · Default', 'is Selected=No, State=Default, is Disabled=No', '8:2428', 632, 1460, 24, 24, 8, [F, O], []),
 ]),
 dict(key='title-content', cells=[
  ('XS (14) · solo descripción (8:2495)', 'on Dark=False, is Mobile=False, Size=XS (14), Weight=Medium, Centered=False, Subtitle=False, Title=False, Description=True, Link=False', '8:2495', 806, 1460, 174, 16, 123, TODAS, []),
  ('XS (14) · solo título (8:3384)', 'on Dark=False, is Mobile=False, Size=XS (14), Weight=Medium, Centered=False, Subtitle=False, Title=True, Description=False, Link=False', '8:3384', 1020, 1460, 174, 20, 123, TODAS, []),
  ('L (24) · centrado · título y descripción (8:3384)', 'on Dark=False, is Mobile=False, Size=L (24), Weight=Medium, Centered=True, Subtitle=False, Title=True, Description=True, Link=False', '8:3384', 1234, 1460, 174, 60, 24, TODAS, []),
  ('L (24) · móvil · centrado · título y descripción (8:4298)', 'on Dark=False, is Mobile=True, Size=L (24), Weight=Medium, Centered=True, Subtitle=False, Title=True, Description=True, Link=False', '8:4298', 40, 1604, 174, 52, 24, TODAS, []),
  ('XS (14) · solo descripción (8:4298)', 'on Dark=False, is Mobile=False, Size=XS (14), Weight=Medium, Centered=False, Subtitle=False, Title=False, Description=True, Link=False', '8:4298', 254, 1604, 174, 16, 12, [O, A], []),
 ]),
 dict(key='list', cells=[
  ('Small · ícono · una acción (8:7251)', 'Small=True, Icon=True, Description=None, Sidetext=None, Actions=One, is Loading=False', '8:7251', 40, 1070, 500, 40, 45, TODAS, []),
  ('Small · ícono · descripción · una acción (8:8017)', 'Small=True, Icon=True, Description=Default, Sidetext=None, Actions=One, is Loading=False', '8:8017', 580, 1070, 500, 40, 19, TODAS, []),
  ('Small · ícono (8:13041)', 'Small=True, Icon=True, Description=None, Sidetext=None, Actions=None, is Loading=False', '8:13041', 40, 1150, 500, 40, 18, [O, A], []),
  ('ícono · descripción (8:7251)', 'Small=False, Icon=True, Description=Default, Sidetext=None, Actions=None, is Loading=False', '8:7251', 580, 1150, 500, 46, 12, [O, A], []),
  ('ícono (8:11627)', 'Small=False, Icon=True, Description=None, Sidetext=None, Actions=None, is Loading=False', '8:11627', 40, 1236, 500, 40, 8, [O, A], []),
  ('sin ícono · descripción (8:13041)', 'Small=False, Icon=False, Description=Default, Sidetext=None, Actions=None, is Loading=False', '8:13041', 580, 1236, 500, 46, 6, [O, A], []),
 ]),
 dict(key='card', cells=[
  ('Sin elevación · con padding (8:7984)', 'is Elevated=False, has Padding=True', '8:7984', 1126, 148, 194, 144, 19, TODAS, []),
  ('Sin elevación · con padding (8:9182)', 'is Elevated=False, has Padding=True', '8:9182', 1360, 148, 194, 144, 13, TODAS, []),
 ]),
 dict(key='card-footer', cells=[
  ('Default', 'Type=Default', '8:2387', 40, 40, 277, 68, 48, [F, O], []),
 ]),
 dict(key='group-heading', cells=[
  ('Section · 1 acción', 'Type=Section, Actions=1, is Mobile=False', '8:13994', 40, 332, 858, 36, 6, [O, A], []),
 ]),
 dict(key='divider', cells=[
  ('Horizontal (8:6810)', 'is Horizontal=True, Full width=No', '8:6810', 1115, 332, 40, 1, 56, TODAS, []),
  ('Horizontal (8:45)', 'is Horizontal=True, Full width=No', '8:45', 1195, 332, 40, 1, 48, [F, O], []),
  ('Horizontal · padding 24 (8:45)', 'is Horizontal=True, Full width=Padding 24', '8:45', 1275, 332, 40, 1, 6, [O, A], []),
  ('Horizontal · padding 24 (8:6810)', 'is Horizontal=True, Full width=Padding 24', '8:6810', 1355, 332, 40, 1, 6, [O, A], []),
 ]),
 dict(key='reading-progress', cells=[
  ('Sin leer', 'Estado=Sin leer', '8:28628', 152, 1348, 552, 56, 2, [F], ['bg/default', 'bg/muted', 'text/primary', 'text/secondary']),
  ('En progreso', 'Estado=En progreso', '8:28628', 744, 1348, 552, 56, 1, [F], ['bg/default', 'bg/muted', 'text/primary', 'text/secondary', 'brand/default']),
  ('Completo', 'Estado=Completo', '8:28628', 40, 1460, 552, 56, 1, [F], ['feedback/success-bg', 'bg/muted', 'feedback/success-icon', 'text/primary', 'bg/subtle', 'brand/default']),
 ]),
 dict(key='badges', cells=[
  ('Text · Info · Large', 'Type=Text, State=Info, Size=Large', '8:76', 565, 40, 106, 37, 8, [O, A], []),
 ]),
 dict(key='badge-success', cells=[
  ('Única', '—', '8:2418', 711, 40, 104, 25, 48, [F, O], []),
 ]),
 dict(key='pills', cells=[
  ('Base pill', 'Type=Base pill', '8:2448', 855, 40, 30, 20, 8, [F, O], []),
 ]),
 dict(key='spinner', cells=[
  ('Base spinner · Light', 'State=Base spinner, Over=Light', '8:4285', 742, 1460, 24, 24, 2, [F], ['Strokes/color-strokes-primarycolor-default']),
 ]),
 dict(key='tooltip', cells=[
  ('Única', '—', '8:10667', 596, 1604, 372, 64, 3, [F], []),
 ]),
 dict(key='avatar', cells=[
  ('Icon · Error · circular (8:10151)', 'Type=Icon, Color=Error, is Circle=Yes, has Badge=No, has Dot=No, Size=Medium, isLoading=False', '8:10151', 357, 40, 64, 64, 12, [F, O, E], ['Color/States/Error/color-error', 'Color/States/Error/color-on-error']),
  ('Icon · Default · cuadrado (8:5327)', 'Type=Icon, Color=Default, is Circle=No, has Badge=No, has Dot=No, Size=Medium, isLoading=False', '8:5327', 461, 40, 64, 64, 6, [O, A], []),
 ]),
 dict(key='icon-container', cells=[
  ('Medium · 24 px', 'Size=Medium - 24px', '8:1454', 434, 408, 24, 24, 24, [F, O, A], []),
 ]),
 dict(key='scrollbar', cells=[
  ('Vertical', 'Orientation=Vertical', '8:10775', 696, 1460, 6, 104, 8, [O, A], []),
 ]),
 dict(key='illustration', cells=[
  ('Design 4', 'Design=4', '8:248', 40, 550, 1128, 480, 260, TODAS, ['Primary/PR500', 'DarkOverlayElement/DO40', 'DarkOverlayElement/DO60', 'PrimaryAlpha/PRA10', 'DarkOverlayElement/DO20', 'DarkOverlayElement/100']),
 ]),
]

# Nombre, descripción y total de variantes del set tal como están en Figma.
# total: variantes del set principal (None si no aplica o no se midió).
META_EXTRA = {
 'card-footer': dict(name='.cardFooter', group='Contenido', total=None, desc='', props={}),
 'badge-success': dict(name='Badges/Medium/Success/with Icon/Bottom Rounded', group='Estado y feedback', total=1, desc='', props={}),
 'illustration': dict(name='Img lib/Ilustration graph, icon', group='Otros', total=None, desc='', props={}),
}

# Información de cada componente tal como está en Figma (nombre, descripción, total de variantes del set principal y propiedades).
META = {
 'button': dict(name='Button', group='Acciones', total=254, desc='Para armado de flujos utilizamos Button Row', props={'Variant': ['Primary', 'Outline', 'Black', 'None', 'Alt', 'Ghost'], 'State': ['Default', 'Disabled', 'Hover', 'Skeleton', 'Loading', 'inProgress', 'Active', 'Focused'], 'Size': ['Large', 'Small', 'Medium'], 'on Dark': ['False', 'True'], 'has Text': ['True', 'False'], 'Show Icon Left': 'BOOLEAN', 'Show Icon Right': 'BOOLEAN'}),
 'button-small': dict(name='Button/Small', group='Acciones', total=105, desc='Botón pequeño. Se utilizará dentro de elementos que requieren un accionable pero puedan ser leídos en segunda jerarquía.', props={'Variant': ['Primary', 'Secundary', 'Tertiary'], 'State': ['Default', 'Loading', 'Disabled', 'Hover', 'Progress', 'Active', 'Focused'], 'on Dark': ['False', 'True'], 'Icon': ['False', 'True'], 'Text': ['True', 'False'], 'is Loading': ['false', 'true']}),
 'button-icon': dict(name='Button Icon', group='Acciones', total=30, desc='', props={'Type': ['Default', 'Outline'], 'State': ['Disabled', 'Default', 'Hover', 'Focus', 'Active'], 'Size': ['Sm', 'Md', 'Lg'], 'Show Badge Indicator': 'BOOLEAN', 'Icon': 'INSTANCE_SWAP'}),
 'chip': dict(name='Chip · Ir a la página siguiente', group='Acciones', total=1, desc='', props={}),
 'dropdown': dict(name='Dropdown', group='Formularios', total=6, desc='', props={'State': ['Expand', 'Hover', 'Focus', 'Disabled', 'Default', 'Error'], 'Text title': 'TEXT', 'Text helper': 'TEXT', 'Show helper text': 'BOOLEAN', 'Show title': 'BOOLEAN'}),
 'input-password': dict(name='inputPassword', group='Formularios', total=37, desc='', props={'state': ['default', 'hovered', 'focused', 'typing', 'disabled', 'readOnly', 'prefilled', 'error', 'success', 'Filled'], 'density': ['default', 'compact'], 'theme': ['light', 'dark'], 'hasLabel': 'BOOLEAN', 'hasHelperText': 'BOOLEAN', 'hasRequirementList': 'BOOLEAN', 'hasLeadingIcon': 'BOOLEAN', 'hasTrailingIcon': 'BOOLEAN'}),
 'input-otp': dict(name='inputOTP', group='Formularios', total=18, desc='', props={'state': ['default', 'focused', 'typing', 'disabled', 'error', 'success'], 'digits': ['4', '6', '8'], 'hasLabel': 'BOOLEAN', 'hasHelperText': 'BOOLEAN'}),
 'otp-cell': dict(name='OTPinput', group='Formularios', total=24, desc='', props={'state': ['default', 'hovered', 'focused', 'typing', 'disabled', 'error', 'success', 'filled'], 'size': ['sm', 'md', 'lg']}),
 'helper-text': dict(name='_helperText', group='Formularios', total=6, desc='', props={'type': ['default', 'success', 'error'], 'theme': ['light', 'dark'], 'hasIcon': 'BOOLEAN'}),
 'requirement-list': dict(name='_requirementList', group='Formularios', total=6, desc='', props={'type': ['default', 'success', 'error'], 'theme': ['light', 'dark'], 'hasIcon': 'BOOLEAN'}),
 'checkmark': dict(name='Toggle / Checkmark', group='Formularios', total=2, desc='', props={'State': ['Default (Larger)', 'Selected (Larger)']}),
 'radio': dict(name='Radio button circle', group='Formularios', total=8, desc='', props={'is Selected': ['No', 'Yes'], 'State': ['Focus', 'Default', 'Hover'], 'is Disabled': ['No', 'Yes']}),
 'title-content': dict(name='Title content', group='Contenido', total=248, desc='Título. Bajada. Descripción. Titular. Textos. Title.', props={'Size': ['XL (32)', 'L (24)', 'M (20)', 'S (16)', 'XS (14)'], 'Weight': ['Medium', 'Bold'], 'Centered': ['True', 'False'], 'Subtitle': ['True', 'False'], 'Title': ['True', 'False'], 'Description': ['True', 'False'], 'Link': ['True', 'False'], 'on Dark': ['True', 'False'], 'is Mobile': ['False', 'True']}),
 'list': dict(name='List', group='Contenido', total=361, desc='Pueden tener: icono o imagen, título, detalle del título, accionables o texto junto a un detalle o badge, doble icono a la derecha.', props={'Sidetext': ['None', 'Default', 'w/ Description', 'w/ Badge', 'Badge Only', 'w/ Badge Inline'], 'Actions': ['None', 'One', 'Two'], 'Description': ['None', 'Default', 'w/ Date', 'Date Only', 'Subtitle (Copetín)'], 'Small': ['False', 'True'], 'Icon': ['False', 'True'], 'is Loading': ['True', 'False']}),
 'card': dict(name='Card container', group='Contenido', total=4, desc='', props={'is Elevated': ['False', 'True'], 'has Padding': ['True', 'False'], 'Content': 'INSTANCE_SWAP', 'has Image': 'BOOLEAN', 'has Badge': 'BOOLEAN', 'has Footer': 'BOOLEAN'}),
 'group-heading': dict(name='CardGroupHeading', group='Contenido', total=12, desc='Va con 12px de distancia con el Card. Section heading.', props={'Type': ['Section', 'Filter', 'Pills'], 'Actions': ['1', '2', '3', '4'], 'is Mobile': ['False', 'True'], 'hasButton': 'BOOLEAN', 'filterActive': 'BOOLEAN', 'hasTitle': 'BOOLEAN'}),
 'divider': dict(name='Divider', group='Contenido', total=4, desc='', props={'is Horizontal': ['True', 'False'], 'Full width': ['No', 'Padding 24', 'Padding 16']}),
 'reading-progress': dict(name='Progreso de lectura', group='Contenido', total=3, desc='', props={'Estado': ['Sin leer', 'En progreso', 'Completo']}),
 'badges': dict(name='Badges', group='Estado y feedback', total=40, desc='Permiten diferenciar o resaltar el estado del elemento al que están relacionados', props={'Type': ['Text', 'with Icon', 'Icon', 'Dot'], 'State': ['Info', 'Default', 'Success', 'Error', 'Warning'], 'Size': ['Large', 'Medium', 'Small']}),
 'pills': dict(name='Base Pills', group='Estado y feedback', total=4, desc='', props={'Type': ['Base pill', 'Base pill icon', 'Base pill icon removable', 'Base pill removable']}),
 'spinner': dict(name='Spinner', group='Estado y feedback', total=6, desc='', props={'State': ['Base spinner', 'State4', 'State3', 'State5', 'State6'], 'Over': ['Light', 'Dark']}),
 'tooltip': dict(name='Tooltip · Firma bloqueada', group='Estado y feedback', total=1, desc='', props={}),
 'avatar': dict(name='Avatar', group='Otros', total=188, desc='', props={'Type': ['Text', 'Icon', 'Image', 'Image L'], 'Color': ['Image', 'Default', 'Highlight', 'White', 'Success', 'Error', 'Info', 'Warning'], 'Size': ['Medium', 'Small'], 'is Circle': ['No', 'Yes'], 'has Badge': ['Yes', 'No'], 'has Dot': ['No', 'Yes'], 'isLoading': ['False', 'true']}),
 'icon-container': dict(name='Icon container', group='Otros', total=3, desc='Reemplazar el icono interno de este contenedor.', props={'Size': ['Small - 16px', 'Medium - 24px', 'Large - 32px']}),
 'scrollbar': dict(name='Scrollbar', group='Otros', total=2, desc='', props={'Orientation': ['Horizontal', 'Vertical']}),
}
META.update(META_EXTRA)
