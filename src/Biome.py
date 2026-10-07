import enum
class BiomeType(enum.Enum):
    WheatFields = 0
    Woods = 1
    Water = 2
    Pasture = 3
    Bog = 4
    Mines = 5
    NoType = 6

    def __str__(self):
        return self.name


class Biome:
    def __init__(self, BiomeType : BiomeType):
        self.BiomeType : BiomeType = None
        self.AverageRGB : int = 0

    def set_BiomeType(self, BiomeType):
        self.BiomeType = BiomeType

    def set_AverageRGB(self, AverageRGB : int):
        if AverageRGB < 0 or AverageRGB > 255:
            return False
        else:
            self.AverageRGB = AverageRGB
