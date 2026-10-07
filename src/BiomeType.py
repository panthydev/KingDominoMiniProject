import enum
class BiomeType(enum.Enum):
    WheatFields = 0
    Woods = 1
    Water = 2
    Pasture = 3
    Bog = 4
    Mines = 5

    def __str__(self):
        return self.name