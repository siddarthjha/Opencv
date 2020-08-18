import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('a.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
#[0-hue-180, 1-saturation-256], 
cv2.imshow('2d', hist)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2D Histogram in numpy

hist, xbins, ybins = np.histogram2d(hsv.ravel(),hsv.ravel(),[180,256],[[0,180],[0,256]])
plt.imshow(hist, interpolation = 'nearest')
plt.show()
