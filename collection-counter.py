from collections import *
n = int(input())
size = list(map(int,input().split()))
si = Counter(size)
sum = 0
m = int(input())
for i in range(m):
    l = list(map(int,input().split()))
    if si[l[0]] >= 1:
        sum += l[1]
        si[l[0]] -= 1
print(sum)