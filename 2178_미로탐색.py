N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
q =[]

q.append((0, 0))
visited[0][0] = 1
while q:
    x, y = q.pop(0)
    for k in range(4):
        next_i = x + di[k]
        next_J = y + dj[k]
        if 0<=next_i<N and 0<=next_J<M and maze[next_i][next_J]==1 and visited[next_i][next_J]==0:
            q.append((next_i, next_J))
            visited[next_i][next_J] = visited[x][y] + 1
            if (next_i, next_J) == (N-1, M-1):
                print(visited[next_i][next_J])
# for l in visited:
#     print(l)
# print(visited[N-1][M-1])
 