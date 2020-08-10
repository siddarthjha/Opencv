import numpy as np
import cv2

img = cv2.imread('a.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

