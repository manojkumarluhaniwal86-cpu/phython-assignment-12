import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

kernel = np.ones((9,9), np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)

cv2.imwrite("tophat.jpg", tophat)
cv2.imwrite("blackhat.jpg", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
