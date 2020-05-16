def dfs(n, k, energy, cnt):  # N, 정류장번호, 남은용량, 교체횟수
    global min

    if cnt > min:
        return

    # 종점에 도착한 경우
    if k == n:
        if min > cnt: min = cnt
    else:
        # 교체하지 않고 통과
        if energy > 0:
            dfs(n, k + 1, energy - 1, cnt)
        # 교체하고 통과
        dfs(n, k + 1, arr[k] - 1, cnt + 1)

import sys
sys.stdin = open('전기버스2.txt')
T = int(input())

for tc in range(1, T+1):          
    arr = list(map(int, input().split()))       # 정류장 수, 충전지 용
    min = 987654321
    dfs(arr[0], 2, arr[1]-1, 0)                 # 2번 정류장일 때 1번 정류장에서 충전량에서 -1 함
    print('#{} {}'.format(tc, min))

