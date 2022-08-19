import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.isOpened(), cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#se setar abaixo da menor resolucao (640, 360), ele vai manter esses valores
cap.set(3, 400)# 3 se refere a CAP_PROP_FRAME_WIDTH
cap.set(4, 400)# 4 se refere a CAP_PROP_FRAME_HEIGHT

print(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    cv.imshow("Video", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()
