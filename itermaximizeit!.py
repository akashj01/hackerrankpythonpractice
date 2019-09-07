from itertools import *
from itertools import product

n = list(map(int,input().split()))
arr = []
for i in range(n[0]):
    l = list(map(int,input().split()))
    for j in range(1,len(l)):
        l[j] = l[j]**2
    arr.append(l[1:])
sum_max = 0
for i in product(*arr):
    su = sum(j for j in i) % n[1]
    if su > sum_max:
        sum_max = su
print(sum_max)
