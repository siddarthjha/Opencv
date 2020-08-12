import numpy as np
import cv2
from matplotlib import pyplot as plt

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
img = cv2.imread('b.jpg', 0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 270, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Rotation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.warpAffine takes a 2x3 transformation matrix while cv2.warpPerspective takes a 3x3 transformation matrix as input.

# Affine Transformation
img = cv2.imread('a.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols,ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.show()
