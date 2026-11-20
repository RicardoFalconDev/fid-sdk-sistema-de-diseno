# Pantallas reales del SDK exportadas de Figma ("FID SDK — Variables", página Flujo) con los tokens
# del paquete que se aplican en cada parte. Los tokens salen de DESIGN.md (catálogo y recetas), no de
# las variables que tienen vinculadas los componentes en Figma (son de la librería vieja).
# Recorte: x 300–1140 de la pantalla de 1440 (imagen a 2x). Cajas en px a 1x dentro del recorte: (x, y, w, h).
# marca=True: el token cambia con la personalización del cliente (primary, primaryText, radius o font).

SCREENS = [
 dict(key='inicio', title='Inicio del flujo', node='8:55858', seccion='Flujo Alta · Inicio Onboarding', w=840, h=800,
  desc='La primera pantalla del alta: ilustración, título, lista de pasos, casilla de términos y botón primario.',
  spots=[
   ('Fondo de la app', (0, 72, 840, 728), ['--bg-surface'], False, 'El fondo gris claro que rodea la tarjeta.'),
   ('Header', (0, 0, 840, 72), ['--bg-default', '--stroke-subtle'], False, 'Fondo blanco y la línea fina de abajo.'),
   ('Tarjeta', (120, 96, 600, 636), ['--bg-default', '--stroke-default', '--radius-lg'], False, 'El contenedor del paso. El radio de la tarjeta es fijo: no cambia con el radio del cliente.'),
   ('Ilustración', (370, 132, 100, 84), ['.ill-primary', '--brand-default'], True, 'ill-onboarding pintada con la clase .ill-primary: sigue el color de marca.'),
   ('Título', (152, 248, 536, 30), ['--text-primary'], False, 'Títulos y contenido principal.'),
   ('Descripción', (152, 282, 536, 50), ['--text-secondary'], False, 'Cuerpo y descripciones.'),
   ('Tiles de ícono', (152, 372, 40, 152), ['--brand-tint', '--stroke-brand-subtle', '--brand-default'], True, 'Fondo, borde y color del ícono salen de la escala de acento.'),
   ('Casilla', (152, 580, 24, 24), ['--brand-default', '--button-primary-text'], True, 'El fondo es el color de marca y el tilde usa el color de texto del botón primario.'),
   ('Botón primario', (288, 652, 265, 48), ['--button-primary-bg', '--button-primary-text', '--radius-button', '--font-family-default'], True, 'Acá se ven las cuatro propiedades del cliente: color, color del texto, radio y fuente.'),
   ('Pie “Powered by FID”', (120, 732, 600, 32), ['--bg-surface'], False, 'El logo FID es fijo: no se personaliza.'),
  ]),
 dict(key='otp', title='Código de seguridad', node='8:19476', seccion='Firmar documento · OTP', w=840, h=676,
  desc='Ingreso del código: celdas con foco, link, ayuda y botones secundario y deshabilitado.',
  spots=[
   ('Ilustración', (358, 124, 128, 100), ['.ill-primary', '--brand-default'], True, 'ill-sms pintada con .ill-primary: sigue el color de marca.'),
   ('Link', (366, 314, 248, 22), ['--text-link'], False, 'Links con subrayado. No cambia con la marca.'),
   ('Celda con foco', (144, 382, 72, 72), ['--stroke-primary', '--accent-4'], True, 'Borde de marca y aro de foco de 3 px con el paso 4 de la escala de acento.'),
   ('Celdas de código', (240, 382, 456, 72), ['--stroke-strong'], False, 'Borde de los campos y de la celda de código.'),
   ('Ayuda', (144, 462, 552, 18), ['--text-tertiary'], False, 'Apoyo, metadatos y ayudas.'),
   ('Botón secundario', (144, 532, 264, 48), ['--button-secondary-bg', '--button-secondary-border', '--button-secondary-text', '--radius-button'], True, 'Los colores son fijos; el radio sí cambia con el cliente.'),
   ('Botón deshabilitado', (432, 532, 264, 48), ['--button-disabled-bg', '--button-disabled-border', '--button-disabled-text', '--radius-button'], True, 'Colores fijos; el radio sí cambia con el cliente.'),
  ]),
 dict(key='error', title='Error recuperable', node='8:57174', seccion='Errores · Error genérico recuperable', w=840, h=608,
  desc='Un error del que se puede salir reintentando: ilustración fija, título, descripción y botón primario.',
  spots=[
   ('Ilustración de error', (384, 194, 72, 72), ['error-x'], False, 'error-x es fija: no sigue la marca, para que el error se lea siempre igual.'),
   ('Título', (195, 302, 450, 30), ['--text-primary'], False, 'Títulos y contenido principal.'),
   ('Descripción', (195, 334, 450, 24), ['--text-secondary'], False, 'Cuerpo y descripciones.'),
   ('Botón primario', (292, 390, 256, 48), ['--button-primary-bg', '--button-primary-text', '--radius-button', '--font-family-default'], True, 'El mismo botón primario: cambia con las cuatro propiedades del cliente.'),
  ]),
]
