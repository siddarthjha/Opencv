import numpy as np
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# There 150 color spaced conversions in opencv
print(flags)

