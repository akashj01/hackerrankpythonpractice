# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set(map(int,input().split()))
n = int(input())
k = 0
print(s)
for i in range(n):
    si = set(map(int,input().split()))
    print(s.issuperset(si))
    if not s.issuperset(si):
        k = k+1
print(k)
if k > 0:
    print('False')
else:
    print('True')