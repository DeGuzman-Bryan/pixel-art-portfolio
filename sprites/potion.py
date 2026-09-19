from PIL import Image

# 16x16 Grid & Output Scaling
GRID_SIZE = 16
SCALE = 16  # Exports a sharp 256x256 pixel image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),         # Transparent
    'K': (20, 20, 30, 255),     # Dark Outline
    'C': (180, 120, 70, 255),   # Cork Top
    'c': (120, 75, 40, 255),    # Cork Shadow
    'G': (180, 210, 230, 255),  # Glass Highlight
    'g': (100, 130, 160, 255),  # Glass Shadow
    'R': (230, 40, 70, 255),    # Red Liquid (Bright)
    'r': (150, 20, 40, 255),    # Red Liquid (Shadow)
    'W': (255, 255, 255, 255)   # Glass Reflection
}

# 16x16 Pixel Matrix
SPRITE_DATA = [
    "................",
    "......cCCc......",
    "......cCCc......",
    ".....KKGGKK.....",
    ".....KGGGGK.....",
    "....KKgGGgKK....",
    "...KgGGGGGGgK...",
    "..KgWWWRRRRRgK..",
    "..KgWWWRRRRRgK..",
    "..KgRRRRRRRRgK..",
    "..KgrrrrrrrrgK..",
    "..KgrrrrrrrrgK..",
    "...KgrrrrrrgK...",
    "....KKgrrgKK....",
    "......KKKK......",
    "................"
]

def generate_potion():
    img = Image.new("RGBA", (GRID_SIZE, GRID_SIZE), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS.get(symbol, (0, 0, 0, 0))

    # Scale with nearest neighbor for clean pixel edges
    scaled_img = img.resize((GRID_SIZE * SCALE, GRID_SIZE * SCALE), Image.NEAREST)
    
    # Save to project root folder
    output_path = "potion_sprite.png"
    scaled_img.save(output_path)
    print(f"Potion sprite generated: {output_path}")

if __name__ == "__main__":
    generate_potion()