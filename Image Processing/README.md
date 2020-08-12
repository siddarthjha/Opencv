# Changing Colorspaces
You will learn following functions : **cv2.cvtColor(), cv2.inRange() etc.**
*  [Color-space](Colorspaces.py)

# Image Thresholding
You will learn these functions : cv2.threshold, cv2.adaptiveThreshold etc.
### Otsu’s Binarization
It automatically calculates a threshold value from image histogram for a bimodal image. Like we give the threshold value in cv2.threshold, instead of it this calculates the threshold value.  

For images which are not bimodal, binarization won’t be accurate.
* [Image Thresholding](Thresholding.py)

If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black).

# Geometric Transformations of Images
You will see these functions: **cv2.getPerspectiveTransform**

cv2.warpAffine takes a 2x3 transformation matrix while cv2.warpPerspective takes a 3x3 transformation matrix as input.


**cv2.INTER_AREA:** This is used when we need need to shrink an image.

**cv2.INTER_CUBIC:** This is slow but more efficient.

**cv2.INTER_LINEAR:** This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.

* [Geometric Transformations](Geometric_Transformations.py)

# Smoothing Images
Blur imagess with various low pass filters

Apply custom-made filters to images (2D convolution)
