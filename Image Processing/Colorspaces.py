import numpy as np
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# There 150 color spaced conversions in opencv
print(flags)

# For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. 
img = cv2.imread('a.jpg')
cv2.namedWindow('pic', cv2.WINDOW_NORMAL)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Hue Saturation Value
cv2.imshow('pic', img)
cv2.waitKey(0)
cv2.destroyWindow('pic')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
