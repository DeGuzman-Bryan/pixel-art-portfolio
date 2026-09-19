from PIL import Image

GRID_SIZE = 16
SCALE = 16  # Exports a crisp 256x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    'R': (220, 60, 90, 255),   # Crimson Hair Ribbon
    'H': (210, 140, 80, 255),  # Light Chestnut Hair
    'h': (150, 85, 45, 255),   # Mid Chestnut Hair
    'd': (85, 45, 20, 255),    # Dark Hair Shadow
    'S': (255, 220, 190, 255), # Skin Light
    's': (225, 175, 140, 255), # Skin Shadow
    'E': (60, 140, 230, 255),  # Sparkly Blue Eyes
    'e': (20, 40, 80, 255),    # Lash / Eye Outline
    'C': (170, 75, 160, 255),  # Magenta/Purple Tunic
    'c': (110, 40, 105, 255),  # Tunic Shadow
    'W': (245, 245, 250, 255),  # White Trim / Collar / Socks
    'B': (90, 50, 30, 255)     # Leather Boots
}

# 16x16 Character Matrix (Khrixia)
SPRITE_DATA = [
    "................",
    "....RR..RR......",
    "...RHHHHHHR.....",
    "..HHHHHHHHHH....",
    "..HHSSSSSSHH....",
    "..HSEsEEsESH....",
    "..HSSSSSSSSH....",
    "..hHSSssSSHH....",
    "...hWWCCWWh.....",
    "...hCCCCCCh.....",
    "...hCCCCCCh.....",
    "...hWW..WWh.....",
    "...hSS..SSd.....",
    "....WW..WW......",
    "....BB..BB......",
    "................"
]

def generate_khrixia_sprite():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    scaled_img.save("khrixia_sprite.png")
    print("Khrixia sprite generated: khrixia_sprite.png")

if __name__ == "__main__":
    generate_khrixia_sprite()