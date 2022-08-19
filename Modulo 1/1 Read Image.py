import cv2 as cv

img = cv.imread("../Ronaldo-1.jpg") #,0 grey scale
#print(img) #faz o print de array
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
#cv.im