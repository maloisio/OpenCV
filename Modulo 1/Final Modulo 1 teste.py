import datetime
import math

import cv2 as cv

eyeCascade = cv.CascadeClassifier("../haarcascade_eye_tree_eyeglasses.xml")
faceCascade = cv.CascadeClassifier("../haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    ret, frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # converte o frame para grayscale
    eyeCascadeDetect = eyeCascade.detectMultiScale(gray_img)  # aplica o haarcascade para encontrar o olho
    faceCascadeDetect = faceCascade.detectMultiScale(gray_img) #aplica o haarcascade para encontrar a face

    if ret == True: #ou if ret
        # desenha o retangulo
        for (x, y, w, h) in eyeCascadeDetect:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

            for (fx, fy, fw, fh) in faceCascadeDetect:
                cv.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), thickness=3)
                #inputa texto em baixo do rosto
                cv.putText(frame, "Rosto", (fx, fy + fh + 20), font, 0.5, (0, 0, 255),
                            1, cv.LINE_AA)
                cv.line(frame, (math.floor(fx+fw/2), fy - 20), (math.floor(fx+fw/2), fy + fh + 20),
                        (0, 0, 255), thickness=1)
                cv.line(frame, (fx - 20, math.floor(fy + fh/2)), ((fx + fw + 20), math.floor(fy + fh/2)),
                        (0, 0, 255), thickness=1)


        text = "Largura: " + str(cap.get(3)) + " Altura: " + str(cap.get(4)) + " "
        curDate = str(datetime.datetime.now())
        frame = cv.putText(frame, text + curDate, (10, 50), font, 0.5, (0, 0, 255),
                           1, cv.LINE_AA)

        cv.imshow("Video", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

cap.release()
cv.destroyAllWindows()