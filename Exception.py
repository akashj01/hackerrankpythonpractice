lis = []
for i in range(int(input())):
    n = list(map(str,input().split()))
    lis.append(n)
for [a,b] in lis:

    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as j:
        print('Error Code:',j)