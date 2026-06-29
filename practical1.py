import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Error: image.jpg not found!")
    exit()

cv2.imshow("Original Image", img)

cv2.imwrite("saved_image.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
