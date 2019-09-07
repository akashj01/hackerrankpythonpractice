# The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.
#
# linalg.det
#
# The linalg.det tool computes the determinant of an array.
#
# print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
# linalg.eig
#
# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
#
# vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
# print vals                                      #Output : [ 3. -1.]
# print vecs                                      #Output : [[ 0.70710678 -0.70710678]
#                                                 #          [ 0.70710678  0.70710678]]
# linalg.inv
#
# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
#
# print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
#                                                 #          [ 0.66666667 -0.33333333]]
# Other routines can be found here


import numpy
numpy.set_printoptions(sign=' ')
n = int(input())
lis = []
for i in range(n):
    m = list(map(float,input().split()))
    lis.append(m)
arr = numpy.array(lis,float)
print('%.2f'%numpy.linalg.det(arr))
