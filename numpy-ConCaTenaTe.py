import numpy
n = list(map(int,input().split()))
l = []
for i in range(n[0]):
    m = list(map(int,input().split()))
    l.append(m)
arr1 = numpy.array(l,int)
l.clear()
for i in range(n[1]):
    m = list(map(int,input().split()))
    l.append(m)
arr2 = numpy.array(l,int)
print(numpy.concatenate((arr1,arr2),axis=0))
