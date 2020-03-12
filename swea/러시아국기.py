import sys
sys.stdin = open("러시아국기.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    minC = N*M

    for i in range(0, N-2):
        for j in range(i+1, N-1):
            w_cnt = b_cnt = r_cnt = 0
            W = arr[:i+1]
            B = arr[i+1:j+1]
            R = arr[j+1:]
            for w in W:
                w_cnt += w.count('W')
            for b in B:
                b_cnt += b.count('B')
            for r in R:
                r_cnt += r.count('R')
            cnt = M*N-(w_cnt + b_cnt + r_cnt)
            if cnt < minC:
                minC = cnt

    print("#{} {}".format(tc+1, minC))