import cv2 as cv

eyeCascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX

while cap.isOpened(): #cap.isOpenede True
    _, frame = cap.read() #converte video em frame
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#converte o frame para grayscale
    eyeCascadeDetect = eyeCascade.detectMultiScale(gray_img)#aplica o haarcascade para encontrar o olho
    faceCascadeDetect = faceCascade.detectMultiScale(gray_img, 1.1, 4) #aplica o haarcascade para encontrar a face

    #desenha o retangulo
    for (x, y, w, h) in eyeCascadeDetect:
        cv.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), thickness=4)

        for (fx, fy, fw, fh) in faceCascadeDetect:
            cv.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), thickness=4)
            cv.putText(frame, "Rosto", (fx, fy + fh + 20), font, 0.5, (0, 0, 255),
                                        1, cv.LINE_AA)
        cv.imshow("Frame", frame) # vai mostrando o frame a cada for porque e video

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()


