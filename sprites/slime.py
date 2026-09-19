from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a sharp 256x256 pixel image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),         # Transparent
    'K': (15, 35, 20, 255),     # Dark Outline
    'g': (160, 240, 140, 255),  # Slime Highlight
    'G': (70, 190, 90, 255),    # Slime Midtone
    'D': (30, 120, 60, 255),    # Slime Shadow
    'W': (240, 255, 240, 255),  # Eye White
    'E': (15, 35, 20, 255)      # Eye Pupil
}

# 16x16 Pixel Matrix (Acid Slime)
SPRITE_DATA = [
    "................",
    "................",
    "......KKKK......",
    "....KKggggKK....",
    "...KggWWggWWgK..",
    "..KggEEggEEgggK.",
    "..KgggggggggggK.",
    ".KggggGGGGGGgggK",
    ".KgggGGGGGGGGggK",
    "KggGGDDDDDDGGggK",
    "KgGGDDDDDDDDGGgK",
    "KGGDDDDDDDDDDGGK",
    ".KGGDDDDDDDDGGK.",
    "..KKKKKKKKKKKK..",
    "................",
    "................"
]

def generate_slime():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            if symbol != '.':
                pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("slime_sprite.png")
    print("Slime sprite generated: slime_sprite.png")

if __name__ == "__main__":
    generate_slime()