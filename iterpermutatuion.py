from itertools import *
n = list(map(str,input().split()))
lis = list(permutations(n[0],int(n[1])))

f = []
for j in lis:
    exp = list(j)
    st = ''.join(exp)
    f.append(st)
f.sort()
x = 0
for i in f:
    x += 1
    print(i,end='')
    if x != len(f):
        print('')