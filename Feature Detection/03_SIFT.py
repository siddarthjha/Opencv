import cv2
import numpy as np

# INSTALL opencv-contrib-python
# As SIFT and SURF is removed from opencv

img = cv2.imread('b.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kps = sift.detect(gray, None)

kp,des = sift.compute(gray, kps) # Computes Keypoint descriptor from the computed keypoints
print(des)

img = cv2.drawKeypoints(gray, kps, outImage = None)

cv2.imshow('vgf', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# The flag will draw a circle with size of keypoint and show it's orientation 
img = cv2.drawKeypoints(gray, kps, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, outImage = None)
cv2.imshow('vgf', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
