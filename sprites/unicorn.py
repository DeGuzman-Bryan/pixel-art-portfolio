# sprites/unicorn.py
from PIL import Image

# 16x16 Grid for a smaller, single sprite
GRID_W = 16
GRID_H = 16
SCALE = 16 # Exports a crisp 256x256 px image

# New Color Palette for the Unicorn (Pale Pink body, Blue/Magenta mane, Gold horn)
COLORS_UNICORN = {
    '.': (0, 0, 0, 0),        # Transparent
    'P': (255, 230, 240, 255), # Pale Pink (Body)
    'p': (220, 180, 200, 255), # Mid Pink (Body Shadow)
    'C': (0, 255, 255, 255),   # Cyan (Mane)
    'M': (255, 0, 255, 255),   # Magenta (Mane)
    'K': (0, 0, 0, 255),       # Black (Outline/Details)
    'G': (255, 215, 0, 255),   # Gold (Horn)
    'g': (200, 200, 200, 255), # Light Grey (Hooves)
    
    # >>> FIX: Defining 'E' for the Eye as a dark indigo/blue detail color.
    'E': (40, 60, 140, 255),   # Dark Indigo/Blue (Eye Detail)
}

# 16x16 Sprite Matrix for Unicorn (ASCII text matrix)
UNICORN_DATA = [
    "................",
    ".......GGG......",
    "......GPPPPG....",
    ".....KPPPPPPK...",
    "....KPPPPPKKKK..",
    "...KPPPPPK....K.",
    "...KPPPPPK..E.K.", # Line 35: ASCII 'E' is used here!
    "...KPpPPpPPPPK..",
    "...KPpPpPMMMK...",
    "....KpPPPMMMKK..",
    "....KpPPMMMCCCK.",
    "....KKPPCCCCCMK.",
    "....KPMMCCCCCMMK",
    "...KPPPPPPMMMCCC",
    "...KggggKggggK..",
    "....KKKKK.KKKK.."
]

def generate_unicorn_sprite():
    # ... logic remains the same ...
    img = Image.new("RGBA", (GRID_W, GRID_H), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(UNICORN_DATA):
        for x, symbol in enumerate(row):
            # Lookup the RGBA color based on the symbol
            pixels[x, y] = COLORS_UNICORN[symbol] # <--- Crashing line is fixed!

    # Scale the image and save it
    scaled_img = img.resize((GRID_W * SCALE, GRID_H * SCALE), Image.NEAREST)
    scaled_img.save("unicorn_sprite.png")
    print("Unicorn sprite generated: unicorn_sprite.png")

if __name__ == "__main__":
    generate_unicorn_sprite()