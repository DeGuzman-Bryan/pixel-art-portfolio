from PIL import Image

# 1. Define colors: (Red, Green, Blue, Alpha/Opacity)
PALETTE = {
    0: (0, 0, 0, 0),        # Transparent
    1: (20, 20, 20, 255),    # Black (Outline)
    2: (139, 69, 19, 255),   # Brown (Cork stopper)
    3: (100, 200, 255, 255), # Light Blue (Glass highlights)
    4: (255, 50, 80, 255),   # Bright Red (Liquid contents)
    5: (180, 20, 50, 255),   # Dark Red (Liquid shadow)
}

# 2. Design the sprite grid (16 rows x 16 columns)
grid = [
    [0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,3,3,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,3,3,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,3,3,1,1,0,0,0,0,0],
    [0,0,0,0,1,3,3,3,3,3,3,1,0,0,0,0],
    [0,0,0,1,3,3,3,3,3,3,3,3,1,0,0,0],
    [0,0,0,1,3,3,4,4,4,4,3,3,1,0,0,0],
    [0,0,1,3,3,4,4,4,4,4,4,3,3,1,0,0],
    [0,0,1,3,4,4,4,4,4,4,4,4,3,1,0,0],
    [0,0,1,1,4,4,4,4,4,4,5,5,1,1,0,0],
    [0,0,1,5,5,5,5,5,5,5,5,5,5,1,0,0],
    [0,0,1,5,5,5,5,5,5,5,5,5,5,1,0,0],
    [0,0,0,1,1,5,5,5,5,5,5,1,1,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
]

# 3. Create raw image file
height, width = len(grid), len(grid[0])
img = Image.new("RGBA", (width, height))

for y in range(height):
    for x in range(width):
        color_index = grid[y][x]
        img.putpixel((x, y), PALETTE[color_index])

# 4. Upscale for high resolution clarity and save
scale_multiplier = 16  # Makes a 256x256 clean PNG image
scaled_img = img.resize((width * scale_multiplier, height * scale_multiplier), Image.NEAREST)
scaled_img.save("potion_sprite.png")

print("Success! Generated potion_sprite.png in your folder.")