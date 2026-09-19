from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a sharp 256x256 pixel image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),         # Transparent
    'K': (20, 20, 30, 255),     # Dark Outline
    'w': (160, 100, 50, 255),   # Wood Highlight
    'W': (100, 60, 30, 255),    # Wood Shadow
    'R': (180, 40, 60, 255),    # Red Binding Ribbon
    'S': (240, 200, 80, 255),   # Straw Light
    's': (180, 140, 40, 255),   # Straw Shadow
}

# 16x16 Pixel Matrix (Diagonal Flying Witch Broom)
SPRITE_DATA = [
    ".KK.............",
    ".KwWK...........",
    "..KwWK..........",
    "...KwWK.........",
    "....KwWK........",
    ".....KwWK.......",
    "......KwWK......",
    ".......KwWK.....",
    "........KwWK....",
    ".........KRRK...",
    "..........KSSK..",
    ".........KSsSSK.",
    "........KSsSSsSK",
    ".......KSsSSsSK.",
    "......KSsSSsSK..",
    "......KKKKKK...."
]

def generate_broom():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            if symbol != '.':
                pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("broom_sprite.png")
    print("Witch broom sprite generated: broom_sprite.png")

if __name__ == "__main__":
    generate_broom()