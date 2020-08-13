import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('b.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((10, 10), np.float32) / 100
dst = cv2.filter2D(img, -1, kernel) # Blurs the part of image 

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

