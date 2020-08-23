import numpy as np
import cv2
from matplotlib import pyplot as plt

"""
Foreground Extraction Using GrabCut Algorithm
1. Draw a rectangle of foreground region.
2. Then algorithm segments it iteratively.
"""
img = cv2.imread('b.jpg')
print(img.shape[:2])
mask = np.zeros(img.shape[:2], np.uint8)
print(mask)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (180, 30, 500, 1000)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
"""
1. Input image
2. It is a mask image where we specify which areas are background, foreground or probable background/foreground etc. 
It is done by the following flags, cv2.GC_BGD, cv2.GC_FGD, cv2.GC_PR_BGD, cv2.GC_PR_FGD, or simply pass 0,1,2,3 to image.
3. Rectangle co-ordinates(x, y, w, h)
4. bdgModel, fgdModel - These are arrays used by the algorithm internally. You just create two np.float64 type zero arrays of size (1,65).
5. Number of iterations
6. Mode - It should be cv2.GC_INIT_WITH_RECT or cv2.GC_INIT_WITH_MASK or combined which decides whether we are drawing rectangle or final touchup strokes.
"""
mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
print(mask2)
img = img * mask2[:, :, np.newaxis]

plt.imshow(img), plt.colorbar(), plt.show()
cv2.imwrite('m.jpg', img)

# Doing the same thing with the mask this time
# newmask is the mask image I manually labelled
newmask = cv2.imread('m.jpg',0)

cv2.imshow('Newmask', newmask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

mask = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
img = img * mask[:, :, np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()
