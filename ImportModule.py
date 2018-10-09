#!/usr/bin/python

#	============================================================
#	Purpose: To import a module and its method by using 
#	variable names.
#	------------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	9.10.2018
#	============================================================

'''	The follwoing approaches are equivalent of 
	----------------------------------------------------------------------
	from MyModule import div as method
	----------------------------------------------------------------------
'''
from importlib import import_module
module = 'MyModule' 
method = 'div'

#	1st Approach [generally encouraged]
x = import_module(module)
y = getattr(x, method)
z = y()
print(z)

#	2nd Approach [generally discouraged]
x = __import__(module, globals(), locals(), [method], 0)
y = getattr(x, method)
z = y()
print(z)



