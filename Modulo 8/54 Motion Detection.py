import cv2 as cv

cap = cv.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    motionDiff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(motionDiff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    dilate = cv.dilate(thresh, None, iterations=3)

    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv.imshow("Motion", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

cap.release()
cv.destroyAllWindows()
