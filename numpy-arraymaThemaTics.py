import numpy
n = list(map(int,input().split()))
lis = []
for j in range(n[0]):
    inp = list(map(int,input().split()))
    lis.append(inp)
arr1 = numpy.array(lis,int)
lis.clear()
for j in range(n[0]):
    inp = list(map(int,input().split()))
    lis.append(inp)
arr2 = numpy.array(lis,int)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)
