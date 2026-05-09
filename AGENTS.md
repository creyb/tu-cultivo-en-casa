# AGENTS.md

## Project Shape
- Small Hugo site (Spanish, Spain); config at `hugo.toml`; active theme is `themes/papermod` (regular directory, not a submodule).
- No root `package.json`, npm, test, lint, or codegen configs.
- Content sections: `content/guias-cultivo/`, `content/huerto-urbano/`, `content/cuidado-mantenimiento/`, `content/reviews-productos/`.
- Design system documented in `DESIGN.md` (colors, typography, layout conventions).
- Custom CSS lives at `assets/css/extended/custom.css` — heavily overrides PaperMod with the design system (colors, typography, card layouts, mobile nav, homepage hero).

## Commands
- `hugo` — build site into `public/`.
- `hugo server -D` — serve with drafts at `http://localhost:1313/`.
- Hugo `v0.161.0+extended` installed.

## Hugo Config
- `baseURL = 'https://creyb.github.io/tu-cultivo-en-casa/'`, `locale = 'es-es'`, `title = 'Tu Cultivo en Casa'`, `theme = "papermod"`.
- `params.mainSections` = `["guias-cultivo", "huerto-urbano", "cuidado-mantenimiento", "reviews-productos"]` — new content must use one of these section names to appear on the homepage.
- Taxonomies: `category = "categoria"` and `tag = "tag"`. Use front matter fields `categoria` and `tag` (not `categories`/`tags`).
- Main menu defined in `hugo.toml` with 4 entries: Guías, Huerto Urbano, Cuidado, Reviews.

## Layout & Theme Overrides
- Root `layouts/` overrides theme: `baseof.html`, `index.html`, `list.html`, `rss.xml`.
- `layouts/partials/header.html`, `footer.html`, `head.html` — custom header with sticky nav + mobile hamburger.
- `layouts/_default/single.html` — single post template.
- `layouts/_default/_markup/render-image.html` — Hugo render hook that adds `?v=2` cache-buster and `loading="lazy"` to all markdown images.
- `layouts/_partials/templates/` — template fragments (e.g., `opengraph.html`); check before adding new partials.
- Avoid editing `themes/papermod` directly. For site-specific changes, add files under root `layouts/`, `assets/css/extended/`, or `static/`.
- `custom.css` uses `!important` extensively to override PaperMod — follow this pattern for consistency.

## Content Creation
- New posts go under the appropriate content section; use `archetypes/default.md` as the front matter template.
- Posts default to `draft = false` in the archetype.
- Images at `/images/name.webp` → place in `static/images/name.webp`. Use WebP format.
- Body images in markdown: `![alt](/images/name.webp)` — rendered full-width by default via `custom.css`.

## CI / Deploy
- `.github/workflows/hugo.yml` builds and deploys to GitHub Pages on every push to `main`.
- CI uses Hugo `0.161.0` extended, installs Dart Sass, and builds with `--gc --minify --baseURL "https://creyb.github.io/tu-cultivo-en-casa/"`.
- Do not hand-edit `public/` or `resources/_gen/`; they are rebuild artifacts.

## Generated Files
- `public/`, `resources/_gen/`, `.hugo_build.lock` are Hugo outputs. Do not hand-edit.
- Edit source in `content/`, `hugo.toml`, `layouts/`, `assets/`, `static/`, or `archetypes/` then rebuild.

## Repo-local Skills
- `.agents/skills/` and `.claude/skills/` contain repo-local OpenCode/Claude skills (e.g., `hugo-content-generator`, `copywriting`, `seo-audit`, `frontend-design`). Load them via the `skill` tool when the task matches their description.
