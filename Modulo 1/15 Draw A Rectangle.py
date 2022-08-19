import cv2 as cv

img = cv.imread("../lena.jpg", 1)#segundo parametro 1 colorido

#(inicio x, inicio y), (vai ate x, desce ou sobe y), (cor), (largura da linha)
img = cv.rectangle(img, (100, 100), (255, 300), (0, 0, 255), thickness=7)

#preenchimento

img = cv.rectangle(img, (100, 100), (255, 300), (0, 255, 0), -1) # -1 significa preenchimento

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()