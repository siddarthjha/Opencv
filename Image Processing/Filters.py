import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('b.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((4, 4), np.float32) / 16
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# Averaging
img = cv2.imread('b.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur = cv2.blur(img, (5, 5))

# Gaussian Blur
gblur = cv2.GaussianBlur(img, (7,7), 0)

# Median Blur
img1 = cv2.imread('n.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# Take a noisy image for this
median = cv2.medianBlur(img1, 5)

# Bilateral Filtering
bblur = cv2.bilateralFilter(img,9,75,75)

# Plotting all of them
plt.subplot(321), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322), plt.imshow(blur), plt.title('Averaging(Blurred)')
plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(gblur), plt.title('Gaussian Filtering')
plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(img1), plt.title('Median Original')
plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(median), plt.title('Median Filtering')
plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(bblur), plt.title('Bilateral Filtering') # Note surface texture is gone but edges are still preservec
plt.xticks([]), plt.yticks([])

plt.show()
"""
You can use a for loop  and list for more clean code :) 
I was changing it constantly to see the differences and all... so it's like this.
"""


