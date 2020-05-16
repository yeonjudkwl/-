def backtrack(idx, remain, cnt):
    global N, min_cnt, stops
    # 다음 정류장 도착할 때 배터리 감소
    remain -= 1
    if idx == N:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    # 가지치기
    if cnt > min_cnt:
        return
    # 배터리 교환
    backtrack(idx+1, stops[idx], cnt+1)
    # 배터리 교환 x
    if remain > 0:
        backtrack(idx+1, remain, cnt)

import sys
sys.stdin = open("전기버스2.txt")

for tc in range(int(input())):
    stops = list(map(int, input().split()))
    # 정류장 개수
    N = stops[0]
    min_cnt = 999

    backtrack(2, stops[1], 0)

    print("#{} {}".format(tc+1, min_cnt))