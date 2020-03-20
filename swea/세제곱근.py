import sys
sys.stdin = open("세제곱근.txt")

arr = [i**3 for i in range(1000001)]
for tc in range(int(input())):
    N = int(input())

    l, r = 1, 1000000
    rst = -1
    while l <= r:
        c = (l+r)//2
        if arr[c] == N:
            rst = c
            break
        if arr[c] < N:
            l = c + 1
        else:
            r = c - 1

    print("#{} {}".format(tc+1, rst))