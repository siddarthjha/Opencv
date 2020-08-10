"""
The function used is cv2.threshold. 
First argument is the source image, which should be a grayscale image.
Second argument is the threshold value which is used to classify the pixel values. 
Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. 
"""
# Simple Thresholding

# Adaptive Thresholding

"""
The function used is cv2.threshold. 
First argument is the source image, which should be a grayscale image.
Second argument is the  maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
Third argument is the
ADAPTIVE_THRESH_MEAN_C − threshold value is the mean of neighborhood area. (OR)
ADAPTIVE_THRESH_GAUSSIAN_C − threshold value is the weighted sum of neighborhood values where weights are a Gaussian window.
Fourth Argument is the threshold type -> variable of integer type representing the type of threshold to be used.
Fifth Argument is the blockSize − A variable of the integer type representing size of the pixelneighborhood used to calculate the threshold value.
Sixth Argument is C (Constant) − A variable of double type representing the constant used in the both methods (subtracted from the mean or weighted mean).

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('b.jpg', 0)
ret,thresh1 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 140, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) # ADAPTIVE THRESHOLDING
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
ret2,th4 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # OTSU'S BINARIZATION

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 'Adaptive Mean', 'Adaptive Gaussian', 'Otsu']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, th2, th3, th4]

for i in range(9):
    
    plt.subplot(3, 3, i+1)   # Sub-plot (n rows, ncolumns, indexof the particular plot
    plt.imshow(images[i], 'gray') 
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.imshow('Mean', th2)
cv2.imshow('Gaussian', th3)
cv2.waitKey(0)
cv2.destroyAllWindows()

