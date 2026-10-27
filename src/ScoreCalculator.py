import Tile
import numpy as np
import TileGrid
import Utils
import Biome
from src.Tile import Tile


def CalculateScoreForAllBoards(tileGrids : list[TileGrid.TileGrid]):
    for board in tileGrids:
        CalculateScoreForBoard(board)


def CalculateScoreForBoard(tileGrid : TileGrid.TileGrid):
    Regions = []
    for biome in tileGrid.BiomesPresent:
        CurrentRegions = CalculateRegionByBiome(biome)
        Regions.append(CurrentRegions)

# REMEMBER THERE CAN BE MULTIPLE OF THE SAME BIOME TYPE BUT BE DIFFERENT REGIONS
#This function should prolly return a list of regions
def CalculateRegionByBiome(tileGrid : TileGrid.TileGrid, biomeToCheck : Biome.BiomeType) -> list[tuple[Biome.BiomeType, int]]:
    Regions = [[]] # this one has tiles, WE DONT return this one
    currentRegion = []
    for collumn in tileGrid:
        for tile in collumn:
            if tile.BiomeType == biomeToCheck:
                currentRegion.append(tile)



def CheckNeighbourTilesForSameBiome(tileGrid : TileGrid.TileGrid,
                                    tilePos : tuple[int, int],
                                    CurrentRegion : list[Tile.Tile],
                                    biomeToCheck : Biome.BiomeType,
                                    savedNeighbours = None) -> list[Tile.Tile]:

    tile = tileGrid.get_tile_by_Position(tilePos)

    positions = CalculateNeighbourPositions(tile)

    CorrectTiles = savedNeighbours

    if tile.BiomeType == biomeToCheck:
        if tile not in CurrentRegion:
            CorrectTiles.append(tile)

    for pos in positions:
        temp_tile = tileGrid.get_tile_by_Position(pos)
        if temp_tile.BiomeType == biomeToCheck:
            if temp_tile not in CurrentRegion:
                CorrectTiles.append(temp_tile)


    if CorrectTiles is not []:
        for tile in CorrectTiles:
            if tile not in CurrentRegion:
                CurrentRegion.append(tile)


        for tile in CorrectTiles:
            if tile in CurrentRegion:
                CorrectTiles.remove(tile)
            CheckNeighbourTilesForSameBiome(tileGrid, tile.getPosition(), CurrentRegion, biomeToCheck, CorrectTiles)


    CorrectTiles = [] # reset correct tiles list #although this should already be the case, else we wouldnt be here lmao
    if len(CorrectTiles) == 0: return [] # FIX THIS LATER
    #When this returns, it signifies the end of a region / territory.





    #check and save all neighbour tiles that are the right biome
    #check if tile is already in region list
    #all tiles that are not already in the region list are added to the region list and to a temp list
    # check all neighbours of the temp list, and their neighbours until all tiles are in region list or not the same biome ()



def CalculateNeighbourPositions(tile : Tile.Tile) -> list[tuple[int, int]]:


    Position1 = (tile.x -1, tile.y)
    Position2 = (tile.x +1, tile.y)

    Position3 = (tile.x, tile.y -1)
    Position4 = (tile.x, tile.y +1)
    Positions = [Position1, Position2, Position3, Position4]

# tuple can be accessed with an index and not x y components because fuck you python
    for pos in Positions:
        if pos[0] < 0 or pos[1] < 0 or pos[0] > 4 or pos[1] > 4: # if the coords are out of bounds
            Positions.remove(pos) # not sure if im allowed to modify a list while iterating through it

    return Positions







