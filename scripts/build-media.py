#!/usr/bin/env python3
"""Build deterministic launch art from the two project-owned master images."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "source"

PARCHMENT = "#E7D8B5"
PAPER = "#F2E9D4"
BRASS = "#B99352"
OXBLOOD = "#7E1F2B"
CHARCOAL = "#0B0A09"
INK = "#17130F"
MUTED = "#B9AA8C"


def font_candidates(kind: str) -> list[Path]:
    windows = Path("C:/Windows/Fonts")
    linux = Path("/usr/share/fonts/truetype/dejavu")
    mac = Path("/System/Library/Fonts")
    return {
        "serif": [windows / "georgia.ttf", linux / "DejaVuSerif.ttf", mac / "NewYork.ttf"],
        "serif-bold": [windows / "georgiab.ttf", linux / "DejaVuSerif-Bold.ttf", mac / "NewYork.ttf"],
        "sans": [windows / "segoeui.ttf", linux / "DejaVuSans.ttf", mac / "Helvetica.ttc"],
        "sans-bold": [windows / "seguisb.ttf", linux / "DejaVuSans-Bold.ttf", mac / "Helvetica.ttc"],
        "mono": [windows / "consola.ttf", linux / "DejaVuSansMono.ttf", mac / "Menlo.ttc"],
    }[kind]


def load_font(kind: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in font_candidates(kind):
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def cover(image: Image.Image, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=centering)


def rgba(color: str, alpha: int) -> tuple[int, int, int, int]:
    rgb = tuple(bytes.fromhex(color.removeprefix("#")))
    return (*rgb, alpha)


def horizontal_alpha(size: tuple[int, int], left: int, right: int) -> Image.Image:
    width, height = size
    row = Image.new("L", (width, 1))
    if width == 1:
        row.putpixel((0, 0), left)
    else:
        row.putdata([round(left + (right - left) * x / (width - 1)) for x in range(width)])
    return row.resize((width, height))


def vertical_alpha(size: tuple[int, int], top: int, bottom: int) -> Image.Image:
    width, height = size
    column = Image.new("L", (1, height))
    if height == 1:
        column.putpixel((0, 0), top)
    else:
        column.putdata([round(top + (bottom - top) * y / (height - 1)) for y in range(height)])
    return column.resize((width, height))


def tint_layer(size: tuple[int, int], color: str, alpha: Image.Image) -> Image.Image:
    layer = Image.new("RGBA", size, rgba(color, 255))
    layer.putalpha(alpha)
    return layer


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill, width: int) -> None:
    draw.text(((width - text_width(draw, text, font)) // 2, y), text, font=font, fill=fill)


def draw_brand_mark(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0) -> None:
    radius = int(22 * scale)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=BRASS, width=max(1, int(2 * scale)))
    draw.line((x - radius // 2, y, x + radius // 2, y), fill=BRASS, width=max(1, int(2 * scale)))
    draw.line((x, y - radius // 2, x, y + radius // 2), fill=BRASS, width=max(1, int(2 * scale)))


def save_png(image: Image.Image, name: str) -> None:
    image.convert("RGB").save(ASSETS / name, format="PNG", optimize=True)


def build_hero(master: Image.Image) -> Image.Image:
    size = (1400, 700)
    canvas = cover(master, size, centering=(0.52, 0.46)).convert("RGBA")
    canvas = ImageEnhance.Color(canvas).enhance(0.88)
    canvas.alpha_composite(tint_layer(size, CHARCOAL, horizontal_alpha(size, 242, 5)))
    canvas.alpha_composite(tint_layer(size, OXBLOOD, horizontal_alpha(size, 32, 0)))

    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((18, 18, 1382, 682), radius=28, outline=rgba(BRASS, 150), width=2)
    draw.line((78, 92, 78, 598), fill=OXBLOOD, width=6)
    draw_brand_mark(draw, 112, 90, 0.72)
    draw.text((148, 75), "HALL OF FAME STUDIO  ·  AGENT 002", font=load_font("mono", 20), fill=MUTED)
    draw.text((112, 200), "Warren Buffett", font=load_font("serif-bold", 70), fill=PAPER)
    draw.text((116, 292), "Deep Capital Allocation Agent", font=load_font("serif", 34), fill=PARCHMENT)
    draw.text((116, 382), "SEE THE DOWNSIDE.", font=load_font("sans-bold", 21), fill=BRASS)
    draw.text((116, 416), "PRESERVE THE OPTIONS.", font=load_font("sans-bold", 21), fill=BRASS)
    draw.text((116, 450), "LET TIME DO THE WORK.", font=load_font("sans-bold", 21), fill=BRASS)
    draw.rounded_rectangle((114, 532, 442, 582), radius=25, fill=rgba(PAPER, 238))
    draw.text((143, 547), "REPOSITORY-PREQUALIFIED", font=load_font("mono", 16), fill=INK)
    draw.text((116, 617), "46 SOURCES  ·  56 OBSERVATIONS  ·  12 SKILLS", font=load_font("mono", 16), fill=MUTED)
    return canvas


def build_poster(master: Image.Image) -> Image.Image:
    size = (1200, 1500)
    canvas = cover(master, size, centering=(0.5, 0.52)).convert("RGBA")
    canvas = ImageEnhance.Color(canvas).enhance(0.82)
    canvas.alpha_composite(tint_layer(size, CHARCOAL, vertical_alpha(size, 245, 0)))
    lower = tint_layer(size, CHARCOAL, vertical_alpha(size, 0, 210))
    canvas.alpha_composite(lower)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((34, 34, 1166, 1466), outline=rgba(BRASS, 190), width=2)
    draw.rectangle((52, 52, 1148, 1448), outline=rgba(PARCHMENT, 80), width=1)
    draw_brand_mark(draw, 92, 92, 0.85)
    draw.text((132, 73), "HALL OF FAME STUDIO  ·  RELEASE 002", font=load_font("mono", 20), fill=MUTED)
    centered(draw, 160, "WARREN BUFFETT", load_font("serif-bold", 72), PAPER, size[0])
    centered(draw, 250, "DEEP AGENT", load_font("serif", 34), PARCHMENT, size[0])
    draw.line((300, 320, 900, 320), fill=OXBLOOD, width=5)
    centered(draw, 346, "TIME  ·  JUDGMENT  ·  STEWARDSHIP", load_font("mono", 18), BRASS, size[0])
    draw.rounded_rectangle((258, 1330, 942, 1394), radius=32, fill=rgba(CHARCOAL, 220), outline=rgba(BRASS, 180), width=2)
    centered(draw, 1347, "SEE THE DOWNSIDE. PRESERVE THE OPTIONS.", load_font("sans-bold", 19), PAPER, size[0])
    centered(draw, 1412, "PART OF HALL OF FAME STUDIO", load_font("mono", 17), MUTED, size[0])
    return canvas


def build_social(hero: Image.Image) -> Image.Image:
    canvas = cover(hero.convert("RGB"), (1280, 640), centering=(0.5, 0.5)).convert("RGBA")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((18, 18, 1262, 622), outline=rgba(BRASS, 170), width=2)
    draw.rectangle((990, 548, 1220, 592), fill=rgba(CHARCOAL, 210))
    draw.text((1013, 561), "OPEN-SOURCE AGENT", font=load_font("mono", 14), fill=PARCHMENT)
    return canvas


def fade_in_out(index: int, start: int, end: int, ramp: int = 5) -> float:
    if index < start or index >= end:
        return 0.0
    return min(1.0, (index - start + 1) / ramp, (end - index) / ramp)


def alpha_text(layer: Image.Image, xy, text: str, font, fill: str, alpha: float) -> None:
    color = rgba(fill, max(0, min(255, round(alpha * 255))))
    ImageDraw.Draw(layer).text(xy, text, font=font, fill=color)


def gif_palette(frame: Image.Image) -> Image.Image:
    return frame.convert("RGB").convert("P", palette=Image.Palette.ADAPTIVE, colors=64)


def save_gif(frames: Iterable[Image.Image], name: str, duration: int = 110) -> None:
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


def demo_background(hero: Image.Image) -> Image.Image:
    bg = cover(hero.convert("RGB"), (960, 540), centering=(0.48, 0.5)).filter(ImageFilter.GaussianBlur(5)).convert("RGBA")
    bg.alpha_composite(Image.new("RGBA", bg.size, rgba(CHARCOAL, 190)))
    return bg


def build_demo(hero: Image.Image) -> list[Image.Image]:
    frames: list[Image.Image] = []
    bg = demo_background(hero)
    total = 64
    for i in range(total):
        frame = bg.copy()
        draw = ImageDraw.Draw(frame)
        draw.rectangle((22, 22, 938, 518), outline=rgba(BRASS, 150), width=2)
        draw_brand_mark(draw, 55, 53, 0.55)
        draw.text((83, 39), "HALL OF FAME STUDIO  ·  DECISION ROOM", font=load_font("mono", 14), fill=MUTED)
        draw.text((770, 39), "AGENT 002", font=load_font("mono", 14), fill=BRASS)

        if i < 16:
            a = fade_in_out(i, 0, 16)
            alpha_text(frame, (92, 155), "Should we bet the company", load_font("serif-bold", 38), PAPER, a)
            alpha_text(frame, (92, 205), "on this acquisition?", load_font("serif-bold", 38), PAPER, a)
            alpha_text(frame, (94, 284), "A high-conviction question.", load_font("sans", 20), MUTED, a)
            alpha_text(frame, (94, 316), "An irreversible answer.", load_font("sans", 20), OXBLOOD, a)
        elif i < 36:
            a = fade_in_out(i, 16, 36)
            alpha_text(frame, (72, 112), "FIRST: SEPARATE RISK FROM NOISE", load_font("mono", 17), BRASS, a)
            cards = [
                ("WHAT IS KNOWN", "Primary evidence"),
                ("WHAT CAN BREAK", "Permanent loss"),
                ("WHAT IS REVERSIBLE", "Stage the commitment"),
                ("WHAT ELSE WINS", "Next-best use"),
            ]
            for n, (title, subtitle) in enumerate(cards):
                col, row = n % 2, n // 2
                x, y = 72 + col * 420, 165 + row * 132
                offset = max(0, 24 - (i - 16 - n * 2) * 6)
                draw.rounded_rectangle((x + offset, y, x + 390 + offset, y + 106), radius=15, fill=rgba("#17120E", round(220 * a)), outline=rgba(BRASS, round(130 * a)), width=2)
                alpha_text(frame, (x + 22 + offset, y + 22), title, load_font("sans-bold", 17), PAPER, a)
                alpha_text(frame, (x + 22 + offset, y + 58), subtitle, load_font("sans", 16), MUTED, a)
        elif i < 52:
            a = fade_in_out(i, 36, 52)
            alpha_text(frame, (72, 105), "THEN: MAKE THE DECISION INSPECTABLE", load_font("mono", 17), BRASS, a)
            artifacts = ["Downside & Leverage Map", "Opportunity Cost Ledger", "Capital Allocation Board", "Owner Decision Memo"]
            for n, artifact in enumerate(artifacts):
                y = 165 + n * 70
                length = min(700, max(0, (i - 36 - n * 2) * 70))
                draw.line((82, y + 26, 82 + length, y + 26), fill=rgba(BRASS, round(100 * a)), width=1)
                draw.ellipse((72, y + 16, 92, y + 36), fill=rgba(OXBLOOD, round(255 * a)), outline=rgba(PAPER, round(170 * a)))
                alpha_text(frame, (115, y + 8), artifact, load_font("serif", 24), PAPER, a)
        else:
            a = fade_in_out(i, 52, 64)
            alpha_text(frame, (84, 150), "A calm partner for", load_font("serif", 34), PARCHMENT, a)
            alpha_text(frame, (84, 198), "irreversible decisions.", load_font("serif-bold", 40), PAPER, a)
            alpha_text(frame, (86, 284), "12 callable Skills  ·  evidence-grounded  ·  revision-ready", load_font("mono", 16), BRASS, a)
            draw.rounded_rectangle((84, 350, 424, 404), radius=27, fill=rgba(PAPER, round(240 * a)))
            alpha_text(frame, (116, 367), "WARREN BUFFETT AGENT", load_font("sans-bold", 17), INK, a)
            alpha_text(frame, (86, 445), "PART OF HALL OF FAME STUDIO", load_font("mono", 15), MUTED, a)
        frames.append(frame)
    return frames


def build_teaser(hero: Image.Image) -> list[Image.Image]:
    frames: list[Image.Image] = []
    base = cover(hero.convert("RGB"), (960, 540), centering=(0.52, 0.5)).convert("RGBA")
    total = 56
    for i in range(total):
        moving = base.copy()
        moving.alpha_composite(Image.new("RGBA", moving.size, rgba(CHARCOAL, 74)))
        draw = ImageDraw.Draw(moving)
        draw.rectangle((20, 20, 940, 520), outline=rgba(BRASS, 150), width=2)
        if i < 14:
            a = fade_in_out(i, 0, 14)
            alpha_text(moving, (66, 70), "HALL OF FAME STUDIO", load_font("mono", 16), BRASS, a)
            alpha_text(moving, (64, 170), "AGENT 002", load_font("sans-bold", 58), PAPER, a)
            alpha_text(moving, (66, 247), "enters the room.", load_font("serif", 34), PARCHMENT, a)
        elif i < 28:
            a = fade_in_out(i, 14, 28)
            alpha_text(moving, (66, 150), "NOT A QUOTE BOT.", load_font("sans-bold", 48), PAPER, a)
            alpha_text(moving, (68, 222), "Not market theater.", load_font("serif", 31), PARCHMENT, a)
            alpha_text(moving, (68, 270), "A long-term owner at your table.", load_font("serif", 31), PARCHMENT, a)
        elif i < 43:
            a = fade_in_out(i, 28, 43)
            alpha_text(moving, (66, 122), "UNDERSTAND", load_font("mono", 18), BRASS, a)
            alpha_text(moving, (66, 172), "VALUE", load_font("mono", 18), BRASS, a)
            alpha_text(moving, (66, 222), "ALLOCATE", load_font("mono", 18), BRASS, a)
            alpha_text(moving, (66, 272), "PROTECT", load_font("mono", 18), BRASS, a)
            alpha_text(moving, (66, 343), "12 Skills. One coherent judgment system.", load_font("serif-bold", 28), PAPER, a)
        else:
            a = fade_in_out(i, 43, 56)
            alpha_text(moving, (66, 132), "WARREN BUFFETT", load_font("serif-bold", 52), PAPER, a)
            alpha_text(moving, (68, 200), "DEEP CAPITAL ALLOCATION AGENT", load_font("mono", 18), BRASS, a)
            draw.rounded_rectangle((66, 286, 428, 342), radius=28, fill=rgba(PAPER, round(238 * a)))
            alpha_text(moving, (97, 303), "EXPLORE THE OPEN REPOSITORY", load_font("sans-bold", 15), INK, a)
            alpha_text(moving, (68, 405), "PART OF HALL OF FAME STUDIO", load_font("mono", 15), MUTED, a)
        frames.append(moving)
    return frames


def main() -> None:
    hero_master = Image.open(SOURCE / "hero-master.png")
    poster_master = Image.open(SOURCE / "poster-master.png")
    hero = build_hero(hero_master)
    poster = build_poster(poster_master)
    social = build_social(hero)
    save_png(hero, "hero.png")
    save_png(poster, "poster.png")
    save_png(social, "social-card.png")
    save_gif(build_demo(hero_master), "demo.gif", duration=110)
    save_gif(build_teaser(hero_master), "teaser.gif", duration=120)
    print("Built assets/hero.png")
    print("Built assets/poster.png")
    print("Built assets/social-card.png")
    print("Built assets/demo.gif")
    print("Built assets/teaser.gif")


if __name__ == "__main__":
    main()
