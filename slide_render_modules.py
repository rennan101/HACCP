import math
import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080

def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/SFPro.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def ease_out_back(t, s=1.70158):
    t = max(0.0, min(1.0, t))
    t = t - 1
    return (t * t * ((s + 1) * t + s) + 1)

def draw_header(draw, category, title, subtitle=None):
    draw.rectangle([(0, 0), (WIDTH, 14)], fill="#0284C7")
    draw.text((140, 100), category.upper(), fill="#0284C7", font=get_font(22, bold=True))
    draw.text((140, 140), title, fill="#0F172A", font=get_font(52, bold=True))
    if subtitle:
        draw.text((140, 210), subtitle, fill="#475569", font=get_font(26))

def draw_footer(draw, slide_num):
    draw.line([(140, 950), (1780, 950)], fill="#E2E8F0", width=1)
    draw.text((140, 975), "HACCP Level 2 Food & Dairy Training Masterclass", fill="#64748B", font=get_font(22))
    draw.text((1600, 975), f"Slide {slide_num:02d} / 26", fill="#64748B", font=get_font(22))

def draw_nasa_rocket(draw, cx, cy, scale=1.0):
    # Rocket Body
    w, h = int(35 * scale), int(90 * scale)
    draw.rounded_rectangle([(cx - w, cy - h), (cx + w, cy + h)], radius=int(20*scale), fill="#E2E8F0", outline="#0284C7", width=max(2, int(3*scale)))
    # Cone
    draw.polygon([(cx - w, cy - h), (cx + w, cy - h), (cx, cy - h - int(45*scale))], fill="#EF4444")
    # Window
    draw.ellipse([(cx - int(18*scale), cy - int(35*scale)), (cx + int(18*scale), cy + int(1*scale))], fill="#0284C7")
    draw.ellipse([(cx - int(12*scale), cy - int(29*scale)), (cx + int(12*scale), cy - int(5*scale))], fill="#38BDF8")
    # Fins
    draw.polygon([(cx - w, cy + int(20*scale)), (cx - w - int(30*scale), cy + h), (cx - w, cy + h)], fill="#0284C7")
    draw.polygon([(cx + w, cy + int(20*scale)), (cx + w + int(30*scale), cy + h), (cx + w, cy + h)], fill="#0284C7")
    # Thruster flame
    draw.polygon([(cx - int(20*scale), cy + h), (cx + int(20*scale), cy + h), (cx, cy + h + int(45*scale))], fill="#F59E0B")

def draw_canned_food(draw, cx, cy, scale=1.0):
    w, h = int(45 * scale), int(65 * scale)
    draw.rounded_rectangle([(cx - w, cy - h), (cx + w, cy + h)], radius=int(10*scale), fill="#CBD5E1", outline="#475569", width=max(2, int(3*scale)))
    draw.rectangle([(cx - w, cy - int(h*0.5)), (cx + w, cy + int(h*0.5))], fill="#F59E0B")
    draw.ellipse([(cx - w, cy - h - int(10*scale)), (cx + w, cy - h + int(10*scale))], fill="#94A3B8")

def draw_codex_book(draw, cx, cy, scale=1.0):
    w, h = int(55 * scale), int(70 * scale)
    draw.rounded_rectangle([(cx - w, cy - h), (cx + w, cy + h)], radius=int(8*scale), fill="#1E293B", outline="#FBBF24", width=max(2, int(3*scale)))
    draw.rectangle([(cx - w, cy - h), (cx - w + int(15*scale), cy + h)], fill="#F59E0B")
    draw.text((cx - int(20*scale), cy - int(15*scale)), "CODEX", fill="#FBBF24", font=get_font(max(10, int(16*scale)), bold=True))

def draw_law_seal(draw, cx, cy, scale=1.0):
    r = int(55 * scale)
    draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill="#059669", outline="#10B981", width=max(2, int(4*scale)))
    draw.text((cx - int(42*scale), cy - int(12*scale)), "LAW (EC)", fill="#FFFFFF", font=get_font(max(10, int(18*scale)), bold=True))
