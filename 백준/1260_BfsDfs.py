def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for w in range(N+1):
        if data[v][w] == 1 and visited[w] == 0:
            dfs(w)

def bfs(v):
    stack = []
    visited[v] = 1
    stack.append(v)

    while stack:
        rst = stack.pop(0)
        print(rst, end=" ")

        for w in range(N+1):
            if data[rst][w] == 1 and visited[w] == 0:
                visited[w] = 1
                stack.append(w)



N, M, V = map(int, input().split())
data = [[0 for _ in range(N+1)]for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    data[x][y] = 1
    data[y][x] = 1

dfs(V)
visited = [0 for _ in range(N+1)]
print()
bfs(V)