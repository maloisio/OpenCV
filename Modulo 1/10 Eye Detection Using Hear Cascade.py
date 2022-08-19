import cv2 as cv

eyeCascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

img = cv.imread("../Ronaldo-1.jpg")
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

eyeDetect = eyeCascade.detectMultiScale(grayImg)

for(x, y, w, h) in eyeDetect: #4 pontos para fazer um retangulo, o for faz 2 vezes porque sao 2 olhos
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=4)
    #cv.imshow("Image", img)
    #cv.waitKey(0)

cv.imshow("Image", img)
cv.waitKey(0)
