n = list(map(int,input().split()))
lis = []
for i in range(n[1]):
    m = list(map(float,input().split()))
    lis.append(m)
X = [lis[0]]
for i in range(1,n[1]):
    X = X + [lis[i]]
for i in zip(*X):
    print(sum(i)/n[1])
