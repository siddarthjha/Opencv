import numpy as np
import cv2

img = cv2.imread('a.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
# Pixel values of given row column of the image
green = img[100, 100, 1]
red = img[100, 100, 2]
print(green)
print(red)
all = img[3000, 120]   # If you cross the dimensions of the image then you will get an index error-(try [7000,10000])
print(all)
# You can also change the value
img[100, 100] = [255, 0, 0]
print(img[100, 100)
# Numpy is a optimized library for fast array calculations. So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.  
# Better pixel accessing and editing method : 
print(img.item(100, 100, 1))
img.itemset((10, 10, 2), 250)
print(img.item(10, 10, 2))          
cv2.waitKey(0)
cv2.destroyWindow('Image')
