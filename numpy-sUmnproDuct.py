import numpy
n = list(map(int,input().split()))
lis = []
for i in range(n[0]):
    m = list(map(int,input().split()))
    lis.append(m)
arr = numpy.array(lis,int)
x = numpy.sum(arr,axis=0)
print(numpy.prod(x,axis=0))
