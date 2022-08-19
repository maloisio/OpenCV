import cv2 as cv


img = cv.imread("../Ronaldo-1.jpg", 1)
cv.imshow("Image", img)


#CRIANDO NOVA IMAGEM

cv.imwrite("../New-Ronaldo.jpg", img)
cv.waitKey(0)