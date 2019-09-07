from itertools import *
s = str(input())
x = 0
if len(s) > 1:
    for i in range(len(s)):

        if i != 0:
            if s[i] == s[i-1]:
                x += 1
            if s[i] != s[i-1] :
                l = (x,int(s[i-1]))
                print('{} '.format(l),end='')
                x = 1
            if i == len(s)-1:
                l = (x, int(s[i]))
                print('{} '.format(l),end='')
        if i == 0:
            x += 1
if len(s) == 1:
    l = (1,int(s[0]))
    print(l)




