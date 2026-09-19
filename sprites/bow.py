from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'S': (230, 230, 240, 255),  # Silver Bowstring
    'W': (180, 115, 60, 255),  # Light Wood Highlight
    'w': (120, 70, 30, 255),   # Medium Wood Body
    'D': (70, 40, 15, 255),    # Dark Wood Shadow
    'G': (240, 195, 60, 255),  # Gold Limb Tips
    'g': (170, 125, 30, 255),  # Dark Gold
    'R': (180, 50, 40, 255)    # Leather Grip Wrap
}

# 16x16 Longbow Matrix
SPRITE_DATA = [
    "................",
    "................",
    "..SSGG..........",
    "..SgWwD.........",
    "..S.WwD.........",
    "..S..WwD........",
    "..S...WwD.......",
    "..S....RRR......",
    "..S....RRR......",
    "..S...WwD.......",
    "..S..WwD........",
    "..S.WwD.........",
    "..SgWwD.........",
    "..SSGG..........",
    "................",
    "................"
]

def generate_bow_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("bow_sprite.png")
    print("Bow sprite generated: bow_sprite.png")

if __name__ == "__main__":
    generate_bow_sprite()