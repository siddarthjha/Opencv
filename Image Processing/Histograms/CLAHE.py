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

# CLAHE for Color images

bgr = cv2.imread('b.jpg')
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
# L-lightness, a & b for color components green-red & blue-yellow


clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(10, 10))

lab[:, :, 0] = clahe.apply(lab[:, :, 0])

qnt = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR) 
hs = np.hstack((bgr, qnt))
cv2.namedWindow('quant', cv2.WINDOW_NORMAL)
cv2.imshow('quant', hs)
cv2.waitKey(0)
cv2.destroyAllWindows()
