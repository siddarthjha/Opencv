import numpy as np
import cv2

img = cv2.imread('b.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3) # Edge detection can also do thresholding

lines = cv2.HoughLines(edges,1,np.pi/180,200) # grayscale image, p, theta vlaues, Threshold value
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Hough', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('houghlines3.jpg',img)

# Probabilistic Hough Transform
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('Houg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('houghlines5.jpg',img)
