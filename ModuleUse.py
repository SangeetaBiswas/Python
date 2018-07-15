#!/usr/bin/python

#	Purpose: To learn how to use modules by following 
#	"A Byte of Python" by Swaroop C H. available on
#	https://python.swaroopch.com/
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	30.6.2018
#	--------------------------------------------------------

import sys	#	Built-in Module 
import os	#	Built-in Module
import MyModule as mm	#	User-defined module. When
						#	module has a long name, we
						#	can give short name for our
						#	convenience.

__version__ = 'v1.1'

#	The following two print() statements will
#	print the same information
print('Name of this module: {}'.format(__name__))	

#	It is better to use module's name with its objects
#	in order to avoid confusion with objects of other
#	modules having the same name.
print('Version of this program: {}'.format(__version__))
print('Version of MyModule: {}'.format(mm.__version__))
print('Version of sys module: {}'.format(sys.version))

#	We can get Program's name via sys module as we get
#	from CLI in C. But we cannot get argc.
print('Name of this program: {}'.format(sys.argv[0]))
print('No. of CLI arguments: {}'.format(len(sys.argv)))	

#	Module 'os' has interesting usage specially when
#	we need to deal with multiple files with different
#	naming styles. 
#	os.walk() returns dirPath, subdirs and filenames.
dirName = '/home/sangeeta/Programming/TensorFlow/ADCIS/exudates'
for dirPath, subDir, imgFileList in os.walk(dirName):
	print(dirPath)
	print(subDir)
	for imgFileName in imgFileList:
		print(imgFileName)

#	Usage of user-defined module 
#	(i.e., my module named MyModule)
print('a + b: {}'.format(mm.add()))
print('a - b: {}'.format(mm.sub()))
print('a * b: {}'.format(mm.mul()))
print('a / b: {}'.format(mm.div()))
