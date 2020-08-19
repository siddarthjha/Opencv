import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
low = cv2.pyrDown(img)
plt.subplot(121), plt.imshow(img), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(low), plt.title('Low'), plt.xticks([]), plt.yticks([])
plt.show()
for i in range(4):
	low = cv2.pyrUp(low)
	plt.subplot(2, 2, i+1), plt.imshow(low), plt.title('Low'), plt.xticks([]), plt.yticks([])
	if i == 3:
		plt.show()
		for j in range(4):
			low = cv2.pyrUp(low)
			plt.subplot(2, 2, j+1), plt.imshow(low)
			plt.title('Up'), plt.xticks([]), plt.yticks([])
		plt.show()
