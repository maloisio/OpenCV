import numpy as np
import cv2 as cv

img = np.zeros([512, 512, 3], np.uint8)

cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()