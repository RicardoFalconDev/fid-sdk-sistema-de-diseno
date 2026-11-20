# Tokens del paquete (DESIGN.md) que se aplican en cada parte de las pantallas del SDK.
# Las pantallas y las cajas salen de Figma ("FID SDK — Variables", página Flujo) y están en pantallas.json
# (recorte x 300–1140 y desde abajo del header, que lo pone el integrador; imágenes a 2x en ../pantallas/).
# Cada clave: (nombre, tokens, sigue la marca, nota).

KEYS = {
 'bg': ('Fondo de la app', ['--bg-surface'], False, 'El fondo que rodea la tarjeta.'),
 'card': ('Tarjeta', ['--bg-default', '--stroke-default', '--radius-lg'], False, 'El contenedor del paso. Su radio es fijo: no cambia con el radio del cliente.'),
 'foot': ('Pie “Powered by FID”', ['--bg-surface'], False, 'El logo FID es fijo: no se personaliza.'),
 'th': ('Título', ['--text-primary'], False, 'Títulos y contenido principal.'),
 'tt': ('Título y descripción', ['--text-primary', '--text-secondary'], False, 'Título con su bajada.'),
 'tb': ('Texto', ['--text-secondary'], False, 'Cuerpo y descripciones.'),
 'tl': ('Texto con link', ['--text-secondary', '--text-link'], False, 'El link va subrayado y no cambia con la marca.'),
 'lk': ('Link', ['--text-link'], False, 'Links con subrayado. No cambia con la marca.'),
 'ta': ('Texto de apoyo', ['--text-tertiary'], False, 'Apoyo, metadatos y ayudas.'),
 'callout': ('Aviso', ['--feedback-warning-bg', '--text-secondary'], False, 'Fondo de advertencia, fijo.'),
 'bp': ('Botón primario', ['--button-primary-bg', '--button-primary-text', '--radius-button', '--font-family-default'], True, 'Cambia con las cuatro propiedades del cliente: color, color del texto, radio y fuente.'),
 'bs': ('Botón secundario', ['--button-secondary-bg', '--button-secondary-border', '--button-secondary-text', '--radius-button'], True, 'Los colores son fijos; el radio cambia con el cliente.'),
 'bd': ('Botón deshabilitado', ['--button-disabled-bg', '--button-disabled-border', '--button-disabled-text', '--radius-button'], True, 'Los colores son fijos; el radio cambia con el cliente.'),
 'oc': ('Celdas de código', ['--stroke-strong'], False, 'Borde de la celda de código.'),
 'of': ('Celda con foco', ['--stroke-primary', '--accent-4'], True, 'Borde de marca y aro de foco de 3 px con el paso 4 de la escala de acento.'),
 'os': ('Celdas con el código correcto', ['--feedback-success-border'], False, 'Estado de éxito, fijo.'),
 'oe': ('Celdas con el código incorrecto', ['--feedback-error-border'], False, 'Estado de error, fijo.'),
 'ha': ('Ayuda del campo', ['--text-tertiary'], False, 'Apoyo, metadatos y ayudas.'),
 'he': ('Mensaje de error', ['--feedback-error-text', '--feedback-error-icon'], False, 'Estado de error, fijo.'),
 'hs': ('Mensaje de éxito', ['--feedback-success-text', '--feedback-success-icon'], False, 'Estado de éxito, fijo.'),
 'pc': ('Campo de clave', ['--stroke-strong', '--text-primary', '--text-placeholder', '--text-tertiary'], False, 'Borde del campo, texto, placeholder y ayuda.'),
 'pf': ('Campo con foco', ['--stroke-primary', '--text-primary'], True, 'El borde de foco es el color de marca.'),
 'pe': ('Campo con error', ['--feedback-error-border', '--feedback-error-text'], False, 'Estado de error, fijo.'),
 'dv': ('Separador', ['--stroke-subtle'], False, 'Líneas finas.'),
 'li': ('Lista con tile de ícono', ['--brand-tint', '--stroke-brand-subtle', '--brand-default', '--text-primary'], True, 'Fondo, borde y color del ícono salen de la escala de acento.'),
 'ck': ('Casilla', ['--brand-default', '--button-primary-text'], True, 'El fondo es el color de marca y el tilde usa el color de texto del botón primario.'),
 'bi': ('Badge informativo', ['--feedback-info-bg', '--feedback-info-border', '--feedback-info-text'], False, 'Estado informativo, fijo.'),
 'pr': ('Progreso de lectura', ['--bg-muted', '--brand-default', '--text-primary', '--text-secondary'], True, 'La barra de avance es el color de marca.'),
 'sp': ('Spinner', ['--stroke-default', '--brand-default'], True, 'Pista gris y tramo de marca.'),
 'tp': ('Tooltip', ['--bg-inverse', '--text-inverse'], False, 'Fondo oscuro, fijo.'),
 'il': ('Ilustración', ['.ill-primary', '.ill-primary-50'], True, 'SVG inline: las partes de marca siguen el color del cliente.'),
 'lt_ok': ('Lottie de éxito', ['success-check.json'], False, 'Es fijo: verde, no se recolorea con la marca.'),
 'lt_face': ('Lottie del escáner facial', ['face-scan.json', '.lt-primary', '.lt-primary-50'], True, 'Se recolorea con tint-lottie.js.'),
 'lt_brand': ('Animación de marca', ['.lt-primary'], True, 'El azul sigue la marca.'),
 'cs': ('Lottie card skeleton', ['card-skeleton.json', '.lt-primary'], True, 'Sus rellenos azules siguen la marca con tint-lottie.js.'),
 'ae_err': ('Ícono de error', ['--feedback-error-bg', '--feedback-error-text'], False, 'Estado de error, fijo: no sigue la marca.'),
 'ae_warn': ('Ícono de advertencia', ['--feedback-warning-bg', '--feedback-warning-icon'], False, 'Estado de advertencia, fijo.'),
}

# Una página por flujo, en el orden de Figma.
FLOW_PAGES = [
 ('p-firmar', 'Firmar documento'),
 ('p-olvide', 'Olvidé mi clave de firma'),
 ('p-alta', 'Flujo Alta'),
 ('p-errores', 'Errores'),
]

# Estado que distingue pantallas con el mismo título.
ESTADOS = [('oe', 'con error'), ('pe', 'con error'), ('he', 'con error'), ('os', 'código correcto'), ('hs', 'código correcto'),
           ('of', 'con foco'), ('pf', 'con foco'), ('tp', 'con tooltip')]
