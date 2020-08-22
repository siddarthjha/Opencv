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
print(img[100, 100])
# Numpy is a optimized library for fast array calculations. So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.  
# Better pixel accessing and editing method : 
print(img.item(100, 100, 1))
img.itemset((10, 10, 2), 250)
print(img.item(10, 10, 2))   
print(img.shape) # Gives the no of rows and columns of image   
print(img.size)
print(img.dtype)
# img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is caused by invalid datatype.
# Sometimes, you will have to play with certain region of images. For eye detection in images, 
# first perform face detection over the image until the face is found, then search within the face region for eyes.
face = img[280:540, 330:790]
img[573:833, 700:1160] = face
# so here we have copied part of image to other part
# Splitting and Merging Image Channels
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
cv2.waitKey(0)
cv2.destroyWindow('Image')

# Making Borders for Images (Padding)

BLUE = [255,0,0]

img1 = cv2.imread('a.jpg')
img1 = img1[:, :, 0]

replicate = cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231)
plt.imshow(img1, 'gray')
plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234)
plt.imshow(reflect101,'gray')
plt.title('REFLECT_101')
plt.subplot(235)
plt.imshow(wrap,'gray')
plt.title('WRAP')
plt.subplot(236)
plt.imshow(constant,'gray')
plt.title('CONSTANT')
plt.xticks([])
plt.yticks([])
plt.show()
