#!/usr/bin/env python3
"""
Mango Book Image Generator
--------------------------
Generates all interior page images for a "Mango the Crocodile" book using the
Gemini image API (Nano Banana), keeping the character consistent by passing a
locked reference image into every call.

SETUP (one time):
  pip install google-genai pillow
  export GEMINI_API_KEY="your_key_here"     # get a key at https://aistudio.google.com/apikey

RUN:
  python generate_mango_images.py

OUTPUT:
  Saves page_1.png ... page_N.png into ./mango_images/
"""

import os
import sys
from io import BytesIO

try:
    from google import genai
    from google.genai import types
    from PIL import Image
except ImportError:
    sys.exit("Missing libs. Run: pip install google-genai pillow")

# ----------------------------------------------------------------------
# CONFIG — key and reference are bundled in the skill's assets/ folder
# ----------------------------------------------------------------------
import pathlib
ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"

API_KEY = os.getenv("GEMINI_API_KEY") or (ASSETS / "gemini_key.txt").read_text().strip()
if not API_KEY or "PASTE_YOUR" in API_KEY:
    sys.exit("No API key: edit assets/gemini_key.txt in the skill (or set GEMINI_API_KEY).")

MODEL = "gemini-3-pro-image"          # Nano Banana Pro (best for books).
                                      # For cheaper/faster use: "gemini-3.1-flash-image"
REFERENCE_IMAGE = str(ASSETS / "mango_reference.jpg")   # bundled locked Mango reference
OUTPUT_DIR = "mango_images"

# The unchanging style + character description prepended to every scene.
STYLE = (
    "Classic cinematic 3D kids storybook illustration style, soft warm lighting, "
    "same character every time: a small round cute baby crocodile named Mango — "
    "chubby body, stubby legs, big round head, huge friendly brown eyes, mint-green "
    "skin with a soft pale belly, one tiny snaggle-tooth, and a row of bumps along "
    "his back. Keep Mango's design IDENTICAL to the reference image. Square 1:1 "
    "composition, no text or words in the image, no signs. "
)

# One entry per interior page: (filename, scene-specific prompt incl. back-ridge color)
SCENES = [
    ("page_1", "Joyful afternoon at the sunny riverbank school. Mango beams with excitement "
               "as the heron teacher announces Mango will tell a story at tomorrow's River Show, "
               "young animal friends clapping. Back-ridge bumps glow soft green."),
    ("page_2", "Evening at the riverbank, dusk colors. Mango lies awake looking troubled while a "
               "small fluffy gray worry-cloud hovers above Mango's head. Back-ridge bumps flicker yellow."),
    ("page_3", "Next morning. Mango sits at breakfast by the river looking unwell and anxious, "
               "holding tummy, food untouched on a leaf plate, the worry cloud bigger and darker overhead. "
               "Back-ridge bumps deep yellow."),
    ("page_4", "Mango sits hunched on a mossy rock trying to hide, while wise old turtle Gogo "
               "sits gently beside Mango, listening kindly, warm morning light. Back-ridge bumps yellow."),
    ("page_5", "Mango stands tall taking a slow deep breath, eyes closed, peaceful expression, "
               "while the small worry-cloud above shrinks and begins to fade away. Back-ridge bumps "
               "yellow softening toward green."),
    ("page_6", "Triumphant moment at the River Show: Mango stands on a log stage telling a story "
               "with open arms, animal audience delighted, heron teacher smiling proudly. Back-ridge "
               "bumps glow bright vivid green."),
    ("page_7", "Night scene. Mango lies peacefully on the riverbank under a starry sky whispering "
               "up at the stars, calm smile, fireflies around. Back-ridge bumps glow the softest steady green."),
]

# ----------------------------------------------------------------------
# GENERATE
# ----------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = genai.Client(api_key=API_KEY)

    if not os.path.exists(REFERENCE_IMAGE):
        sys.exit(f"Reference image not found: {REFERENCE_IMAGE}")
    ref = Image.open(REFERENCE_IMAGE)

    for name, scene in SCENES:
        prompt = STYLE + " SCENE: " + scene
        print(f"Generating {name} ...")
        try:
            resp = client.models.generate_content(
                model=MODEL,
                contents=[prompt, ref],   # text prompt + reference image = character consistency
            )
            saved = False
            for part in resp.candidates[0].content.parts:
                if getattr(part, "inline_data", None) is not None:
                    img = Image.open(BytesIO(part.inline_data.data))
                    out = os.path.join(OUTPUT_DIR, f"{name}.png")
                    img.save(out)
                    print(f"  saved -> {out}")
                    saved = True
            if not saved:
                print(f"  !! no image returned for {name} (check prompt / quota)")
        except Exception as e:
            print(f"  ERROR on {name}: {e}")

    print("\nDone. Images are in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
