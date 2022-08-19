import cv2 as cv

faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faceCascadeDetect = faceCascade.detectMultiScale(gray_img, 1.1, 5)

    for(x, y, w, h) in faceCascadeDetect:# 4 pontos necessario para fazer o retangulo
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)

        cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()
