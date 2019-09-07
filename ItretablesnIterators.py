from itertools import *
n = list(range(1,int(input())+1))
lis = list(map(str,input().split()))
m = int(input())
com = list(combinations(n,m))
num = len(com)
a =[]
for i in range(1,len(lis)+1):
    if lis[i-1] == 'a':
        a.append(int(i))
sum = 0
for j in com:
    for i in range(len(a)):
        if a[i] in j:
            sum += 1
            break
print(sum/num)








