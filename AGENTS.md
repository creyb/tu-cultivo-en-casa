# AGENTS.md

## Project Shape
- This is a small Hugo site rooted at `hugo.toml`; the active theme is the `themes/ananke` git submodule.
- Do not treat `themes/ananke/package.json` as the site manifest. Its npm scripts are for Ananke theme development, not normal site work.
- Root content can be section-based, e.g. `content/posts/` publishes under `/posts/` and `content/huerto-urbano/` publishes under `/huerto-urbano/`. There are no root npm, test, lint, CI, or codegen configs in this repo.

## Commands
- Run from the repo root: `hugo` to build the site into `public/`.
- Run from the repo root: `hugo server -D` to serve drafts and published content at `http://localhost:1313/`.
- The installed/verified Hugo is `v0.161.0+extended`; Ananke declares a minimum Hugo version of `0.160.0`.

## Hugo Content Notes
- `hugo.toml` sets `baseURL = 'https://example.org/'`, `locale = 'en-us'`, `title = 'My New Hugo Project'`, and `theme = "ananke"`.
- Ananke home recent posts come from `params.mainSections`; keep new content sections there if they should appear on the homepage.
- Taxonomies are customized as `category = "categoria"` and `tag = "tag"`. Use front matter fields `categoria` and `tag` if you want taxonomy pages under `/categoria/` and `/tag/`; conventional `categories`/`tags` fields do not populate those configured taxonomy pages.
- Images referenced as `/images/name.jpg` should be placed in `static/images/name.jpg`; Hugo publishes `static/` files at the site root.

## Generated Files
- `public/`, `resources/_gen/`, and `.hugo_build.lock` are Hugo-generated outputs. They are currently tracked or present, and running `hugo` can dirty them; do not hand-edit generated HTML/CSS there.
- Prefer editing source files in `content/`, `hugo.toml`, `layouts/`, `assets/`, `static/`, or `archetypes/` and then rebuild.

## Theme Boundary
- `themes/ananke` is a submodule from `https://github.com/theNewDynamic/gohugo-theme-ananke`; avoid editing it for site-specific changes unless the task explicitly requires theme work.
- For site-specific presentation overrides, add files under root `layouts/`, `assets/`, or `static/` rather than modifying the theme submodule.
