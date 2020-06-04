# 인접 리스트

def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        t = q.popleft()
        for w in G[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1
                if visited[w] < 4:
                    cnt += 1
    return cnt

from collections import deque
import sys
sys.stdin = open("상원이의생일파티.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())
    G = {i:[] for i in range(1, V+1)}
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)
    # print(G)

    ans = bfs(1)
    print("#{} {}".format(tc+1, ans))