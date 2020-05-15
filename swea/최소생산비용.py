def perm(n,k):
    global result
    if k != n:
        sum = 0
        for i in range(k):
            sum += V[i][arr[i]]
            if sum > result:
                return
    if k == n:
        sum = 0
        for i in range(N):
            sum += V[i][arr[i]]
        if sum < result:
            result = sum
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open("최소생산비용.txt")

for tc in range(int(input())):
    N =int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    result = 999999

    perm(N,0)
    print("#{} {}".format(tc+1,result))