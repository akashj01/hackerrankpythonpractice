def average(array):
    s = set(array)

    sum = 0
    for i in s:
        sum += i
    return  sum/len(s)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)