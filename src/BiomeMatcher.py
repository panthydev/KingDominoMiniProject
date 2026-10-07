from Tile import Tile
from Biome import *
from src.TileGrid import TileGrid


class BiomeMatcher:

    Biomes = {}
    Tolerance = 10 # tolerance used when matching Avg rgb values to avg rgb values of predefined biomes

    def __init__(self):
        BiomeMatcher.Biomes = {}
        for biomeType in BiomeType: # adds a biome obj to biome dict, for each biome type
            BiomeObj = Biome(biomeType)
            BiomeObj.set_AverageRGB(100) # testing value
            BiomeMatcher.Biomes[biomeType] = BiomeObj


    def MatchAllTiles(self, tile_grid: TileGrid):
        SuccesCount = 0
        for row in tile_grid.grid:
            for tile in row:
                B_Result = BiomeMatcher.MatchTile(self, tile)

                if B_Result: SuccesCount += 1

        print("Tiles matched to a biomeType: " + str(SuccesCount))





    def MatchTile(self, tile: Tile) -> bool: # modifies the tile, returns bool to see success or fail
        biome_type = BiomeMatcher.matchAverageRGB(self, tile.AverageRGB)
        tile.SetBiomeType(biome_type)

        if biome_type is biome_type.NoType:
            return False
        else:
            return True


    def matchAverageRGB(self, AverageRGB: int) -> BiomeType:
        for biome in BiomeMatcher.Biomes:
            if biome.BiomeType == BiomeType.NoType: return biome.NoType

            if biome.AverageRGB - BiomeMatcher.Tolerance <= AverageRGB <= biome.AverageRGB + BiomeMatcher.Tolerance:
                return biome.BiomeType
        return BiomeType.NoType