x,k = map(int,input().split())
s = input().replace('x',str(x))
if eval(s) == k:
    print('True')
else:
    print('False')

    # use of eval() Function is main in this proBlem

