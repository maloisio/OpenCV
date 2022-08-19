import cv2 as cv

eyeCascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

cap = cv.VideoCapture(0)

while cap.isOpened(): #cap.isOpenede True
    _, frame = cap.read() #converte video em frame
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # converte o frame para grayscale
    eyeCascadeDetect = eyeCascade.detectMultiScale(gray_img)


    for (x, y, w, h) in eyeCascadeDetect:
        cv.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), thickness=4)

        cv.imshow("Frame", frame) # vai mostrando o frame a cada for porque e video

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()


