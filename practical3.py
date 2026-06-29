import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

horizontal = cv2.flip(img, 1)
vertical = cv2.flip(img, 0)
both = cv2.flip(img, -1)

cv2.imshow("Original", img)
cv2.imshow("Horizontal Flip", horizontal)
cv2.imshow("Vertical Flip", vertical)
cv2.imshow("Both Flip", both)

cv2.imwrite("horizontal.jpg", horizontal)
cv2.imwrite("vertical.jpg", vertical)
cv2.imwrite("both.jpg", both)

cv2.waitKey(0)
cv2.destroyAllWindows()
