from collections import *
d = deque()
for i in range(int(input())):
    com = list(map(str,input().split()))
    if com[0] == 'append':
        d.append(int(com[1]))
    if com[0] == 'appendleft':
        d.appendleft(int(com[1]))
    if com[0] == 'pop':
        d.pop()
    if com[0] == 'popleft':
        d.popleft()
for i in range(len(d)):
    print('{} '.format(d[i]),end='')
#    print(d[i],end='')
#    if i != len(d)-1:
#       print(' ')
