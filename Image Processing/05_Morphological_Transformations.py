import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('b.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.uint8)

# Erosion - It is useful for removing small white noises
erosion = cv2.erode(img, kernel, iterations = 1)

# dilation - It increases the white region in the image or size of foreground object increases.
dilation = cv2.dilate(img,kernel,iterations = 1)
# erosion removes white noises, but it also shrinks our object.
# So we dilate it. Since noise is gone, they won’t come back, but our object area increases

# Opening - Opening is just another name of erosion followed by dilation. It is useful in removing noise,
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

# Closing - Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# Plot the above ones also by yourself

# Plotting
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(dilation), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(111), plt.imshow(closing), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.show()
