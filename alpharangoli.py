def print_rangoli(size):
    a = ((4*size)-3)//2
    b = ord('a')+size - 1

    for i in range(1,size+1):
        for j in range(a):
            print('-',end='')

        for k in range(i-1):
            print(chr(b),end='')
            print('-',end='')
            b = b-1
        print(chr(b),end='')
        for k in range(i-1):
            b = b+1
            print('-',end='')
            print(chr(b),end='')
        for j in range(a):
            print('-',end='')
        print('')
        a = a-2

    a = a+4
    for i in range(size,1,-1):
        for j in range(a):
            print('-',end='')

        for k in range(i-1,1,-1):
            print(chr(b),end='')
            print('-',end='')
            b = b-1
        print(chr(b),end='')
        for k in range(i-1,1,-1):
            b = b+1
            print('-',end='')
            print(chr(b),end='')
        for j in range(a):
            print('-',end='')
        print('')
        a = a+2


    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)