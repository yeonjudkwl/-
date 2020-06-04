# 인접 행렬

def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        for w in range(1, V+1):
            if G[v][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
                if visited[w] < 4:
                    cnt += 1
    return cnt

from collections import deque
import sys
sys.stdin = open("상원이의생일파티.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1][v2] = 1
        G[v2][v1] = 1

    ans = bfs(1)
    print("#{} {}".format(tc+1, ans))