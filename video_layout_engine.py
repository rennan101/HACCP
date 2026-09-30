import os
import math
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
ICON_CACHE = {}

def get_font(size, bold=False):
    try:
        return ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=1 if bold else 0)
    except Exception:
        fb = f"/System/Library/Fonts/Supplemental/Arial{' Bold' if bold else ''}.ttf"
        return ImageFont.truetype(fb, size) if os.path.exists(fb) else ImageFont.load_default()

def get_food_icon(icon_path, size):
    if not icon_path:
        return None
    key = (icon_path, size)
    if key in ICON_CACHE:
        return ICON_CACHE[key]
    full_path = os.path.join("presentation", icon_path) if not icon_path.startswith("presentation") else icon_path
    if os.path.exists(full_path):
        raw = Image.open(full_path).convert("RGBA")
        resized = raw.resize((size, size), Image.Resampling.LANCZOS)
        ICON_CACHE[key] = resized
        return resized
    return None

def wrap_text(text, font, max_width, draw):
    lines = []
    for raw_line in text.split("\n"):
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        is_bullet = raw_line.startswith("•") or raw_line.startswith("-")
        prefix, indent = ("• ", "   ") if is_bullet else ("", "")
        words = raw_line.lstrip("•- ").strip().split()
        if not words:
            continue
        cur = prefix + words[0]
        for w in words[1:]:
            test = cur + " " + w
            if draw.textlength(test, font=font) <= max_width:
                cur = test
            else:
                lines.append(cur)
                cur = indent + w
        if cur:
            lines.append(cur)
    return lines

