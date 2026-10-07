import cv2
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join("..","TrainingImages", "1.jpg")
image = cv2.imread(image_path)


if image is None:
    sys.exit(f"Error: Can't read the {image_path}.")

'''
else:
    print("Image read.")
    cv2.imshow("Image Preview", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print("Current Working Directory: ", os.getcwd())
print("Current Image Path: ", os.path.abspath(os.path.join("TrainingImages", "1.jpg")))
'''

crop_pixels = 5
# -crop_pixels auto calcs (height -5) and (width -5)
cropped_image = image[crop_pixels:-crop_pixels, crop_pixels:-crop_pixels]

cv2.imshow("Original Preview", image)
cv2.imshow("Cropped Preview", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()