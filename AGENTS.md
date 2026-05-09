# AGENTS.md

## Commands
- `hugo server -D` — local dev with drafts at `http://localhost:1313/`.
- `hugo` — build into `public/`.
- Requires Hugo `v0.161.0+extended`.

## Content Voice & Tone
- **Persona**: "Amigo experto" — cercano, práctico y basado en experiencia real.
- **Register**: Primera persona del plural ("He probado..."). Evitar impersonal ("se recomienda").
- **Style**: Directo, con frases cortas y consejos accionables. Usa emojis con moderación (🌱, 💧, 🍅, ✅, ⚠️) para dar dinamismo y escanabilidad.
- **Reviews**: Evitar exageraciones tipo "¡el mejor del mundo!". Ser honesto: pros, contras, y para quién es ideal.
- **Consistency**: Mantener el mismo ritmo, longitud de frases y nivel de detalle entre posts.

## Content Gotchas
- New posts must use one of `params.mainSections` to appear on the homepage: `guias-cultivo`, `huerto-urbano`, `cuidado-mantenimiento`, `reviews-productos`.
- Taxonomies are renamed: use front matter keys `categoria` and `tag` (not `categories`/`tags`).
- Place images in `static/images/name.webp` (WebP only). Markdown images are automatically cache-busted (`?v=2`) and lazily-loaded by `layouts/_default/_markup/render-image.html`.
- Use `archetypes/default.md` for front matter template.
- Legal pages exist at root: `about.md`, `aviso-legal.md`, `politica-cookies.md`. Mark legal pages with `noindex: true` and `hiddenInHomeList: true`.

## Layout Features
- **TOC**: enabled by default (`ShowToc = true` in `hugo.toml`). Custom collapsible styling in `layouts/partials/toc.html`.
- **Breadcrumbs**: enabled (`ShowBreadCrumbs = true`).
- **Cookie consent**: GDPR banner via `layouts/partials/cookie-consent.html`. Categories: necessary, analytics, marketing (affiliates). Do not remove the partial from `footer.html`.
- **Footer**: hardcoded links to `/aviso-legal/` and `/politica-cookies/` in `layouts/partials/footer.html`.

## Theme & Styling
- Do not edit `themes/papermod/` directly. Override via root `layouts/`, `assets/css/extended/`, or `static/`.
- `assets/css/extended/custom.css` overrides PaperMod with `!important` throughout — follow this pattern.
- Design tokens are in `DESIGN.md`.

## CI / Deploy
- `.github/workflows/hugo.yml` deploys to GitHub Pages on push to `main`.
- CI builds with: `--gc --minify --baseURL "https://tucultivoencasa.com/"`.
- Post-deploy job pings Google and Bing sitemaps automatically.
- Custom domain via `static/CNAME` (`tucultivoencasa.com`). Do not remove or rename this file.
- Do not hand-edit `public/`, `resources/_gen/`, or `.hugo_build.lock`.

## Repo-local Skills
- `.agents/skills/` and `.claude/skills/` contain repo-local skills (e.g., `hugo-content-generator`, `copywriting`, `seo-audit`). Load via the `skill` tool when applicable.
