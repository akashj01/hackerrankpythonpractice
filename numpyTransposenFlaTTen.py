import numpy
n = list(map(int,input().split()))
l =[]
for i in range(n[0]):
    m = list(map(int,input().split()))
    l.append(m)
arr = numpy.array(l,int)
print(arr.transpose())
print(arr.flatten())