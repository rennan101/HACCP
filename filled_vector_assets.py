import math
from PIL import Image, ImageDraw

def draw_filled_dairy_tank(draw, center_x, center_y, scale=1.0, float_offset=0):
    if scale <= 0.05:
        return
    cy = center_y + float_offset
    w = int(85 * scale)
    h = int(120 * scale)
    x1, y1 = center_x - w, cy - h
    x2, y2 = center_x + w, cy + h
    
    shadow_w = int(w * 1.3)
    shadow_h = int(18 * scale)
    draw.ellipse([(center_x - shadow_w, y2 + int(12*scale)), (center_x + shadow_w, y2 + int(12*scale) + shadow_h)], fill="#E2E8F0")
    
    draw.rounded_rectangle([(x1, y1 + int(30*scale)), (x2, y2 - int(25*scale))], radius=max(2, int(16*scale)), fill="#CBD5E1")
    draw.rectangle([(center_x - int(25*scale), y1 + int(30*scale)), (center_x + int(10*scale), y2 - int(25*scale))], fill="#F1F5F9")
    draw.rectangle([(center_x + int(18*scale), y1 + int(30*scale)), (center_x + int(30*scale), y2 - int(25*scale))], fill="#E2E8F0")
    
    draw.ellipse([(x1, y1), (x2, y1 + int(60*scale))], fill="#94A3B8")
    draw.ellipse([(x1 + int(10*scale), y1 + int(6*scale)), (x2 - int(10*scale), y1 + int(48*scale))], fill="#E2E8F0")
    
    draw.ellipse([(center_x - int(20*scale), y1 + int(12*scale)), (center_x + int(20*scale), y1 + int(36*scale))], fill="#0284C7")
    draw.ellipse([(center_x - int(14*scale), y1 + int(16*scale)), (center_x + int(14*scale), y1 + int(32*scale))], fill="#38BDF8")
    
    leg_w = max(2, int(12 * scale))
    draw.rectangle([(x1 + int(15*scale), y2 - int(25*scale)), (x1 + int(15*scale) + leg_w, y2 + int(20*scale))], fill="#64748B")
    draw.rectangle([(x2 - int(15*scale) - leg_w, y2 - int(25*scale)), (x2 - int(15*scale), y2 + int(20*scale))], fill="#64748B")
    
    draw.rectangle([(center_x - int(14*scale), y2 - int(25*scale)), (center_x + int(14*scale), y2 + int(10*scale))], fill="#0284C7")
    draw.ellipse([(center_x - int(18*scale), y2 + int(8*scale)), (center_x + int(18*scale), y2 + int(24*scale))], fill="#0369A1")
    draw.rounded_rectangle([(center_x - int(38*scale), cy - int(20*scale)), (center_x + int(38*scale), cy + int(20*scale))], radius=max(2, int(6*scale)), fill="#0F172A")
    draw.ellipse([(center_x - int(28*scale), cy - int(6*scale)), (center_x - int(18*scale), cy + int(6*scale))], fill="#10B981")

def draw_filled_microbe(draw, center_x, center_y, scale=1.0, float_offset=0):
    if scale <= 0.05:
        return
    cy = center_y + float_offset
    r = int(55 * scale)
    
    draw.ellipse([(center_x - r, cy + int(r*0.8)), (center_x + r, cy + int(r*1.2))], fill="#FEE2E2")
    draw.ellipse([(center_x - r, cy - r), (center_x + r, cy + r)], fill="#EF4444")
    draw.ellipse([(center_x - int(r*0.75), cy - int(r*0.75)), (center_x + int(r*0.75), cy + int(r*0.75))], fill="#F87171")
    
    draw.ellipse([(center_x - int(18*scale), cy - int(18*scale)), (center_x + int(18*scale), cy + int(18*scale))], fill="#B91C1C")
    draw.ellipse([(center_x + int(12*scale), cy + int(10*scale)), (center_x + int(28*scale), cy + int(26*scale))], fill="#FECA57")
    draw.ellipse([(center_x - int(28*scale), cy + int(12*scale)), (center_x - int(14*scale), cy + int(26*scale))], fill="#FFFFFF")
    
    for angle in range(0, 360, 36):
        rad = math.radians(angle)
        px = center_x + math.cos(rad) * (r + int(12 * scale))
        py = cy + math.sin(rad) * (r + int(12 * scale))
        node_r = max(1, int(7*scale))
        draw.ellipse([(px - node_r, py - node_r), (px + node_r, py + node_r)], fill="#DC2626")

