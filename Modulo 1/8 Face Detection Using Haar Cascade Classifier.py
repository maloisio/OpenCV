import cv2 as cv

faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("../teste12.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faceCascadeDetect = faceCascade.detectMultiScale(gray_img, 1.1, 4)

for(x, y, w, h) in faceCascadeDetect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow("Image", img)
cv.waitKey(0)