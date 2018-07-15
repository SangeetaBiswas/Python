#!/usr/bin/python3

#	Purpose: To learn syntex used in Python by following 
#	"A Byte of Python" available on
#	https://python.swaroopch.com/
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	29.6.2018
#	--------------------------------------------------------

#	In Python, it is possible to write multiple 
#	logical statements in one line by separating them
#	using ;. However, it is highly discouraged to do 
#	that. 
str1 = 'Hello'; str2 = 'World'	# Not a good style	

#	How to use strings in Python
#	----------------------------------------------------------
#	1.	All the following print statements will do 
#		the same thing.
#	2.	By using \, it is possible to write one logical 
#		statements into multiple lines.
#	----------------------------------------------------------	
print('Hello, World')
print("Hello, World")
print('Hello, \
World')
print("Hel\
lo, \
Wor\
ld")
str3 = str1 + ', ' + str2
print(str3)
print('{0}, {1}'.format(str1,str2))
print('{}, {}'.format(str1,str2))
print('{0}{comma}{str4}'.format(str1,comma = ', ',str4 = 'World'))
print('{0}{comma}{str4}'.format(str1,\
		comma = ', ',\
		str4 = 'World')\
	)
print('{0}{comma}{str4}'.format(str1,
		comma = ', ',
		str4 = 'World')
	)

print("Hello,", str2)	

#	By default, print() adds \n at the end of string.
#	Favourite characters can be added by discarding 
#	'\n' at the end by using 'end ='.
#	'end =' is not supported in version 2.x.y.
print("Hello,", end = '')	#	'\n' will be discarded but 
							#	no character will be added.
print("world")
print("Hello,", end = ' ')	#	'\n' will be discarded and 
							#	a blank space will be added.
print("world")

#	Usage of Variables
#	--------------------------------------------------------
#	A blank space will be added before num1 in version 3.x.y.
#	In 2.x.y, output will inside in parenthesis.
#	e.g., 
#	In Python 2.7.12	---->	The first number is 23	
#	In Python 3.5.2	----> ('The first number is ', 23) 
#	--------------------------------------------------------

num1 = 55
num2 = 7
print('The first number is ', num1)
print('num1 / num2 = ', num1 / num2)
print('(num1) / num2 [with flooring] = ', num1 // num2)
print('(num1) ^ num2 = ', num1 ** num2)

#	Input-Output
#	-------------------------------------------------------
#	In Python 2.x.y, raw_input() is used for taking
#	input from the user. In Python 3.x.y, input() is used.
#	-------------------------------------------------------
print('What is your current rent?: ', end = '')
num1 = int(input())
num2 = int(input('What was your previos rent?: '))
print("Your current rent is {}.".format(num1))
print("Your previous rent was {}.".format(num2))

#	if--else
#	-------------------------------------------------------
#	Python does not use curly brackets for blocking,
#	instead it uses indentation. It is necessary to be
#	careful using indentation. Four blank spaces are 
#	officially recommended for one block. 
#	-------------------------------------------------------	
print("Suggestion:")
if num1 > num2:
	print("\tYour current rent is higher than your previous rent.")
	print("\tIt is better for you to reduce your expenses for entertainment.")	
	print("\tOtherwise you will be in debt.")
elif num1 == num2:
	print('''\thmm...
\tNot bad.
\tYou do not need to be worried about your expenses.''')
else:
	print('\tWoW!!! Great!!!')
	print('\tNow you can save some money, ', end = '')
	print('since your current rent is lower than the previous one.')

#	Loop
#	-------------------------------------------------------
#	1.	for..in statement is iterates over a sequence of 
#		objects
#	2.	A while statement can have an optional else clause.
#	-------------------------------------------------------
for i in range(8):
	j = 0
	while j < i:
		print('{}.{}. {}'.format(i, j, 'Bangladesh'))
		j += 1
	else:
		print('{}. {}'.format(i, 'Rajshahi'))
	print('{}. {}'.format(i, 'CSE, RU'))	

#	Function
#	-------------------------------------------------------
#	1.	Any function should be defined before calling.
#	2.	In order to use a global variable, 'global'
#		needs to be write in front of a variable inside
#		a function. Otherwise, all variables inside a
#		a function will be considered as local variables.
#	3.	A function can return multiple values, which is
#		different from C/C++.
#	-------------------------------------------------------
def addition():
	a, b = readTwoNumbers()
	add = a + b
	return add

def subtraction(a, b):
	global sub
	c = int(input('How much do you want to shift: '))
	sub = a - b << c	

def readTwoNumbers():
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	return int(x),int(y)

add = 0; sub = 0	#	Putting multiple logical statements
					#	in a single line is not a good style.
print('sum [Before calling addition()] = {}'.format(add))
print('sub [Before calling subtraction()] = {}'.format(sub))
addition()
subtraction(5, 4)
result = add + sub
print('sum [After calling addition()] = {}'.format(add))
print('sub [After calling subtraction()] = {}'.format(sub))
