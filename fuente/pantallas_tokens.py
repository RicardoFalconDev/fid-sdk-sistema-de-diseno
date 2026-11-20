# Tokens del paquete (DESIGN.md) que se aplican en cada parte de las pantallas del SDK.
# Las pantallas y las cajas salen de Figma ("FID SDK — Variables", página Flujo) y están en pantallas.json
# (recorte x 300–1140 y desde abajo del header, que lo pone el integrador; imágenes a 2x en ../pantallas/).
# pantallas_medidas.json trae, por pantalla y por parte, los estilos de texto (tamaño/interlineado/peso)
# y el radio medidos en Figma; build.py los cruza con los estilos de texto y los radios del paquete.
# Cada clave: (nombre, [(función, token)], nota). La tipografía, la fuente y el radio se agregan solos.

KEYS = {
 'bg': ('Fondo de la app', [('Fondo', '--bg-surface')], 'El fondo que rodea la tarjeta.'),
 'card': ('Tarjeta', [('Fondo', '--bg-default'), ('Borde', '--stroke-default'), ('Radio', '--radius-lg')], 'El contenedor del paso. Su radio es fijo: no cambia con el radio del cliente.'),
 'foot': ('Pie “Powered by FID”', [('Fondo', '--bg-surface')], 'El logo FID es fijo: no se personaliza.'),
 'th': ('Título', [('Texto', '--text-primary')], ''),
 'tt': ('Título y descripción', [('Título', '--text-primary'), ('Descripción', '--text-secondary')], ''),
 'tb': ('Texto', [('Texto', '--text-secondary')], ''),
 'tl': ('Texto con link', [('Texto', '--text-secondary'), ('Link', '--text-link')], 'El link va subrayado y no cambia con la marca.'),
 'lk': ('Link', [('Texto', '--text-link')], 'Links con subrayado. No cambia con la marca.'),
 'ta': ('Texto de apoyo', [('Texto', '--text-tertiary')], ''),
 'callout': ('Aviso', [('Fondo', '--feedback-warning-bg'), ('Texto', '--text-secondary')], 'Fondo de advertencia, fijo.'),
 'bp': ('Botón primario', [('Fondo', '--button-primary-bg'), ('Texto', '--button-primary-text')], 'Cambia con las cuatro propiedades del cliente.'),
 'bs': ('Botón secundario', [('Fondo', '--button-secondary-bg'), ('Borde', '--button-secondary-border'), ('Texto', '--button-secondary-text')], 'Los colores son fijos; el radio y la fuente cambian con el cliente.'),
 'bd': ('Botón deshabilitado', [('Fondo', '--button-disabled-bg'), ('Borde', '--button-disabled-border'), ('Texto', '--button-disabled-text')], 'Los colores son fijos; el radio y la fuente cambian con el cliente.'),
 'oc': ('Celdas de código', [('Borde', '--stroke-strong')], ''),
 'of': ('Celda con foco', [('Borde', '--stroke-primary'), ('Aro de foco', '--accent-4')], 'Aro de 3 px, sin desenfoque.'),
 'os': ('Celdas con el código correcto', [('Borde', '--feedback-success-border')], 'Estado de éxito, fijo.'),
 'oe': ('Celdas con el código incorrecto', [('Borde', '--feedback-error-border')], 'Estado de error, fijo.'),
 'ha': ('Ayuda del campo', [('Texto', '--text-tertiary')], ''),
 'he': ('Mensaje de error', [('Texto', '--feedback-error-text'), ('Ícono', '--feedback-error-icon')], 'Estado de error, fijo.'),
 'hs': ('Mensaje de éxito', [('Texto', '--feedback-success-text'), ('Ícono', '--feedback-success-icon')], 'Estado de éxito, fijo.'),
 'pc': ('Campo de clave', [('Borde', '--stroke-strong'), ('Texto', '--text-primary'), ('Placeholder', '--text-placeholder'), ('Ayuda', '--text-tertiary')], ''),
 'pf': ('Campo con foco', [('Borde', '--stroke-primary'), ('Texto', '--text-primary')], 'El borde de foco es el color de marca.'),
 'pe': ('Campo con error', [('Borde', '--feedback-error-border'), ('Mensaje', '--feedback-error-text')], 'Estado de error, fijo.'),
 'dv': ('Separador', [('Línea', '--stroke-subtle')], ''),
 'li': ('Lista con tile de ícono', [('Fondo del tile', '--brand-tint'), ('Borde del tile', '--stroke-brand-subtle'), ('Ícono', '--brand-default'), ('Texto', '--text-primary')], ''),
 'ck': ('Casilla', [('Fondo', '--brand-default'), ('Tilde', '--button-primary-text')], ''),
 'bi': ('Badge informativo', [('Fondo', '--feedback-info-bg'), ('Borde', '--feedback-info-border'), ('Texto', '--feedback-info-text')], 'Estado informativo, fijo.'),
 'pr': ('Progreso de lectura', [('Pista', '--bg-muted'), ('Avance', '--brand-default'), ('Texto', '--text-primary'), ('Contador', '--text-secondary')], ''),
 'sp': ('Spinner', [('Pista', '--stroke-default'), ('Tramo', '--brand-default')], ''),
 'tp': ('Tooltip', [('Fondo', '--bg-inverse'), ('Texto', '--text-inverse')], ''),
 'il': ('Ilustración', [('Partes de marca', '.ill-primary'), ('Partes suaves', '.ill-primary-50')], 'SVG inline: el color lo pone el CSS.'),
 'lt_ok': ('Lottie de éxito', [('Archivo', 'success-check.json')], 'Es fijo: verde, no se recolorea con la marca.'),
 'lt_face': ('Lottie del escáner facial', [('Archivo', 'face-scan.json'), ('Trazo', '.lt-primary'), ('Silueta', '.lt-primary-50')], 'Se recolorea con tint-lottie.js.'),
 'lt_brand': ('Animación de marca', [('Color', '.lt-primary')], ''),
 'cs': ('Lottie card skeleton', [('Archivo', 'card-skeleton.json'), ('Rellenos', '.lt-primary')], 'Se recolorea con tint-lottie.js.'),
 'ae_err': ('Ícono de error', [('Fondo', '--feedback-error-bg'), ('Ícono', '--feedback-error-text')], 'Estado de error, fijo: no sigue la marca.'),
 'ae_warn': ('Ícono de advertencia', [('Fondo', '--feedback-warning-bg'), ('Ícono', '--feedback-warning-icon')], 'Estado de advertencia, fijo.'),
}

