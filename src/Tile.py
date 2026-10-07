from tkinter import Image
from src.Biome import BiomeType


class Tile:
    def __init__(self, x, y):
        self.x : int = x
        self.y : int = y
        self.image : Image = None
        self.AverageRGB = 0
        self.BiomeType : BiomeType = None
        self.CrownAmount : int = 0


    def SetBiomeType(self, BiomeType : BiomeType):
        self.BiomeType = BiomeType

    def AddCrownAmount(self, amount : int):
        if self.CrownAmount + amount > 3:
            return
        else:
            self.CrownAmount += amount

    def SetAverageRGB(self, RGB : tuple):
        self.AverageRGB = RGB

    def SetImage(self, image : Image):
        self.image = image

    def PrintPosition(self):
        print(self.x, self.y)

    def PrintBiomeType(self):
        print(str(self.BiomeType))

    def PrintCrownAmount(self):
        print(str(self.CrownAmount))

    def PrintAverageRGB(self):
        print(self.AverageRGB)

