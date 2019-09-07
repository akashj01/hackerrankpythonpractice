n,m = map(int,input().split())
print(n,m)
a = (m//2) - 1
b = 1
for i in range(1,(n//2)+1):
    for j in range(a):
        print('-',end='')
    for k in range(b):
        print('.|.',end='')
    for l in range(a):
        print('-',end='')
    print()
    a -= 3
    b += 2
string = 'WELCOME'
print(string.center(m,'-'))
a = a +3
b = b - 2
for i in range(1,(n//2)+1):
    for j in range(a):
        print('-',end='')
    for k in range(b):
        print('.|.',end='')
    for l in range(a):
        print('-',end='')
    print()
    a += 3
    b -= 2
