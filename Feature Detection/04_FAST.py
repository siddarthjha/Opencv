import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('b.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector(40)

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
cv2.imshow('Fast true', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('fast_true.png',img2)


# Print all default params
print("Threshold: ", fast.getInt('threshold'))
print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
print("neighborhood: ", fast.getInt('type'))
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imshow('Fast true', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)

print("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))

cv2.imshow('fast_false', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

