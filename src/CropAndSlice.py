import cv2
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.abspath(os.path.join(script_dir, "..", "TrainingImages", "1.jpg"))

image = cv2.imread(image_path)

if image is None:
    sys.exit(f"Error: Can't read the image at {image_path}.")

# Define how many pixels to crop from the edges
crop_pixels = 5

# Crop the image: image[y_start:y_end, x_start:x_end]
# Using -crop_pixels automatically calculates (height - 5) and (width - 5)
cropped_image = image[crop_pixels:-crop_pixels, crop_pixels:-crop_pixels]

print("Image read and cropped.")

# Display both to see the difference
cv2.imshow("Original Preview", image)
cv2.imshow("Cropped Preview", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()