# deque로 해야 시간 초과 안 뜸
from collections import deque

M, N = map(int, input().split())
warehouse = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = [[0 for _ in range(M)]for _ in range(N)]
rst = 0

# 익은 토마토들 queue에 다 넣어두고 시작하기
# 안그러면 이 경우에, 한 쪽방향에서만 시작하는 걸로 여김
'''
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
'''
for i in range(N):
    for j in range(M):
        if warehouse[i][j] == 1:
            queue.append((i, j))
            warehouse[i][j] = 2
while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<M and warehouse[nx][ny]==0 and warehouse[nx][ny]!=-1 and visited[nx][ny]==0:
            queue.append((nx, ny))
            warehouse[nx][ny] = 1
            visited[nx][ny] = visited[x][y] + 1
            # for l in visited:
            #     print(l)
            # print()

maxV = visited[0][0]
for i in range(N):
    for j in range(M):
        if visited[i][j] > maxV:
            maxV = visited[i][j]
rst = maxV
for i in range(N):
    if 0 in warehouse[i]:
        rst = -1
print(rst)
