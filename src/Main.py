import time
from pprint import pprint
from tkinter import Image
import os
import cv2
from cv2 import *
from pathlib import Path
import numpy as np
import TemplateMatcher
from src import Utils
from src.Biome import BiomeType
from src.BiomeMatcher import BiomeMatcher
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
def CalcAverageRGBForAllBoards(TileGrids):
    for tile_grid in TileGrids:
        Utils.CalcAverageRGBForBoard(tile_grid)
def CalculateBiomeForAllBoards(TileGrids):
    biomeMatcher = BiomeMatcher()
    for tile_grid in TileGrids:
        biomeMatcher.MatchAllTiles(tile_grid)

def DoTemplateMatching(TileGrids):
    for tile_grid in TileGrids:
        TemplateMatcher.CheckAllTilesForTemplate(tile_grid, TemplateMatcher.maskOriginal)

def DoBiomesPresentCheck(TileGrids):
    for tile_grid in TileGrids:
        BiomesPresent = {}
        for row in tile_grid.grid:
            for tile in row:
                BiomesPresent[tile.GetBiomeType()] = True
        tile_grid.SetBiomesPresent(BiomesPresent)







folder_path = Path("../IMAGES")  #images in this folder are named 1.jpg, 2.jpg, 3.jpg ... n.jpg
#currently this path leads to all the images, we should probably only do one at a time.

CreateTileGrids(folder_path)
CalcAverageRGBForAllBoards(TileGrids)
CalculateBiomeForAllBoards(TileGrids)
#DoTemplateMatching(TileGrids)
DoBiomesPresentCheck(TileGrids)









#rows are actually collumns, here, should probably rename this everywhere
for tile_grid in TileGrids:
    for row in tile_grid.grid:
        for tile in row:
            cv2.imshow("LMAO", tile.GetImage())
            tile.PrintBiomeType()
            cv2.waitKey(0)


#figure out the biomes on each board / TileGrid




