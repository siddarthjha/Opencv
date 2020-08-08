import numpy as np
import cv2 


cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
img1 = cv2.imread('a.jpg')
img2 = cv2.imread('x.jpg')
print(img1.size)
print(img2.size)

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
