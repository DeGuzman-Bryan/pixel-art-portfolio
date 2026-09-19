from PIL import Image, ImageDraw

# Grid dimensions and scale
grid_w, grid_h = 32, 32
scale = 16

# Create transparent canvas
image = Image.new("RGBA", (grid_w * scale, grid_h * scale), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Color Palette for Direwolf
_ = None                    # Transparent
K = (15, 18, 28, 255)       # Dark Outline
D = (45, 52, 70, 255)       # Dark Shadow Fur
M = (85, 95, 118, 255)      # Midtone Blue-Grey Fur
L = (145, 160, 185, 255)    # Light Fur Highlight
W = (225, 235, 245, 255)    # White Muzzle / Fur
E = (255, 70, 50, 255)      # Glowing Red Eye
G = (255, 180, 30, 255)     # Inner Eye Gold
N = (10, 10, 15, 255)       # Black Nose
T = (230, 230, 240, 255)    # Sharp Fangs / Teeth

# 32x32 Pixel Map Matrix
pixel_map = [
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,K,K,_,_,_,_,_,_,_,_,_,_,_,_,_,K,K,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,K,D,M,K,_,_,_,_,_,_,_,_,_,_,_,K,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,K,_,_,_,_,_,_,_,_,_,_,K,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,K,_,_,_,_,_,_,_,_,_,_,K,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,M,K,K,K,K,K,K,K,K,K,K,M,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,K,D,M,L,L,M,M,M,M,M,M,M,M,L,L,M,D,K,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,K,K,D,M,L,L,M,M,M,M,M,M,L,L,M,D,K,K,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,D,M,L,W,W,L,M,M,M,M,L,W,W,L,M,D,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,W,E,G,W,L,M,M,L,W,G,E,W,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,W,E,G,W,L,M,M,L,W,G,E,W,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,K,D,M,L,W,W,L,M,M,M,M,L,W,W,L,M,D,K,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,K,D,M,L,L,M,W,N,N,W,M,L,L,M,D,K,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,K,K,D,M,M,W,N,N,N,N,W,M,M,D,K,K,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,K,D,D,W,W,W,W,W,W,W,W,D,D,K,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,K,K,D,W,T,W,W,W,W,T,W,D,K,K,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,K,D,M,K,K,K,K,K,K,K,K,K,K,M,D,K,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,K,D,M,L,M,D,K,W,W,W,W,K,D,M,L,M,D,K,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,W,L,M,D,K,K,K,K,D,M,L,W,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,M,L,W,W,L,M,M,M,M,M,M,L,W,W,L,M,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,K,D,M,L,W,W,W,W,L,M,M,M,M,L,W,W,W,W,L,M,D,K,_,_,_,_,_,_,_,_],
    [_,_,K,D,M,L,W,W,W,W,W,L,M,M,L,W,W,W,W,W,L,M,D,K,_,_,_,_,_,_,_,_],
    [_,_,K,D,D,M,L,W,W,W,W,W,W,W,W,W,W,W,W,L,M,D,D,K,_,_,_,_,_,_,_,_],
    [_,_,_,K,D,D,M,L,W,W,W,W,W,W,W,W,W,W,L,M,D,D,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,K,K,D,D,M,L,L,W,W,W,W,W,W,L,L,M,D,D,K,K,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,K,K,D,D,M,M,L,L,W,W,L,L,M,M,D,D,K,K,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,K,K,D,D,D,M,M,M,M,M,M,D,D,D,K,K,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,K,K,K,D,D,D,D,D,D,D,D,K,K,K,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,K,K,K,K,K,K,K,K,K,K,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_]
]

# Render pixel grid
for y in range(grid_h):
    for x in range(grid_w):
        color = pixel_map[y][x]
        if color is not None:
            draw.rectangle(
                [x * scale, y * scale, (x + 1) * scale - 1, (y + 1) * scale - 1],
                fill=color
            )

# Save image outside the sprites folder (root directory)
output_path = "wolf_sprite.png"
image.save(output_path)
print(f"Wolf sprite generated: {output_path}")