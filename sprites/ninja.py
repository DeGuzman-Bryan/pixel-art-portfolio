import os
from PIL import Image

# Sinisigurado na mai-save sa labas ng 'sprites' folder (sa root directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "../ninja_sprite.png")

# 32x32 Pixel Art Canvas for Ninja
img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
pixels = img.load()

# Color Palette
BLACK_GARB = (25, 25, 35, 255)
DARK_GRAY = (45, 45, 60, 255)
MID_GRAY = (80, 85, 105, 255)
RED_SASH = (200, 30, 40, 255)
SKIN = (220, 175, 135, 255)
EYE = (255, 255, 255, 255)
PUPIL = (10, 10, 15, 255)
STEEL = (190, 200, 210, 255)
STEEL_DARK = (110, 120, 135, 255)
GOLD = (230, 180, 50, 255)

# Head & Hood
for x in range(10, 22):
    for y in range(4, 13):
        pixels[x, y] = BLACK_GARB

# Hood Highlights
for x in range(11, 21):
    pixels[x, 4] = MID_GRAY

# Eye Slit & Face Contour
for x in range(11, 21):
    pixels[x, 9] = SKIN
    pixels[x, 10] = SKIN

# Eyes
pixels[13, 9] = EYE
pixels[14, 9] = PUPIL
pixels[18, 9] = EYE
pixels[19, 9] = PUPIL

# Headband / Red Accent
for x in range(10, 22):
    pixels[x, 7] = RED_SASH
pixels[8, 7] = RED_SASH
pixels[9, 7] = RED_SASH
pixels[7, 8] = RED_SASH
pixels[6, 9] = RED_SASH

# Torso / Gi
for x in range(10, 22):
    for y in range(13, 23):
        pixels[x, y] = BLACK_GARB

# Gi Overlap Details
for y in range(13, 19):
    pixels[15, y] = DARK_GRAY
    pixels[16, y] = DARK_GRAY

# Red Belt / Obi
for x in range(9, 23):
    pixels[x, 19] = RED_SASH
    pixels[x, 20] = RED_SASH

# Belt ties
pixels[13, 21] = RED_SASH
pixels[13, 22] = RED_SASH
pixels[14, 21] = RED_SASH

# Arms & Wraps
for y in range(14, 21):
    pixels[8, y] = DARK_GRAY
    pixels[9, y] = DARK_GRAY
    pixels[22, y] = DARK_GRAY
    pixels[23, y] = DARK_GRAY

# Wrist Wraps
pixels[8, 18] = RED_SASH
pixels[9, 18] = RED_SASH
pixels[22, 18] = RED_SASH
pixels[23, 18] = RED_SASH

# Legs & Shin Wraps
for x in range(10, 15):
    for y in range(23, 31):
        pixels[x, y] = BLACK_GARB
for x in range(17, 22):
    for y in range(23, 31):
        pixels[x, y] = BLACK_GARB

for x in range(10, 15):
    pixels[x, 27] = DARK_GRAY
    pixels[x, 29] = RED_SASH
for x in range(17, 22):
    pixels[x, 27] = DARK_GRAY
    pixels[x, 29] = RED_SASH

# Katana Sheath & Hilt
pixels[23, 6] = GOLD
pixels[24, 5] = STEEL
pixels[25, 4] = STEEL
pixels[26, 3] = STEEL
pixels[22, 7] = GOLD
pixels[23, 8] = GOLD
pixels[21, 9] = STEEL_DARK
pixels[20, 11] = STEEL_DARK
pixels[19, 13] = STEEL_DARK
pixels[18, 15] = STEEL_DARK

# Resize 8x using NEAREST to make canvas 256x256
scaled_img = img.resize((256, 256), Image.NEAREST)
scaled_img.save(output_path)
print(f"Successfully generated upscaled {output_path}")