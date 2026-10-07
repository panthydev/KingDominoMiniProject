import time
from pprint import pprint
from tkinter import Image
import os
import cv2
from cv2 import *
from pathlib import Path
import numpy as np

from src.Biome import BiomeType
from src.TileGrid import TileGrid
from src.Tile import Tile


def CalcAverageRGB(Tile: Tile) -> int:
    image = cv2.cvtColor(Tile.image, cv2.COLOR_BGR2RGB)

    averageRGB = np.mean(image, axis=(0,1))
    return int(np.sum(averageRGB))


def setBiome(tile: Tile, a: int):
    tile.SetBiomeType(BiomeType(a - 1))


def showTileInfo(tile: Tile):
   # cv2.imshow(str(tile), tile.image)

    print("""Choose BiomeType:
               WheatFields = 1
               Woods = 2
               water = 3
               pasture = 4
               bog = 5
               Mines = 6
               Skip = 0""")


folder_path = Path("../../TrainingImages")  #images in this folder are named 1.jpg, 2.jpg, 3.jpg ... n.jpg

Images = []
TileGrids = []
print(folder_path.absolute())
print(list(folder_path.glob("*.jpg")))
for file in folder_path.glob("*.jpg"):
    tile_grid = TileGrid()
    image = cv2.imread(str(file))

    cropped_image = image[10:-10, 10:-10]

    height, width = cropped_image.shape[:2]  # dont care about the channels, just get the h and w

    tile_height = height // 5
    tile_width = width // 5

    for y in range(5):
        for x in range(5):
            tile_image = cropped_image[
                y * tile_height:(y + 1) * tile_height,
                x * tile_width:(x + 1) * tile_width
            ]
            tile = Tile(x, y)
            tile.SetImage(tile_image)
            tile_grid.set_tile_by_Position(tile, x, y)

    TileGrids.append(tile_grid)

count = 0
for tile_grid in TileGrids:
    for tile in tile_grid:
        cv2.destroyAllWindows()
        count += 1
        print(f"Processing tile {count}/1850")
        showTileInfo(tile)
        #key = cv2.waitKey(0)
        key = ord('2')

        if key == ord('0'):
            print("\n skipping this one")
            continue

        if ord('1') <= key <= ord('6'):  #only if key is 1 -> 6
            setBiome(tile, key - ord('0'))
            tile.SetAverageRGB(CalcAverageRGB(tile))
            tile.PrintBiomeType()
            tile.PrintAverageRGB()
            #time.sleep(4)
            os.system("cls")

Biomes: dict[BiomeType, list[Tile]] = {}
BiomesAverageRGB: dict[BiomeType, int] = {}

for biomeType in BiomeType:
    Biomes[biomeType] = []


for tile_grid in TileGrids:
    for tile in tile_grid:
        Biomes[tile.BiomeType].append(tile)

for BiomeType in Biomes:
    if len(Biomes[BiomeType]) == 0:
        continue

    SumRGB = 0
    for tile in Biomes[BiomeType]:
        SumRGB += tile.AverageRGB


    BiomesAverageRGB[BiomeType] = SumRGB // len(Biomes[BiomeType])
    print(f"Biome RGB averages:"
          f"{BiomeType}: {BiomesAverageRGB[BiomeType]}")


