# Trevanto Industrial — Sitio web (catálogo)

Página web tipo catálogo para Trevanto Industrial, comercializadora de suministros para empaque industrial (cintas, film stretch, flejes, cajas, bolsas, grapas, protección de carga y seguridad industrial).

## Estructura

```
index.html          → sitio final, autocontenido (HTML+CSS+JS+imágenes en base64). Listo para publicar tal cual.
src/template.html   → plantilla editable (con marcadores {{LOGO_HORIZONTAL}}, {{LOGO_ICON}}, {{HERO_BANNER}} y CATALOG_CARDS)
src/build.py        → script que genera index.html a partir de template.html + src/assets/*
src/assets/         → logo horizontal, ícono y banner de héroe usados por el build
```

## Cómo editar el sitio

1. Edita `src/template.html` (estilos, secciones, textos) o las imágenes en `src/assets/`.
2. Regenera el sitio final:
   ```bash
   python3 src/build.py
   ```
3. Esto sobreescribe `index.html` en la raíz del repo.

## Cómo verlo localmente

Basta con abrir `index.html` en el navegador (no requiere servidor ni build tools para verlo).

## Publicarlo (GitHub Pages)

Con el repo ya en GitHub: Settings → Pages → Deploy from a branch → selecciona `main` y carpeta `/ (root)`. El sitio quedará disponible en `https://<usuario>.github.io/<repo>/`.

## Pendientes conocidos

- Teléfono/WhatsApp y ubicación en la sección de Contacto siguen como marcadores `[Pendiente]`.
- Fotos reales de producto (por ahora se usan íconos).
- Confirmar nombre/logo oficial: "Trevanto Industrial" (usado aquí) vs. "Trevanto Suministros" (nombre documentado previamente en el proyecto de Claude).
