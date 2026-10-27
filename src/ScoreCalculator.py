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
        CurrentRegions = CalculateRegionByBiome(tileGrid, biome)
        Regions.append(CurrentRegions)
    DoScoreCalculation(Regions)

# REMEMBER THERE CAN BE MULTIPLE OF THE SAME BIOME TYPE BUT BE DIFFERENT REGIONS
#This function should prolly return a list of regions
def CalculateRegionByBiome(
    tileGrid: TileGrid.TileGrid,
    biomeToCheck: Biome.BiomeType
) -> list[list[Tile.Tile]]:

    Regions = []
    Visited = set()

    for column in tileGrid.grid:
        for tile in column:
            pos = tile.getPosition()

            if pos in Visited or tile.BiomeType != biomeToCheck:
                continue

            CurrentRegion = []
            ToVisit = [tile]

            while ToVisit:
                current = ToVisit.pop()
                currentPos = current.getPosition()

                if currentPos in Visited:
                    continue

                Visited.add(currentPos)
                CurrentRegion.append(current)

                for neighbourPos in CalculateNeighbourPositions(current):
                    neighbour = tileGrid.get_tile_by_Position(neighbourPos)

                    if (neighbourPos not in Visited and neighbour.BiomeType == biomeToCheck):
                        ToVisit.append(neighbour)

            Regions.append(CurrentRegion)

    return Regions

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


def DoScoreCalculation(allRegions : list[[[]]]) -> list[[Tile]]:
    finalScore = 0
    for biomeRegions in allRegions:
        for region in biomeRegions:
            totalCrowns = 0
            for tile in region:
                if tile.GetCrownAmount() <= 0:
                    continue
                else:
                    totalCrowns += tile.GetCrownAmount()
            if totalCrowns > 0:
                finalScore += totalCrowns * len(region)
    print("Final Score: " + str(finalScore))









