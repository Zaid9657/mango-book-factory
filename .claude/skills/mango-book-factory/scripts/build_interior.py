from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

U = "/mnt/user-data/uploads/"
OUT = "/mnt/user-data/outputs/Mango_and_the_Busy_Brain_INTERIOR.pdf"

PAGE = 8.5 * inch
c = canvas.Canvas(OUT, pagesize=(PAGE, PAGE))

imgs = {i: U + f"page_{i}.png" for i in range(1, 8)}

# ---------- styles ----------
title_style = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=32,
                             leading=38, alignment=TA_CENTER, textColor="#1d6b3f")
sub_style   = ParagraphStyle("sub", fontName="Helvetica-Oblique", fontSize=14,
                             leading=19, alignment=TA_CENTER, textColor="#555555")
body_style  = ParagraphStyle("body", fontName="Helvetica", fontSize=17,
                             leading=26, alignment=TA_CENTER, textColor="#222222")
small_style = ParagraphStyle("small", fontName="Helvetica", fontSize=9.5,
                             leading=13, alignment=TA_CENTER, textColor="#888888")
note_h      = ParagraphStyle("noteh", fontName="Helvetica-Bold", fontSize=20,
                             leading=26, alignment=TA_CENTER, textColor="#1d6b3f")
note_body   = ParagraphStyle("noteb", fontName="Helvetica", fontSize=12.5,
                             leading=18.5, alignment=TA_LEFT, textColor="#222222")
end_style   = ParagraphStyle("end", fontName="Helvetica-Oblique", fontSize=16,
                             leading=24, alignment=TA_CENTER, textColor="#1d6b3f")
chart_style = ParagraphStyle("chart", fontName="Helvetica", fontSize=14,
                             leading=24, alignment=TA_LEFT, textColor="#222222")

def white_page():
    c.setFillColorRGB(1, 1, 1)
    c.rect(0, 0, PAGE, PAGE, fill=1, stroke=0)

def full_image(path):
    c.drawImage(ImageReader(path), 0, 0, PAGE, PAGE, preserveAspectRatio=False)

def block(text, style, y_bottom, height, x=0.8*inch, w=None):
    w = w or PAGE - 1.6*inch
    f = Frame(x, y_bottom, w, height, leftPadding=0, rightPadding=0,
              topPadding=6, bottomPadding=6, showBoundary=0)
    f.addFromList([Paragraph(text, style)], c)

def deco_ridge(y):
    """Small green bump motif as a page decoration."""
    c.setFillColorRGB(0.45, 0.83, 0.55)
    cx = PAGE/2 - 0.55*inch
    for i in range(5):
        r = 0.09*inch
        c.circle(cx + i*0.28*inch, y, r, fill=1, stroke=0)

# ============================================================
# p1 TITLE PAGE
white_page()
block("Mango and the Busy Brain", title_style, PAGE-3.4*inch, 1.6*inch)
block("A Mango the Crocodile Story", sub_style, PAGE-4.05*inch, 0.5*inch)
deco_ridge(PAGE-4.5*inch)
c.showPage()

# p2 COPYRIGHT / DEDICATION
white_page()
block("For every kid whose brain moves fast.", sub_style, PAGE-3.4*inch, 0.7*inch)
block("Copyright \u00a9 2026. All rights reserved.<br/>"
      "No part of this book may be reproduced without permission.<br/>"
      "Independently published.", small_style, 1.1*inch, 1.0*inch)
c.showPage()

