import cv2
import numpy as np
import math

# ----------- OPENCV LOGO ---------------
r1 = 70                                            # Radius for the red, green, blue circle
r2 = 30                                            # Radius for the black circle in red, green, blue circles

ang = 60

d = 70
h = int(d/2*math.sqrt(3))

dot_red = (256, 128)                               # Center coordinates for red circle

dot_green = (dot_red[0]-d//2, dot_red[1]+h)        # Center coordinates for green circle
dot_blue = (dot_red[0]+d//2, dot_red[1]+h)         # Center coordinates for blue circle

red   = (0, 0, 255)
blue  = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

full = -1                                          # Thickness

img = np.zeros((512, 512, 3), np.uint8)
cv2.circle(img, dot_red, r1, red, full)
cv2.circle(img, dot_green, r1, green, full)
cv2.circle(img, dot_blue, r1, blue, full)
cv2.circle(img, dot_red, r2, black, full)
cv2.circle(img, dot_green, r2, black, full)
cv2.circle(img, dot_blue, r2, black, full)

cv2.ellipse(img, dot_red, (r1, r1), ang, 0, ang, black, full)
cv2.ellipse(img, dot_green, (r1, r1), 360-ang, 0, ang, black, full)
cv2.ellipse(img, dot_blue, (r1, r1), 360-2*ang, ang, 0, black, full)

cv2.imwrite("opencv_logo.png", img)

cv2.imshow('frame', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()


