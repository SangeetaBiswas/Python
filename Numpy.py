#!/usr/bin/python

#	========================================================
#	Purpose: How to handle multidimensional array using
#	numpy libray. 
#	1.	NumPy is a math library for Python.
#	2.	NumPy Stands for Numrical Python.
#	4.	Some Tutorials:
#	https://www.machinelearningplus.com/python/numpy-tutorial-part1-array-python-examples/
#	https://www.datacamp.com/community/tutorials/python-numpy-tutorial
#	--------------------------------------------------------
#	Sangeeta Biswas
#	Post-Doc Researcher
#	Brno University of Technology, Czech Republic
#	4.7.2018
#	========================================================

import numpy as np

print('Version of Numpy: {}'.format(np.__version__))

#	--------------------------------------------------
#	Comparison between Python list and NumPy array
#	--------------------------------------------------
#	We can see slightly difference when we print
#	normal Python list and NumPy array. There
#	is no comma between two elements in NumPy array.
p_1D = [1, 2, 3, 4, 5]	# Python 1D array is just a list
np_1D = np.array([1, 2, 3, 4, 5])	# Numpy 1D array
print ("p_1D: {}\nnp_1D: {}".format(p_1D, np_1D))

p_2D = [[1, 2, 3],[4, 5, 6]]	# Python 2D array 
np_2D = np.array([[1, 2, 3],[4, 5, 6]])	# Numpy 2D array
print ("p_2D: {}\nnp_2D: {}".format(p_2D, np_2D))
print('1st Column of np_2D: {}'.format(np_2D[:,0]))
print('2nd Row of np_2D: {}'.format(np_2D[1,:]))

#	--------------------------------------------------
#	Some Information about nD NumPy array
#	--------------------------------------------------
n1 = np_1D.shape
print('np_1D is {}'.format(n1))
n1, n2 = np_2D.shape
print('np_2D is {}*{}'.format(n1, n2))
print('Type of np_2D: {}'.format(type(np_2D)))
print('Data Type of np_2D: {}'.format(np_2D.dtype))
print('Size of np_2D: {}'.format(np_2D.size))
print('Dimension of np_2D: {}'.format(np_2D.ndim))

#	--------------------------------------------------
#	Some Operations on Numpy array
#	--------------------------------------------------
#	1.	make evenly spaced array.
#		'stop' will be included in array from 
#		linspace(), but not in arange() 
a = np.arange(1, 16, 2)	# (start, stop, step)
print('a: {}'.format(a))
b = np.linspace(1,5,4)	# (start, stop, no. of elements)
print('b: {}'.format(b))

#	2.	make some special arrays
Z = np.zeros((2,5,4), dtype = 'int32')
print('Zero Matrix: {}'.format(Z))
O = np.ones((2,5,4), dtype = 'int32')
print('One Matrix: {}'.format(O))
I = np.eye(4,4, dtype = 'int32')
print('Identity Matrix: {}'.format(I))
R = np.random.random((4,2,3))
print('Matrix with random elements: {}'.format(R))

#	3.	turn 1D array into nD array
B = a.reshape(4,2)
print('B: {}'.format(B))
C = a.reshape(2, 2, 2)
print('C: {}'.format(C))

#	4. 	perform mathmatical operations on elements 
#		of an array
RAdd_B = B.sum(axis = 0)
CAdd_B = B.sum(axis = 1)
print("Row-wise addition of elements of Matrix-B: {}".format(RAdd_B))
print("Column-wise addition of elements of Matrix-B: {}".format(CAdd_B))
C_2 = np.array(C / 2, dtype = 'float64')
print('C_2: {}'.format(C_2))

#	5.	change data type of an array
#		** int --> str is not possible.
numl = [1, 2, 0]
NumM = np.array(numl)
IntM = NumM.astype('str').astype('float').astype('bool').astype('int')
print('NumM: {}'.format(NumM))
print('IntM: {}'.format(IntM))

#	6.	perform mathematical operations on multiple
#		nD arrays
P = np.array([[1,2],[2,3],[4,5]])
Q = np.array([[1,2],[2,3],[4,5]])
U = P + Q
V = P - Q
W = P * Q
X = P / Q
print('P: {}'.format(P))
print('Q: {}'.format(Q))
print('P + Q: {}'.format(U))
print('P - Q: {}'.format(V))
print('P * Q: {}'.format(W))
print('P / Q: {}'.format(X))

#	7. make an array from other arrays
Y = np.zeros((2,3,2), dtype = 'int')
Y[0,:,:] = P  
Y[1,:,:] = Q 
print('Y: {}'.format(Y))

#	8. expand the dimension of an array
G = np.zeros((2,3,2), dtype = 'int')
print('G: {}, shape: {}'.format(G, G.shape))
G = Y
print('G: {}, shape: {}'.format(G, G.shape))
for i in range(4):
	G = np.expand_dims(G, axis=0)
	print('G: {}, shape: {}'.format(G, G.shape))

#	9. append single axis at a time to an array.
H = np.ones((3,2), dtype = 'int')
J = np.zeros((1,3,2), dtype = 'int')
I = np.zeros((1,3,2), dtype = 'int')
print('I: {}, shape: {}'.format(I, I.shape))
for i in range(4):
	I = np.append(I, J, axis = 0)
	I[i+1,:,:] = H + i
	print('I: {}, shape: {}'.format(I, I.shape))

#	10. concatenate multiple axes to an array
M1 = np.array([[1,2,3],[4,5,6]])
M2 = np.array([[1,1,1],[2,2,2],[3,3,3]])
M3 = np.zeros((4,3))
print('{}{}{}'.format(M1.shape, M2.shape, M3.shape))
M4 = np.concatenate((M1,M2,M3), axis = 0)
print(M4)

#	11. take some sepecific elements from an array.
D1 = np.arange(0,70,2)
indices = np.arange(5, 30, 4)
F1 = np.take(D1,indices)
print('D1: {}'.format(D1))
print('indices: {}'.format(indices))
print('F1: {}'.format(F1))

D2 = np.array([[1,2,3],[1,1,1],[0,0,0],[2,2,2],[4,4,4]])
indices = np.arange(1, 3)
F2 = np.take(D2,indices)
print('D2: {}'.format(D2))
print('indices: {}'.format(indices))
print('F2: {}'.format(F2))

#	12. turn python list to numpy array
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
mat4D = []
for i in range(6):
	mat4D.append(mat3D)
np_mat3D = np.array(mat3D)
np_mat4D = np.array(mat4D)
print('Shape of mat3D: {}'.format(np_mat3D.shape))
print('Shape of mat4D: {}'.format(np_mat4D.shape))