# ---------- story: 7 spreads = image page + text page ----------
story = [
    (1, "Mango loved mornings at the riverbank.<br/><br/>"
        "The dragonflies zipped past. The lily pads bobbed. The water sparkled "
        "like it was winking.<br/><br/>"
        "And Mango's brain? Mango's brain was already going a thousand miles a "
        "minute &mdash; even before breakfast.<br/><br/>"
        "<i>What if I could catch a dragonfly? What if I built a raft? What if "
        "lily pads could talk?</i>"),
    (2, "School at the riverbank meant sitting on a log while Mr. Heron taught "
        "important things.<br/><br/>"
        "Today it was how rivers find their way to the sea. Mango listened&hellip; "
        "for about thirty seconds.<br/><br/>"
        "Then a leaf fell and spun on the water. Then a beetle crawled by. Then "
        "Mango's busy brain wandered far, far away &mdash; all by itself."),
    (3, "\u201cMango? Can you tell me what we just learned?\u201d<br/><br/>"
        "Mango's back-ridge flickered yellow.<br/><br/>"
        "\u201cUm&hellip; rivers go somewhere?\u201d<br/><br/>"
        "A few animals giggled. Mango stared at the ground, and the little "
        "lights along Mango's back went dull and gray."),
    (4, "After school, Mango sat alone, tossing pebbles into the water. "
        "One. <i>Plunk.</i> Two. <i>Plunk.</i><br/><br/>"
        "Gogo the turtle sat down beside Mango. He didn't rush. He never did."
        "<br/><br/>"
        "\u201cMy brain won't work right,\u201d Mango muttered. \u201cIt's like "
        "it has its own legs.\u201d<br/><br/>"
        "\u201cOr,\u201d said Gogo gently, \u201cyours notices things the rest "
        "of us miss.\u201d"),
    (5, "The next day, Mango tried as hard as a little crocodile can try.<br/><br/>"
        "Sit still. Fold hands. Squeeze every wriggle in.<br/><br/>"
        "But the harder Mango fought, the louder the buzzing grew &mdash; and "
        "Mango missed every single word.<br/><br/>"
        "\u201cYou were fighting your brain,\u201d said Gogo. \u201cDon't trap "
        "it, Mango. <i>Aim</i> it.\u201d"),
    (6, "Out in the reeds, Mango stopped fighting &mdash; and pointed the busy "
        "brain at the river.<br/><br/>"
        "It noticed everything at once. The swirl by the bend. The fast water "
        "by the curve.<br/><br/>"
        "\u201cMr. Heron! Follow the fast water and it leads you home!\u201d"
        "<br/><br/>"
        "\u201cExactly right,\u201d the heron smiled. \u201cThat is the skill "
        "of an explorer.\u201d And Mango's back glowed bright, bright green."),
    (7, "That night, Mango's brain still jumped &mdash; from stars to fish to "
        "floating rafts.<br/><br/>"
        "Mango smiled, and gently aimed it. <i>Stars. Just the stars for now.</i>"
        "<br/><br/>"
        "It wandered. Mango aimed it again. It wasn't perfect. It never would "
        "be.<br/><br/>"
        "But the brain that wandered in class was the same brain that found "
        "the river's secret. And maybe that was what made Mango&hellip; "
        "<i>Mango.</i>"),
]

for idx, txt in story:
    # image page
    full_image(imgs[idx])
    c.showPage()
    # facing text page
    white_page()
    block(txt, body_style, 1.6*inch, PAGE - 3.2*inch)
    deco_ridge(1.15*inch)
    c.showPage()

# p17 closing message
white_page()
block("For every kid whose brain moves fast:<br/><br/>"
      "You are not broken. You are not behind.<br/>"
      "You just notice more &mdash; and that is something worth keeping.",
      end_style, PAGE-4.8*inch, 2.2*inch)
deco_ridge(PAGE-5.2*inch)
c.showPage()

# p18-19 A NOTE FOR PARENTS (the psychiatrist moat)
white_page()
block("A Note for Parents", note_h, PAGE-1.7*inch, 0.6*inch)
block("As a child and adolescent psychiatrist, I meet many children like Mango "
      "&mdash; bright, curious kids whose attention seems to \u201chave its own "
      "legs.\u201d A busy brain is not a character flaw, and it is not a "
      "discipline problem. It is a different style of attention: quick to "
      "notice, quick to move on.<br/><br/>"
      "This book's idea &mdash; <b>\u201cdon't trap it, aim it\u201d</b> &mdash; "
      "comes from what actually helps. Forcing a child to suppress every "
      "wriggle and wandering thought usually backfires: the effort of sitting "
      "still consumes the very attention we wanted them to use. Redirecting "
      "works better than restricting.<br/><br/>"
      "How to use this story at home:<br/>"
      "&bull; <b>Name the signal.</b> Like Mango's colors, every child has body "
      "signals. Help your child notice theirs without judgment.<br/>"
      "&bull; <b>Practice \u201caiming.\u201d</b> When attention drifts, try "
      "\u201ccome back to one thing\u201d &mdash; gently, like Mango with the "
      "stars. Expect it to wander again. That's normal. The skill is the "
      "return, not the staying.",
      note_body, 1.0*inch, PAGE - 2.9*inch)
