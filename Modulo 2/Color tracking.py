import numpy as np
import cv2 as cv
import sys

frame2 = np.zeros([512, 512, 3], np.uint8)  # criacao imagem preta
font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture("../Players.mp4")

tracker5 = cv.TrackerMIL_create()
tracker = cv.TrackerMIL_create()
tracker2 = cv.TrackerMIL_create()
tracker3 = cv.TrackerMIL_create()
tracker4 = cv.TrackerMIL_create()
success, img = cap.read()

bbox = cv.selectROI("Tracking", img, False)
bbox2 = cv.selectROI("Tracking", img, False)
bbox3 = cv.selectROI("Tracking", img, False)
bbox4 = cv.selectROI("Tracking", img, False)

tracker.init(img, bbox)
tracker2.init(img, bbox2)
tracker3.init(img, bbox3)
tracker4.init(img, bbox4)

lowerBlueHsv = np.array([90, 50, 50])
upperBlueHsv = np.array([130, 255, 255])

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(img, (x,y), ((x+w),(y+h)), (255, 0, 255), 3, 1)

while cap.isOpened():

    success, img = cap.read()
    success, bbox = tracker.update(img)
    success, bbox2 = tracker2.update(img)
    success, bbox3 = tracker3.update(img)
    success, bbox4 = tracker4.update(img)

    if success:
        drawBox(img, bbox)
        drawBox(img, bbox2)
        drawBox(img, bbox3)
        drawBox(img, bbox4)
    else:
        cv.putText(img, "Lost", (75, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)


    cv.imshow("Tracking", img)

    if cv.waitKey(1) & 0xff == ord("q"):
        break

cv.destroyAllWindows()
