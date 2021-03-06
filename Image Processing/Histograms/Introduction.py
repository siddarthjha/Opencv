import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('b.jpg', 0)
# Histogram in Open-Cv
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) # blue
print(hist)
plt.plot(hist)
plt.show()

# Histogram in Matplotlib
# hist, bins = np.histogram(img.ravel(), 256, [0, 256])
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# Another way of matplotlib of BGR
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
