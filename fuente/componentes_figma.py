# Datos exportados de Figma "FID SDK — Variables" (página Flujo, componentes de librería usados en las pantallas del SDK).
# Cada hoja se armó con instancias reales de las variantes; las celdas son posiciones dentro de la hoja (px a 1x).
# vars = variables vinculadas en Figma a esa variante (nombre tal como está en la librería).
B = 'Primitves/brand/700 main'
W = 'Color/Key Colors/white'
N90 = 'Color/Primitives/Neutral/neutral90'
N30 = 'Color/Primitives/Neutral/neutral30'
N20 = 'Color/Primitives/Neutral/neutral20'
N80 = 'Color/Primitives/Neutral/neutral80'
DIS = 'Color/Buttons/Disabled/color-interactive-disabled'
ODIS = 'Color/Buttons/Disabled/color-on-interactive-disabled'
BGD = 'Backgrounds/White-Dark/color-bg-default'
TXD = 'Texts/color-text-default'
ERB = 'Feedback/Error/color-error-bg-alert'

SHEETS = [
 dict(key='button', frame='180:3', fw=1520, fh=657, props=['Variant', 'State', 'Size'], fixed={'on Dark': 'False', 'has Text': 'True'}, cells=[
  (('Primary', 'Hover', 'Large'), 40, 40, 256, 48, ['Primitves/brand/300', W]),
  (('Outline', 'Hover', 'Large'), 336, 40, 256, 48, ['Color/Primitives/Neutral/Neutral-alpha/alpha10', 'Color/Primitives/Neutral/neutral70', N30]),
  (('Primary', 'Default', 'Large'), 632, 40, 256, 48, [B, W]),
  (('Outline', 'Default', 'Large'), 928, 40, 256, 48, [N90, N30]),
  (('Primary', 'Disabled', 'Large'), 1224, 40, 256, 48, [DIS, ODIS]),
  (('Outline', 'Disabled', 'Large'), 40, 128, 256, 48, ['Color/Buttons/Disabled/color-interactive-outline', ODIS]),
  (('Black', 'Default', 'Large'), 336, 128, 256, 48, [N20, W]),
  (('None', 'Skeleton', 'Large'), 632, 128, 256, 49, []),
  (('Alt', 'Default', 'Large'), 928, 128, 256, 48, [B]),
  (('Alt', 'Loading', 'Large'), 1224, 128, 256, 48, ['Primitves/brand/500']),
  (('Outline', 'Loading', 'Large'), 40, 216, 256, 48, [N90, 'Primitves/brand/500']),
  (('Black', 'Disabled', 'Large'), 336, 216, 256, 48, [DIS, ODIS]),
  (('Alt', 'Disabled', 'Large'), 632, 216, 256, 48, ['Color/Primitives/Neutral/Neutral-alpha/alpha10', ODIS]),
  (('Black', 'Hover', 'Large'), 928, 216, 256, 48, ['Color/Primitives/Neutral/Neutral-alpha/alpha50', W]),
  (('Alt', 'Hover', 'Large'), 1224, 216, 256, 48, ['Primitves/brand/800']),
  (('Primary', 'inProgress', 'Large'), 40, 304, 256, 49, [B, W]),
  (('Black', 'inProgress', 'Large'), 336, 304, 256, 48, [N20, 'Color/Primitives/Neutral/neutral10', W]),
  (('Primary', 'Active', 'Large'), 632, 304, 256, 48, [B, W]),
  (('Black', 'Active', 'Large'), 928, 304, 256, 48, ['Color/Primitives/Neutral/neutral10', W]),
  (('Primary', 'Loading', 'Large'), 1224, 304, 256, 49, [B, W]),
  (('Black', 'Loading', 'Large'), 40, 392, 256, 49, [N20, W]),
  (('Alt', 'Active', 'Large'), 336, 392, 256, 48, ['Primitves/brand/800']),
  (('Outline', 'Active', 'Large'), 632, 392, 256, 48, ['Color/Primitives/Neutral/Neutral-alpha/alpha50', 'Color/Primitives/Neutral/neutral70', N30]),
  (('Primary', 'Focused', 'Large'), 928, 392, 256, 48, [B, N80, W]),
  (('Black', 'Focused', 'Large'), 1224, 392, 256, 48, [N20, N80, W]),
  (('Alt', 'Focused', 'Large'), 40, 480, 256, 48, [N80, B]),
  (('Outline', 'Focused', 'Large'), 336, 480, 256, 48, [N80, N90, N30]),
  (('Ghost', 'Default', 'Large'), 632, 480, 256, 48, [W, B]),
  (('Ghost', 'Loading', 'Large'), 928, 480, 256, 48, [W, 'Primitves/brand/500']),
  (('Ghost', 'Disabled', 'Large'), 1224, 480, 256, 48, [DIS, ODIS]),
  (('Ghost', 'Hover', 'Large'), 40, 568, 256, 48, ['Primitves/brand/50', B]),
  (('Ghost', 'Active', 'Large'), 336, 568, 256, 48, ['Primitves/brand/100', B]),
  (('Ghost', 'Focused', 'Large'), 632, 568, 256, 48, [W, N80, B]),
  (('Primary', 'Default', 'Medium'), 928, 568, 256, 36, [B, W]),
  (('Primary', 'Default', 'Small'), 1224, 568, 117, 36, [B, W]),
 ]),
 dict(key='button-small', frame='180:519', fw=1558, fh=196, props=['Variant', 'State'], fixed={'on Dark': 'False', 'Icon': 'False', 'Text': 'True', 'is Loading': 'false'}, cells=[
  (('Tertiary', 'Default'), 40, 40, 70, 36, []), (('Secundary', 'Default'), 150, 40, 70, 36, []), (('Primary', 'Default'), 260, 40, 70, 36, []),
  (('Primary', 'Loading'), 370, 40, 48, 40, []), (('Primary', 'Disabled'), 458, 40, 70, 36, []), (('Tertiary', 'Disabled'), 568, 40, 70, 36, []),
  (('Primary', 'Hover'), 678, 40, 70, 36, []), (('Tertiary', 'Hover'), 788, 40, 70, 36, []), (('Primary', 'Progress'), 898, 40, 70, 37, []),
  (('Primary', 'Active'), 1008, 40, 70, 36, []), (('Tertiary', 'Active'), 1118, 40, 70, 36, []), (('Primary', 'Focused'), 1228, 40, 70, 36, []),
  (('Tertiary', 'Focused'), 1338, 40, 70, 36, []), (('Secundary', 'Disabled'), 1448, 40, 70, 36, []), (('Secundary', 'Hover'), 40, 120, 70, 36, []),
  (('Secundary', 'Active'), 150, 120, 70, 36, []), (('Secundary', 'Focused'), 260, 120, 70, 36, []),
 ]),
 dict(key='button-icon', frame='180:608', fw=920, fh=128, props=['Type', 'State'], fixed={'Size': 'Md'}, cells=[
  (('Default', 'Default'), 40, 40, 48, 48, [BGD, TXD, ERB]), (('Default', 'Disabled'), 128, 40, 48, 48, [BGD, TXD, ERB]),
  (('Default', 'Active'), 216, 40, 48, 48, ['Backgrounds/White-Dark/color-bg-subtle', TXD, ERB, BGD]),
  (('Default', 'Hover'), 304, 40, 48, 48, ['Backgrounds/White-Dark/color-bg-subtle-light', TXD, ERB, BGD]),
  (('Default', 'Focus'), 392, 40, 48, 48, [BGD, 'Strokes/color-stroke-bold', TXD, ERB]),
  (('Outline', 'Default'), 480, 40, 48, 48, [BGD, 'Strokes/color-strokes-default', TXD, ERB]),
  (('Outline', 'Disabled'), 568, 40, 48, 48, [BGD, 'Strokes/color-strokes-default', TXD, ERB]),
  (('Outline', 'Active'), 656, 40, 48, 48, ['Backgrounds/White-Dark/color-bg-subtle', 'Strokes/color-strokes-default', TXD, ERB, BGD]),
  (('Outline', 'Hover'), 744, 40, 48, 48, [BGD, 'Strokes/color-stroke-secondarycolor-default', TXD, ERB]),
  (('Outline', 'Focus'), 832, 40, 48, 48, [BGD, 'Strokes/color-stroke-bold', TXD, ERB]),
 ]),
 dict(key='dropdown', frame='180:679', fw=1616, fh=700, props=['State'], fixed={}, cells=[
  (('Expand',), 40, 40, 354, 478, [TXD, 'Backgrounds/White-Dark/color-bg-inputs', 'Strokes/color-strokes-default', 'Texts/color-text-subtle', BGD, 'Strokes/color-stroke-subtle', 'Backgrounds/White-Dark/color-bg-muted', 'Texts/color-text-subtle-light']),
  (('Default',), 434, 40, 354, 102, [TXD, 'Backgrounds/White-Dark/color-bg-inputs', 'Strokes/color-strokes-default', 'Texts/color-text-subtle']),
  (('Error',), 828, 40, 354, 102, ['Feedback/Error/color-error-text', 'Backgrounds/White-Dark/color-bg-inputs', 'Strokes/color-stroke-error', 'Texts/color-text-subtle', TXD]),
  (('Disabled',), 1222, 40, 354, 101, ['Texts/color-text-muted', 'Backgrounds/White-Dark/color-bg-muted', 'Strokes/color-strokes-default']),
  (('Hover',), 40, 558, 354, 102, [TXD, 'Backgrounds/White-Dark/color-bg-muted', 'Strokes/color-stroke-subtle', 'Texts/color-text-subtle']),
  (('Focus',), 434, 558, 354, 102, [TXD, 'Backgrounds/White-Dark/color-bg-inputs', 'Strokes/color-stroke-bold', 'Texts/color-text-subtle']),
 ]),
 dict(key='input-password', frame='180:768', fw=1388, fh=852, props=['state'], fixed={'density': 'default', 'theme': 'light'}, cells=[
  (('hovered',), 40, 40, 297, 231, []), (('error',), 377, 40, 297, 228, []), (('success',), 714, 40, 297, 228, []), (('readOnly',), 1051, 40, 297, 117, []),
  (('prefilled',), 40, 310, 297, 117, []), (('focused',), 377, 310, 297, 231, []), (('typing',), 714, 310, 297, 231, []), (('default',), 1051, 310, 297, 231, []),
  (('Filled',), 40, 581, 297, 231, [TXD]), (('disabled',), 377, 581, 297, 117, ['Action/color-action-text-disable']),
 ]),
 dict(key='input-otp', frame='180:1169', fw=1416, fh=324, props=['state'], fixed={'digits': '6'}, cells=[
  (('error',), 40, 40, 304, 102, []), (('default',), 384, 40, 304, 102, []), (('success',), 728, 40, 304, 102, []),
  (('typing',), 1072, 40, 304, 102, []), (('focused',), 40, 182, 304, 102, []), (('disabled',), 384, 182, 304, 102, []),
 ]),
 dict(key='otp-cell', frame='180:1312', fw=808, fh=136, props=['state'], fixed={'size': 'md'}, cells=[
  (('default',), 40, 40, 56, 56, []), (('filled',), 136, 40, 56, 56, []), (('focused',), 232, 40, 56, 56, []), (('hovered',), 328, 40, 56, 56, []),
  (('typing',), 424, 40, 56, 56, []), (('disabled',), 520, 40, 56, 56, []), (('error',), 616, 40, 56, 56, ['red/700']), (('success',), 712, 40, 56, 56, []),
 ]),
 dict(key='helper-text', frame='180:1339', fw=448, fh=98, props=['type'], fixed={'theme': 'light'}, cells=[
  (('default',), 40, 40, 81, 18, []), (('success',), 160, 40, 111, 18, []), (('error',), 311, 40, 96, 18, []),
 ]),
 dict(key='requirement-list', frame='180:1350', fw=527, fh=98, props=['type'], fixed={'theme': 'light'}, cells=[
  (('default',), 40, 40, 123, 18, []), (('success',), 202, 40, 122, 18, []), (('error',), 364, 40, 122, 18, []),
 ]),
 dict(key='title-content', frame='180:1363', fw=1538, fh=180, props=['Size', 'Weight'], fixed={'on Dark': 'False', 'is Mobile': 'False', 'Centered': 'False', 'Subtitle': 'True', 'Title': 'True', 'Description': 'True', 'Link': 'False'}, cells=[
  (('S (16)', 'Bold'), 40, 40, 174, 68, []), (('S (16)', 'Medium'), 254, 40, 174, 68, []), (('XS (14)', 'Bold'), 468, 40, 174, 58, []),
  (('XS (14)', 'Medium'), 682, 40, 174, 58, []), (('XL (32)', 'Medium'), 896, 40, 174, 100, []), (('L (24)', 'Medium'), 1110, 40, 174, 84, []),
  (('M (20)', 'Medium'), 1324, 40, 174, 76, []),
 ]),
 dict(key='list', frame='180:1392', fw=1120, fh=389, props=['Sidetext', 'Actions'], fixed={'Small': 'False', 'Icon': 'True', 'Description': 'Default', 'is Loading': 'False'}, cells=[
  (('None', 'Two'), 40, 40, 500, 46, []), (('None', 'One'), 580, 40, 500, 46, []), (('w/ Description', 'None'), 40, 126, 500, 46, []),
  (('w/ Badge', 'None'), 580, 126, 500, 51, []), (('w/ Badge Inline', 'None'), 40, 216, 500, 46, []), (('Badge Only', 'None'), 580, 216, 500, 46, []),
  (('Default', 'None'), 40, 302, 500, 46, []), (('None', 'None'), 580, 302, 500, 46, []),
 ]),
 dict(key='card', frame='180:1675', fw=976, fh=224, props=['is Elevated', 'has Padding'], fixed={}, cells=[
  (('False', 'True'), 40, 40, 194, 144, []), (('False', 'False'), 274, 40, 194, 112, []), (('True', 'True'), 508, 40, 194, 144, []), (('True', 'False'), 742, 40, 194, 112, []),
 ]),
 dict(key='divider', frame='180:1740', fw=321, fh=120, props=['is Horizontal', 'Full width'], fixed={}, cells=[
  (('True', 'No'), 40, 40, 40, 1, []), (('True', 'Padding 24'), 120, 40, 40, 1, []), (('False', 'No'), 200, 40, 1, 40, []), (('True', 'Padding 16'), 241, 40, 40, 1, []),
 ]),
 dict(key='checkmark', frame='180:1747', fw=168, fh=104, props=['State'], fixed={}, cells=[
  (('Default (Larger)',), 40, 40, 24, 24, []), (('Selected (Larger)',), 104, 40, 24, 24, []),
 ]),
 dict(key='radio', frame='180:1754', fw=552, fh=104, props=['is Selected', 'State', 'is Disabled'], fixed={}, cells=[
  (('Yes', 'Focus', 'No'), 40, 40, 24, 24, []), (('Yes', 'Hover', 'No'), 104, 40, 24, 24, []), (('No', 'Focus', 'No'), 168, 40, 24, 24, []),
  (('No', 'Hover', 'No'), 232, 40, 24, 24, []), (('No', 'Default', 'No'), 296, 40, 24, 24, []), (('No', 'Default', 'Yes'), 360, 40, 24, 24, []),
  (('Yes', 'Default', 'No'), 424, 40, 24, 24, []), (('Yes', 'Default', 'Yes'), 488, 40, 24, 24, []),
 ]),
 dict(key='badges', frame='180:1803', fw=1536, fh=169, props=['Type', 'State'], fixed={'Size': 'Medium'}, cells=[
  (('Text', 'Default'), 40, 40, 80, 25, []), (('Text', 'Info'), 160, 40, 80, 25, []), (('Text', 'Success'), 280, 40, 80, 25, []),
  (('Text', 'Error'), 400, 40, 80, 25, []), (('Text', 'Warning'), 520, 40, 80, 25, []), (('with Icon', 'Default'), 640, 40, 104, 25, []),
  (('Icon', 'Default'), 784, 40, 24, 24, []), (('Icon', 'Info'), 848, 40, 24, 24, []), (('Icon', 'Success'), 912, 40, 24, 24, []),
  (('Icon', 'Error'), 976, 40, 24, 24, []), (('Icon', 'Warning'), 1040, 40, 24, 24, []), (('with Icon', 'Info'), 1104, 40, 104, 25, []),
  (('with Icon', 'Success'), 1248, 40, 104, 25, []), (('with Icon', 'Error'), 1392, 40, 104, 25, []), (('with Icon', 'Warning'), 40, 104, 104, 25, []),
 ]),
 dict(key='pills', frame='180:1936', fw=416, fh=100, props=['Type'], fixed={}, cells=[
  (('Base pill removable',), 40, 40, 54, 20, []), (('Base pill',), 134, 40, 30, 20, []), (('Base pill icon removable',), 204, 40, 78, 20, []), (('Base pill icon',), 322, 40, 54, 20, []),
 ]),
 dict(key='spinner', frame='180:1961', fw=232, fh=104, props=['State'], fixed={'Over': 'Light'}, cells=[
  (('Base spinner',), 40, 40, 24, 24, ['Strokes/color-strokes-primarycolor-default']), (('State4',), 104, 40, 24, 24, ['Strokes/color-strokes-primarycolor-default']),
  (('State3',), 168, 40, 24, 24, ['Strokes/color-strokes-primarycolor-default']),
 ]),
 dict(key='avatar', frame='180:1998', fw=1600, fh=144, props=['Type', 'Color'], fixed={'is Circle': 'Yes', 'has Badge': 'No', 'has Dot': 'No', 'Size': 'Medium', 'isLoading': 'False'}, cells=[
  (('Text', 'Highlight'), 40, 40, 64, 64, ['Color/Primitives/Primary/primary95', 'Color/Primitives/Primary/primary50']),
  (('Text', 'Success'), 144, 40, 64, 64, ['Color/Primitives/Success/success98', 'Color/States/Success/color-on-success']),
  (('Text', 'Error'), 248, 40, 64, 64, ['Color/States/Error/color-error', 'Color/States/Error/color-on-error']),
  (('Text', 'Info'), 352, 40, 64, 64, ['Color/States/Info/color-info', 'Color/States/Info/color-on-info']),
  (('Text', 'Warning'), 456, 40, 64, 64, ['Color/States/Warning/color-warning', 'Color/States/Warning/color-on-warning']),
  (('Text', 'White'), 560, 40, 64, 64, ['Color/Primitives/Neutral/neutral98', 'Color/Primitives/Neutral/neutral95', 'Color/Primitives/Primary/primary60']),
  (('Text', 'Default'), 664, 40, 64, 64, ['Color/Surface/color-surface-lowest', N20]),
  (('Icon', 'Highlight'), 768, 40, 64, 64, ['Color/Primitives/Primary/primary95', 'Color/Primitives/Primary/primary50']),
  (('Icon', 'Success'), 872, 40, 64, 64, ['Color/Primitives/Success/success98', 'Color/States/Success/color-on-success']),
  (('Icon', 'Error'), 976, 40, 64, 64, ['Color/States/Error/color-error', 'Color/States/Error/color-on-error']),
  (('Icon', 'Info'), 1080, 40, 64, 64, ['Color/States/Info/color-info', 'Color/States/Info/color-on-info']),
  (('Icon', 'Warning'), 1184, 40, 64, 64, ['Color/States/Warning/color-warning', 'Color/States/Warning/color-on-warning']),
  (('Icon', 'White'), 1288, 40, 64, 64, ['Color/Primitives/Neutral/neutral98', 'Color/Primitives/Neutral/neutral95', 'Color/Primitives/Primary/primary60']),
  (('Icon', 'Default'), 1392, 40, 64, 64, ['Color/Surface/color-surface-lowest', N20]),
  (('Image', 'Image'), 1496, 40, 64, 64, ['Color/Primitives/Neutral/neutral95']),
 ]),
 dict(key='tooltip', frame='180:2057', fw=452, fh=144, props=[], fixed={}, cells=[((), 40, 40, 372, 64, [])]),
 dict(key='chip', frame='180:2070', fw=217, fh=115, props=[], fixed={}, cells=[((), 40, 40, 137, 35, [])]),
 dict(key='scrollbar', frame='180:2075', fw=230, fh=184, props=['Orientation'], fixed={}, cells=[(('Horizontal',), 40, 40, 104, 6, []), (('Vertical',), 184, 40, 6, 104, [])]),
 dict(key='icon-container', frame='180:2080', fw=232, fh=112, props=['Size'], fixed={}, cells=[
  (('Medium - 24px',), 40, 40, 24, 24, []), (('Large - 32px',), 104, 40, 32, 32, []), (('Small - 16px',), 176, 40, 16, 16, []),
 ]),
 dict(key='reading-progress', frame='180:2092', fw=1224, fh=232, props=['Estado'], fixed={}, cells=[
  (('Sin leer',), 40, 40, 552, 56, ['bg/default', 'bg/muted', 'text/primary', 'text/secondary']),
  (('En progreso',), 632, 40, 552, 56, ['bg/default', 'bg/muted', 'text/primary', 'text/secondary', 'brand/default']),
  (('Completo',), 40, 136, 552, 56, ['feedback/success-bg', 'bg/muted', 'feedback/success-icon', 'text/primary', 'bg/subtle', 'brand/default']),
 ]),
 dict(key='group-heading', frame='180:2133', fw=938, fh=648, props=['Type', 'Actions'], fixed={'is Mobile': 'False'}, cells=[
  (('Section', '1'), 40, 40, 858, 36, []), (('Pills', '4'), 40, 116, 858, 36, []), (('Pills', '3'), 40, 192, 858, 36, []), (('Pills', '2'), 40, 268, 858, 36, []),
  (('Filter', '4'), 40, 344, 858, 36, []), (('Filter', '3'), 40, 420, 858, 36, []), (('Filter', '2'), 40, 496, 858, 36, []), (('Filter', '1'), 40, 572, 858, 36, []),
 ]),
]

# Información de cada componente (nombre, descripción y propiedades tal como están en Figma).
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
