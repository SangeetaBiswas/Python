#!/home/sangeeta/Tensorflow/bin/python

#	========================================================
#	Purpose: To understand how os.walk() works.
#	--------------------------------------------------------
#	os.walk() generates a 3-tuple 
#	(dirpath, dirnames, filenames) by walking directory 
#	tree either top-down or bottom-up way. 	
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	4.7.2018
#	========================================================

#	Import modules
import os
import numpy as np

#	A loop is necessary to get a list of all image files.
imgDir = "/home/sangeeta/Programming/TensorFlow/STARE/all-images/"
for dirPath, subDir, imgList in os.walk(imgDir):
	imgList

#	It is not possible to add a specific string with each 
#	element of a normal python list. We can do it if we 
#	convert it into a NumPy array. 
imgFileNames = np.array(imgList)
imgFileNames = np.core.defchararray.add(dirPath, imgFileNames)	
for imgFile in imgFileNames:
	print(imgFile)
