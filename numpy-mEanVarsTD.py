import numpy

numpy.set_printoptions(sign=' ')
n = list(map(int,input().split()))

lis = []
for i in range(n[0]):
    m = list(map(int,input().split()))
    lis.append(m)
arr = numpy.array(lis,int)
mean = numpy.mean(arr,axis=1)
print(mean)
var = numpy.var(arr,axis=0)
print(var)
print(numpy.around( numpy.std(arr), 12))
