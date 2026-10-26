import os

import cv2
import numpy as np

from src.Tile import Tile

templateOriginal = cv2.imread('Templates/CrownFinal.png', 0) #temp not working
threshold = 0.15


def CheckTileForTemplate(Tile : Tile, template, Image = None ):
    height, width = template.shape
    tileImage = cv2.cvtColor(Tile.image, cv2.COLOR_BGR2GRAY) # dont know if bgr2 is what its on by default, check it with breakpoints

    if Image is None:
        tileImage2 = tileImage.copy()
    else:
        tileImage2 = Image.copy()
    result = cv2.matchTemplate(tileImage2, template, cv2.TM_CCORR_NORMED)
    os.system("cls")

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    has_crown = min_val <= threshold #is it within threshold =

    location = max_loc



    displayImage = tileImage2.copy()


    print("\n Crown found?: " + str(has_crown))

    if has_crown:
        Tile.CrownAmount += 1

        bottomRight = (location[0] + width, location[1] + height)
        cv2.rectangle(displayImage, location, bottomRight, 255, 4)

    cv2.imshow("Image", displayImage)
    cv2.imshow("Template", template)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if(has_crown):
        Tile.CrownAmount += 1
        # Remove the detected crown from the image
        x, y = max_loc
        tileImage2[y:y + height, x:x + width] = 0

        # Search the modified image for another crown
        CheckTileForTemplate(Tile, template, tileImage2)


def CheckAllTilesForTemplate(TileGrid, template : np.array):
    for collumn in TileGrid.grid:
        for tile in collumn:
            templateCopy = template.copy()
            for i in range(4):
                if i == 1:
                    templateCopy = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
                    CheckTileForTemplate(tile, templateCopy)
                elif i == 2:
                    templateCopy = cv2.rotate(template, cv2.ROTATE_180)
                    CheckTileForTemplate(tile, templateCopy)
                elif i == 3:
                    templateCopy = cv2.rotate(template, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    CheckTileForTemplate(tile, templateCopy)
                else:
                    CheckTileForTemplate(tile, templateCopy)






