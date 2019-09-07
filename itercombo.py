# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
n = list(map(str,input().split()))
for i in range(1,int(n[1])+1):
    l = list(combinations(n[0],i))
    h=[]
    for j in l:
        k = list(j)
        k.sort()
        h.append(k)
    h.sort()
    x = 0
    for j in h:
        arr = ''.join(j)
        print(arr,end='')
        x += 1
        if (x != len(l) or i != int(n[1])):
            print('')
