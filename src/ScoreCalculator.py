import Tile
import numpy as np
import TileGrid
import Utils
import Biome



def CalculateScoreForAllBoards(tileGrids : list[TileGrid.TileGrid]):
    for board in tileGrids:
        CalculateScoreForBoard(board)


def CalculateScoreForBoard(tileGrid : TileGrid.TileGrid):
    pass


def CalculateRegionByBiome(tileGrid : TileGrid.TileGrid, biomeToCheck : Biome.BiomeType):
    pass



