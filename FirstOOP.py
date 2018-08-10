#!/usr/bin/python3

#	========================================================
#	Purpose: to understand how to do Object-Oriented
#	Programming in Python.
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	10.8.2018
#	========================================================

class Book:
	#	Class Variable
	'''	A class variable is shared by all objects of 
		this class. Therefore, if one object modify this
		value, other objects can see the modified value.'''
	noOfBooks = 0

	#	----------------------------------------------------
	#	Instance Methods
	'''	-------------------
		An instance method is bound to an object. Its first
		parameter is always the pointer of an object. It
		acts like 'this' pointer of C++. It is conventionally 
		named as 'self'. It is usually passed hiddenly, but 
		it needs to be received explicitly. On the other
		hand 'this' parameter in C++ does not need to be 
		received explicitly.'''
	#	----------------------------------------------------

	#	Constructor
	''' Constructor method is automatically called when an
	object is created in order to initializing instance 
	variables.'''
	def __init__(self, title = 'xxx'):
		print('Constructor is being called for "{}"'.format(title))
		self.title = title
		self.author = 'yyy'
		self.year = 1600
		self.price = '0 USD'
		Book.noOfBooks += 1
		self.ID = Book.noOfBooks

	#	Destructor
	''' Destructor method is automatically called for each
		object when the program is terminated. It is called
		in FCFD (First Created First Destroyed) order. '''
	def __del__(self):
		print('Book-{} was deleted.'.format(self.ID))
		Book.noOfBooks -= 1
		print('Number of Remaining Books: {}'.format(Book.noOfBooks))

	#	Regular Methods
	def modifyBookInfo(self):
		self.title = input('Title of Book: ')
		print('Who is the author of this book: ', end = '')
		self.author = input()
		print('In which year, this book was published: ', end = '')
		self.year = input()
		print('What is the price of this book: ', end = '')
		self.price = input()

	def getSpecificBookInfo(self):
		print('ID: {}'.format(self.ID))
		print('Title: {}'.format(self.title))
		print('Author: {}'.format(self.author))		
		print('Publishing Year: {}'.format(self.year))
		print('Price: {}'.format(self.price))		

#	Objects
firstBook = Book()

'''	Class variable can be accessed either by an object's
	name or by the Class' name.'''
print('Number of Available Books: {}'.format(firstBook.noOfBooks))
print('Number of Available Books: {}'.format(Book.noOfBooks))

secondBook = Book('Linux System Programming: Talking Directly to the Kernel and C Library')
print('Number of Available Books: {}'.format(Book.noOfBooks))

thirdBook = Book('Operating System Concepts')
print('Number of Available Books: {}'.format(Book.noOfBooks))

print('----------------------------------------')
print(" Book's information before modification ")
print('----------------------------------------')
firstBook.getSpecificBookInfo()

firstBook.modifyBookInfo()

print('----------------------------------------')
print(" Book's information after modification ")
print('----------------------------------------')
firstBook.getSpecificBookInfo()

print('-----------------------------')
print(' Destructor is being called ')
print('-----------------------------')
