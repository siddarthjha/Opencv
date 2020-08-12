import numpy as np
import cv2

# Scaling
img = cv2.imread('a.jpg')
print(img.shape)

cv2.imshow('img', img)
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_AREA)
print(res.shape)
print(img.shape)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Translation
img = cv2.imread('b.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotation
