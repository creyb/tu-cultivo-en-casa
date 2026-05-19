# AGENTS.md

## Commands
- `hugo server -D` — local dev with drafts at `http://localhost:1313/`.
- `hugo` — build into `public/`.
- Requires Hugo `v0.161.0+extended`.

## Critical Config
- `[markup.goldmark.renderer] unsafe = true` is **enabled** in `hugo.toml`. Raw HTML in markdown content renders as HTML (required for affiliate links, custom markup). Do **not** disable this.
- Taxonomies are remapped: front matter keys are `categoria` and `tag` (not `categories`/`tags`).

## Content Architecture
- Posts must live under one of `params.mainSections` to appear on the homepage: `guias-cultivo`, `huerto-urbano`, `cuidado-mantenimiento`, `reviews-productos`.
- Each section has an `_index.md` for its listing page.
- The default archetype (`archetypes/default.md`) only supplies `date`, `draft`, `title`. Production posts need additional front matter manually (see existing posts for the pattern):
  - `summary` — card/listing excerpt
  - `description` — SEO meta description
  - `categoria` — array, e.g., `["guias-cultivo"]`
  - `tag` — array of strings
  - `cover.image`, `cover.title`, `cover.alt`
  - `featured_image` — same path as `cover.image` (used by layouts)
- Legal pages at root (`about.md`, `aviso-legal.md`, `politica-cookies.md`) must include `noindex: true` and `hiddenInHomeList: true`.

## Images
- Place images in `static/images/name.webp` (WebP only).
- `layouts/_default/_markup/render-image.html` automatically appends `?v=2`, adds `loading="lazy"`, and hardcodes `width="800" height="450"` on all markdown images. If you need different dimensions or behavior, use raw `<img>` HTML.

## Affiliate Links
- Amazon affiliate links must be raw HTML (not markdown) with:
  ```html
  <a href="..." target="_blank" rel="noopener noreferrer nofollow">...</a>
  ```
- Always include a disclaimer paragraph near the first affiliate link.

## Theme & Styling
- Do not edit `themes/papermod/` directly. Override via root `layouts/`, `assets/css/extended/`, or `static/`.
- `assets/css/extended/custom.css` overrides PaperMod using `!important` throughout — follow this pattern for any new rules.
- Design tokens are defined in `DESIGN.md`.

## Layout Features
- **TOC**: enabled by default (`ShowToc = true`). Custom collapsible styling in `layouts/partials/toc.html`.
- **Breadcrumbs**: enabled (`ShowBreadCrumbs = true`).
- **Cookie consent**: GDPR banner via `layouts/partials/cookie-consent.html`. Categories: necessary, analytics, marketing (affiliates). Do not remove the partial from `footer.html`.
- **Footer**: hardcoded links to `/aviso-legal/` and `/politica-cookies/` in `layouts/partials/footer.html`.

## CI / Deploy
- `.github/workflows/hugo.yml` deploys to GitHub Pages on push to `main`.
- CI builds with: `--gc --minify --baseURL "https://tucultivoencasa.com/"`.
- Post-deploy job pings Google and Bing sitemaps automatically.
- Custom domain via `static/CNAME` (`tucultivoencasa.com`). Do not remove or rename this file.
- Do not hand-edit `public/`, `resources/_gen/`, or `.hugo_build.lock`. CI regenerates these; local `hugo` runs will dirty the working tree.

## Content Voice & Tone
- **Persona**: "Amigo experto" — cercano, práctico y basado en experiencia real.
- **Register**: Primera persona del plural ("He probado..."). Evitar impersonal ("se recomienda").
- **Style**: Directo, con frases cortas y consejos accionables. Usa emojis con moderación (🌱, 💧, 🍅, ✅, ⚠️) para dinamismo y escaneabilidad.
- **Reviews**: Evitar exageraciones tipo "¡el mejor del mundo!". Ser honesto: pros, contras, y para quién es ideal.
- **Consistency**: Mantener el mismo ritmo, longitud de frases y nivel de detalle entre posts.

## Repo-local Skills
- `.agents/skills/` and `.claude/skills/` contain repo-local skills (e.g., `hugo-content-generator`, `copywriting`, `seo-audit`). Load via the `skill` tool when applicable.
