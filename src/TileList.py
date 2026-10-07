from src.Tile import Tile


class TileList:

    WIDTH = 5
    HEIGHT = 5
    def __init__(self):
        self.tiles: list[list[Tile]] = [] # init the 2d list

        for y in range(self.HEIGHT): # make all the rows
            row = []
            for x in range(self.WIDTH): #fill each row with a tile
                row.append(Tile(x, y)) #create the individual tile obj and add it to row
            self.tiles.append(row) # put the row in the 2d list

    def set_tile_by_Position(self, tile: Tile, x: int, y: int):
        self.tiles[x][y] = tile

