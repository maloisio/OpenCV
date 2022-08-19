import cv2 as cv

img = cv.imread("../lena.jpg", 1)

#(imagem, (centro do circulo), (raio do circulo), (cor), (largura linha)
#img = cv.circle(img, (255, 255), 10, (255, 0, 0), thickness=3)
img = cv.circle(img, (255, 255), 10, (255, 0, 0), -1)#preenchimento do circulo

cv.imshow("Imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()
