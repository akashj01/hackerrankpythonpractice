from collections import *
final = []
for i in range(int(input())):
    m = int(input())
    lis = deque(map(int,input().split()))
    x = 1
    for j in range(m):
        if lis[0] >= lis[-1]:
            st = lis.popleft()
        else:
            st = lis.pop()
        if j != 0:
            if pt >= st:
                pass
            else:
                x = 0
                break
        pt = st
    final.append(x)
for i in final:
    if i == 1:
        print('Yes')
    if i == 0:
        print('No')