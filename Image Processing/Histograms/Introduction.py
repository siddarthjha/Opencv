import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('a.jpg')
# Histogram in Open-Cv
hist = cv2.calcHist([img], [2], None, [16], [0, 15])
print(hist)
plt.plot(hist)
plt.show()

# Histogram in Numpy
# hist, bins = np.histogram(img.ravel(), 256, [0, 256])
plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

