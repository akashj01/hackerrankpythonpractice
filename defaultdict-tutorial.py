from collections import *
n = list(map(int,input().split()))
d = defaultdict(list)
lis = []
for i in range(1,n[0]+1):
    x = input()
    d[x].append(i)
for i in range(n[1]):
    y = input()
    lis.append(y)
for i in range(0,n[1]):
    if lis[i] in d:
        for j in d[lis[i]]:
            print('{} '.format(j),end='')
    else:
        print('-1',end='')
    if i != n[1]-1:
        print('')