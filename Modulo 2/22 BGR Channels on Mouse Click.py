import numpy as np
import cv2 as cv


def clickEvent(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        strBgr = str(blue) + ", " + str(red) + ", " + str(green)
        cv.putText(img, strBgr, (x, y), font, 1, (0, 255, 255), 1)
        cv.imshow("Image", img)


img = cv.imread("Ronaldo-Kick.jpg")

cv.imshow("Image", img)
cv.setMouseCallback("Image", clickEvent)

cv.waitKey(0)
cv.destroyAllWindows()
