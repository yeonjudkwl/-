def bfs():
    rst = 0
    while queue:
        #현재 위치
        x, y = queue.pop(0)
        
        #4방향
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 and maze[nx][ny] != 1:
                #다음 위치 
                queue.append((nx, ny))
                #거리 계산
                visited[nx][ny] = visited[x][y] + 1
                #도착지면 거리 저장
                if maze[nx][ny] == 3:
                    rst = visited[x][y]
                    break
    return rst
    
import sys
sys.stdin = open("미로의거리.txt")

for tc in range(int(input())):
    N = int(input())
    maze = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = []
    result = 0

    for i in range(N):
        maze[i] = list(map(int, input()))

    for i in range(N):
        for j in range(N):
            #출발지
            if maze[i][j] == 2:
                queue.append((i, j))
                result = bfs()
    
    print("#{} {}".format(tc+1, result))