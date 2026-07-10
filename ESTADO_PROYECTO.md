# Estado del proyecto y auditoría SEO

Fecha de revisión: 10 de julio de 2026.

## Resumen ejecutivo

`Tu Cultivo en Casa` está bien planteado como sitio nicho en Hugo: tiene arquitectura por silos, páginas pilar, posts largos, imágenes WebP, metadatos completos, breadcrumbs, canonical, sitemap generado por Hugo, robots activo, consentimiento de cookies y despliegue automatizado en GitHub Pages.

La base técnica es sólida. Las mejoras con más impacto ahora no son rehacer la web, sino reforzar autoridad, enriquecer datos estructurados, cerrar huecos de clústeres y mantener un control editorial más estricto.

Prioridades principales:

1. Añadir schema específico para FAQs y, en reviews, `Product`/`Review` cuando haya datos suficientes y no sea engañoso.
2. Reforzar E-E-A-T con página de autor más indexable o perfiles de autor, metodología real y señales de contacto.
3. Completar clústeres pendientes: otoño/invierno, cultivos fáciles, problemas comunes, poda y abonado.
4. Auditar Search Console cuando haya datos reales: queries, CTR, páginas con impresiones y canibalizaciones.
5. Mantener una revisión automática de caracteres CJK antes de publicar contenido largo.

## Estado actual

- CMS/generador: Hugo con PaperMod personalizado.
- Dominio canónico: `https://tucultivoencasa.com/`.
- Idioma: español (`defaultContentLanguage = "es"`).
- Secciones principales: `guias-cultivo`, `huerto-urbano`, `cuidado-mantenimiento`, `reviews-productos`.
- Contenido Markdown revisado: 26 archivos.
- Posts/secciones en silos principales: 23 archivos.
- Páginas legales/raíz: `about.md`, `aviso-legal.md`, `politica-cookies.md`.
- Frontmatter obligatorio en posts publicados: sin faltas detectadas en la revisión.
- Imágenes: WebP en `static/images/`.
- CI/CD: GitHub Pages con Hugo `0.161.0`, `--gc`, `--minify` y `baseURL` de producción.

## Arquitectura y clústeres

### Silos existentes

- `guias-cultivo`: cultivo por especie o familia. Actualmente cubre tomate cherry, pimientos, aromáticas y zanahorias.
- `huerto-urbano`: planificación transversal y calendarios. Actualmente cubre junio, julio, agosto y asociaciones.
- `cuidado-mantenimiento`: riego, plagas, compostaje, vacaciones, hongos y control biológico.
- `reviews-productos`: macetas, riego por goteo y sustrato.

### Lectura SEO

La arquitectura es coherente para un sitio informacional/afiliación. Las páginas pilar enlazan a artículos hijos y los posts tienen módulo de relacionados por `categoria` y `tag`, lo que ayuda a distribuir autoridad interna.

El clúster más fuerte es `cuidado-mantenimiento`, especialmente plagas/riego/verano. El clúster más monetizable es `reviews-productos`, pero todavía es pequeño. `guias-cultivo` necesita más cobertura de cultivos básicos para competir por long tails de principiantes.

### Huecos recomendados

- Cultivos: lechuga, fresas, calabacín en maceta, judías verdes, rabanitos, espinacas, menta/romero/tomillo.
- Temporada: qué plantar en septiembre, octubre, noviembre, invierno y calendario anual descargable.
- Problemas: hojas amarillas, puntas secas, exceso de riego, falta de sol, trasplante fallido, flores que se caen.
- Mantenimiento: poda de tomate, abonado por cultivo, rotación en macetas, limpieza de sustrato usado.
- Reviews: jardineras autorriego, humus de lombriz, tijeras de poda, mesas de cultivo, mallas de sombreo, pulverizadores.

## Auditoría técnica SEO

### Fortalezas

- `enableRobotsTXT = true` en `hugo.toml`.
- Canonical self-referencing en `layouts/partials/head.html`.
- Meta robots con `index, follow` en producción y `noindex` fuera de producción.
- Noindex aplicado a páginas legales y páginas raíz no transaccionales.
- Breadcrumbs visibles y schema `BreadcrumbList`.
- Schema `BlogPosting` en páginas de contenido.
- Open Graph configurado con título, descripción, imagen y datos de artículo.
- Sitemap generado por Hugo y ping automático a Google/Bing tras deploy.
- Imágenes en formato WebP y lazy loading en imágenes Markdown.
- Cookie consent con Consent Mode v2 para GA4.

### Hallazgos técnicos

