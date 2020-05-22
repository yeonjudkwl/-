import sys
sys.stdin = open("Dijkstra_최소이동거리.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        s,e,c = map(int, input().split())
        adj[s].append([e,c])
        
    INF = float('inf')
    dist = [INF] * (V+1)
    selected = [False] * (V+1)

    dist[0] = 0
    cnt = 0
    while cnt < (V+1):
        #dist의 값이 최소인 정점
        min = INF
        u = -1
        for i in range((V+1)):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i
        
        # 결정
        selected[u] = True
        cnt += 1
        # 간선완화
        for w, cost in adj[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
    print("#{} {}".format(tc+1, dist[-1]))