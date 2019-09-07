from collections import *
ord = defaultdict(lambda : 0)
for i in range(int(input())):
    x = input()
    ord[x] += 1
print(len(ord))
for i,j in ord.items():
    print('{} '.format(j),end='')




