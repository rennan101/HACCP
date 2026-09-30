from PIL import ImageDraw

def draw_centered_text(draw, text, box_center_x, box_center_y, font, fill):
    """Draws multiline or single-line text perfectly centered inside a bounding coordinate."""
    lines = text.split("\n")
    line_heights = []
    line_widths = []
    
    for l in lines:
        bbox = draw.textbbox((0, 0), l, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        line_widths.append(w)
        line_heights.append(h)
        
    total_height = sum(line_heights) + (len(lines) - 1) * 8
    start_y = box_center_y - total_height // 2
    
    curr_y = start_y
    for i, l in enumerate(lines):
        w = line_widths[i]
        h = line_heights[i]
        line_x = box_center_x - w // 2
        draw.text((line_x, curr_y), l, fill=fill, font=font)
        curr_y += h + 8

def draw_centered_box_text(draw, box_coords, text, font, fill_text, box_bg=None, box_border=None, radius=12, border_w=2):
    """Draws a rounded card box and places text precisely centered inside it."""
    x1, y1, x2, y2 = box_coords
    if box_bg or box_border:
        draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=radius, fill=box_bg, outline=box_border, width=border_w)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    draw_centered_text(draw, text, center_x, center_y, font, fill_text)
