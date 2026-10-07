import cv2
import os
import sys
from src.TileGrid import TileGrid

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.abspath(os.path.join(script_dir, "..", "TrainingImages", "1.jpg"))

image = cv2.imread(image_path)

if image is None:
    sys.exit(f"Error: Can't read the image at {image_path}.")

crop_pixels = 5
# Using -crop_pixels automatically calculates (height - 5) and (width - 5)
cropped_image = image[crop_pixels:-crop_pixels, crop_pixels:-crop_pixels]
print("Image read and cropped.")

# Tile grid object
the_tile_grid = TileGrid()

# Total dimensions of the image crop
img_height, img_width = cropped_image.shape[:2]

# Calc width & height of a tile using int division
tile_width = img_width // TileGrid.WIDTH
tile_height = img_height // TileGrid.HEIGHT

# Loop through the grid, slice the image, and update the tiles
for y in range(TileGrid.HEIGHT):
    for x in range(TileGrid.WIDTH):
        # Calcs start and end pixel of specific tiles
        start_y = y * tile_height
        end_y = start_y + tile_height
        start_x = x * tile_width
        end_x = start_x + tile_width

        # Slice numpy array to get square
        image_slice = cropped_image[start_y:end_y, start_x:end_x]

        # Fetch pre-created tile from grid, and attach image slice
        current_tile = the_tile_grid.grid[y][x]
        current_tile.image_slice = image_slice

print(f"Successfully populated TileGrid with {TileGrid.WIDTH * TileGrid.HEIGHT} image slices.")

cv2.imshow("Top Left Tile", the_tile_grid.grid[0][0].image_slice)
cv2.waitKey(0)
cv2.destroyAllWindows()