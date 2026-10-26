import os

import cv2
import numpy as np

from src.Tile import Tile

templateSource = cv2.imread('Templates/Crown3Final.png', cv2.IMREAD_UNCHANGED) #temp not working
print(templateSource.shape)
print("Template dimensions:", templateSource.shape)
threshold = 0.95
#0.91 without mask
template = templateSource[:, :, :3]
maskOriginal = templateSource[:, :, 3]

def CheckTileForTemplate(Tile : Tile, template, mask,  Image = None ):
    height, width = template.shape[:2]

    tileImage = Tile.image.copy()
    #tileImage = cv2.cvtColor(Tile.image, cv2.COLOR_BGR2GRAY) # dont know if bgr2 is what its on by default, check it with breakpoints


    if Image is None:
        tileImage2 = tileImage.copy()
    else:
        tileImage2 = Image.copy()
    result = cv2.matchTemplate(tileImage2, template, cv2.TM_CCOEFF_NORMED, mask=mask)
    os.system("cls")

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if not np.isfinite(max_val): return # we dont like infinity here


    has_crown = max_val >= threshold #is it within threshold =

    location = max_loc



    displayImage = tileImage2.copy()

    print(f"Best score: {max_val:.4f}, Crown found: {has_crown}")
    print("\n Crown found?: " + str(has_crown))

    if has_crown:


        bottomRight = (location[0] + width, location[1] + height)
        cv2.rectangle(displayImage, location, bottomRight, 255, 4)

    cv2.imshow("Image", displayImage)
    cv2.imshow("Template", template)
    cv2.imshow("Mask", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if(has_crown):

        Tile.CrownAmount += 1
        # Remove the detected crown from the image
        x, y = max_loc
        tileImage2[y:y + height, x:x + width] = 0

        # Search the modified image for another crown
        CheckTileForTemplate(Tile, template, mask, tileImage2)


def CheckAllTilesForTemplate(TileGrid, template : np.array, mask):
    for collumn in TileGrid.grid:
        for tile in collumn:
            templateCopy = template.copy()
            maskCopy = mask.copy()
            for i in range(4):
                if i == 1:
                    templateCopy = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
                    maskCopy = cv2.rotate(mask, cv2.ROTATE_90_CLOCKWISE)

                    CheckTileForTemplate(tile, templateCopy, maskCopy)
                elif i == 2:
                    templateCopy = cv2.rotate(template, cv2.ROTATE_180)
                    maskCopy = cv2.rotate(mask, cv2.ROTATE_180)

                    CheckTileForTemplate(tile, templateCopy, maskCopy)
                elif i == 3:
                    templateCopy = cv2.rotate(template, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    maskCopy = cv2.rotate(mask, cv2.ROTATE_90_COUNTERCLOCKWISE)

                    CheckTileForTemplate(tile, templateCopy, maskCopy)
                else:
                    CheckTileForTemplate(tile, templateCopy, maskCopy)