def draw_filled_chemical_bottle(draw, center_x, center_y, scale=1.0, float_offset=0):
    if scale <= 0.05:
        return
    cy = center_y + float_offset
    w = int(50 * scale)
    h = int(70 * scale)
    
    draw.ellipse([(center_x - w, cy + h - int(5*scale)), (center_x + w, cy + h + int(15*scale))], fill="#FEF3C7")
    draw.rounded_rectangle([(center_x - w, cy - int(h*0.5)), (center_x + w, cy + h)], radius=max(2, int(12*scale)), fill="#F59E0B")
    draw.rounded_rectangle([(center_x - int(20*scale), cy - h), (center_x + int(20*scale), cy - int(h*0.5))], radius=max(2, int(6*scale)), fill="#D97706")
    draw.rectangle([(center_x - int(16*scale), cy - int(h*0.9)), (center_x + int(16*scale), cy - int(h*0.7))], fill="#92400E")
    
    draw.rounded_rectangle([(center_x - int(38*scale), cy - int(15*scale)), (center_x + int(38*scale), cy + int(45*scale))], radius=max(2, int(6*scale)), fill="#FFFFFF")
    pts = [
        (center_x, cy - int(5*scale)),
        (center_x + int(20*scale), cy + int(15*scale)),
        (center_x, cy + int(35*scale)),
        (center_x - int(20*scale), cy + int(15*scale))
    ]
    draw.polygon(pts, fill="#EF4444")
    draw.ellipse([(center_x - int(6*scale), cy + int(10*scale)), (center_x + int(6*scale), cy + int(22*scale))], fill="#FFFFFF")

def draw_filled_filter_gear(draw, center_x, center_y, scale=1.0, float_offset=0):
    if scale <= 0.05:
        return
    cy = center_y + float_offset
    r = int(55 * scale)
    
    draw.ellipse([(center_x - r, cy + int(r*0.8)), (center_x + r, cy + int(r*1.2))], fill="#E0F2FE")
    
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        gx = center_x + math.cos(rad) * int(r * 0.95)
        gy = cy + math.sin(rad) * int(r * 0.95)
        t_r = max(1, int(14*scale))
        draw.ellipse([(gx - t_r, gy - t_r), (gx + t_r, gy + t_r)], fill="#0284C7")
        
    draw.ellipse([(center_x - r, cy - r), (center_x + r, cy + r)], fill="#0369A1")
    draw.ellipse([(center_x - int(r*0.75), cy - int(r*0.75)), (center_x + int(r*0.75), cy + int(r*0.75))], fill="#BAE6FD")
    
    step = max(4, int(16*scale))
    bar_w = max(1, int(3*scale))
    for o in range(-int(r*0.5), int(r*0.6), step):
        draw.line([(center_x + o, cy - int(r*0.6)), (center_x + o, cy + int(r*0.6))], fill="#0284C7", width=bar_w)
        draw.line([(center_x - int(r*0.6), cy + o), (center_x + int(r*0.6), cy + o)], fill="#0284C7", width=bar_w)
        
    draw.ellipse([(center_x - int(16*scale), cy - int(16*scale)), (center_x + int(16*scale), cy + int(16*scale))], fill="#0F172A")
    draw.ellipse([(center_x - int(8*scale), cy - int(8*scale)), (center_x + int(8*scale), cy + int(8*scale))], fill="#38BDF8")

def draw_filled_quality_shield(draw, center_x, center_y, scale=1.0, float_offset=0):
    if scale <= 0.05:
        return
    cy = center_y + float_offset
    w = int(70 * scale)
    h = int(90 * scale)
    
    draw.ellipse([(center_x - w, cy + h), (center_x + w, cy + h + int(20*scale))], fill="#D1FAE5")
    
    pts_outer = [
        (center_x, cy - h),
        (center_x + w, cy - int(h * 0.7)),
        (center_x + w, cy + int(h * 0.3)),
        (center_x, cy + h),
        (center_x - w, cy + int(h * 0.3)),
        (center_x - w, cy - int(h * 0.7))
    ]
    draw.polygon(pts_outer, fill="#059669")
    
    inset = max(2, int(8 * scale))
    pts_inner = [
        (center_x, cy - h + inset),
        (center_x + w - inset, cy - int(h * 0.7) + int(inset*0.5)),
        (center_x + w - inset, cy + int(h * 0.3) - int(inset*0.5)),
        (center_x, cy + h - inset),
        (center_x - w + inset, cy + int(h * 0.3) - int(inset*0.5)),
        (center_x - w + inset, cy - int(h * 0.7) + int(inset*0.5))
    ]
    draw.polygon(pts_inner, fill="#10B981")
    
    r_star = int(32 * scale)
    star_pts = []
    for i in range(10):
        rad = math.radians(i * 36 - 90)
        curr_r = r_star if i % 2 == 0 else int(r_star * 0.45)
        star_pts.append((center_x + math.cos(rad) * curr_r, cy + math.sin(rad) * curr_r))
    draw.polygon(star_pts, fill="#FBBF24")
    draw.ellipse([(center_x - int(8*scale), cy - int(8*scale)), (center_x + int(8*scale), cy + int(8*scale))], fill="#F59E0B")

def draw_filled_thermometer_gauge(draw, center_x, center_y, scale=1.0, float_offset=0, temp_val="72.5°C"):
    if scale <= 0.05:
        return
    cy = center_y + float_offset
    r = int(55 * scale)
    draw.ellipse([(center_x - r, cy - r), (center_x + r, cy + r)], fill="#0F172A", outline="#EF4444", width=max(2, int(4*scale)))
    draw.ellipse([(center_x - int(r*0.8), cy - int(r*0.8)), (center_x + int(r*0.8), cy + int(r*0.8))], fill="#1E293B")
    draw.ellipse([(center_x - int(12*scale), cy - int(12*scale)), (center_x + int(12*scale), cy + int(12*scale))], fill="#EF4444")
