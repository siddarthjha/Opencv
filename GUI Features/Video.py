import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)                                     # This function enables the camera and capture the video 


if cap.isOpened() == False:
	print('Error')

while cap.isOpened():
	 # Capture frame-by-frame
	ret, frame = cap.read()                               # This function reads the captured video frame by frame and returns boolean value
	
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # This function converts the color video into gray
	cv2.imshow('frame', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()                                                 # This function releases the camera
cv2.destroyAllWindows()
