from calendar import *
date = list(map(int,input().split()))
x = weekday(date[2],date[0],date[1])
if x == 0:
    print('MONDAY',end='')
elif x == 1:
    print('TUESDAY',end='')
elif x ==2:
    print('WEDNESDAY',end='')
elif x == 3:
    print('THURSDAY',end='')
elif x == 4:
    print('FRIDAY',end='')
elif x == 5:
    print('SATURDAY',end='')
else:
    print('SUNDAY',end='')