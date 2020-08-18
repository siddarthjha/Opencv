import numpy as np
import cv2

img = cv2.imread('a.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) # The lower the clip-limit the better
# Clip-limit is the contrast of image (1-3)
cl1 = clahe.apply(img)
cl1 = np.hstack((img, cl1))
cv2.namedWindow('quant', cv2.WINDOW_NORMAL)
cv2.imshow('quant', cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()


