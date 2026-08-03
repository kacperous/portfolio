#!/usr/bin/env python3
"""Przycina zdjecie do kwadratowego portretu uzywanego w naglowku CV.

Uzycie:  python3 cv/crop_photo.py [plik_zrodlowy]
Wynik:   cv/assets/photo.jpg (kwadrat 600x600, gotowy pod okragly kadr)

Domyslnie bierze cv/photo.jpeg. Kadr jest wyliczany z FACE_BOX, czyli
prostokata twarzy w oryginale (piksele). Jesli podmienisz zdjecie na inne,
zaktualizuj FACE_BOX albo podaj wlasny kadr przez --box.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent
DEFAULT_SRC = ROOT / "photo.jpeg"
OUT = ROOT / "assets" / "photo.jpg"

# Prostokat glowy w oryginale: (lewo, gora, prawo, dol)
FACE_BOX = (597, 464, 877, 826)

# Ile wysokosci glowy ma obejmowac kadr i jak bardzo zejsc ponizej jej srodka
CROP_SCALE = 2.3
CENTER_DROP = 0.18

SIZE = 600


def crop(src: Path, out: Path, face_box, scale=CROP_SCALE):
    img = Image.open(src).convert("RGB")
    left, top, right, bottom = face_box
    head_h = bottom - top
    cx = (left + right) / 2
    cy = (top + bottom) / 2 + head_h * CENTER_DROP

    half = head_h * scale / 2
    box = [cx - half, cy - half, cx + half, cy + half]

    # utrzymanie kadru w granicach obrazu, bez zmiany jego rozmiaru
    for i, limit in ((0, img.width), (1, img.height)):
        lo, hi = box[i], box[i + 2]
        if lo < 0:
            box[i], box[i + 2] = 0, hi - lo
        elif hi > limit:
            box[i], box[i + 2] = lo - (hi - limit), limit
    box = [max(0, round(box[0])), max(0, round(box[1])),
           min(img.width, round(box[2])), min(img.height, round(box[3]))]

    face = img.crop(box).resize((SIZE, SIZE), Image.LANCZOS)

    # zdjecie jest ciemne i chlodne, delikatnie je podnosimy
    face = ImageEnhance.Brightness(face).enhance(1.22)
    face = ImageEnhance.Contrast(face).enhance(1.08)
    face = ImageEnhance.Color(face).enhance(1.06)

    out.parent.mkdir(parents=True, exist_ok=True)
    face.save(out, "JPEG", quality=90, optimize=True)
    return box


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", default=str(DEFAULT_SRC))
    ap.add_argument("--scale", type=float, default=CROP_SCALE,
                    help="ile wysokosci glowy obejmuje kadr (domyslnie 2.3)")
    args = ap.parse_args()

    src = Path(args.source)
    if not src.exists():
        raise SystemExit(f"brak pliku: {src}")

    box = crop(src, OUT, FACE_BOX, args.scale)
    print(f"{src.name} -> {OUT.relative_to(ROOT.parent)}  kadr {box}, {SIZE}x{SIZE}")


if __name__ == "__main__":
    main()
