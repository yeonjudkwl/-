import sys
sys.stdin = open("이진탐색.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    # A리스트 정렬
    A.sort()

    # B리스트 요소 추출 및 확인
    for i in range(M):
        target = B[i]
        l = 0
        r = N-1
        
        #체크
        flag = 0
        while l <= r:
            m = (l + r) // 2
            if target < A[m]:
                r = m - 1
                # 연속할 경우 해당 x
                if flag == 1: break
                flag = 1
            elif target == A[m]:
                cnt += 1
                break
            else:
                l = m + 1
                # 연속할 경우 해당 x
                if flag == 2: break
                flag = 2

    print("#{} {}".format(tc+1, cnt))