from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'L': (240, 245, 255, 255),  # Blade Light Highlight
    'S': (170, 185, 205, 255),  # Silver Blade Body
    's': (100, 115, 140, 255),  # Steel Shadow Edge
    'G': (240, 195, 60, 255),   # Gold Crossguard/Pommel
    'g': (170, 125, 30, 255),   # Dark Gold Shadow
    'R': (220, 50, 50, 255),    # Ruby Gem
    'B': (100, 60, 35, 255)     # Leather Grip Wrap
}

# 16x16 Diagonal Sword Matrix
SPRITE_DATA = [
    "...............L",
    "..............LS",
    ".............LSs",
    "............LSs.",
    "...........LSs..",
    "..........LSs...",
    ".........LSs....",
    "........LSs.....",
    ".......LSs......",
    "......GGGG......",
    ".....GGGRGG.....",
    "....gGg..gGg....",
    "......BBB.......",
    ".....BBB........",
    "....GgG.........",
    "................"
]

def generate_sword_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("sword_sprite.png")
    print("Sword sprite generated: sword_sprite.png")

if __name__ == "__main__":
    generate_sword_sprite()