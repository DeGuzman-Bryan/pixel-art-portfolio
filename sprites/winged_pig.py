from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'P': (255, 182, 193, 255),  # Light Pink Body
    'p': (230, 135, 155, 255),  # Mid Pink Shadow
    'd': (170, 75, 95, 255),    # Dark Pink Outline / Shade
    'S': (255, 200, 212, 255),  # Snout Pink
    'N': (150, 55, 80, 255),    # Nostril / Dark Snout
    'E': (35, 25, 35, 255),     # Eye
    'W': (250, 250, 255, 255),  # White Feather
    'w': (185, 200, 220, 255),  # Wing Shadow
    'H': (120, 60, 80, 255)     # Hoof
}

# 16x16 Winged Pig (Flying Pig) Matrix
SPRITE_DATA = [
    "................",
    "....WW....WW....",
    "...WwwW..WwwW...",
    "..WwwwwWWwwwwW..",
    "..WwwPPPPPPwwW..",
    "...WPPPEPPPPW...",
    "....PPPPPPSS....",
    "....PPPPPPNN....",
    "....pPPPPPPP....",
    ".....ppppppd....",
    ".....dHHdHHd....",
    ".....HH..HH.....",
    "................",
    "................",
    "................",
    "................"
]

def generate_winged_pig_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("winged_pig_sprite.png")
    print("Winged Pig sprite generated: winged_pig_sprite.png")

if __name__ == "__main__":
    generate_winged_pig_sprite()