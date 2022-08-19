import datetime

import cv2 as cv

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True: #ou if ret
        font = cv.FONT_HERSHEY_SIMPLEX
        text = "Largura: " + str(cap.get(3)) + " Altura: " + str(cap.get(4)) + " "
        curDate = str(datetime.datetime.now())
        frame = cv.putText(frame, text + curDate, (10, 50), font, 0.5, (0, 0, 255),
                           1, cv.LINE_AA)

        cv.imshow("Video", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

cap.release()
cv.destroyAllWindows()
