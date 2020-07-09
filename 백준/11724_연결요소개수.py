def dfs(v):
    visited[v] = 1
    # print('*',visited)
    for w in range(N+1):
        if data[v][w] == 1 and visited[w] == 0:
            data[v][w] = 0
            data[w][v] = 0
            dfs(w)

N, M = map(int, input().split())
data = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 0
for _ in range(M):
    x, y = map(int, input().split())
    data[x][y] = 1
    data[y][x] = 1

dfs(1)
cnt+=1

for i in range(1, len(visited)):
    if visited[i] == 0:
        dfs(i)
        cnt+=1

print(cnt)