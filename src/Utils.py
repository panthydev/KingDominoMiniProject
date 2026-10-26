import cv2
import numpy as np

from src.ImageInfoTool.Main import CalcAverageRGB
from src.Tile import Tile




def CalcAverageRGBForBoard(TileGrid):
    for row in TileGrid.grid:
        for tile in row:
            AverageRGB = CalcAverageRGB(tile)
            tile.SetAverageRGB(AverageRGB)


def CalcAverageRGB(Tile: Tile) -> tuple[int, int, int]:
    image = cv2.cvtColor(Tile.image, cv2.COLOR_BGR2RGB)

    averageRGB = np.mean(image, axis=(0, 1))
    return tuple((averageRGB).astype(int))

