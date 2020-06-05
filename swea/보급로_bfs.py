from collections import deque
import sys
sys.stdin = open("보급로.txt")
T = int(input())
INF = float('inf')

def check(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1: return False
    # if visit[x][y] : return False
    return True

def bfs(x,y):
    deq = deque()
    dx = [0, 0 ,1, -1]
    dy = [1, -1, 0, 0]
    # 출발점 가중치 0으로
    dist[x][y] = 0
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()        #deQueue
        # if x == N-1 and y == N-1 : return   # 도착점에 도달하면 return
        # visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # (x,y)의 인접한 정점의 가중치 엡데이트
            if check(nx, ny) and dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                deq.append((nx, ny))

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]
    # visit = [[0] * N for _ in range(N)]

    bfs(0,0)
    print("#{} {}".format(tc+1, dist[N-1][N-1]))