from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'L': (240, 215, 155, 255),  # Light Hemp Highlight
    'M': (190, 145, 80, 255),   # Medium Hemp Body
    'D': (125, 85, 40, 255),    # Dark Hemp Shadow
    'd': (65, 40, 18, 255),     # Deep Outline / Inner Hole Shadow
    'W': (210, 170, 110, 255)   # Binding Wrap Highlight
}

# 16x16 Coiled Rope Matrix
SPRITE_DATA = [
    "................",
    ".....LLLLL......",
    "...LLMMMMMLL....",
    "..LMMdddddMML...",
    ".LMMd.....dMML..",
    ".LMd..LLLL.dML..",
    ".LMd.LWWWWLdML..",
    ".LMd.LWWWWLdML..",
    ".LMd.DddddDdML..",
    ".LMd..DDDD.dML..",
    ".LMMd.....dMML..",
    "..LMMdddddMML...",
    "...DDMMMMMDD....",
    ".....DDDDD......",
    "................",
    "................"
]

def generate_rope_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("rope_sprite.png")
    print("Rope sprite generated: rope_sprite.png")

if __name__ == "__main__":
    generate_rope_sprite()