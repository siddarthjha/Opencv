import cv2
import numpy as np

img = cv2.imread('b.jpg',0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
# Aspect Ratio
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

# Extent - Extent is the ratio of contour area to bounding rectangle area. 
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

#  Solidity - Solidity is the ratio of contour area to its convex hull area.
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

#  Equivalent Diameter - Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# Orientation - Orientation is the angle at which object is directed. Following method also gives the Major Axis and Minor Axis lengths.
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

# Mask and Pixel Points
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
pixelpoints = cv2.findNonZero(mask)

# Maximum Value, Minimum Value and their locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)

mean_val = cv2.mean(im,mask = mask)

