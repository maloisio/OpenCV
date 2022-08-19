import cv2 as cv

img = cv.imread("Ball.jpg")

img = cv.rectangle(img, (455, 205), (700, 445), (255, 0, 0), 2)
img = cv.rectangle(img, (10, 10), (255, 250), (0, 0, 255), 2)

#[y1
myImg = img[205:445, 455:700] #pegando a bola da imagem original
img[10:250, 10:255] = myImg #imagem original vai receber a bola no lugar novo

cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()