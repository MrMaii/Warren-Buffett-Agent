#!/usr/bin/env python3
"""Build the unified Hall of Fame Studio archive-plate media kit."""

from __future__ import annotations

import math
from pathlib import Path
from shutil import copyfile
from typing import Iterable

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "source"
MASTER_SIZE = (1536, 1024)
MOTION_SIZE = (768, 512)


def read_master(path: Path) -> Image.Image:
    with Image.open(path) as image:
        return image.convert("RGB").copy()


def load_master() -> Image.Image:
    hero_master = read_master(SOURCE / "hero-master.png")
    poster_master = read_master(SOURCE / "poster-master.png")
    if hero_master.size != MASTER_SIZE or poster_master.size != MASTER_SIZE:
        raise ValueError(f"Archive plate must be {MASTER_SIZE[0]}x{MASTER_SIZE[1]}")
    if hero_master.tobytes() != poster_master.tobytes():
        raise ValueError("hero-master.png and poster-master.png must be identical archive plates")
    return hero_master


def copy_master(name: str) -> None:
    copyfile(SOURCE / "hero-master.png", ASSETS / name)


def motion_frame(master: Image.Image, index: int, total: int, drift: float) -> Image.Image:
    phase = index / max(1, total - 1)
    cycle = 0.5 - 0.5 * math.cos(phase * math.pi * 2)
    scale = 1.0 + 0.026 * cycle
    scaled_size = (round(MOTION_SIZE[0] * scale), round(MOTION_SIZE[1] * scale))
    scaled = master.resize(scaled_size, Image.Resampling.LANCZOS)
    max_x = max(0, scaled.width - MOTION_SIZE[0])
    max_y = max(0, scaled.height - MOTION_SIZE[1])
    x_ratio = 0.5 + drift * math.sin(phase * math.pi * 2)
    y_ratio = 0.5 + drift * 0.35 * math.cos(phase * math.pi * 2)
    left = round(max_x * min(1.0, max(0.0, x_ratio)))
    top = round(max_y * min(1.0, max(0.0, y_ratio)))
    frame = scaled.crop((left, top, left + MOTION_SIZE[0], top + MOTION_SIZE[1]))
    return ImageEnhance.Brightness(frame).enhance(0.985 + cycle * 0.03)


def build_motion(master: Image.Image, frame_count: int, drift: float) -> list[Image.Image]:
    return [motion_frame(master, index, frame_count, drift) for index in range(frame_count)]


def gif_palette(frame: Image.Image) -> Image.Image:
    return frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=96)


def save_gif(frames: Iterable[Image.Image], name: str, duration: int) -> None:
    palette_frames = [gif_palette(frame) for frame in frames]
    palette_frames[0].save(
        ASSETS / name,
        save_all=True,
        append_images=palette_frames[1:],
        duration=duration,
        loop=0,
        optimize=True,
        disposal=1,
    )


def main() -> None:
    master = load_master()
    for name in ["hero.png", "poster.png", "social-card.png"]:
        copy_master(name)
    save_gif(build_motion(master, 36, 0.12), "demo.gif", 110)
    save_gif(build_motion(master, 48, 0.08), "teaser.gif", 120)
    for name in ["hero.png", "poster.png", "social-card.png", "demo.gif", "teaser.gif"]:
        print("Built assets/" + name)


if __name__ == "__main__":
    main()
