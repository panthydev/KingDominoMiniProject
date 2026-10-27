from src.Biome import BiomeType
from src.Tile import Tile


class TileGrid:

    WIDTH = 5
    HEIGHT = 5
    def __init__(self):
        self.grid: list[list[Tile]] = [] # init the 2d list
        self.BiomesPresent: dict[BiomeType, bool] = {}

        for y in range(self.HEIGHT): # make all the rows
            row = []
            for x in range(self.WIDTH): #fill each row with a tile
                row.append(Tile(x, y)) #create the individual tile obj and add it to row
            self.grid.append(row) # put the row in the 2d list

    def __iter__(self):
        for row in self.grid:
            for tile in row:
                yield tile

    def set_tile_by_Position(self, tile: Tile, x: int, y: int):
        self.grid[x][y] = tile
    def get_tile_by_Position(self, pos : tuple[int, int]) -> Tile:
        x = pos[0]
        y = pos[1]
        return self.grid[x][y]

    def SetBiomesPresent(self, BiomesPresentDict):
        self.BiomesPresent = BiomesPresentDict