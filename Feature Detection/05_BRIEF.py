import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('b.jpg',0)
print(img.shape)

# Initiate STAR detector
star = cv2.xfeatures2d.StarDetector_create()

# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# find the keypoints with STAR
kp = star.detect(img,None)

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
img = cv2.drawKeypoints(img, kp, outImage = None)
cv2.imshow('BRIEF', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(brief.getByte())
print(des.shape)
