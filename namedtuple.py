from collections import *
n = int(input())
av = 0
l = ','.join(map(str,input().split()))
std = namedtuple('std',l)
for i in range(n):
    lis = map(str,input().split())
    st = std(*lis)
    av += int(st.MARKS)
print(av/n)