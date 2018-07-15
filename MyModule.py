#	Purpose: To learn how to create a user-defined module
#	by following 
#	"A Byte of Python" --- Swaroop C H available on
#	https://python.swaroopch.com/
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	30.6.2018
#	--------------------------------------------------------

__name__ = 'MyModule'
__version__ = '1.1'

def readInput():
	a = int(input('a: '))
	b = int(input('b: '))
	return a,b

def add():
	a, b = readInput()
	result = a + b
	return result

def sub():
	a, b = readInput()
	result = a - b
	return result

def mul():
	a, b = readInput()
	result = a * b
	return result

def div():
	a, b = readInput()
	result = a / b
	return result
