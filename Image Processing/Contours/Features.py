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
perimeter = cv2.arcLength(cnt,True)
# It is also called arc length. Second argument specify whether shape is a closed contour (if passed True), or just a curve.
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
# Contour Approximation
# Use this function to approximate the shape. In this, second argument is called epsilon, 
# which is maximum distance from contour to approximated contour. It is an accuracy parameter.
