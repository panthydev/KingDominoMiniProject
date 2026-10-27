from tkinter import Image
import cv2
import numpy as np

from src.Biome import BiomeType


class Tile:
    def __init__(self, x, y):
        self.x : int = x
        self.y : int = y
        self.image : np.ndarray | None = None
        self.AverageRGB : tuple = (0, 0, 0)
        self.BiomeType = BiomeType.NoType
        self.CrownAmount : int = 0

    def GetBiomeSpecificCrown(self):
        image = None
        if self.BiomeType.value == BiomeType.Pasture.value:
            image = cv2.imread('Templates/PastureCrown.png', cv2.IMREAD_UNCHANGED)
        elif self.BiomeType.value == BiomeType.Water.value:
            image = cv2.imread('Templates/WaterCrown.png', cv2.IMREAD_UNCHANGED)
        elif self.BiomeType.value == BiomeType.WheatFields.value:
            image = cv2.imread('Templates/WheatCrown.png', cv2.IMREAD_UNCHANGED)
        elif self.BiomeType.value == BiomeType.Mines.value:
            image = cv2.imread('Templates/MineCrown.png', cv2.IMREAD_UNCHANGED)
        elif self.BiomeType.value == BiomeType.Woods.value:
            image = cv2.imread('Templates/ForestCrown.png', cv2.IMREAD_UNCHANGED)
        elif self.BiomeType.value == BiomeType.Bog.value:
            image = cv2.imread('Templates/BogCrown.png', cv2.IMREAD_UNCHANGED)
        return image

    def SetBiomeType(self, BiomeType : BiomeType):
        self.BiomeType = BiomeType

    def AddCrownAmount(self, amount : int):
        if self.CrownAmount + amount > 3:
            return
        else:
            self.CrownAmount += amount

    def SetAverageRGB(self, RGB : tuple[int,int,int]):
        self.AverageRGB = RGB

    def SetImage(self, image : np.ndarray):
        self.image = image

    def PrintPosition(self):
        print(self.x, self.y)

    def PrintBiomeType(self):
        print(str(self.BiomeType))

    def PrintCrownAmount(self):
        print(str(self.CrownAmount))

    def PrintAverageRGB(self):
        print(self.AverageRGB)

    def GetImage(self):
        return self.image

    def GetBiomeType(self):
        return self.BiomeType