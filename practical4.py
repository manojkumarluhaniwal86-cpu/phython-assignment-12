import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

# Draw Line
cv2.line(img, (50, 50), (300, 50), (255, 0, 0), 3)

# Draw Rectangle
cv2.rectangle(img, (50, 100), (250, 250), (0, 255, 0), 3)

# Draw Circle
cv2.circle(img, (400, 180), 60, (0, 0, 255), 3)

# Draw Polygon
pts = np.array([[350,300],[450,350],[400,450],[300,400]], np.int32)
cv2.polylines(img, [pts], True, (255,255,0), 3)

# Add Text
cv2.putText(
    img,
    "OpenCV Practical",
    (30, 500),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255,255,255),
    2
)

cv2.imshow("Drawing Shapes", img)

cv2.imwrite("drawing.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
