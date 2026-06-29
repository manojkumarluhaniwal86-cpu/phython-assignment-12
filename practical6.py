import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

rotated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)

cv2.imwrite("rotated.jpg", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
