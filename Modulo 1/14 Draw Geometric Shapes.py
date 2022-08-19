import cv2 as cv

img = cv.imread("../lena.jpg", 1)#segundo parametro 1 colorido

img = cv.line(img, (0, 255), (512, 255), (255, 0, 0), thickness=7)
img = cv.line(img, (255, 0), (255, 512), (255, 0, 0), thickness=7)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()