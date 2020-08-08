import numpy as np
import cv2

img = cv2.imread('a.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
green = img[100, 100, 1]
red = img[100, 100, 2]
print(green)
print(red)
all = img[3000, 120]   # If you cross the dimensions of the image then you will get an index error-(try [7000,10000])
print(all)
cv2.waitKey(0)
cv2.destroyWindow('Image')
