import cv2
import os

# config
IMAGES_ROOT = "./images"
IMAGE_NAME = "3.jpg"

# reading image
img_path = os.path.join(IMAGES_ROOT, IMAGE_NAME)
img = cv2.imread(img_path)

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)

# Cartoonization
color= cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)

cv2.waitKey()
cv2.destroyAllWindows()