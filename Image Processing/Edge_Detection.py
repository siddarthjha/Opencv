import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a.jpg',0)
edges = cv2.Canny(img, 150, 250)

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.namedWindow('canny', cv2.WINDOW_NORMAL)
cv2.imshow('canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
