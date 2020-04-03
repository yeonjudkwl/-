'''
6
5
1 2
1 3
3 4
2 3
4 5
'''
N = int(input())
M = int(input())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = 0
queue = []

#인접 행렬
for _ in range(M):
    x, y = map(int, input().split())
    G[x][y] = 1
    G[y][x] = 1

queue.append((1, 0))
visited[1] = 1

while queue:
    v, k = queue.pop(0)
    #거리
    k += 1
    for w in range(N+1):
        if G[v][w] == 1 and visited[w] == 0 and k < 3:
            visited[w] = 1
            G[v][w] = 0
            G[w][v] = 0
            queue.append((w, k))
            #초대할 친구 수
            cnt+=1
print(cnt)