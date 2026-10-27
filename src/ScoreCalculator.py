import Tile
import numpy as np
import TileGrid
import Utils
import Biome



def CalculateScoreForAllBoards(tileGrids : list[TileGrid.TileGrid]):
    for board in tileGrids:
        CalculateScoreForBoard(board)


def CalculateScoreForBoard(tileGrid : TileGrid.TileGrid):
    for biome in tileGrid.BiomesPresent:
        CalculateRegionByBiome(biome)

# REMEMBER THERE CAN BE MULTIPLE OF THE SAME BIOME TYPE BUT BE DIFFERENT REGIONS
#This function should prolly return a list of regions
def CalculateRegionByBiome(tileGrid : TileGrid.TileGrid, biomeToCheck : Biome.BiomeType) -> list[tuple[Biome.BiomeType, int]]:
    pass



