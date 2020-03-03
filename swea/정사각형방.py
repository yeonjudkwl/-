import sys
sys.stdin = open("정사각형방.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    #index와 방번호 맞추기위해 +1 and 시작위치가 1일때 index 0에서 판단해야하므로 index 0번째 필수.
    visited = [0]*(N*N+1)
    cnt = 0
    maxCnt = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                next_i = i + di[k]
                next_j = j + dj[k]
                if 0<=next_i<N and 0<=next_j<N and data[next_i][next_j]==data[i][j]+1:
                    visited[data[i][j]] = 1

    #연속된 1개수 세기(오른쪽부터세기 => maxCnt가 같을 경우 '>='를 통해 방 번호가 작은거 선택하기 위해)
    for i in range(N*N, -1, -1):
        if visited[i] == 1:
            cnt += 1
        else:
            #오른쪽부터 왔으므로 start가 작은 값으로 갱신
            if cnt >= maxCnt:
                maxCnt = cnt
                #else구문이므로 현재위치는 visited가 0임. 따라서 maxCnt의 시작위치는 visited가 1인 오른쪽 값임.
                start = i+1
            cnt=0

    # maxCnt+1: 자기자신(방) count에 추가
    print("#{} {} {}".format(tc+1, start, maxCnt+1))
