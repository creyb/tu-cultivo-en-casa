#!/usr/bin/env python3
"""Download Fal-generated images, upscale to 1600x900, convert to WebP."""
import urllib.request
import os
from PIL import Image
import io

IMAGES = [
    {
        "url": "https://v3b.fal.media/files/b/0a9cd69a/LqitOXuCS-aeWDEv9MNzg_oOpvtd96.png",
        "name": "huerto-vacaciones-hero.webp",
        "alt": "Huerto urbano preparado para vacaciones con sistema de riego",
    },
    {
        "url": "https://v3b.fal.media/files/b/0a9cd69a/n2rizIA9GteJbV0M8DKC1_QM7fe20y.png",
        "name": "riego-botella-invertida-maceta.webp",
        "alt": "Sistema de riego casero con botella invertida en maceta",
    },
    {
        "url": "https://v3b.fal.media/files/b/0a9cd69a/lCZCdbWUTlv7YE8XmYfHW_zKqEbD7o.png",
        "name": "malla-sombreo-macetas-verano.webp",
        "alt": "Malla de sombreo protegiendo macetas del sol",
    },
    {
        "url": "https://v3b.fal.media/files/b/0a9cd69a/g6DJRgv_3lNj8PkWSe0Mv_ANyJZuWL.png",
        "name": "programador-riego-digital-grifo.webp",
        "alt": "Programador de riego digital conectado al grifo del jardín",
    },
]

OUTPUT_DIR = r"C:\Users\usuario\Trabajo\tu-cultivo-en-casa\static\images"
TARGET_SIZE = (1600, 900)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img in IMAGES:
    print(f"Downloading {img['name']}...")
    req = urllib.request.Request(img["url"], headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    pil = Image.open(io.BytesIO(data)).convert("RGB")
    pil = pil.resize(TARGET_SIZE, Image.LANCZOS)
    out_path = os.path.join(OUTPUT_DIR, img["name"])
    pil.save(out_path, "WEBP", quality=85, method=6)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"  -> {out_path} ({size_kb:.1f} KB, {pil.size})")

print("\nDone.")
