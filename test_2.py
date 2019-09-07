def print_formatted(number):
    for i in range(1, number + 1):
        a = str(i)
        print(a.rjust(6), end='')

        a = oct(i)
        l = list(a)

        l.remove(l[0])
        l.remove(l[0])
        a = ''.join(l)
        print(a.rjust(6), end='')
        a = hex(i)
        l = list(a)


        l.remove(l[0])
        l.remove(l[0])
        a = ''.join(l)
        a = a.upper()
        print(a.rjust(6), end='')
        a = bin(i)
        l = list(a)

        l.remove(l[0])
        l.remove(l[0])
        a = ''.join(l)
        if i < number:
            l = list(a)
            l.append(' ')
            a = ''.join(l)
            print(a.rjust(7), end='')
        elif i == number:
            print(a.rjust(6),end='')
        if i < (number):
         print('')

    # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

