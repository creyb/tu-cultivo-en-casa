# AGENTS.md

## Project Shape
- Small Hugo site (Spanish, Spain); config at `hugo.toml`; active theme is `themes/papermod` (regular directory, not a submodule).
- `.gitmodules` still references `themes/ananke` but the submodule is not initialized; ignore it.
- No root npm, test, lint, CI, or codegen configs.
- Content sections: `content/guias-cultivo/`, `content/huerto-urbano/`, `content/cuidado-mantenimiento/`, `content/reviews-productos/`.
- Design system documented in `DESIGN.md` (colors, typography, layout conventions).
- Custom CSS lives at `assets/css/extended/custom.css` — heavily overrides PaperMod with the design system (colors, typography, card layouts, mobile nav, homepage hero).

## Commands
- `hugo` — build site into `public/`.
- `hugo server -D` — serve with drafts at `http://localhost:1313/`.
- Hugo `v0.161.0+extended` installed.

## Hugo Config
- `baseURL = 'https://example.org/'`, `locale = 'es-es'`, `title = 'Tu Cultivo en Casa'`, `theme = "papermod"`.
- `params.mainSections` = `["guias-cultivo", "huerto-urbano", "cuidado-mantenimiento", "reviews-productos"]` — new content must use one of these section names to appear on the homepage.
- Taxonomies: `category = "categoria"` and `tag = "tag"`. Use front matter fields `categoria` and `tag` (not `categories`/`tags`).
- Main menu defined in `hugo.toml` with 4 entries: Guías, Huerto Urbano, Cuidado, Reviews.

## Layout Structure
- Root `layouts/` overrides theme: `baseof.html`, `index.html`, `list.html`, `rss.xml`.
- `layouts/partials/header.html` and `footer.html` — custom header with sticky nav + mobile hamburger.
- `layouts/_default/single.html` — single post template.
- `layouts/_partials/templates/` — template fragments (check before adding new partials).

## Content Creation
- New posts go under the appropriate content section; use `archetypes/default.md` as the front matter template.
- Posts default to `draft = false` in the archetype.
- Images at `/images/name.webp` → place in `static/images/name.webp`. Use WebP format.
- Body images in markdown: `![alt](/images/name.webp)` — rendered full-width by default via `custom.css`.

## Generated Files
- `public/`, `resources/_gen/`, `.hugo_build.lock` are Hugo outputs. Do not hand-edit.
- Edit source in `content/`, `hugo.toml`, `layouts/`, `assets/`, `static/`, or `archetypes/` then rebuild.

## Theme Boundary
- `themes/papermod` is the active theme; avoid editing it for site-specific changes.
- For site-specific overrides, add files under root `layouts/`, `assets/css/extended/`, or `static/`.
- `custom.css` uses `!important` extensively to override PaperMod — follow this pattern for consistency.
