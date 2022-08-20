import numpy as np
import cv2 as cv
import sys
from scipy.spatial import distance as dist

xIndex = []
yIndex = []
wIndex = []
hIndex = []

frame2 = np.zeros([512, 512, 3], np.uint8)  # criacao imagem preta
font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture(0)

tracker = cv.TrackerMIL_create()
tracker2 = cv.TrackerMIL_create()
tracker3 = cv.TrackerMIL_create()

success, img = cap.read()

bbox = cv.selectROI("Tracking", img, False)
bbox2 = cv.selectROI("Tracking", img, False)
bbox3 = cv.selectROI("Tracking", img, False)

tracker.init(img, bbox)
tracker2.init(img, bbox2)
tracker3.init(img, bbox3)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
    cv.circle(img, (int(x + w / 2), int(y + h / 2)), 4, (0, 0, 255), -1)
    xIndex.append(x)
    yIndex.append(y)
    wIndex.append(w)
    hIndex.append(h)

while cap.isOpened():

    success, img = cap.read()
    success, bbox = tracker.update(img)
    success, bbox2 = tracker2.update(img)
    success, bbox3 = tracker3.update(img)

    if success:
        drawBox(img, bbox)
        drawBox(img, bbox2)
        drawBox(img, bbox3)

    else:
        cv.putText(img, "Lost", (75, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    if len(xIndex) >= 3:
        for i in range(int(len(xIndex))):
            distEuc = dist.euclidean((int(xIndex[i] + wIndex[i] / 2), int(yIndex[i] + hIndex[i] / 2)),
                                     (int(xIndex[i - 1] + wIndex[i - 1] / 2),
                                      int(yIndex[i - 1] + hIndex[i - 1] / 2)))

        if int(distEuc) > 100:
            cv.line(img, (int(xIndex[i] + wIndex[i] / 2), int(yIndex[i] + hIndex[i] / 2)),
                    (int(xIndex[i - 1] + wIndex[i - 1] / 2), int(yIndex[i - 1] + hIndex[i - 1] / 2)), (255, 0, 0), 3)

    cv.imshow("Tracking", img)

    if cv.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
