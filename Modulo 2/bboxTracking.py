import numpy as np
import cv2 as cv
import sys

frame2 = np.zeros([512, 512, 3], np.uint8)  # criacao imagem preta
font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture("../Players.mp4")


tracker = cv.TrackerMIL_create()
tracker2 = cv.TrackerMIL_create()

success, img = cap.read()

bbox = cv.selectROI("Tracking", img, False)
bbox2 = cv.selectROI("Tracking", img, False)


tracker.init(img, bbox)
tracker2.init(img, bbox2)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(img, (x,y), ((x+w),(y+h)), (255, 0, 255), 3, 1)


while cap.isOpened():

    success, img = cap.read()
    success, bbox = tracker.update(img)
    success, bbox2 = tracker2.update(img)

    if success:
        drawBox(img, bbox)
        drawBox(img, bbox2)

    else:
        cv.putText(img, "Lost", (75, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

    cv.imshow("Tracking", img)

    if cv.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()