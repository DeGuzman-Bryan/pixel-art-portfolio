from PIL import Image

GRID_WIDTH = 16
GRID_HEIGHT = 20
SCALE = 16  # Exports a sharp 256x320 px PNG image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'G': (85, 155, 60, 255),    # Goblin Green Skin
    'g': (55, 105, 40, 255),    # Dark Green Shadow
    'L': (130, 195, 90, 255),   # Light Green Highlight
    'R': (210, 45, 45, 255),    # Red Eye
    'Y': (240, 220, 90, 255),   # Yellow Eye Pupil
    'W': (240, 240, 220, 255),  # Fangs/Teeth
    'B': (110, 70, 45, 255),    # Brown Leather Garb
    'b': (70, 40, 25, 255),     # Dark Leather / Boots
    'M': (170, 175, 180, 255)   # Iron Dagger Blade
}

# 16x20 Pixel Matrix
SPRITE_DATA = [
    "................",
    "....LLGGGGLL....",
    "...LGGGGGGGGLL..",
    ".LLGGGGGGGGGGLL.",
    "gLGGGGGGGGGGGGg.",
    "gLGGgGGGGGGgGGg.",
    ".gGG.RY..YR.GGg.",
    "..GG.RY..YR.GG..",
    "..GGGgWWWWgGGG..",
    "...GGGWWWWGGG...",
    "....ggGggGgg....",
    "...BBBBBBBBBB...",
    "..BBBBbBBbBBBB..",
    ".M.BBBBbbBBBB...",
    ".MBBBBbbbbBBBB..",
    ".M.ggBBBBBBgg...",
    "...gGG....GGg...",
    "...gGG....GGg...",
    "...bBb....bBb...",
    "................"
]

def generate_goblin_sprite():
    img = Image.new("RGBA", (GRID_WIDTH, GRID_HEIGHT), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_WIDTH * SCALE, GRID_HEIGHT * SCALE), Image.NEAREST)
    scaled_img.save("goblin_sprite.png")
    print("Goblin sprite successfully generated: goblin_sprite.png")

if __name__ == "__main__":
    generate_goblin_sprite()