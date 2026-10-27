from Tile import Tile
from Biome import *
from src.TileGrid import TileGrid


class BiomeMatcher:

    Biomes = {}


    def __init__(self):
        BiomeMatcher.Biomes = {}
        for biomeType in BiomeType: # adds a biome obj to biome dict, for each biome type
            BiomeObj = Biome(biomeType)

            #worst most harcoded code known to man, disgusting
            avgRGB = (0, 0, 0)
            if(biomeType == BiomeType.WheatFields):
                avgRGB = (165, 141, 12)
            elif(biomeType == BiomeType.Woods):
                avgRGB = (42, 52, 24)
            elif(biomeType == BiomeType.Water):
                avgRGB = (23, 74, 131)
            elif(biomeType == BiomeType.Pasture):
                avgRGB = (89, 119, 25)
            elif(biomeType == BiomeType.Bog):
                avgRGB = (99, 86, 52)
            elif(biomeType == BiomeType.Mines):
                avgRGB = (62, 53, 29)
            elif(biomeType == BiomeType.NoType):
                avgRGB = (0, 0, 0)
            elif(biomeType == BiomeType.Table):
                avgRGB = (136, 106, 39)

            BiomeObj.set_AverageRGB(avgRGB)



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

        if biome_type is BiomeType.NoType:
            return False
        else:
            return True


    def matchAverageRGB(self, AverageRGB: tuple [int, int, int]) -> BiomeType:
        results = {}

        for biome in BiomeMatcher.Biomes.values():
            if biome.BiomeType == BiomeType.NoType: continue

            distance = 0

            for a, b in zip(AverageRGB, biome.AverageRGB):  distance += (a - b)**2

            distance = distance**0.5
            results[distance] = biome

        ShortestDistanceKey = min(results)

        return results[ShortestDistanceKey].BiomeType