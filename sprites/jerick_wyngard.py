from PIL import Image

GRID_W = 32
GRID_H = 16
SCALE = 16  # Exports a crisp 512x256 px image

# Color Palette (RGBA)
COLORS = {
    '.': (0, 0, 0, 0),          # Transparent
    # Jerick (Knight / Warrior)
    'S': (255, 215, 180, 255),  # Skin
    's': (210, 160, 130, 255),  # Skin Shadow
    'J': (45, 40, 55, 255),     # Jerick Hair (Dark Charcoal)
    'A': (70, 130, 200, 255),   # Jerick Blue Armor
    'a': (40, 80, 140, 255),    # Jerick Dark Blue Armor
    'M': (190, 200, 210, 255),  # Metallic Silver
    'm': (120, 130, 145, 255),  # Dark Silver
    # Wyngard (Ranger / Scout)
    'W': (240, 200, 90, 255),   # Wyngard Hair (Blond/Gold)
    'w': (180, 140, 40, 255),   # Wyngard Hair Shadow
    'C': (45, 130, 80, 255),    # Wyngard Forest Green Cloak
    'c': (25, 80, 45, 255),     # Wyngard Dark Green Cloak
    'B': (110, 70, 40, 255),    # Brown Leather
    'b': (65, 40, 20, 255),     # Dark Brown Leather
    'E': (20, 20, 30, 255)      # Eyes/Outlines
}

# 32x16 Dual Sprite Matrix
SPRITE_DATA = [
    "................................",
    "....JJJJ..........WWWW..........",
    "...JJJJJJ........WWWWWW.........",
    "...JJSSJJ........WWWSSWW........",
    "...JSEESJ........WSEESWW........",
    "...JSSSSJ........WSSSSWW........",
    "....JsSJ..........WsSWW.........",
    "...MMAMMM........CCBCCCC........",
    "..MAAAAMAM......CCCBCCCCc.......",
    "..MAAAAMAM......CCCBCCCCc.......",
    "..mAAaAMAm......cccBcccc........",
    "...mMAAMm........cCBBcc.........",
    "...SS..SS........BB..BB.........",
    "...mm..mm........bb..bb.........",
    "...mm..mm........bb..bb.........",
    "................................"
]

def generate_jerick_wyngard_sprite():
    img = Image.new("RGBA", (GRID_W, GRID_H), (0, 0, 0, 0))
    pixels = img.load()

    for y, row in enumerate(SPRITE_DATA):
        for x, symbol in enumerate(row):
            pixels[x, y] = COLORS[symbol]

    scaled_img = img.resize((GRID_W * SCALE, GRID_H * SCALE), Image.NEAREST)
    scaled_img.save("jerick_wyngard_sprite.png")
    print("Jerick & Wyngard sprite generated: jerick_wyngard_sprite.png")

if __name__ == "__main__":
    generate_jerick_wyngard_sprite()