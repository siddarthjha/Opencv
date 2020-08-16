import cv2
import numpy as np

img = cv2.imread('b.jpg',0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt #  a dictionary of all moment values calculated. 
# Moments- help you to calculate some features like center of mass of the object, area of the object etc. 
print(M)

area = cv2.contourArea(cnt)
# Contour area

perimeter = cv2.arcLength(cnt, True)
# It is also called arc length. Second argument specify whether shape is a closed contour (if passed True), or just a curve.

epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
# Contour Approximation
# Use this function to approximate the shape. In this, second argument is called epsilon, 
# which is maximum distance from contour to approximated contour. It is an accuracy parameter.

hull = cv2.convexHull(cnt) # Convex Hull
# hull = cv2.convexHull(points[contours we pass], hull[the output,normally we avoid], clockwise[True for clockwise], returnPoints[True returns
# cordinates of hull points]]
k = cv2.isContourConvex(cnt)
# To check a curve is convex or not

x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# Straight Bounding Rectangle

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(im, [box], 0, (0, 0, 255), 2)
# Rotated Rectangle
