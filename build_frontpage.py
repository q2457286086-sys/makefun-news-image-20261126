#!/usr/bin/env python3
"""Compose the 26 November 2026 front page (1024x1024) from hero.png.

Fresh build for news-image-20261126. Layout: masthead, lead headline,
hero photograph, deck, two secondary-story columns, an IN BRIEF band,
and a footer. Deterministic: fixed text, fixed geometry, fixed fonts.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RULE = (18, 18, 18)
ACCENT = (158, 28, 20)
GREY = (84, 80, 72)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width` px."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, text, fnt, width, leading, fill=INK):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)
    x0, x1 = MARGIN, W - MARGIN
    cw = x1 - x0

    # ---- Masthead ----
    y = 20
    d.text((x0, y), "THE WORLD TODAY", font=font(SERIF, 54), fill=INK)
    y += 64
    d.line([(x0, y), (x1, y)], fill=RULE, width=3)
    y += 7
    d.text((x0, y), "THURSDAY 26 NOVEMBER 2026", font=font(SANS_B, 19), fill=ACCENT)
    d.text((x1, y), "ONE DAY  •  ONE PAGE", font=font(SANS_B, 19), fill=INK,
           anchor="ra")
    y += 26
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)

    # ---- Lead headline ----
    y += 10
    y = draw_para(d, x0, y, "STORM POSTPONES THE PARADE",
                  font(SERIF, 46), cw, 52)
    y = draw_para(d, x0, y, "AS NEW YORK BRACES FOR THANKSGIVING",
                  font(SERIF, 30), cw, 36)
    y += 4

    # ---- Hero photograph ----
    hero = Image.open("hero.png").convert("RGB")
    hw, hh = x1 - x0, 225
    hero = hero.resize((hw, hh), Image.LANCZOS)
    page.paste(hero, (x0, y))
    d.rectangle([x0, y, x1, y + hh], outline=RULE, width=2)
    y += hh + 6
    y = draw_para(d, x0, y,
                  "Giant balloons strain against high winds and driving rain "
                  "over a Manhattan avenue as a huge storm hits New York on "
                  "Thanksgiving Day.",
                  font(SERIF_R, 17), cw, 22, fill=GREY)
    y += 4
    d.line([(x0, y), (x1, y)], fill=RULE, width=1)

    # ---- Deck ----
    y += 8
    y = draw_para(d, x0, y,
                  "The Macy's Thanksgiving Day Parade was postponed as the "
                  "storm swept the city, and Thanksgiving travel descended "
                  "into chaos, with storms nationwide and a radar issue at "
                  "Chicago O'Hare stranding flyers on the busiest travel "
                  "day of the year.",
                  font(SERIF_R, 21), cw, 28)
    y += 8
    d.line([(x0, y), (x1, y)], fill=RULE, width=1)

    # ---- Secondary stories: two columns ----
    col_w = (cw - 28) // 2
    y += 10
    col_top = y

    stories = [
        ("TARIFFS AIMED AT OVERCAPACITY",
         "Washington proposes new tariffs of up to 25% on Indian goods, "
         "with a lower rate possible if a trade deal is reached."),
        ("CAIRO BLAZE KILLS AT LEAST 30",
         "A massive fire swept through Cairo after a fuel truck overturned, "
         "killing at least 30 people."),
        ("KIM SEEKS WIDER NUCLEAR ROLE",
         "North Korea's Kim calls for wider deployment and diversified use "
         "of tactical nuclear weapons."),
        ("UKRAINE HITS RUSSIAN AIR BASE",
         "Kyiv says it struck a major Russian air base, damaging five "
         "planes, as NATO boosts air surveillance on its eastern flank."),
    ]
    for i, (head, body) in enumerate(stories):
        cx = x0 if i % 2 == 0 else x0 + col_w + 28
        cy = col_top + (i // 2) * 92
        cy = draw_para(d, cx, cy, head, font(SANS_B, 17), col_w, 21)
        draw_para(d, cx, cy + 1, body, font(SERIF_R, 16), col_w, 21)

    y = col_top + 2 * 92 + 4
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)

    # ---- IN BRIEF band ----
    y += 8
    d.text((x0, y), "IN BRIEF", font=font(SANS_B, 18), fill=ACCENT)
    y += 24
    briefs = [
        "Birthright: a second judge blocks Trump's newest order curtailing "
        "birthright citizenship.",
        "China: Politburo member and Shanghai party chief Chen Jining under "
        "investigation in a shock corruption probe.",
        "Yemen's Houthis launch a fresh attack on Riyadh; tankers hit by "
        "explosions in the Strait of Hormuz, Tehran says.",
        "Nvidia: US finds no evidence China told Alice Huang to spy on CEO "
        "Jensen Huang; VP Vance defends Huang.",
        "Duran Duran guitarist and songwriter Andy Taylor dies at 65.",
        "WHO chief urges an end to the US fuel blockade on Cuba; South "
        "African court rules the Ramaphosa report unlawful.",
        "UN: five women are killed every hour globally by a partner or "
        "relative.",
        "Dozens of countries urge Russia to halt alleged use of a riot "
        "agent in Ukraine.",
    ]
    for item in briefs:
        y = draw_para(d, x0 + 14, y, "\u2022  " + item,
                      font(SANS, 15), cw - 14, 18)
        y += 1

    # ---- Footer ----
    d.line([(x0, H - 44), (x1, H - 44)], fill=RULE, width=1)
    d.text((x0, H - 36),
           "All headlines checked against reports dated 26 November 2026.",
           font=font(SANS, 14), fill=GREY)
    d.text((x1, H - 36), "THE WORLD TODAY", font=font(SANS_B, 14),
           fill=GREY, anchor="ra")

    page.save("entry.png", optimize=True)
    print("wrote entry.png", page.size)


if __name__ == "__main__":
    main()
