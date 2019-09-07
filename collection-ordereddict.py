
from collections import OrderedDict

n = int(input())
qu = []
ordinary_dictionary = OrderedDict()
for i in range(n):
    lis =list(map(str,input().split()))
    x = ''
    for j in range(len(lis)-1):
        x += lis[j]
        if j != len(lis)-2:
            x += ' '
    qu.append([x,int(lis[len(lis)-1])])
    ordinary_dictionary[x] = int(lis[len(lis)-1])

print(ordinary_dictionary)
for i,j in ordinary_dictionary.items():
    y = qu.count([i,j])
    print(i,j*y)