def fit_image_contain(img, target_w, target_h, bg_color="#F8FAFC"):
    bg = Image.new("RGB", (target_w, target_h), bg_color)
    img_ratio, target_ratio = img.width / img.height, target_w / target_h
    new_w = target_w if img_ratio > target_ratio else int(target_h * img_ratio)
    new_h = int(target_w / img_ratio) if img_ratio > target_ratio else target_h
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    bg.paste(resized, ((target_w - new_w) // 2, (target_h - new_h) // 2))
    return bg

def draw_sync_card(draw, box, el, t, base_img=None, is_allergen=False, is_pillar=False):
    x, y, w, h = box
    start_t = el["start_time"]
    end_t = el.get("end_time", 999.0)
    if t < start_t:
        return

    is_active = (start_t <= t < end_t)
    color_map = {"success": "#059669", "danger": "#DC2626", "warning": "#D97706", "purple": "#7C3AED"}
    c_color = color_map.get(el.get("color"), "#0284C7")

    if is_active:
        pulse_o = int(math.sin(t * 8) * 2 + 3)
        draw.rounded_rectangle([(x - pulse_o, y - pulse_o), (x + w + pulse_o, y + h + pulse_o)], radius=14, outline=c_color, width=3)

    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=12, fill="#FFFFFF", outline=c_color if is_active else "#E2E8F0", width=2 if is_active else 1)

    if is_allergen or is_pillar:
        draw.rectangle([(x, y), (x + w, y + 6)], fill=c_color)
        icon_sz = 76 if is_allergen else 84
        food_icon = get_food_icon(el.get("food_icon"), icon_sz)
        if food_icon and base_img:
            base_img.paste(food_icon, (x + (w - icon_sz) // 2, y + (10 if is_allergen else 18)), mask=food_icon)

        tag_str = el.get("tag", "ALLERGEN" if is_allergen else "PRP").upper()
        font_tag = get_font(12 if is_allergen else 14, bold=True)
        tw = draw.textlength(tag_str, font=font_tag)
        draw.text((x + (w - tw) // 2, y + (88 if is_allergen else 112)), tag_str, fill=c_color, font=font_tag)

        font_head = get_font(18 if is_allergen else 22, bold=True)
        head_lines = wrap_text(el["heading"], font_head, w - 16, draw)
        hy = y + (106 if is_allergen else 138)
        for hl in head_lines[:2]:
            hw = draw.textlength(hl, font=font_head)
            draw.text((x + (w - hw) // 2, hy), hl, fill="#0F172A", font=font_head)
            hy += 22 if is_allergen else 26

        font_desc = get_font(14 if is_allergen else 16.5)
        desc_lines = wrap_text(el.get("description", ""), font_desc, w - 16, draw)
        dy = hy + (6 if is_allergen else 12)
        for dl in desc_lines[: (3 if is_allergen else 4)]:
            dw = draw.textlength(dl, font=font_desc)
            draw.text((x + (w - dw) // 2, dy), dl, fill="#64748B", font=font_desc)
            dy += 19 if is_allergen else 24
        return

    draw.rectangle([(x, y + 4), (x + 6, y + h - 4)], fill=c_color)
    is_very_large = (w > 800 and h > 200)
    is_timeline = (w > 400 and w <= 500)
    is_large = is_very_large or is_timeline

    icon_sz = 88 if is_very_large else (80 if is_timeline else 68)
    food_icon = get_food_icon(el.get("food_icon"), icon_sz)
    if food_icon and base_img:
        base_img.paste(food_icon, (x + w - icon_sz - 18, y + 18), mask=food_icon)

    font_tag = get_font(17 if is_large else 12, bold=True)
    font_head = get_font(32 if is_very_large else (28 if is_timeline else (18 if w > 300 else 15)), bold=True)
    font_desc = get_font(23 if is_very_large else (21 if is_timeline else (15 if w > 500 else 13.5)))

    tag_str = el.get("tag", "KEY CONCEPT").upper()
    draw.text((x + (30 if is_large else 20), y + (24 if is_large else 14)), tag_str, fill=c_color, font=font_tag)

    max_w = w - (icon_sz + 50 if food_icon else 50)
    head_lines = wrap_text(el["heading"], font_head, max_w, draw)
    dy = y + (62 if is_very_large else (58 if is_timeline else 36))
    h_step = 38 if is_very_large else (34 if is_timeline else 22)
    for h_line in head_lines[:2]:
        draw.text((x + (30 if is_large else 20), dy), h_line, fill="#0F172A", font=font_head)
        dy += h_step

    dy += (18 if is_large else 6)
    raw_desc = el.get("description", "")
    desc_lines = wrap_text(raw_desc, font_desc, max_w if (food_icon and dy < y + icon_sz + 30) else (w - 56 if is_large else w - 38), draw)
    line_h = 38 if is_very_large else (32 if is_timeline else 22)
    for d_line in desc_lines:
        if dy + line_h > y + h - 8:
            break
        draw.text((x + (30 if is_large else 20), dy), d_line, fill="#475569", font=font_desc)
        extra_gap = 10 if (is_large and (d_line.startswith("•") or "•" in raw_desc)) else 0
        dy += line_h + extra_gap

def draw_banner(draw, box, el, t):
    x, y, w, h = box
    if t < el["start_time"]:
        return
    is_active = (el["start_time"] <= t < el.get("end_time", 999.0))
    if is_active:
        pulse_o = int(math.sin(t * 8) * 2 + 3)
        draw.rounded_rectangle([(x - pulse_o, y - pulse_o), (x + w + pulse_o, y + h + pulse_o)], radius=14, outline="#38BDF8", width=3)
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=12, fill="#0F172A")
    draw.rectangle([(x, y + 4), (x + 8, y + h - 4)], fill="#38BDF8")
    font_h, font_p = get_font(23, bold=True), get_font(18)
    dy = y + 18
    for line in wrap_text(el["heading"], font_h, w - 40, draw)[:2]:
        draw.text((x + 24, dy), line, fill="#38BDF8", font=font_h)
        dy += 28
    for line in wrap_text(el.get("description", ""), font_p, w - 40, draw)[:3]:
        draw.text((x + 24, dy), line, fill="#E2E8F0", font=font_p)
        dy += 24

def render_slide_frame(slide, t, dur, hero_img):
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
    draw = ImageDraw.Draw(img)

    draw.rectangle([(0, 0), (WIDTH, 8)], fill="#0284C7")
    draw.text((80, 36), slide["category"].upper(), fill="#0284C7", font=get_font(15, bold=True))
    draw.text((80, 64), slide["title"], fill="#0F172A", font=get_font(36, bold=True))
    draw.text((80, 116), slide["subtitle"], fill="#64748B", font=get_font(18))

    mode = slide.get("layout_mode", "split_photo")
    elements = slide["elements"]

    if mode == "split_photo":
        cards = [e for e in elements if e.get("type") != "banner"]
        banner = next((e for e in elements if e.get("type") == "banner"), None)
        card_y = 180
        total_items = len(cards) + (1 if banner else 0)
        card_h = 145 if total_items == 3 else (160 if total_items == 2 else 125)
        for el in cards:
            draw_sync_card(draw, (80, card_y, 900, card_h), el, t, base_img=img)
            card_y += card_h + 16
        if banner:
            draw_banner(draw, (80, card_y, 900, 130), banner, t)
        if hero_img:
            mask = Image.new("L", (820, 500), 0)
            ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (820, 500)], radius=18, fill=255)
            img.paste(hero_img, (1020, 180), mask=mask)
            draw.rounded_rectangle([(1020, 180), (1840, 680)], radius=18, outline="#CBD5E1", width=2)

    elif mode == "allergens_grid_7x2":
        for i, el in enumerate(elements):
            col, row = i % 7, i // 7
            draw_sync_card(draw, (80 + col * 254, 190 + row * 290, 238, 275), el, t, base_img=img, is_allergen=True)

    elif mode == "full_width_grid_2col":
        n = len(elements)
        h, gap = (110, 14) if n > 6 else (135, 18)
        for i, el in enumerate(elements):
            col, row = i % 2, i // 2
            draw_sync_card(draw, (80 + col * 900, 180 + row * (h + gap), 860, h), el, t, base_img=img)

    elif mode == "comparison_split":
        old_card = next((e for e in elements if "old" in e["id"]), None)
        new_card = next((e for e in elements if "new" in e["id"]), None)
        banner = next((e for e in elements if e.get("type") == "banner"), None)
        if old_card:
            draw_sync_card(draw, (80, 180, 860, 470), old_card, t, base_img=img)
        if new_card:
            draw_sync_card(draw, (980, 180, 860, 470), new_card, t, base_img=img)
        if banner:
            draw_banner(draw, (80, 675, 1760, 100), banner, t)

    elif mode in ["horizontal_timeline", "horizontal_flow"]:
        for i, el in enumerate(elements):
            draw_sync_card(draw, (80 + i * 445, 200, 425, 460), el, t, base_img=img)

    elif mode == "full_width_alert_split":
        c_cards = [e for e in elements if e.get("type") != "warning_box"]
        warn = next((e for e in elements if e.get("type") == "warning_box"), None)
        for i, el in enumerate(c_cards):
            draw_sync_card(draw, (80 + i * 900, 180, 860, 270), el, t, base_img=img)
        if warn and t >= warn["start_time"]:
            draw.rounded_rectangle([(80, 480), (1840, 730)], radius=16, fill="#FEF2F2", outline="#EF4444", width=2)
            f_ic = get_food_icon(warn.get("food_icon"), 84)
            if f_ic:
                img.paste(f_ic, (1730, 495), mask=f_ic)
            draw.text((115, 508), warn["heading"].upper(), fill="#DC2626", font=get_font(28, bold=True))
            dy = 560
            for line in wrap_text(warn.get("description", ""), get_font(22), 1580, draw):
                draw.text((115, dy), line, fill="#7F1D1D", font=get_font(22))
                dy += 34

    elif mode == "full_width_grid_2x4":
        for i, el in enumerate(elements):
            col, row = i % 2, i // 2
            draw_sync_card(draw, (80 + col * 900, 180 + row * 135, 860, 120), el, t, base_img=img)

    elif mode == "lab_table":
        draw.rounded_rectangle([(80, 180), (1840, 235)], radius=8, fill="#0F172A")
        for x_pos, title in [(110, "TEST PARAMETER"), (680, "TARGET SPECIFICATION"), (1120, "ACTION LIMIT"), (1520, "REJECT THRESHOLD")]:
            draw.text((x_pos, 196), title, fill="#FFFFFF", font=get_font(16, bold=True))
        for i, el in enumerate(elements):
            if t >= el["start_time"]:
                y = 250 + i * 85
                is_act = (el["start_time"] <= t < el.get("end_time", 999.0))
                draw.rounded_rectangle([(80, y), (1840, y + 70)], radius=8, fill="#FFFFFF", outline="#0284C7" if is_act else "#E2E8F0", width=2 if is_act else 1)
                food_icon = get_food_icon(el.get("food_icon"), 28)
                if food_icon:
                    img.paste(food_icon, (110, y + 21), mask=food_icon)
                draw.text((146 if food_icon else 110, y + 24), el["param"], fill="#0F172A", font=get_font(18, bold=True))
                draw.text((680, y + 24), el["target"], fill="#059669", font=get_font(18, bold=True))
                draw.text((1120, y + 24), el["action"], fill="#D97706", font=get_font(18))
                draw.text((1520, y + 24), el["reject"], fill="#DC2626", font=get_font(18, bold=True))

    elif mode == "pillar_architecture":
        for i, el in enumerate(elements):
            draw_sync_card(draw, (80 + i * 254, 210, 238, 440), el, t, base_img=img, is_pillar=True)

    elif mode == "pdca_quadrants":
        for i, el in enumerate(elements):
            col, row = i % 2, i // 2
            draw_sync_card(draw, (80 + col * 900, 180 + row * 275, 860, 260), el, t, base_img=img)

    elif mode == "assessment_checklist":
        ref = next((e for e in elements if e["id"] == "s26_ref"), None)
        quiz = next((e for e in elements if e["id"] == "s26_quiz"), None)
        banner = next((e for e in elements if e.get("type") == "banner"), None)
        if ref:
            draw_sync_card(draw, (80, 180, 840, 480), ref, t, base_img=img)
        if quiz:
            draw_sync_card(draw, (960, 180, 880, 480), quiz, t, base_img=img)
        if banner:
            draw_banner(draw, (80, 685, 1760, 100), banner, t)

    draw.line([(80, 930), (1840, 930)], fill="#E2E8F0", width=1)
    draw.text((80, 948), "HACCP Level 2 Food Safety & Dairy Processing Masterclass", fill="#94A3B8", font=get_font(14))
    draw.text((1700, 948), f"Slide {slide['slide_num']:02d} / 26", fill="#94A3B8", font=get_font(14))

    if t < 0.35:
        progress = max(0.0, min(1.0, t / 0.35))
        ease = 1.0 - math.pow(1.0 - progress, 3)
        blank = Image.new("RGB", (WIDTH, HEIGHT), color="#F8FAFC")
        ImageDraw.Draw(blank).rectangle([(0, 0), (WIDTH, 8)], fill="#0284C7")
        img = Image.blend(blank, img, ease)

    return img
