from itertools import *
n = list(map(str,input().split()))
lis = list(combinations_with_replacement(n[0],int(n[1])))
print(lis)
f = []
for j in lis:
    exp = list(j)
    exp.sort()
    st = ''.join(exp)
    f.append(st)
f.sort()
x = 0
for i in f:
    x += 1
    print(i,end='')
    if x != len(f):
        print('')