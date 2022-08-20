import cv2 as cv


# dimensions = img.shape
# imgHeight = img.shape[0]
# imgWidth = img.shape[1]
# imgChannels = img.shape[2]

# cv.line(img, (int(imgWidth/2),0), (int(imgWidth/2), imgHeight), (0,0,255), 3)


def display():
    pass


cv.namedWindow("Gray Tracker")
cv.createTrackbar("H", "Gray Tracker", 0, 255, display)
cv.createTrackbar("A", "Gray Tracker", 0, 15000, display)
cv.createTrackbar("Ab", "Gray Tracker", 15000, 0, display)

while True:
    img = cv.imread("..\pneu2.jpg")
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    lH = cv.getTrackbarPos("H", "Gray Tracker")
    lA = cv.getTrackbarPos("A", "Gray Tracker")
    lAb = cv.getTrackbarPos("Ab", "Gray Tracker")
    # new, thresh = cv.threshold(imgGray, 150, 255, 120)
    new, thresh2 = cv.threshold(imgGray, lH, 255, cv.THRESH_BINARY_INV)
    # new, thresh3 = cv.threshold(imgGray, 230, 255, 120)
    # new, thresh4 = cv.threshold(imgGray, 80, 255, 120)
    # new, thresh5 = cv.threshold(imgGray, 127, 255, 120)

    contours, hierachy = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("Countour Numbers = " + str(len(contours)))

    # print(contours[0])
    if len(contours) != 0:
        for contours in contours:
            if (cv.contourArea(contours) > lA):  # para nao ficar pegando pontos pequenos
                x, y, w, h = cv.boundingRect(contours)
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)
                cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    cv.imshow("Image2", thresh2)
    # cv.imshow("Image3", thresh3)
    # cv.imshow("Image4", thresh4)
    # cv.imshow("Image5", thresh5)
    cv.imshow("Image", img)
    cv.imshow("Gray Image", imgGray)

    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()
