import cv2 as cv

img = cv.imread("../lena.jpg", 1)

font = cv.FONT_HERSHEY_SIMPLEX

#(imagem), (texto, (onde comeca), (font?), (tamanho fonte), (cor fonte), (thickness), (?)
img = cv.putText(img, "Meu texto", (155, 255), font, 1, (0, 0, 255),
                 2, cv.LINE_AA)

cv.imshow("Imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()