import cv2 as cv

img = cv.imread("../New-Ronaldo.jpg", 1)
cv.imshow("Image", img)

e = cv.waitKey(0)

if e == 27:
    cv.destroyAllWindows()
elif e == ord("s"):
    cv.imwrite("../The-New-Ronaldo.jpg", img)
    cv.destroyAllWindows()