- Impacto alto: falta schema específico para FAQs visibles. Hay artículos con secciones FAQ, pero solo se genera `BlogPosting` y `BreadcrumbList`.
- Impacto medio: reviews sin schema de producto/review. Debe añadirse solo si el contenido representa productos concretos con datos verificables y sin afirmar pruebas propias cuando no existan.
- Impacto medio: `about.md` está en `noindex`. Es correcto si se considera página legal/interna, pero limita señales E-E-A-T públicas. Conviene valorar una página de autor o equipo indexable diferente de la legal.
- Impacto medio: algunas imágenes de cards no tienen `width`/`height`, lo que puede afectar CLS según plantilla y CSS.
- Impacto bajo: `meta keywords` está presente. No perjudica, pero Google no lo usa y no debería ser prioridad.

## Auditoría on-page

### Fortalezas

- Titles descriptivos y alineados con intención de búsqueda.
- Descripciones y summaries completos en posts.
- H1 único en plantillas principales.
- TOC activo por defecto.
- Enlazado interno manual entre silos y relacionado automático.
- Voz consistente: cercana, práctica y basada en experiencia.

### Hallazgos on-page

- Impacto alto: se detectaron caracteres CJK incrustados en tres artículos. Ya se corrigieron en esta revisión.
- Impacto medio: algunas promesas de experiencia en reviews pueden entrar en tensión con disclaimers de artículos basados en datos públicos de Amazon. Mantener consistencia: si no se ha probado, decirlo claramente en título, intro y conclusión.
- Impacto medio: las páginas pilar son buenas, pero algunas listas de "próximamente" deberían convertirse en enlaces reales a medida que se publiquen para evitar sensación de sitio incompleto.
- Impacto bajo: revisar cada meta description para que no supere demasiado 155-160 caracteres en las páginas más importantes.

## E-E-A-T y confianza

### Bien resuelto

- Transparencia de afiliados en reviews.
- Aviso legal y política de cookies.
- Tono de experiencia propia.
- Metodología editorial explicada en `reviews-productos/_index.md`.

### Mejorable

- Añadir página de autor/equipo indexable con experiencia concreta, fotos propias si existen y metodología de pruebas.
- Añadir página de contacto o formulario simple.
- Marcar fechas de actualización en artículos sensibles: comparativas, precios, calendarios y tratamientos.
- Incluir más fotos propias o pruebas visuales reales cuando sea posible.

## Backlog priorizado

### Prioridad alta

- Implementar schema `FAQPage` para páginas con bloques FAQ reales.
- Revisar coherencia de claims en reviews: "probado", "datos de Amazon", "hemos seleccionado", "hemos usado".
- Crear página indexable de autor/metodología si se quiere reforzar confianza orgánica.
- Publicar 3-5 posts de problemas comunes: hojas amarillas, exceso de riego, falta de floración, caída de flores, sustrato compactado.

### Prioridad media

- Crear clúster de otoño/invierno: septiembre, octubre, noviembre, invierno y calendario anual.
- Añadir más reviews monetizables con intención BOFU: jardineras autorriego, mesas de cultivo, humus de lombriz, tijeras de poda.
- Añadir `width` y `height` a imágenes de cards/listados donde falten.
- Crear una hoja de keyword mapping por URL para evitar canibalización.

### Prioridad baja

- Revisar longitud de titles/descriptions en masa.
- Añadir `sameAs` y datos de organización/persona en `hugo.toml` si hay perfiles sociales reales.
- Crear recursos descargables: checklist de vacaciones, calendario de siembra anual, tabla de riego por cultivo.

## Protocolo de mantenimiento

Antes de publicar un post nuevo:

1. Usar fecha real del día de publicación en frontmatter.
2. Confirmar `summary`, `description`, `categoria`, `tag`, `cover`, `featured_image`.
3. Revisar enlaces internos hacia una página pilar y 2-4 artículos relacionados.
4. Añadir aviso de afiliados antes del primer enlace comercial.
5. Escanear caracteres CJK con el comando indicado en `AGENTS.md`.
6. Ejecutar `hugo --gc --minify --baseURL "https://tucultivoencasa.com/"` antes de desplegar si es posible.

## Comandos útiles

- Desarrollo local: `hugo server -D`.
- Build de producción local: `hugo --gc --minify --baseURL "https://tucultivoencasa.com/"`.
- Escaneo CJK de todo el contenido: `python -c "import pathlib,re; r=re.compile(r'[\\u4e00-\\u9fff\\u3040-\\u309f\\u30a0-\\u30ff]'); print([(str(p), len(r.findall(p.read_text(encoding='utf-8-sig')))) for p in pathlib.Path('content').rglob('*.md') if r.search(p.read_text(encoding='utf-8-sig'))])"`.

## Registro de cambios

- 2026-07-10: auditoría general inicial, creación de este archivo y corrección de tres fragmentos con caracteres CJK incrustados.
