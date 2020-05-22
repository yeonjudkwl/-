import heapq
import sys
sys.stdin = open("MST_최소신장트리.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for _ in range(E):
        s,e,c = map(int, input().split())
        adj[s].append([e,c])
        adj[e].append([s,c])
    # print(adj)
        
    INF = float('inf')
    key = [INF] * (V+1)
    mst = [False] * (V+1)
    pq = []
    result = 0

    key[0] = 0
    # 우선순위큐 -> 원소의 첫번째요소 -> key를 우선순위로
    heapq.heappush(pq, (0,0))

    while pq:
        #최소값 찾기
        #k: key
        k, node = heapq.heappop(pq)
        if mst[node]: continue
        #mst로 선택
        mst[node] = True
        result += k
        #key 갱신 -> key배열/ 큐
        # dest:목적지, wt: 가중치
        for dest, wt in adj[node]:
            if not mst[dest] and wt < key[dest]:
                key[dest] = wt
                #큐 갱신 => 새로운(key, 정점)삽입 => 필요없는 원소는 스킵
                heapq.heappush(pq, (key[dest],dest))
    print("#{} {}".format(tc+1, result))