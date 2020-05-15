def perm(n,k,sum):
    global result
    # 가지치기
    if k != n:
        if sum > result:
            return
    if k == n:
        # 최소생산비용
        if sum < result:
            result = sum
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1,sum+V[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open("최소생산비용.txt")

for tc in range(int(input())):
    N =int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    result = 999999

    perm(N,0,0)
    print("#{} {}".format(tc+1,result))