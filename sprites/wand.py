from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'S': (255, 255, 255, 255),  # Pure White Sparkle
    'C': (140, 230, 255, 255),  # Cyan Magic Core
    'B': (70, 130, 240, 255),   # Blue Magic Outer Glow
    'G': (240, 195, 60, 255),   # Gold Ring / Trim
    'g': (170, 125, 30, 255),   # Dark Gold
    'w': (160, 95, 50, 255),    # Light Wood Highlight
    'W': (110, 55, 25, 255),    # Wood Shaft
    'd': (65, 30, 10, 255)      # Dark Wood Shadow
}

# 16x16 Diagonal Magic Wand Matrix
SPRITE_DATA = [
    "..............S.",
    "............SBCS",
    "...........SBCCB",
    "..........SCCCCS",
    "...........SBCCB",
    "............SBCS",
    ".........GG..S..",
    "........gGg.....",
    ".......wWd......",
    "......wWd.......",
    ".....wWd........",
    "....wWd.........",
    "...wWd..........",
    "..gGg...........",
    ".GG.............",
    "................"
]

def generate_wand_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("wand_sprite.png")
    print("Magic Wand sprite generated: wand_sprite.png")

if __name__ == "__main__":
    generate_wand_sprite()