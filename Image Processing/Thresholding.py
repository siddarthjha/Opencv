"""
The function used is cv2.threshold. 
First argument is the source image, which should be a grayscale image.
Second argument is the threshold value which is used to classify the pixel values. 
Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. 
"""
img = cv2.imread('b.jpg')
ret,thresh1 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 140, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_RGB2BGR)
    plt.subplot(3, 2, i+1),plt.imshow(images[i], 'gray') # Sub-plot (n rows, ncolumns, indexof the particular plot
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