c.showPage()

white_page()
block("&bull; <b>Catch the strengths.</b> Busy-brained children often notice "
      "what others miss. Point it out when it happens &mdash; specific praise "
      "(\u201cyou spotted that before anyone\u201d) builds real confidence, the "
      "kind that survives a hard school day.<br/>"
      "&bull; <b>Keep failure small and safe.</b> Mango tries, fails, and tries "
      "differently. Let your child see that trying again differently is the "
      "win.<br/><br/>"
      "<b>When to seek support:</b> if attention struggles consistently affect "
      "your child's learning, friendships, or self-esteem across settings "
      "(home <i>and</i> school), talk to your pediatrician or a child mental "
      "health professional. An assessment is not a label &mdash; it is a map. "
      "Children do best when the adults around them understand how their "
      "particular brain works.<br/><br/>"
      "Whatever you learn, the message your child needs most is the one this "
      "book ends with: <i>you are not broken, you are not behind &mdash; you "
      "just notice more.</i>",
      note_body, 2.2*inch, PAGE - 3.6*inch)
c.showPage()

# p20 MANGO'S FEELING COLORS chart
white_page()
block("Mango's Feeling Colors", note_h, PAGE-1.7*inch, 0.6*inch)
colors = [
    ((0.42,0.78,0.47), "Soft green &mdash; calm and happy"),
    ((0.98,0.78,0.25), "Yellow &mdash; worried or unsure"),
    ((0.62,0.62,0.62), "Gray &mdash; sad or embarrassed"),
    ((0.95,0.45,0.30), "Red-orange &mdash; angry or frustrated"),
    ((0.30,0.85,0.45), "Bright green &mdash; proud and excited"),
]
y = PAGE - 2.6*inch
for rgb, label in colors:
    c.setFillColorRGB(*rgb)
    c.circle(1.5*inch, y+0.09*inch, 0.16*inch, fill=1, stroke=0)
    block(label, chart_style, y-0.25*inch, 0.7*inch, x=2.0*inch, w=PAGE-2.9*inch)
    y -= 0.72*inch
block("What color is <i>your</i> back-ridge right now?", sub_style, y-0.7*inch, 0.7*inch)
c.showPage()

# p21 TRY IT activity
white_page()
block("Try It: Aim Your Brain", note_h, PAGE-1.7*inch, 0.6*inch)
block("Mango's game for busy brains &mdash; play it anywhere:<br/><br/>"
      "1. Let your brain run! Count five things you can see.<br/><br/>"
      "2. Now <b>aim it</b>: pick just one thing.<br/><br/>"
      "3. Look at only that thing while you take three slow breaths.<br/><br/>"
      "4. Did your brain wander? That's okay &mdash; it always does!<br/>"
      "Just bring it back. <i>The bringing-back is the superpower.</i>",
      chart_style, 1.8*inch, PAGE - 3.6*inch)
deco_ridge(1.3*inch)
c.showPage()

# p22 series page
white_page()
block("More Mango Adventures", note_h, PAGE-2.6*inch, 0.6*inch)
block("Mango's back-ridge has many colors &mdash;<br/>"
      "and every color has a story.<br/><br/>"
      "Look for the next book in the<br/><b>Mango the Crocodile</b> series.",
      body_style, PAGE-4.6*inch, 1.8*inch)
deco_ridge(PAGE-5.0*inch)
c.showPage()

# p23 this book belongs to
white_page()
block("This book belongs to", sub_style, PAGE-3.6*inch, 0.5*inch)
c.setStrokeColorRGB(0.3,0.55,0.4)
c.setLineWidth(1.2)
c.line(2.2*inch, PAGE-4.5*inch, PAGE-2.2*inch, PAGE-4.5*inch)
deco_ridge(PAGE-5.0*inch)
c.showPage()

# p24 blank end page
white_page()
c.showPage()

c.save()
print("pages: 24  saved:", OUT, os.path.getsize(OUT))
