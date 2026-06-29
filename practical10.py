import cv2

img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

edges = cv2.Canny(img, 100, 200)

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)

cv2.imwrite("edges.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
