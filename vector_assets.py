import math
from PIL import Image, ImageDraw

def draw_dairy_tank_icon(draw, center_x, center_y, scale=1.0):
    # Stainless Steel Processing Tank (Vector Drawing)
    w = int(70 * scale)
    h = int(100 * scale)
    x1, y1 = center_x - w, center_y - h
    x2, y2 = center_x + w, center_y + h
    
    # Tank Body
    draw.rounded_rectangle([(x1, y1 + int(20*scale)), (x2, y2 - int(20*scale))], radius=int(12*scale), fill="#E2E8F0", outline="#0284C7", width=max(2, int(4*scale)))
    # Top Dome
    draw.ellipse([(x1, y1), (x2, y1 + int(40*scale))], fill="#CBD5E1", outline="#0284C7", width=max(2, int(4*scale)))
    # Tank Legs
    leg_w = max(2, int(6*scale))
    draw.rectangle([(x1 + int(15*scale), y2 - int(20*scale)), (x1 + int(15*scale) + leg_w, y2 + int(15*scale))], fill="#64748B")
    draw.rectangle([(x2 - int(15*scale) - leg_w, y2 - int(20*scale)), (x2 - int(15*scale), y2 + int(15*scale))], fill="#64748B")
    # Valve & In-line pipe
    draw.rectangle([(center_x - int(8*scale), y2 - int(20*scale)), (center_x + int(8*scale), y2 + int(5*scale))], fill="#0284C7")
    draw.ellipse([(center_x - int(12*scale), y2 + int(5*scale)), (center_x + int(12*scale), y2 + int(15*scale))], fill="#0284C7")

def draw_biohazard_microbe_icon(draw, center_x, center_y, scale=1.0):
    # Microbe / Bacterium Vector
    r = int(50 * scale)
    draw.ellipse([(center_x - r, center_y - r), (center_x + r, center_y + r)], fill="#FEE2E2", outline="#EF4444", width=max(2, int(4*scale)))
    # Spikes around cell
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        sx1 = center_x + math.cos(rad) * r
        sy1 = center_y + math.sin(rad) * r
        sx2 = center_x + math.cos(rad) * (r + int(15 * scale))
        sy2 = center_y + math.sin(rad) * (r + int(15 * scale))
        draw.line([(sx1, sy1), (sx2, sy2)], fill="#EF4444", width=max(2, int(4*scale)))
    # Inner nucleus dots
    draw.ellipse([(center_x - int(15*scale), center_y - int(15*scale)), (center_x + int(15*scale), center_y + int(15*scale))], fill="#EF4444")
    draw.ellipse([(center_x + int(12*scale), center_y + int(10*scale)), (center_x + int(22*scale), center_y + int(20*scale))], fill="#F87171")

def draw_chemical_flask_icon(draw, center_x, center_y, scale=1.0):
    # Erlenmeyer Chemical Flask Vector
    r = int(45 * scale)
    # Neck
    draw.rectangle([(center_x - int(12*scale), center_y - int(55*scale)), (center_x + int(12*scale), center_y - int(15*scale))], fill="#FEF3C7", outline="#F59E0B", width=max(2, int(4*scale)))
    # Lip
    draw.rectangle([(center_x - int(18*scale), center_y - int(60*scale)), (center_x + int(18*scale), center_y - int(52*scale))], fill="#F59E0B")
    # Base triangle
    points = [
        (center_x - int(12*scale), center_y - int(15*scale)),
        (center_x - r - int(10*scale), center_y + r),
        (center_x + r + int(10*scale), center_y + r),
        (center_x + int(12*scale), center_y - int(15*scale))
    ]
    draw.polygon(points, fill="#FEF3C7", outline="#F59E0B")
    draw.line(points + [points[0]], fill="#F59E0B", width=max(2, int(4*scale)))
    # Liquid level
    draw.ellipse([(center_x - int(15*scale), center_y + int(15*scale)), (center_x - int(5*scale), center_y + int(25*scale))], fill="#F59E0B")

def draw_metal_filter_gear_icon(draw, center_x, center_y, scale=1.0):
    # Industrial Gear & Particle Mesh Vector
    r = int(48 * scale)
    draw.ellipse([(center_x - r, center_y - r), (center_x + r, center_y + r)], fill="#E0F2FE", outline="#0284C7", width=max(2, int(4*scale)))
    # Crosshairs / Mesh Grid
    draw.line([(center_x - r, center_y), (center_x + r, center_y)], fill="#0284C7", width=max(1, int(3*scale)))
    draw.line([(center_x, center_y - r), (center_x, center_y + r)], fill="#0284C7", width=max(1, int(3*scale)))
    # Center hub
    draw.ellipse([(center_x - int(16*scale), center_y - int(16*scale)), (center_x + int(16*scale), center_y + int(16*scale))], fill="#0284C7")

def draw_shield_badge_icon(draw, center_x, center_y, scale=1.0):
    # Security / Quality Assurance Shield Vector
    w = int(55 * scale)
    h = int(70 * scale)
    points = [
        (center_x, center_y - h),
        (center_x + w, center_y - int(h * 0.7)),
        (center_x + w, center_y + int(h * 0.2)),
        (center_x, center_y + h),
        (center_x - w, center_y + int(h * 0.2)),
        (center_x - w, center_y - int(h * 0.7))
    ]
    draw.polygon(points, fill="#ECFDF5", outline="#10B981")
    draw.line(points + [points[0]], fill="#10B981", width=max(2, int(4*scale)))
    # Checkmark inside shield
    chk_pts = [
        (center_x - int(20*scale), center_y),
        (center_x - int(5*scale), center_y + int(18*scale)),
        (center_x + int(22*scale), center_y - int(15*scale))
    ]
    draw.line(chk_pts, fill="#10B981", width=max(2, int(6*scale)))
