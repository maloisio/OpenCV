import cv2 as cv

img = cv.imread("Ronaldo-3.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

new, thresh = cv.threshold(imgGray, 127, 255, 0)

contours, hierachy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Countour Numbers = " + str(len(contours)))

print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 2)

cv.imshow("Image", img)
cv.imshow("Gray Image", imgGray)

cv.waitKey(0)
cv.destroyAllWindows()
