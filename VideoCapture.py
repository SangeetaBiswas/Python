#!/usr/bin/python

#	=======================================================
#	Purpose: To understand how to get help from OpenCV
#	for image processing in Python.
#	-------------------------------------------------------
#	Taken help from
#	http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
#	---------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	27.7.2018
#	=======================================================

import cv2
import matplotlib.pyplot as plt

#	Capture a frame.
cap = cv2.VideoCapture(0)
_, frame = cap.read()
print(frame.shape)

#	Display captured frame. Using matplotlib library 
#	instead of OpenCV was just for curiosity....
fig = plt.figure(figsize = (20, 20))
fig.canvas.set_window_title('Smile Please!!')
plt.suptitle('Thank you for your smile.', fontsize = 36, weight = 'bold')	
plt.imshow(frame)
plt.show()
