import numpy as np
import cv2 as cv

img = np.zeros([512, 512, 3], np.uint8)  # criacao imagem preta
font = cv.FONT_HERSHEY_SIMPLEX

def clickEvent(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        coords = str(x) + ", " + str(y)
        cv.putText(img, coords, (x, y), font, 1, (0, 0, 255), 1)
        cv.circle(img, (x, y), 10, (0, 0, 255), -1)
        points.append((x, y))

        if len(points) >= 2:
            cv.line(img, points[-1], points[-2], (0, 255, 255), 5)
        cv.imshow("Image", img)


points = []

cv.imshow("Image", img)
cv.setMouseCallback("Image", clickEvent)

cv.waitKey(0)
cv.destroyAllWindows()