# Clave de las medidas de Figma para cada clave final.
MEDIDA = {'ae_err': 'ae', 'ae_warn': 'ae', 'lt_ok': 'lt', 'lt_face': 'lt', 'lt_brand': 'lt', 'cs': 'im', 'callout': 'ta'}

# Partes que siempre usan --radius-button (el radio que elige el cliente).
RADIO_BOTON = {'bp', 'bs', 'bd'}
# Partes cuyo radio medido incluye el aro de foco de 3 px.
CON_ARO = {'of', 'pf'}
# Partes donde no se informa el radio medido (la forma es del ícono o del componente).
SIN_RADIO = {'sp', 'card', 'bg', 'foot'}

# Una página por flujo, en el orden que pidió el usuario.
FLOW_PAGES = [
 ('p-alta', 'Flujo Alta'),
 ('p-firmar', 'Firmar documento'),
 ('p-errores', 'Errores'),
 ('p-olvide', 'Olvidé mi clave de firma'),
]

# Nombre de la variación según lo que tiene la pantalla.
ESTADOS = [('oe', 'Con error'), ('pe', 'Con error'), ('he', 'Con error'), ('os', 'Código correcto'), ('hs', 'Código correcto'),
           ('of', 'Con foco'), ('pf', 'Con foco'), ('tp', 'Con tooltip')]
