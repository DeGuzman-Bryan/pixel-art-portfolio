from PIL import Image

GRID_WIDTH = 16
GRID_HEIGHT = 26
SCALE = 16  # Exports a crisp pixelated output (256x416 px)

# Color Palette matching the reference image
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'S': (190, 125, 80, 255),   # Skin (Tan)
    's': (150, 95, 58, 255),    # Skin Shadow (Neck/Ears)
    'W': (235, 235, 235, 255),  # White Hair / Eyebrows / Mustache
    'E': (20, 20, 20, 255),     # Eye (Dark)
    'Y': (230, 180, 65, 255),   # Shirt Yellow
    'y': (180, 130, 35, 255),   # Shirt Stripe (Darker Yellow)
    'P': (75, 48, 35, 255),     # Pants (Brown)
    'B': (45, 28, 20, 255)      # Shoes (Dark Brown)
}

# 16x26 Pixel Matrix matching the reference character layout
SPRITE_DATA = [
    "....SSSSSSSS....",
    "...SSSSSSSSSS...",
    "..WSSSSSSSSSSW..",
    ".WWSSSSSSSSSSWW.",
    ".WW.WW....WW.WW.",
    ".WW.SE....ES.WW.",
    "..S.SE....ES.S..",
    "..S..WWWWWW..S..",
    "...S.SSSSSS.S...",
    "....ssssssss....",
    "....ssssssss....",
    "..YYYYYYYYYYYY..",
    ".YYYYYYYYYYYYYY.",
    ".YYyYYYYYYYYyYY.",
    ".YYyYYYYYYYYyYY.",
    ".YYyYYYYYYYYyYY.",
    ".SSyYYYYYYYYySS.",
    ".SSyYYYYYYYYySS.",
    ".SSyYYYYYYYYySS.",
    "..PPPPPPPPPPPP..",
    "..PPP......PPP..",
    "..PPP......PPP..",
    "..PPP......PPP..",
    "..PPP......PPP..",
    "..BBB......BBB..",
    "..BBB......BBB.."
]

def generate_old_man_sprite():
    img = Image.new("RGBA", (GRID_WIDTH, GRID_HEIGHT), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_WIDTH * SCALE, GRID_HEIGHT * SCALE), Image.NEAREST)
    scaled_img.save("old_man_sprite.png")
    print("Old man reference sprite generated successfully: old_man_sprite.png")

if __name__ == "__main__":
    generate_old_man_sprite()