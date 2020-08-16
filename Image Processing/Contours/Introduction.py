import numpy as np
import cv2 

im = cv2.imread('b.jpg')
cv2.imshow('Image', im)
cv2.waitKey(0)
cv2.destroyWindow('Image')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# For determing contour you need to undergo thresholding/ Canny edge for better accuracy
ret,thresh = cv2.threshold(imgray,127,255,0)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyWindow('Thresh')
contours, heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# contours is a Python list of all the contours in the image. Each individual contour
# is a Numpy array of (x,y) coordinates of boundary points of the object.
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyWindow('Contours')

