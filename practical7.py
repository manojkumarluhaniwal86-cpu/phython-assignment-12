import cv2

img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Binary Threshold", thresh)

cv2.imwrite("threshold.jpg", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
