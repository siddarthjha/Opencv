import numpy as np
import cv2 


cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
img1 = cv2.imread('a.jpg')
img2 = cv2.imread('x.jpg')
print(img1.size)
print(img2.size)
# The size must be same or else it will give you a error

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# the values are of alpha to display the % of image more

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
