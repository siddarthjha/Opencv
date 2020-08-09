# Basic Operations on Images
* Access pixel values and modify them
* Access image properties
* Setting Region of Image (ROI)
* Splitting and Merging images

Almost all the operations in this section is mainly related to Numpy rather than OpenCV. A good knowledge of Numpy is required to write better optimized code with OpenCV
* [Operations](ImageOperations.py)

# Arithmetic Operations on Images
You will learn these functions : **cv2.add(), cv2.addWeighted() etc.**
* [Arithmetic Operations](ArithmeticOperations.py)
* [Image transtion Slide Show](SlideShow_transition.py)

**Note:** There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

```
>>> x = np.uint8([250])
>>> y = np.uint8([30])

>>> print cv2.add(x,y) # 250+30 = 280 => 255
[[255]]

>>> print x+y          # 250+30 = 280 % 256 = 24
[24]
```
# Performance Measurement and Improvement Techniques
You will see these functions : **cv2.getTickCount, cv2.getTickFrequency etc.**

* [Performance and Optimization](Performance.py)

#### Default Optimization in OpenCV
```
# check if optimization is enabled
In [5]: cv2.useOptimized()
Out[5]: True

In [6]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 34.9 ms per loop

# Disable it
In [7]: cv2.setUseOptimized(False)

In [8]: cv2.useOptimized()
Out[8]: False

In [9]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 64.1 ms per loop
```
