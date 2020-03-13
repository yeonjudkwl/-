import sys
sys.stdin = open("러시아국기.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    #미리 계산해두기(Memoization)
    w = [0] * N
    b = [0] * N
    r = [0] * N
    for i in range(N):
        w[i] = arr[i].count('W')
        b[i] = arr[i].count('B')
        r[i] = M - w[i] - b[i]

    for i in range(1, N):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]
    
    minC = N*M
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            #흰색이 아닌 칸 수
            cnt = M * (i+1) - w[i]

            #파란색 아닌 칸 수 (i+1 ~ j)
            #j-i = j - (i+1) + 1
            cnt += M * (j - i) - (b[j] - b[i])

            #빨간색 아닌 칸 수 (j+1 ~ 끝)
            #N-1-j = (N-1) - (j+1) + 1
            cnt += M * (N-1-j) - (r[N-1] - r[j])
            
            if cnt < minC:
                minC = cnt

    print("#{} {}".format(tc+1, minC))