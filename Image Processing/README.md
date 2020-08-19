# Changing Colorspaces
You will learn following functions : **cv2.cvtColor(), cv2.inRange() etc.**
*  [Color-space](01_Color_spaces.py)

# Image Thresholding
You will learn these functions : cv2.threshold, cv2.adaptiveThreshold etc.
### Otsu’s Binarization
It automatically calculates a threshold value from image histogram for a bimodal image. Like we give the threshold value in cv2.threshold, instead of it this calculates the threshold value.  

For images which are not bimodal, binarization won’t be accurate.
* [Image Thresholding](02_Thresholding.py)

If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black).

# Geometric Transformations of Images
You will see these functions: **cv2.getPerspectiveTransform**

cv2.warpAffine takes a 2x3 transformation matrix while cv2.warpPerspective takes a 3x3 transformation matrix as input.


**cv2.INTER_AREA:** This is used when we need need to shrink an image.

**cv2.INTER_CUBIC:** This is slow but more efficient.

**cv2.INTER_LINEAR:** This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.

* [Geometric Transformations](03_Geometric_Transformations.py)

# Smoothing Images
Blur images with various low pass filters
1. Averaging.
2. Gaussian Filtering.
3. Median Filtering.
4. Bilateral Filtering.

Apply custom-made filters to images (2D convolution)
* [Image filters](04_Filters.py)

# Morphological Transformations
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images.

We will see different functions like : **cv2.erode(), cv2.dilate(), cv2.morphologyEx() etc.**
* [Morphological Transformations](05_Morphological_Transformations.py)

# Image Gradients
We will see following functions : **cv2.Sobel(), cv2.Scharr(), cv2.Laplacian() etc.**

* [Image Gradients](06_Gradients.py)

# Canny Edge Detection
OpenCV functions for that : **cv2.Canny().**

Steps in Canny Edge Detection:
1. **Noise Reduction:** Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter.
2. **Finding Intensity Gradient of the Image:** Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction.
3. **Non-maximum Suppression:** After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. 
4. **Hysteresis Thresholding:** This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal.

All these steps are included in the cv2.Canny(src, minval, maxval);

* [Edge Detection](07_Edge_Detection.py)

# Image Pyramids
We will see these functions: **cv2.pyrUp(), cv2.pyrDown().**

There are two kinds of Image Pyramids. 

1) Gaussian Pyramid and 
2) Laplacian Pyramids

* [Image Pyramids](08_Image_pyramid.py)
# Contours 
* [Contours](Contours)
# Histograms
* [Histograms](Histograms/README.md)
# Image Transforms in OpenCV
Fourier Transform is used to analyze the frequency characteristics of various filters. For images, 2D Discrete Fourier Transform (DFT) is used to find the frequency domain. A fast algorithm called Fast Fourier Transform (FFT) is used for calculation of DFT
* [Fourier Transform](10_Fourier.py)
