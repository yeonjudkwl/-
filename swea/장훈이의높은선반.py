def powerset(n, k, sum):
    #k개까지 안갔는데 직원의 합이 이미 rst에 있는 값보다 크면 종료(나중에 최소값 찾을꺼니까 미리 가지치기)
    if len(rst) != 0 and sum > rst[-1]:
        return
    if n == k:
        #직원의 키를 합한 값이 B이상이면 append
        if sum >= B:
            rst.append(sum)
    else:
        check[k] = 1
        powerset(n, k+1, sum + H[k])
        check[k] = 0
        powerset(n, k+1, sum)

import sys
sys.stdin = open("장훈이의높은선반.txt")

T = int(input())
for tc in range(T):
    # N: 직원 수, B: 선반높이
    N, B = map(int,input().split())
    # H: 직원들의 키
    H = list(map(int, input().split()))
    check = [0 for _ in range(N)]
    rst = []

    #직원들의 키로 만들 수 있는 높이 모두 구하기(부분집합)
    powerset(N, 0, 0)
    # print(rst)
    print("#{} {}".format(tc+1, min(rst)-B))