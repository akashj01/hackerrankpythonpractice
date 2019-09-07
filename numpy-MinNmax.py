import numpy
n = list(map(int,input().split()))
lis = []
for i in range(n[0]):
    m = list(map(int,input().split()))
    lis.append(m)
arr = numpy.array(lis,int)
min = numpy.min(arr,axis=1)
print(numpy.max(min,axis=0))

