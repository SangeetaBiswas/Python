#!/usr/bin/python

#	========================================================
#	Purpose: To understand how different sequences work
#	in Python mainly following:
#		A Byte of Python by Swaroop C H 
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	7.7.2018
#	========================================================

import operator as opt
import random

#	========================================================
#	1.	LIST
#		A list is holds an ordered collection of items like
#		a dynamic array. It's a mutable data type, therefore, 
#		it's size and elements can be altered.
#	========================================================
fruitList = ['Mango', 'Lichi', 'Apple', 'Blue Berry', 'Orange']
fishList = ['Ilish', 'Salmon', 'Trout', 'EEL']

ffList = fruitList + fishList
print('fruits: {}\nfish: {}'.format(fruitList, fishList))
print('fruits + fish: {}'.format(ffList))
 
#	To access a specific item by an index.
oneFruit1 = fruitList[0]	#	Like a 1D array of C
oneFruit2 = opt.getitem(fruitList, 2)
oneFruit3 = fruitList[-1]	#	To access from the last
print(oneFruit1,oneFruit2,oneFruit3) 

#	To access a specific set of items.
list1 = opt.itemgetter(2,0)(fruitList)
index1 = [1, 4]
list2 = opt.itemgetter(*index1)(fruitList)	#	*indices unpacking 
											#	values of indices list.
index2 = random.sample(range(len(fruitList)), 2)
list3 = opt.itemgetter(*index2)(fruitList)
print('index2: {}'.format(index2))
print(list1, list2, list3)

#	To Add and Delete elements.
fruitList.append('Pine Apple')
del fishList[3]
print('New fruit list: {}'.format(fruitList))
print('New fish list: {}'.format(fishList))

#	To slice a list.
list4 = fruitList[2:]
list5 = fruitList[:-1]
print('fruitList[2:]: {}\nfruitList[:-1]: {}'.format(list4,list5))

#	References
def whatHappens(list1, list2, list3):
	vegList = ['Potato', 'Pumpkin', 'Cabbage', 'Tomato']
	print('List1 (Before): {}'.format(list1))
	list1 = vegList
	print('List1 (After): {}'.format(list1))
	
	#	
	print('List2 (Before): {}'.format(list2))
	list2[2] = 'Parrot'
	list2.append('Crow')
	list2.append('Sparrow')
	print('List2 (After): {}'.format(list2))

	#	Assiging another list to any list
	#	has effect only inside the function.
	print('List3 (Before): {}'.format(list3))
	del list3[1]	# 	list3 and riverList are refering to the 
					#	same object. Therefore, this del operation
					#	will affect the main cityList.
	list3 = vegList[:]	
	del list3[2]	#	Now list3 is copy of vegList. Deletion
					#	operation neither has effect on vegList
					#	nor on cityList.
	print('List3 (After): {}'.format(list3))

riverList = ['Amazon', 'Ganges', 'Nile', 'Mississippi']
birdList = ['Robin', 'Eagle', 'Falcon', 'Kingfisher']
cityList = ['Rajshahi', 'Tokyo', 'Brno', 'Delhi']
print('Rivers (Before): {}'.format(riverList))
print('Birds (Before): {}'.format(birdList))
print('Cities (Before): {}'.format(cityList))
whatHappens(riverList, birdList, cityList)
print('Rivers (After): {}'.format(riverList))
print('Birds (After): {}'.format(birdList))
print('Cities (After): {}'.format(cityList))

#	Multi-types data
dataSet1 = [1,1.5,'a','abc']	#	A list can hold different types of data
								#	which is opposite of C/C++ array.	
print('1 + 1.5: {}'.format(dataSet1[0] + dataSet1[1]))
print('a + 1.5: {}'.format(dataSet1[2] + str(dataSet1[1])))
print('abc + a: {}'.format(dataSet1[3] + dataSet1[2]))

#	Multi-dimensional List
mat2D = [
	[1,2,3],
	['a','b','c']
]
mat3D = [
	[[1,2,3],['a','b','c']],
	[[4,5,6],['x','y','z']],
	[[1.5,2.5,3.5],['ax','by','cz']],
	[['d','e','f'],['ax','by','cz']]
]
print('Mat2D (3-by-3): {}'.format(mat2D))
print('Mat3D (3-by-3-by-4): {}'.format(mat3D))
print('Mat3D[1][1][1]: {}'.format(mat3D[1][1][1]))
mat3D.append(mat2D)
print('Mat3D (3-by-3-by-5): {}'.format(mat3D))
mat3D.append(mat2D)
print('Mat3D (3-by-3-by-6): {}'.format(mat3D))
print('Size of Mat3D: {}'.format(len(mat3D)))

#	========================================================
#	2.	TUPLE
#		Tuples are just like constant strings of C/C++, 
#		i.e., their size and content cannot be modified.
#	========================================================
tuple1 = ('a','b','c','d')
tuple2 = (1,2,3,'d')
print('tuple1: {}\ntuple2: {}'.format(tuple1, tuple2))
print('tuple1 + tuple2: {}'.format(tuple1 + tuple2))

#	'tuple' object does not support item assignment.
#tuple1[1] = 56
#tuple2[3] = 'Aloka'
#print('tuple1: {}\ntuple2: {}'.format(tuple1, tuple2))

#	========================================================
#	3.	DICTIONARY
#		It is like an address book where a value is 
#		associated with a unique key. Therefore, each value
#		can be accessed via that key.
#	========================================================
dic1 = {
	'elem1' : [[1,'abc'],[2.5, 34]],
	'elem2' : 'sangeeta.cse.ru@gmail.com',
	1 : 35,
	2 : 36.57
}
print('Elements of Dictionary: {}, {}'.format(dic1['elem1'], dic1[2]))
#	========================================================
#	4.	SET
#	========================================================
A = {1, 2, 3, 4}
B = {'A', 'B', 'C'}
C = A.union(B)
D = A.intersection(B)
E = A - B
F = A.difference(B)
print('A: {}\nB: {}'.format(A,B))
print('A union B: {}'.format(C))
print('A intersection B: {}'.format(D))
print('A - B: {} or {}'.format(E, F)) 
