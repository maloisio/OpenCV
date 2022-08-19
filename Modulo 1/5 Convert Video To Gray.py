import cv2 as cv

cap = cv.VideoCapture("Players.mp4") #canal 0 para pegar webcam

while(True):
    ret, frame = cap.read()

    gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Frame", gray_vid)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()
