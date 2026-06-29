import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

resized = cv2.resize(img, (500, 500))

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.imwrite("resized_image.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
