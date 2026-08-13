from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from PIL import Image
import os

# ---- KDP wrap geometry: 8.5 x 8.5 trim, 24 pages premium color ----
TRIM = 8.5 * inch
BLEED = 0.125 * inch
SPINE = 24 * 0.002347 * inch          # ~0.0563"
W = BLEED + TRIM + SPINE + TRIM + BLEED
H = TRIM + 2 * BLEED

OUT = "/mnt/user-data/outputs/Mango_and_the_Busy_Brain_COVER.pdf"
c = canvas.Canvas(OUT, pagesize=(W, H))

# zones
back_x0 = 0
front_x0 = BLEED + TRIM + SPINE        # left edge of front incl. its own area
# front spans from front_x0 to W (right bleed included)

# ---------- BACK COVER background: soft cream ----------
c.setFillColorRGB(0.97, 0.96, 0.90)
c.rect(0, 0, BLEED + TRIM + SPINE/2, H, fill=1, stroke=0)

# ---------- SPINE: deep green band ----------
c.setFillColorRGB(0.11, 0.36, 0.23)
c.rect(BLEED + TRIM, 0, SPINE, H, fill=1, stroke=0)

# ---------- FRONT COVER: titled artwork, bled to edges ----------
c.drawImage(ImageReader("/home/claude/cover_titled.jpg"),
            front_x0 - SPINE/2, 0, W - front_x0 + SPINE/2, H,
            preserveAspectRatio=False)

# ---------- BACK COVER content ----------
blurb_h = ParagraphStyle("bh", fontName="Helvetica-Bold", fontSize=19,
                         leading=25, alignment=TA_CENTER, textColor="#1d6b3f")
blurb_b = ParagraphStyle("bb", fontName="Helvetica", fontSize=12.5,
                         leading=19, alignment=TA_CENTER, textColor="#333333")
blurb_i = ParagraphStyle("bi", fontName="Helvetica-Oblique", fontSize=11.5,
                         leading=17, alignment=TA_CENTER, textColor="#1d6b3f")

bx = BLEED + 0.85*inch
bw = TRIM - 1.7*inch

f = Frame(bx, H - 2.3*inch, bw, 1.4*inch, showBoundary=0)
f.addFromList([Paragraph("Mango's brain has its own legs!", blurb_h)], c)

f = Frame(bx, H - 5.6*inch, bw, 3.3*inch, showBoundary=0)
f.addFromList([Paragraph(
    "Mango the little crocodile tries so hard to listen at school &mdash; but "
    "Mango's busy brain keeps running off to dragonflies, beetles, and a "
    "hundred wonderful ideas.<br/><br/>"
    "When sitting still only makes things worse, wise old Gogo the turtle "
    "shares a secret that changes everything: <b>don't trap your busy brain "
    "&mdash; aim it.</b><br/><br/>"
    "A warm, funny story for every child who notices everything, moves fast, "
    "and feels behind &mdash; and for the grown-ups who love them.",
    blurb_b)], c)

f = Frame(bx, H - 6.7*inch, bw, 1.0*inch, showBoundary=0)
f.addFromList([Paragraph(
    "Written with the guidance of a child &amp; adolescent psychiatrist "
    "&mdash; includes a practical Note for Parents.", blurb_i)], c)

# decorative ridge bumps on back
c.setFillColorRGB(0.45, 0.83, 0.55)
cx = BLEED + TRIM/2 - 0.56*inch
for i in range(5):
    c.circle(cx + i*0.28*inch, H - 7.1*inch, 0.085*inch, fill=1, stroke=0)

# ---------- barcode safe area (KDP places barcode here) ----------
c.setFillColorRGB(1, 1, 1)
c.rect(BLEED + TRIM - 2.25*inch, BLEED + 0.25*inch, 2.0*inch, 1.2*inch, fill=1, stroke=0)

c.save()
print(f"Cover wrap saved: {OUT}")
print(f"Size: {W/inch:.3f} x {H/inch:.3f} in  (spine {SPINE/inch:.4f} in)")
