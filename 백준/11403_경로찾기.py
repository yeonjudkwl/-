def dfs(v):
    if v == G and visited[v] == 1:
        result[S][G] = 1

    for w in range(V):
        if data[v][w] == 1 and visited[w] == 0:
            visited[w] = 1
            dfs(w)

V = int(input())
data = [list(map(int, input().split()))for _ in range(V)]
result = [[0 for _ in range(V)]for _ in range(V)]

for i in range(V):
    for j in range(V):
        S, G = i, j
        #매번 초기화 해야 함.
        visited = [0 for _ in range(V)]
        dfs(S)

for i in range(V):
    for j in range(V):
        print(result[i][j], end=" ")
    print()