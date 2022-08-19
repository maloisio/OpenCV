import cv2 as cv

cap = cv.VideoCapture(0) #canal 0 para pegar webcam
print(cap.isOpened())

while(cap.isOpened()):

    ret, frame = cap.read()
    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.release()
cv.destroyAllWindows()
