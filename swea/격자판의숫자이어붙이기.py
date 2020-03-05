def find(i,j,idx,sum):
    #7자리수 만들어졌으면 ij에 대한 탐색종료(다음 ij에 대해 다시 시작해야 됨.)
    if idx==7:
        rst.add(sum)
    else:
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<4 and 0<=nj<4:
                find(ni,nj,idx+1,sum+data[i][j])

import sys
sys.stdin = open("격자판의숫자이어붙이기.txt")

T = int(input())
for tc in range(T):
    data = [list(input().split()) for _ in range(4)]
    rst = set()

    for i in range(4):
        for j in range(4):
            find(i, j, 0, '')
    
    print('#{} {}'.format(tc+1, len(rst)))