import numpy as np
import cv2

# Load an color image in grayscale
#  img = cv2.imread('a.jpg', 0)

img = cv2.imread('a.jpg')        # 1. This function is used to read image
cv2.imshow('image', img)         # 2. This function is used to display the image
cv2.waitKey(0)                   # 3. This is keyboard binding function which works based on the value passed and the corresponding key.
cv2.destroyAllWindows()          # 4. This function simply destroys all the windows we created 

# If you want to remove autosize of picture.
# Probably used for large dimension images. 
cv2.namedWindow('Memories', cv2.WINDOW_NORMAL) 
cv2.imshow('Memories', img)
k = cv2.waitKey(0) # Different way to destroy the window
if k == 27:
	cv2.destroyWindow('Memories') 
elif k == ord('s'):
	cv2.imwrite('newfile.jpg', img)  # 5. This function is used to save an image->First parameter name of the file and Second is the image you want to save it
	cv2.destroyWindow('Memories') 
