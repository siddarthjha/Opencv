import numpy as np
import cv2 

im = cv2.imread('b.jpg')
cv2.imshow('Image', im)
cv2.waitKey(0)
cv2.destroyWindow('Image')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,70,255,0)
thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 4)
#thresh = cv2.Canny(imgray, 127, 255)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyWindow('Thresh')
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #approx_none gives all lines and approx_simple gives limited saving memory and removing redundant points.
# contours is a Python list of all the contours in the image. Each individual contour
# is a Numpy array of (x,y) coordinates of boundary points of the object.
img = cv2.drawContours(im, contours, -1, (0, 0, 255), 1)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyWindow('Contours')
