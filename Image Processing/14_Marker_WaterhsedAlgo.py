import numpy as np
import cv2
from matplotlib import pyplot as plt

# Otsu's Binarization Thresholding
img = cv2.imread('b.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 3) # Morphological Transformation

cv2.imshow('Morph', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3) # Morphological Transformation

# Plotting
plt.subplot(121), plt.imshow(thresh, cmap = 'gray'), plt.title('Otsu Thresh')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(opening, cmap = 'gray'), plt.title('Morph')
plt.xticks([]), plt.yticks([])
plt.show()
