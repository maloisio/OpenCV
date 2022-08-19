import cv2 as cv
import numpy as np


def display():
    pass


cap = cv.VideoCapture("../Players.mp4")

cv.namedWindow("HSV Tracker")
cv.createTrackbar("LH", "HSV Tracker", 0, 255, display)
cv.createTrackbar("LS", "HSV Tracker", 0, 255, display)
cv.createTrackbar("LV", "HSV Tracker", 0, 255, display)

cv.createTrackbar("UH", "HSV Tracker", 255, 255, display)
cv.createTrackbar("US", "HSV Tracker", 255, 255, display)
cv.createTrackbar("UV", "HSV Tracker", 255, 255, display)

while True:
    _, frame = cap.read()

    imgHsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lH = cv.getTrackbarPos("LH", "HSV Tracker")
    lS = cv.getTrackbarPos("LS", "HSV Tracker")
    lV = cv.getTrackbarPos("LV", "HSV Tracker")

    uH = cv.getTrackbarPos("UH", "HSV Tracker")
    uS = cv.getTrackbarPos("US", "HSV Tracker")
    uV = cv.getTrackbarPos("UV", "HSV Tracker")

    lowerHsv = np.array([lH, lS, lV])
    upperHsv = np.array([uH, uS, uV])

    maskHsv = cv.inRange(imgHsv, lowerHsv, upperHsv)

    outputMask = cv.bitwise_and(frame, frame, mask=maskHsv)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", maskHsv)
    cv.imshow("Output", outputMask)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
