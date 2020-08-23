import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('b.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
