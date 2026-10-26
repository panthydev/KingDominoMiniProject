import os

import cv2
import numpy as np

from src.Tile import Tile

template = cv2.imread('Templates/CrownFinal.png', 0) #temp not working

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
def CheckTileForTemplate(Tile : Tile):
    height, width = template.shape
    tileImage = cv2.cvtColor(Tile.image, cv2.COLOR_BGR2GRAY) # dont know if bgr2 is what its on by default, check it with breakpoints

    index = 0
    for method in methods:

        tileImage2 = tileImage.copy()
        result = cv2.matchTemplate(tileImage2, template, method)
        os.system("cls")


        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #print(min_val, max_val, min_loc, max_loc)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        bottomRight = (location[0] + width, location[1] + height)
        cv2.rectangle(tileImage2, location, bottomRight, 255, 4)
        cv2.imshow("Image", tileImage2)
        print("Method: " + str(index))
        print("\n" + str(min_val))
        print("\n" + str(max_val))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        index = index + 1

def CheckAllTilesForTemplate(TileGrid):
    for collumn in TileGrid.grid:
        for tile in collumn:
            CheckTileForTemplate(tile)




