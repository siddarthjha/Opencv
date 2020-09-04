# Understanding Features
Will just try to understand what are features, why are they important, why corners are important etc.

Features are regions of images with variation. Like the corners of a image.
* [Features](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_meaning/py_features_meaning.html)
# Harris Corner Detection
Will understand the concepts behind Harris Corner Detection.
We will see the functions: **cv2.cornerHarris(), cv2.cornerSubPix().**
* [Harris Corner Detection](01_HarrisDetection.py)
# Shi-Tomasi Corner Detector
Will learn about the another corner detector: Shi-Tomasi Corner Detector
We will see the function: **cv2.goodFeaturesToTrack().**<br>
###### This function is more appropriate for tracking
* [Shi-Tomasi Detector](02_ShiTomasi.py)
# Scale-Invariant Feature Transform
Will learn about the concepts of SIFT algorithm
We will learn to find SIFT Keypoints and Descriptors.

**NOTE:**: Make sure you have installed the required modules from [here](requirements.txt)
```
pip install -r requirements.txt
```
* [SIFT](03_SIFT.py) <br>
There is another modification of SIFT which is SURF (Speeded Up Robust Features).<br>
As these both are SIFT and SURF are patented so not free for commercial use.
To implement SIFT you need to install opencv-contrib
```
pip install opencv-contrib-python
```
After installing this the SIFT program will run properly.
# FAST Algorithm for Corner Detection
We will find corners using OpenCV functionalities for FAST algorithm.
* [FAST (Features from Accelerated Segment Test)](04_FAST.py)

All the above methods are really good but when it comes to real time application they are not fast enough. It is several times faster than other existing corner detectors. But it is not robust to high levels of noise. It is dependant on a threshold.
# BRIEF
It provides a shortcut to find the binary strings directly without finding descriptors, other than SIFT and SURF which require descriptors and takes a lot of memory.

But BRIEF doesn't provide feature detectors for that you can use SIFT or SURF, but it is recommended to use CesnSurE as it works slightly better.
* [BRIEF (Binary Robust Independent Elementary Features)](05_BRIEF.py)
# ORB
An efficient alternative to SIFT or SURF. SIFT and SURF are patented and you are supposed to pay them for its use. But ORB is not !!!
* [ORB (Oriented FAST and Rotated BRIEF)](06_ORB.py)
# Feature Matching
Will see how to match features in one image with others.
We will use the Brute-Force matcher and FLANN Matcher in OpenCV
* [Feature Matching](07_FeatureMatching.py)
# 
