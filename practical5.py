import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

rows, cols = img.shape[:2]

# Shift Image (Right = 100 px, Down = 50 px)
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

translated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Translated", translated)

cv2.imwrite("translated.jpg", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
