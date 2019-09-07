n = int(input())
List = []
for i in range(n):
    name = input()
    score = float(input())
    List.append([name,score])
min = 100
for i in range(len(List)):
    if min > List[i][1]:
        min = List[i][1]
minn = []
for i in range(len(List)):
    if min == List[i][1]:
        minn.append(List[i][0])

for i in range(len(minn)):
        List.remove([minn[i],min])
min = 100
for i in range(len(List)):
    if min > List[i][1]:
        min = List[i][1]
        minn = List[i][0]
name = []
for i in range(len(List)):
    if min == List[i][1]:
        name.append(List[i][0])

name.sort()
for i in name:
    print(i)



