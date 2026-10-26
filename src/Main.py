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




Images = []
TileGrids = []

def CreateTileGrids(path):
    for file in path.glob("*.jpg"):
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

folder_path = Path("../TrainingImages")  #images in this folder are named 1.jpg, 2.jpg, 3.jpg ... n.jpg



print(list(folder_path.glob("*.jpg")))
CreateTileGrids(folder_path)
print(TileGrids)
