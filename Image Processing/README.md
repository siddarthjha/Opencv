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
# Image Transforms 
Fourier Transform is used to analyze the frequency characteristics of various filters. For images, 2D Discrete Fourier Transform (DFT) is used to find the frequency domain. A fast algorithm called Fast Fourier Transform (FFT) is used for calculation of DFT
* [Fourier Transform](10_Fourier.py)
# Template Matching
To find objects in an image using Template Matching.
You will see these functions : **cv2.matchTemplate(), cv2.minMaxLoc().**
* [Template matching](11_Template_Matching.py)
# Hough Line Transform
Will see how to use it detect lines in an image.
We will see following functions: **cv2.HoughLines(), cv2.HoughLinesP().** Probabilistic Hough Transform (Optimized hough line transform).
* [Hough Line Transform](12_Hough_Line.py)
# Hough Circle Transform
Will learn to use Hough Transform to find circles in an image.
We will see these functions: **cv2.HoughCircles().**
* [Hough Circle Transform](13_HoughCircle.py)
# Image Segmentation with Watershed Algorithm
Will learn to use marker-based image segmentation using watershed algorithm
We will see: **cv2.watershed().**
* [Segmentation with Watershed Algorithm](14_Marker_WaterhsedAlgo.py)

With normal watershed segmentation we have noise in image so the result is not optimal. So **marker-based Watershed Algorithm** is introduced. We label the objects in the image with a color and other as 0 which we are not sure of. Boundaries of object will have -1.
# Interactive Foreground Extraction using GrabCut Algorithm
Will see GrabCut algorithm to extract foreground in images
We will create an interactive application for this.
* []()
