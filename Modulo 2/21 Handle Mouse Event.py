import cv2 as cv
import numpy as np

# para ver quais tipos de eventos tem
#event = [i for i in dir(cv) if "EVENT" in i]
#print(event)

def clickEvent(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv.FONT_HERSHEY_SIMPLEX
        coords = str(x) + ", " + str(y)
        cv.putText(img, coords, (x, y), font, 1, (0, 0, 255), 1)
        cv.imshow("Image", img)

#img = np.zeros([512, 512, 3], np.uint8)
img = cv.imread("../lena.jpg")

cv.imshow("Image", img)
cv.setMouseCallback("Image", clickEvent)

cv.waitKey(0)
cv.destroyAllWindows()
