import os
from PIL import Image

# Sinisigurado na mai-save sa labas ng 'sprites' folder (sa root directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "../barbarian_sprite.png")

# 32x32 Pixel Art Canvas
img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
pixels = img.load()

# Color Palette
SKIN = (210, 160, 120, 255)
SKIN_SHADOW = (170, 120, 80, 255)
HAIR_RED = (180, 60, 30, 255)
HAIR_DARK = (120, 40, 20, 255)
HELMET = (139, 155, 180, 255)
HELMET_DARK = (80, 95, 120, 255)
HORN = (230, 220, 190, 255)
HORN_DARK = (180, 170, 140, 255)
LEATHER = (100, 60, 40, 255)
LEATHER_DARK = (60, 35, 20, 255)
FUR = (200, 190, 170, 255)
METAL = (190, 200, 210, 255)
METAL_DARK = (100, 110, 120, 255)
GOLD = (230, 180, 50, 255)
EYE = (20, 20, 30, 255)
AXE_WOOD = (110, 70, 40, 255)

# Horns
for y in range(2, 8):
    pixels[8, y] = HORN
    pixels[23, y] = HORN
pixels[7, 3] = HORN
pixels[24, 3] = HORN
pixels[6, 2] = HORN_DARK
pixels[25, 2] = HORN_DARK

# Helmet
for x in range(10, 22):
    for y in range(5, 12):
        pixels[x, y] = HELMET
for x in range(11, 21):
    pixels[x, 5] = HELMET_DARK
pixels[15, 5] = GOLD
pixels[16, 5] = GOLD

# Face & Eyes
for x in range(10, 22):
    for y in range(12, 17):
        pixels[x, y] = SKIN
pixels[12, 14] = EYE
pixels[13, 14] = EYE
pixels[18, 14] = EYE
pixels[19, 14] = EYE

# Red Beard & Hair
for x in range(9, 23):
    for y in range(17, 23):
        pixels[x, y] = HAIR_RED
for x in range(11, 21):
    pixels[x, 23] = HAIR_RED
for x in range(13, 19):
    pixels[x, 24] = HAIR_DARK

# Fur Shoulders
for x in range(7, 25):
    pixels[x, 19] = FUR
    pixels[x, 20] = FUR

# Torso & Belt
for x in range(10, 22):
    for y in range(21, 26):
        pixels[x, y] = LEATHER
for x in range(9, 23):
    pixels[x, 25] = GOLD
    pixels[x, 26] = LEATHER_DARK

# Legs & Boots
for x in range(10, 15):
    for y in range(27, 32):
        pixels[x, y] = LEATHER_DARK
for x in range(17, 22):
    for y in range(27, 32):
        pixels[x, y] = LEATHER_DARK

# Great Axe
for y in range(6, 32):
    pixels[26, y] = AXE_WOOD
    pixels[27, y] = AXE_WOOD

for x in range(21, 26):
    for y in range(8, 18):
        pixels[x, y] = METAL
for x in range(28, 32):
    for y in range(8, 18):
        pixels[x, y] = METAL
pixels[20, 10] = METAL_DARK
pixels[20, 11] = METAL_DARK
pixels[20, 12] = METAL_DARK
pixels[20, 13] = METAL_DARK
pixels[20, 14] = METAL_DARK
pixels[20, 15] = METAL_DARK

# Resize to 256x256 using NEAREST neighbor para lumaki nang pantay ang pixels
scaled_img = img.resize((256, 256), Image.NEAREST)
scaled_img.save(output_path)
print(f"Successfully generated upscaled {output_path}")