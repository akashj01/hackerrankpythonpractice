import numpy
numpy.set_printoptions(sign=' ')
n = int(input())
lis = []
for i in range(n):
    m = list(map(int,input().split()))
    lis.append(m)
arr1 = numpy.matrix(lis,int)
lis.clear()
for i in range(n):
    m = list(map(int,input().split()))
    lis.append(m)
arr2 = numpy.matrix(lis,int)
print(arr1*arr2)
# or we can do dot product of two arrays to get multiplication of two array
# print(numpy.dot(arr1,arr2))



