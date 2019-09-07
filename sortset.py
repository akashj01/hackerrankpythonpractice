# Enter your code here. Read input from STDIN. Print output to STDOUT
sn = int(input())
se = list(map(int,input().split()))
print(se)
sett = set(se)
n = int(input())
for i in range(n):
    name,no = input().split()
    ser = list(map(int,input().split()))
    settwo = set(ser)
    if name == 'intersection_update':
        sett.intersection_update(settwo)
    if name == 'update':
        sett.update(settwo)
    if name == 'difference_update':
        sett.difference_update(settwo)
    if name == 'symmetric_difference_update':
        sett.symmetric_difference_update(settwo)
sum =0
for i in sett:
    sum += i

print(sum)