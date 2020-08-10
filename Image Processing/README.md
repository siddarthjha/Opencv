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
