import cv2 as cv

cap = cv.VideoCapture("motion.avi")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    motiondiff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(motiondiff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    dilate = cv.dilate(thresh, None, iterations=3)

    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 700:
            continue

        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame1, (int(x +w/2), int(y + h/2)), 4, (0, 0, 255), -1)

    cv.imshow("Motion", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(50) == 27:
        break

cap.release()
cv.destroyAllWindows()
