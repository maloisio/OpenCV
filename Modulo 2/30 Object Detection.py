import cv2 as cv
import numpy as np

while True:
    img = cv.imread("Color-Balls-2.jpg")
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerGreen = np.array([40, 58, 127])
    upperGreen = np.array([84, 255, 255])

    maskGreen = cv.inRange(hsv, lowerGreen, upperGreen)

    outputMaskBit = cv.bitwise_and(img, img, mask=maskGreen)

    cv.imshow("Image", img)
    cv.imshow("Mask", maskGreen)
    cv.imshow("Output", outputMaskBit)

    key = cv.waitKey()
    if key == 27:
        break

cv.destroyAllWindows()