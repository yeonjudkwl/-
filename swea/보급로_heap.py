from collections import deque
import heapq
import sys
sys.stdin = open("보급로.txt")

T = int(input())
def minDistacne():
    minV = 987654321
    mx, my = -1, -1
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and dist[i][j] < minV:
                minV = dist[i][j]
                mx, my = i, j
    return mx, my

def check(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1: return False
    if visit[x][y] : return False
    return True

def dijkstra(x,y):
    dx = [0, 0 ,1, -1]
    dy = [1, -1, 0, 0]

    # 출발점 설정
    dist[x][y] = 0
    heapq.heappush(heap,(dist[x][y], x, y))  # (가중치, x, y)   #enQueue

    while True:
        # x, y = minDistacne()
        d, x, y = heapq.heappop(heap)           # 우선순위큐에서 가중치 최소값
        if x == N-1 and y == N-1 : return       # 도착점에 도달하면 리턴
        visit[x][y] = 1                         # 방문체크

        for i in range(4): #최소값(x,y)에 인접한 정점들 중에서
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문가능하고 가중치 엡데이트된다면
            if check(nx, ny) and dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                heapq.heappush(heap, (dist[nx][ny], nx, ny))  # 업데이트 될때만 enQueue

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]          # 가중치
    visit = [[0] * N for _ in range(N)]                 # 방문체크
    heap = []       # heap(우선순위큐)

    dijkstra(0,0)
    print("#{} {}".format(tc+1, dist[N-1][N-1]))