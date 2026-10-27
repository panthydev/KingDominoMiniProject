import Tile
import numpy as np
import TileGrid
import Utils
import Biome



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
                                    tile : Tile.Tile,
                                    CurrentRegion : list[Tile.Tile],
                                    biomeToCheck : Biome.BiomeType) -> list[Tile.Tile]:

    positions = CalculateNeighbourPositions(tile)

    CorrectTiles = []

    for pos in positions:
        temp_tile = tileGrid.get_tile_by_Position(pos)
        if temp_tile.BiomeType == biomeToCheck:
            if temp_tile not in CurrentRegion:
                CorrectTiles.append(temp_tile)


    if CorrectTiles is not []:
        CurrentRegion.extend(CorrectTiles)
        CheckNeighbourTilesForSameBiome(tileGrid, tile, CurrentRegion, biomeToCheck)


    CorrectTiles = [] # reset correct tiles list
    if len(CorrectTiles) == 0: return [] # FIX THIS LATER





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







