import numpy as np
import cv2 
import time
# IT GIVES A SLIDESHOW OF THE IMAGES PASSED.

img1 = cv2.imread('a.jpg')
img2 = cv2.imread('x.jpg')
res = img1
i = 10
inc = 1
cv2.namedWindow('res', cv2.WINDOW_NORMAL)
cv2.imshow('res',res)
while(1):
    if(cv2.waitKey(0) & 0xFF == ord('q')):
        break
    else:
        newimg = np.zeros((640,480))
        res = cv2.addWeighted(img1,0.1*i,img2,0.1*(10-i),0)
        if i == 10 or i == 0:
            inc = -inc
        i = i + inc
        cv2.imshow('res',res)
        # time.sleep(0.2)
