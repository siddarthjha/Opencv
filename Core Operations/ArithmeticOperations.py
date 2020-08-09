import numpy as np
import cv2 

cv2.namedWindow('add', cv2.WINDOW_NORMAL)
img1 = cv2.imread('a.jpg')
img2 = cv2.imread('x.jpg')
print(img1.size)
print(img2.size)
# The size must be same or else it will give you a error

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# the values are of alpha to display the % of image more

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyWindow('add')

# BITWISE OPERATIONS

# Load two images
cv2.namedWindow('res', cv2.WINDOW_NORMAL)
img1 = cv2.imread('a.jpg')
img2 = cv2.imread('opencv_logo.png')

print(img2.shape)
print(img1.shape)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols ]
print(roi.shape)
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Mask inverse', mask_inv)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
cv2.imshow('Blackout area', img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
cv2.imshow('Image 2 region of logo', img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('mask', mask)
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
