# FID SDK · Sistema de diseño

La documentación completa del SDK de FID: fundamentos, tokens en las pantallas, personalización, accesibilidad y código.

**[Abrir el sistema de diseño →](https://ricardofalcondev.github.io/fid-sdk-sistema-de-diseno/)**

| Sección | Páginas |
|---|---|
| Empezar | Introducción, Personalización |
| Fundamentos | Color, Tipografía, Espaciado, Radios y bordes, Íconos, Ilustraciones y Lotties |
| Tokens en las pantallas | Firmar documento, Olvidé mi clave de firma, Flujo Alta, Errores: las 64 pantallas de desktop exportadas de Figma, con el token de cada parte |
| Calidad | Accesibilidad, Lista de verificación |
| Recursos | Enlaces, contenido del paquete y trabajo con IA |

Cada página tiene pestañas (Resumen, Guías, Tokens y Código, según corresponda) y un índice "En esta página".

Fuente de verdad: archivo de Figma "FID SDK — Variables". Si algo contradice a Figma, gana Figma.

## Regenerar

Requiere el paquete `FID SDK - Assets` (CSS, SVG, Lotties, `tokens.json` y `DESIGN.md`):

```bash
python3 fuente/build.py "ruta/a/FID SDK - Assets"
```
