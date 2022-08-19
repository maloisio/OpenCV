import cv2 as cv
import numpy as np
from numpy.ma import append
from scipy.spatial import distance as dist

xIndex = []
yIndex = []
wIndex = []
hIndex = []

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    blurred_frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)  # transforma o frame em hsv

    lowerBlue = np.array([110, 50, 50])  # defenimos o range do loweblue H,S,V
    upperBlue = np.array([130, 255, 255])  # definimos o range do high blue H,S,V

    maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)  # oq estamos aceitando do HSV fica branco e o resto preto

    contours, hierachy, = cv.findContours(maskBlue, cv.RETR_TREE,
                                          cv.CHAIN_APPROX_NONE)  # _ quer dizer que vai receber algo, NONE PEGA TODOS PONTOS, SIMPLE PEGA 4

    if len(contours) != 0:
        for contours in contours:
            if cv.contourArea(contours) > 100:  # para nao ficar pegando pontos pequenos

                # print(contours)
                # cv.drawContours(frame, contours, -1, (0, 255, 255), thickness=2)
                x, y, w, h = cv.boundingRect(
                    contours)  # identificar um retangulo por 4 pontos e retorna as coordenadas do retangulo
                xIndex.append(x)
                yIndex.append(y)
                wIndex.append(w)
                hIndex.append(h)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
                cv.circle(frame, (int(x + w / 2), int(y + h / 2)), 4, (0, 0, 255), -1)

    if len(xIndex) >= 3:
        for i in range(int(len(xIndex))):
            distEuc = dist.euclidean((int(xIndex[i] + wIndex[i] / 2), int(yIndex[i] + hIndex[i] / 2)),
                                     (int(xIndex[i - 1] + wIndex[i - 1] / 2),
                                      int(yIndex[i - 1] + hIndex[i - 1] / 2)))
            distEuc2 = dist.euclidean((int(xIndex[i-1] + wIndex[i-1] / 2), int(yIndex[i-1] + hIndex[i-1] / 2)),
                                     (int(xIndex[i - 2] + wIndex[i - 2] / 2),
                                      int(yIndex[i - 2] + hIndex[i - 2] / 2)))
        print(distEuc)
        print(distEuc2)
        if int(distEuc) > 100:
            cv.line(frame, (int(xIndex[i] + wIndex[i] / 2), int(yIndex[i] + hIndex[i] / 2)), (int(xIndex[i-1] + wIndex[i-1] / 2), int(yIndex[i-1] + hIndex[i-1] / 2)), (255, 0, 0), 3)
            cv.line(maskBlue, (int(xIndex[i] + wIndex[i] / 2), int(yIndex[i] + hIndex[i] / 2)),
                    (int(xIndex[i - 1] + wIndex[i - 1] / 2), int(yIndex[i - 1] + hIndex[i - 1] / 2)), (255, 0, 0), 3)
        if int(distEuc2) > 100:
            cv.line(frame, (int(xIndex[i-1] + wIndex[i-1] / 2), int(yIndex[i-1] + hIndex[i-1] / 2)), (int(xIndex[i-2] + wIndex[i-2] / 2), int(yIndex[i-2] + hIndex[i-2] / 2)), (255, 0, 0), 3)
            cv.line(maskBlue, (int(xIndex[i - 1] + wIndex[i - 1] / 2), int(yIndex[i - 1] + hIndex[i - 1] / 2)),
            (int(xIndex[i - 2] + wIndex[i - 2] / 2), int(yIndex[i - 2] + hIndex[i - 2] / 2)), (255, 0, 0), 3)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", maskBlue)
    # cv.imshow("Output", outputMaskBit)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
