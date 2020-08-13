import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('b.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
