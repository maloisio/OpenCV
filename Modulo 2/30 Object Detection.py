import cv2 as cv
import numpy as np

while True:
    img = cv.imread("Color-Balls-2.jpg")
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerBlue = np.array([40, 58, 127])
    upperBlue = np.array([84, 255, 255])

    maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)

    outputMaskBit = cv.bitwise_and(img, img, mask=maskBlue)

    cv.imshow("Image", img)
    cv.imshow("Mask", maskBlue)
    cv.imshow("Output", outputMaskBit)

    key = cv.waitKey()
    if key == 27:
        break

cv.destroyAllWindows()