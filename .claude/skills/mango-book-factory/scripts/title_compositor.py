from PIL import Image, ImageDraw, ImageFont

src = "/mnt/user-data/uploads/in_a_classic_cinematic_3D_202606040213.jpeg"
im = Image.open(src).convert("RGB")
W, H = im.size  # 2048 x 2048
draw = ImageDraw.Draw(im)

# Use a try-variable font; set a heavy weight by loading at large size
def load(sz):
    try:
        return ImageFont.truetype("Baloo2.ttf", sz)
    except:
        return ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf", sz)

# Two lines for nice stacking
line1 = "Mango and"
line2 = "the Busy Brain"

font = load(210)

def text_w(t, f):
    b = draw.textbbox((0,0), t, font=f)
    return b[2]-b[0], b[3]-b[1]

# shrink to fit width with margin
margin = 180
while True:
    w1,h1 = text_w(line1, font)
    w2,h2 = text_w(line2, font)
    if max(w1,w2) <= W - margin*2:
        break
    size = font.size - 6
    font = load(size)

w1,h1 = text_w(line1, font)
w2,h2 = text_w(line2, font)
line_gap = int(font.size * 0.12)
total_h = h1 + line_gap + h2

# place in upper sky region
top_y = int(H * 0.05)

cream = (255, 250, 235)
green_outline = (28, 92, 58)
shadow = (20, 60, 40)

def draw_text_outlined(cx, y, text, f):
    w,h = text_w(text, f)
    x = (W - w)//2
    # offset for bbox top padding
    bb = draw.textbbox((0,0), text, font=f)
    x -= bb[0]
    y -= bb[1]
    # soft shadow
    off = max(3, f.size//40)
    # thick outline
    ow = max(6, f.size//22)
    for dx in range(-ow, ow+1, 2):
        for dy in range(-ow, ow+1, 2):
            if dx*dx+dy*dy <= ow*ow:
                draw.text((x+dx, y+dy), text, font=f, fill=green_outline)
    draw.text((x, y), text, font=f, fill=cream)

draw_text_outlined(W//2, top_y, line1, font)
draw_text_outlined(W//2, top_y + h1 + line_gap, line2, font)

im.save("/home/claude/cover_titled.jpg", quality=95)
print("done", im.size)
