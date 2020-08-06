import cv2
import numpy as np

# Drawing different shapes

img = np.zeros((512, 512, 3), np.uint8)
# ------------LINE---------------
img = cv2.line(img, (100,100), (100, 300), (0, 0, 255), 5)
img = cv2.line(img, (300,100), (300, 300), (0, 0, 255), 5)
# This function creates the line - (1-the image, 2-Starting coordinates, 3-Ending cordinates, 4-Color of the shape(BGR), 5-Thickness)
cv2.imshow('image', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('image')
# ----------MULTIPLE LINES---------	
img = np.zeros((512, 512, 3), np.uint8)
pts = np.array([[25, 70], [25, 160], [110, 200], [200, 160], [200, 70], [110, 20]], np.int32) 	
pts = pts.reshape((-1, 1, 2)) # UNKNOWN ROWS 1 COLUMN 2 SUB-ELEMENTS.
img = cv2.polyline(img, [pts], True, (0, 0, 255), 5)
cv2.imshow('image', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('image')

# --------------RECTANGLE------------------
img = cv2.rectangle(img, (100, 100), (400, 400), (0, 0, 255), 5)
# This function creates the rectangle - (1-The image, 2-Top left corner, 3-Bottom right corner, 4-Color of the shape(BGR), 5-Thickness)
cv2.imshow('frame', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('frame')
	
# --------------CIRCLE---------------------
img = cv2.circle(img, (250, 250), 70, (0, 0, 255), 5)
# This function created the circle -(1-The image, 2-The center coordinates, 3-Radius of circle, 4-Color of the shape(BGR), 5-Thickness)
cv2.imshow('frame', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('frame')

# -------------ELLIPSE--------------------
img = np.zeros((512, 512, 3), np.uint8)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# Thiis function creates the ellipse -(1-The image, 2-The center coordinates, 3-Axes length(major axis, minor axis), 4-Angle of rotation of
# ellipse in anticlockwise, 5-startAngle and endAngle starting and ending of ellipse arc in clockwise)
cv2.imshow('frame', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('frame')
	
# -------------POLYGON-----------------
img = np.zeros((512, 512, 3), np.uint8)
pt  = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  
# This function creates the nd array with the given data type(optional)
pt  = pt.reshape(-1, 1, 2)
# This function reshapes the nd array in given rows and columns
img = cv2.polylines(img, [pt], True, (0, 0, 255), 3)
# This function creates the polygon -(1-The image, 2-Coordinates of vertices, 3-True means it will be a closed polygon, 4-Color of the shape(BGR)
# The coordinates of the vertices must be 1*2 matrix only so we must reshape it into 1*2) 
cv2.imshow('frame', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('frame')
	
# --------------TEXT ON IMAGE-----------------
img = np.zeros((512, 512, 3), np.uint8)
font= cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Siddarth', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
# This function enables to write text on image -(1-The image, 2-The text, 3-Position coordinate, 4-Font type, 5-Font scale, 6-Color, 7-Thickness, 8-Line type)
cv2.imshow('frame', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyWindow('frame')


