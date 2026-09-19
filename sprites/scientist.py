import os
from PIL import Image

# Sinisigurado na mai-save sa labas ng 'sprites' folder (sa root directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "../scientist_sprite.png")

# 32x32 Pixel Art Canvas for Scientist
img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
pixels = img.load()

# Color Palette
SKIN = (235, 190, 155, 255)
HAIR_GRAY = (210, 215, 220, 255)
HAIR_DARK = (150, 155, 165, 255)
WHITE_COAT = (240, 242, 245, 255)
COAT_SHADOW = (180, 185, 195, 255)
SHIRT = (40, 120, 180, 255)
TIE = (190, 40, 50, 255)
PANTS = (50, 55, 65, 255)
GLASSES_FRAME = (30, 30, 35, 255)
GLASSES_LENS = (190, 235, 255, 255)
FLASK_GLASS = (220, 240, 255, 255)
FLASK_LIQUID = (60, 230, 90, 255)
BUBBLE = (180, 255, 190, 255)

# Wild Scientist Hair
hair_coords = [
    (11, 2), (12, 2), (13, 2), (17, 2), (18, 2), (19, 2),
    (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3),
    (9, 4), (10, 4), (20, 4), (21, 4),
    (8, 5), (9, 5), (21, 5), (22, 5),
    (8, 6), (9, 6), (21, 6), (22, 6),
    (8, 7), (9, 7), (21, 7), (22, 7),
    (9, 8), (21, 8)
]
for x, y in hair_coords:
    pixels[x, y] = HAIR_GRAY
pixels[10, 3] = HAIR_DARK
pixels[20, 3] = HAIR_DARK

# Head / Face Skin
for x in range(11, 20):
    for y in range(4, 12):
        pixels[x, y] = SKIN

# Glasses & Eyes
for x in range(11, 15):
    pixels[x, 6] = GLASSES_FRAME
    pixels[x, 8] = GLASSES_FRAME
pixels[11, 7] = GLASSES_FRAME
pixels[14, 7] = GLASSES_FRAME

for x in range(16, 20):
    pixels[x, 6] = GLASSES_FRAME
    pixels[x, 8] = GLASSES_FRAME
pixels[16, 7] = GLASSES_FRAME
pixels[19, 7] = GLASSES_FRAME

pixels[15, 7] = GLASSES_FRAME

pixels[12, 7] = GLASSES_LENS
pixels[13, 7] = GLASSES_LENS
pixels[17, 7] = GLASSES_LENS
pixels[18, 7] = GLASSES_LENS

# Mustache / Mouth
pixels[14, 10] = HAIR_GRAY
pixels[15, 10] = HAIR_GRAY
pixels[16, 10] = HAIR_GRAY

# Lab Coat Body
for x in range(9, 22):
    for y in range(12, 25):
        pixels[x, y] = WHITE_COAT

# Shirt & Tie
for y in range(12, 18):
    pixels[14, y] = SHIRT
    pixels[15, y] = TIE
    pixels[16, y] = SHIRT

# Shadows
for y in range(12, 25):
    pixels[9, y] = COAT_SHADOW
    pixels[21, y] = COAT_SHADOW

# Left Arm & Chemical Flask
pixels[7, 14] = WHITE_COAT
pixels[8, 14] = WHITE_COAT
pixels[7, 15] = WHITE_COAT
pixels[8, 15] = WHITE_COAT
pixels[7, 16] = SKIN
pixels[8, 16] = SKIN

pixels[6, 17] = FLASK_GLASS
pixels[7, 17] = FLASK_GLASS
pixels[6, 18] = FLASK_GLASS
pixels[7, 18] = FLASK_GLASS

for x in range(4, 9):
    for y in range(19, 22):
        pixels[x, y] = FLASK_LIQUID
pixels[4, 19] = FLASK_GLASS
pixels[8, 19] = FLASK_GLASS
pixels[4, 21] = FLASK_GLASS
pixels[8, 21] = FLASK_GLASS

pixels[6, 15] = BUBBLE
pixels[5, 13] = BUBBLE

# Right Arm
pixels[22, 14] = WHITE_COAT
pixels[23, 14] = WHITE_COAT
pixels[22, 15] = WHITE_COAT
pixels[23, 15] = WHITE_COAT
pixels[22, 16] = WHITE_COAT
pixels[23, 16] = SKIN

# Legs & Shoes
for x in range(11, 15):
    for y in range(25, 31):
        pixels[x, y] = PANTS
for x in range(16, 20):
    for y in range(25, 31):
        pixels[x, y] = PANTS

for x in range(10, 15):
    pixels[x, 31] = GLASSES_FRAME
for x in range(16, 21):
    pixels[x, 31] = GLASSES_FRAME

# Resize 8x using NEAREST
scaled_img = img.resize((256, 256), Image.NEAREST)
scaled_img.save(output_path)
print(f"Successfully generated upscaled {output_path}")