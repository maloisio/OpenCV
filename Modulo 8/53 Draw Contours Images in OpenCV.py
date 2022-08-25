import cv2 as cv
import numpy as np


# cv.line(img, (int(imgWidth/2),0), (int(imgWidth/2), imgHeight), (0,0,255), 3)
imgInit = cv.imread("..\pneu2.jpg")
img = cv.GaussianBlur(imgInit, (5, 5), 0)

hull  =  []
dimensions = img.shape
imgHeight = img.shape[0]
imgWidth = img.shape[1]
imgChannels = img.shape[2]


#bbox = cv.selectROI("Tracking", img, False)

def display():
    pass

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(img, (x,y), ((x+w),(y+h)), (255, 0, 255), 3, 1)

cv.namedWindow("Gray Tracker")
cv.createTrackbar("H", "Gray Tracker", 0, 255, display)
cv.createTrackbar("A", "Gray Tracker", 0, 15000, display)
#cv.createTrackbar("Ab", "Gray Tracker", 15000, 0, display)

#drawBox(img, bbox)

#frame2 = np.zeros([700, int(bbox[3])-int(bbox[1]), imgChannels], np.uint8)


while True:
    img2 = np.zeros([imgWidth, imgHeight, imgChannels], np.uint8)  # criacao imagem preta
   ## newFrame = img[int(bbox[1]):int(bbox[1]) + int(bbox[3]),
   ## int(bbox[0]):int(bbox[0]) + int(bbox[2])]  # pegando a bola da imagem original

    ##img2[int(bbox[1]):int(bbox[1]) + int(bbox[3]), int(bbox[0]):int(bbox[0]) + int(bbox[2])] = newFrame
    img = cv.imread("..\pneu2.jpg")
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img2Gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    lH = cv.getTrackbarPos("H", "Gray Tracker")
    lA = cv.getTrackbarPos("A", "Gray Tracker")
    #lAb = cv.getTrackbarPos("Ab", "Gray Tracker")



    # new, thresh = cv.threshold(imgGray, 150, 255, 120)
    new, thresh2 = cv.threshold(imgGray, lH, 255, cv.THRESH_BINARY_INV)
    new, thresh3 = cv.threshold(img2Gray, lH, 255, cv.THRESH_BINARY_INV)
    # new, thresh3 = cv.threshold(imgGray, 230, 255, 120)
    # new, thresh4 = cv.threshold(imgGray, 80, 255, 120)
    # new, thresh5 = cv.threshold(imgGray, 127, 255, 120)

    contours, hierachy = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    contours2, hierachy = cv.findContours(thresh3, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("Countour Numbers = " + str(len(contours)))

    for i in range(len(contours)):
        hull.append(cv.convexHull(contours[i]))


    # print(contours[0])
    #if len(contours) != 0:
     #   for contours in contours:
      #      if (cv.contourArea(contours) > lA):  # para nao ficar pegando pontos pequenos
       #         x, y, w, h = cv.boundingRect(contours)
        #        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)
         #       cv.drawContours(img, contours, -1, (0, 255, 0), 2)
          #      cv.drawContours(img2, contours, -1, (0, 255, 255), 2)

    # print(contours[0])
    if len(contours) != 0:
        for contours in contours:
            if (cv.contourArea(contours) > lA):  # para nao ficar pegando pontos pequenos
                rect= cv.minAreaRect(contours)
                box= cv.boxPoints(rect)
                box= np.int0(box)
                cv.drawContours(img, [box], -1, (0, 255, 0), 2)
                cv.drawContours(img2, contours, -1, (0, 255, 255), 2)
                cv.drawContours(img2, [box], -1, (0, 255, 255), 2)

                #cv.drawContours(img, hull, i, [0, 0, 255], 1, 8)



    cv.imshow("Image23", img2)
    #cv.imshow("Threash3", thresh3)
    #cv.imshow("Gray Image2", img2Gray)

    #cv.imshow("Image2", thresh2)
    cv.imshow("Image", img)
   # cv.imshow("Gray Image", imgGray)

    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()
