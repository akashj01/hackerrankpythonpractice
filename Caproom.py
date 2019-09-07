# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
roomno = list(map(int,input().split()))
room = set(roomno)
print(sum(room))
print(sum(roomno))
cap = ((sum(room)*k) - sum(roomno))/(k-1)
print(int(cap))





