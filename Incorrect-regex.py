# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    try :
        s = re.compile(input())
        print('True')
    except re.error:
        print('False')
