#!/usr/bin/env python3
"""Download Fal-generated images for the drip irrigation kit article, upscale to 1600x900, convert to WebP.

This script mirrors the pattern in generate_vacation_images.py. Before running,
the four PNG images must be generated with fal-ai/flux-2-pro using the prompts
in the docstring of each entry. The CDN URLs from fal.media should be pasted
into the `url` field of each image dict.

Once you have the URLs, run this script to download, upscale (Lanczos 1600x900),
and convert each PNG to WebP quality 85 method 6, saved in static/images/.

The article content/reviews-productos/mejores-kits-riego-por-goteo-huerto-urbano-comparativa.md
references these files:

- kit-riego-goteo-huerto-hero.webp       (hero)
- componentes-kit-riego-goteo.webp       (kit parts)
- comparativa-kits-riego-goteo.webp      (product lineup)
- instalacion-riego-goteo-balcon.webp    (installation on balcony)

Suggested Flux 2 Pro prompts (no text, no letters):

1. kit-riego-goteo-huerto-hero.webp
   "A photorealistic close-up of a drip irrigation system running through several terracotta and grey plastic pots on a sunny urban balcony. Thin black tubing with small drip emitters, lush green tomato and lettuce plants, warm afternoon light, shallow depth of field, bokeh background. No text. 16:9 composition."

2. componentes-kit-riego-goteo.webp
   "Top-down studio still life of drip irrigation components arranged neatly on a light wooden table: roll of black PE tubing, coiled micro-tubing, handful of pressure-compensating drippers, tees, elbows, mesh filter, pressure regulator. Soft natural light, neutral background, no text, no labels. 16:9."

3. comparativa-kits-riego-goteo.webp
   "Lineup of five different drip irrigation kits displayed on a light surface: budget solar kit, mid-range gravity tank system, premium Gardena and Hozelock kits with branded packaging, plus a small Spanish brand kit. Soft directional light, shallow depth of field, urban garden props in the back. No text. 16:9."

4. instalacion-riego-goteo-balcon.webp
   "A person's hands installing a drip irrigation system on a small urban balcony, threading micro-tubing from a PE main line into a row of pots with herbs and tomatoes. Tools nearby. Warm golden hour light, realistic and authentic mood, no text. 16:9."

Usage:
  1. Generate the 4 PNGs with fal-ai/flux-2-pro (endpoint_id, image_size=landscape_16_9, output_format=png).
  2. Paste the returned fal.media URLs into the `url` fields below.
  3. Run: python scripts/generate_drip_kit_images.py
"""
import urllib.request
import os
import io
from PIL import Image

IMAGES = [
    {
        "url": "https://v3b.fal.media/files/b/0a9dc44c/sKFqti6AGU2cM0bdm65xe_6sRdy26S.png",
        "name": "kit-riego-goteo-huerto-hero.webp",
        "alt": "Kit de riego por goteo instalado en macetas de terraza",
    },
    {
        "url": "https://v3b.fal.media/files/b/0a9dc44c/fHCUqSiOaeOYz0BdFXzpF_76c0v9oQ.png",
        "name": "componentes-kit-riego-goteo.webp",
        "alt": "Componentes de un kit de riego por goteo sobre fondo neutro",
    },
    {
        "url": "https://v3b.fal.media/files/b/0a9dc453/j256DgaixWEXl3wojikBQ_HoCGNEiy.png",
        "name": "comparativa-kits-riego-goteo.webp",
        "alt": "Comparativa de kits de riego por goteo sobre mesa de madera",
    },
    {
        "url": "https://v3b.fal.media/files/b/0a9dc44c/JQCd86DBNHS-7ZITUlU6n_T6MntFLU.png",
        "name": "instalacion-riego-goteo-balcon.webp",
        "alt": "Persona instalando un sistema de riego por goteo en macetas de balcon",
    },
]

OUTPUT_DIR = r"C:\Users\usuario\Trabajo\tu-cultivo-en-casa\static\images"
TARGET_SIZE = (1600, 900)


def download_image(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def process(img_meta: dict) -> None:
    print(f"Downloading {img_meta['name']}...")
    raw = download_image(img_meta["url"])
    pil = Image.open(io.BytesIO(raw)).convert("RGB")
    pil = pil.resize(TARGET_SIZE, Image.LANCZOS)
    out_path = os.path.join(OUTPUT_DIR, img_meta["name"])
    pil.save(out_path, "WEBP", quality=85, method=6)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"  -> {out_path} ({size_kb:.1f} KB, {pil.size})")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for img in IMAGES:
        if "REPLACE_WITH_FAL_CDN_URL" in img["url"]:
            print(f"SKIP {img['name']}: URL not set yet.")
            continue
        process(img)
    print("\nDone.")


if __name__ == "__main__":
    main()