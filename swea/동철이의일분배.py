def perm(n,k):
    global result
    #가지치기
    if k!=n:
        mul = 1
        for i in range(k):
            mul *= (data[i][arr[i]]*0.01)
        if mul*100 <= result:
            return
    if k == n:
        mul = 1
        for i in range(N):
            mul *= (data[i][arr[i]]*0.01)
        if mul*100 > result:
            result = mul*100
    else:
        for i in range(k,n):
            if data[i] == 0:
                return
            else:
                arr[k], arr[i] = arr[i], arr[k]
                perm(n,k+1)
                arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open("동철이의일분배.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    #data의 index 교환을 위한 번호들
    arr = list(range(N))
    result = -999

    perm(N,0)

    print("#{} {:.6f}".format(tc+1, result))