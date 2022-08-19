import numpy as np
import cv2 as cv

frame2 = np.zeros([512, 512, 3], np.uint8)  # criacao imagem preta
font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture("..\Players.mp4")
points = []
xAux = []
yAux = []
re = False
success, frame = cap.read()
bbox = cv.selectROI("Tracking", frame, False)
cv.destroyWindow("Tracking")
def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(img, (x,y), ((x+w),(y+h)), (255, 0, 255), 3, 1)

def clickEvent(event, x, y, flag, param):
    if re == False:
        if event == cv.EVENT_LBUTTONDOWN:
            xAux.append(x)
            yAux.append(y)
            #points.append(x, y)hehe
            coords = str(x) + ", " + str(y)
            cv.putText(frame, coords, (x, y), font, 1, (0, 0, 255), 1)


            # points.append((xAux[i], yAux[i]))

            # if len(points) >= 2:
            # cv.line(frame, points[-1], points[-2], (0, 255, 255), 5)


while cap.isOpened():

    _, frame = cap.read()  # converte video em frame

    cv.imshow("Frame", frame)  # vai mostrando o frame a cada for porque e video
    cv.setMouseCallback("Frame", clickEvent)
    drawBox(frame, bbox)
    print(bbox)

    if re == False:
        for i in range(int(len(xAux))):

            cv.circle(frame, (xAux[i], yAux[i]), 10, (0, 0, 255), -1)
            print(xAux[i], ", ", yAux[i])

            if len(xAux) >= 2:
                if(i != 0):
                    cv.line(frame, (xAux[i - 1], yAux[i - 1]), (xAux[i], yAux[i]), (0, 255, 255), 2)

    if len(xAux) == 3:
        #cv.line(frameee, (xAux[1], yAux[1]), (xAux[2], yAux[2]), (0, 0, 255), 5)
                #cv.line(frame, (xAux[2], yAux[2]), (xAux[3], yAux[3]), (0, 0, 255), 5)
        cv.rectangle(frame, (xAux[0], yAux[0]), (xAux[1], yAux[2]), (0, 0, 255), thickness=7)

        re = True

        #copia para janela nova o retangulo utilizando bolinha individual
        #newFramee = frame[yAux[0]:yAux[2], xAux[0]:xAux[1]]  # pegando a bola da imagem original
        #frame2[yAux[0]:yAux[2], xAux[0]:xAux[1]] = newFrame

    newFrame = frame[int(bbox[1]):int(bbox[1])+int(bbox[3]), int(bbox[0]):int(bbox[0])+int(bbox[2])]  # pegando a bola da imagem original
    frame2[int(bbox[1]):int(bbox[1])+int(bbox[3]), int(bbox[0]):int(bbox[0])+int(bbox[2])] = newFrame

    cv.imshow("Frame", frame)
    cv.imshow("Frame2", frame2)

    #cv.imshow("Image", img)
    if cv.waitKey(50) == 27:
        break

cv.waitKey(0)
cv.destroyAllWindows()
