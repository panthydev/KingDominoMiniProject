import cv2
import numpy as np


class utils:
    def CalcAverageRGB(Tile: Tile) -> tuple[int, int, int]:
        image = cv2.cvtColor(Tile.image, cv2.COLOR_BGR2RGB)

        averageRGB = np.mean(image, axis=(0, 1))
        return tuple((averageRGB).astype(int))