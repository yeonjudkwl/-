import sys
sys.stdin = open("비트연산.txt")

arr = input()

for i in range(0, len(arr), 7):
    res = 0
    for j in range(i, i+7):
        res = res * 2 + int(arr[j])
    print(res, end=' ')