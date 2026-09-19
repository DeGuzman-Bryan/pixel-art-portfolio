from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'Z': (110, 170, 95, 255),  # Light Zombie Green (Head/Skin)
    'z': (65, 115, 55, 255),   # Mid Zombie Green
    'd': (35, 70, 30, 255),    # Dark Skin Shadow
    'R': (230, 40, 40, 255),   # Glowing Red Eye
    'W': (230, 230, 210, 255), # Exposed Bone / Teeth
    'C': (85, 95, 120, 255),   # Tattered Clothes / Shirt
    'c': (50, 58, 80, 255),    # Dark Shirt Shadow
    'P': (90, 70, 55, 255),    # Torn Trousers
    'p': (50, 38, 28, 255)     # Pants Shadow
}

# 16x16 Reanimated Zombie Matrix
SPRITE_DATA = [
    "................",
    ".....ZZZZ.......",
    "....ZZRZZZ......",
    "....ZzZZWZ......",
    "....zzdWWW......",
    ".....zzdd.......",
    "....CCCCCCC.....",
    "..ZZCCCCCCZZ....",
    ".ZZ.CCCCCC.ZZ...",
    ".zz.CCCCCC.zz...",
    "....CCCCCC......",
    "....PPPPPP......",
    "....PPPPPP......",
    "....PP..PP......",
    "....p....p......",
    "................"
]

def generate_zombie_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("zombie_sprite.png")
    print("Zombie sprite generated: zombie_sprite.png")

if __name__ == "__main__":
    generate_zombie_sprite()