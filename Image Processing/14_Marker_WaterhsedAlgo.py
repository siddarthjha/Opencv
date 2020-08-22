import numpy as np
import cv2
from matplotlib import pyplot as plt

# Otsu's Binarization Thresholding
img = cv2.imread('b.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 3)

cv2.imshow('Foreground noise removal', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

cv2.imshow('background noise removal', sure_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

cv2.imshow('Distance Transform', dist_transform)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sure foreground', sure_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

cv2.imshow('Unknown region', unknown)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

# Plotting
plt.subplot(3, 2, 1), plt.imshow(thresh, cmap = 'gray'), plt.title('Otsu Thresh')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 2), plt.imshow(opening, cmap = 'gray'), plt.title('Foreground')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 3), plt.imshow(sure_bg, cmap = 'gray'), plt.title('Background')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4), plt.imshow(sure_fg, cmap = 'gray'), plt.title('Sure Foreground')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 5), plt.imshow(unknown, cmap = 'gray'), plt.title('Unknown')
plt.xticks([]), plt.yticks([])
plt.show()
