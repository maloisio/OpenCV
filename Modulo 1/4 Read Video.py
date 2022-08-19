import cv2 as cv

cap = cv.VideoCapture("Players.mp4") #canal 0 para pegar webcam

while(True):
    ret, frame = cap.read()

    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()
