def perm(n, k):
    global minS
    # 해당 경로의 배터리 합 구하기
    if k == n:
        # idx 순열의 사본
        my_idx = idx[:]
        # 시작점에 사무실 넣기
        my_idx.insert(0, 0)
        # 도착점에 사무실 넣기
        my_idx.append(0)
        # 합 구하기
        my_sum = 0
        for j in range(len(my_idx)-1):
            my_sum += data[my_idx[j]][my_idx[j+1]]
        if my_sum < minS:
            minS = my_sum
    else:
        # 순열
        for i in range(k, n):
            idx[k], idx[i] = idx[i], idx[k]
            perm(n, k+1)
            idx[k], idx[i] = idx[i], idx[k]

import sys
sys.stdin = open("전자카트.txt")

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    minS = 999999
    # 사무실 위치 제외한 idx
    idx = [i for i in range(1, N)]

    print("#{}".format(tc+1), end=' ')
    # 사무실 위치 제외한 후 순열 구하기
    perm(N-1, 0)
    print(minS)