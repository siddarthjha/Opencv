import cv2
import numpy as np
from matplotlib import pyplot as plt

# TO CAPTURE VIDEO FROM CAMERA

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)                                     # This function enables the camera and capture the video 
# if using third party camera then use 1 instead of 0

if cap.isOpened() == False:
	print('Error')
	cap.open()                                            # To open the camera if not opened

while cap.isOpened():
	# Capture frame-by-frame
	ret, frame = cap.read()                               # This function reads the captured video frame by frame and returns boolean value
	
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # This function converts the color video into gray
	cv2.imshow('frame', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()                                                 # This function releases the camera
cv2.destroyAllWindows()

# TO PLAY THE EXISTING VIDEO FILE
cap = cv2.VideoCapture('video.mkv')

while cap.isOpened():
	ret, frame = cap.read()
	cv2.imshow('video', frame)
	if cv2.waitKey(1) & oxFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

# TO SAVE/WRITE THE VIDEO
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)     
if cap.isOpened() == False:
	print('Error')
	cap.open()
fourcc = cv2.VideoWriter_fourcc(*'DIVX')                      # DIVX IS FOR WINDOWS
# * FOURCC = Four character code - is a sequence of bytes used to uniquely identify data formats

width = int(cap.get(3))                                                      # It returns the width
height = int(cap.get(4))                                                     # It returns the height   Default value = (640*480) width*height

out = cv2.VideoWriter('video_write.mkv', fourcc, 20, (width, height))        # This function (parameter-Video Name, fourcc code, frames per sec, (width and height))     

while cap.isOpened():
	ret, frame = cap.read()      
	out.write(frame)   
	cv2.imshow('frame', frame)
	if cv2.waitKey(10) & 0xFF == 27:
		break
cap.release()       
out.release()               
cv2.destroyAllWindows()

