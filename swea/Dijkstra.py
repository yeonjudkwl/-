V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s,e,c = map(int, input().split())
    adj[s].append([e,c])
    
INF = float('inf')
dist = [INF] * V
selected = [False] * V

# 시작점 선택
dist[0] = 0
cnt = 0
# 모든 정점이 선택될때까지
while cnt < V:
    #dist의 값이 최소인 정점
    min = INF
    u =-1
    for i in range(V):
        # 아직 선택되지 않고 dist의 값이 최소인 정점:u
        if not selected[i] and dist[i] < min:
            min = dist[i]
            u = i
    
    # 정점 u의 최단거리 결정
    selected[u] = True
    cnt += 1
    # 정점 u에 인접한 정점에 대해서 간선완화
    for w, cost in adj[u]:
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
print(dist)