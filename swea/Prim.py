import sys
sys.stdin = open("Prim.txt")

# V, E = map(int, input().split())
# adj = [[0 for _ in range(V)] for _ in range(V)]

# for i in range(E):
#     # c 가중치
#     s,e,c = map(int, input().split())
#     adj[s][e] = c
#     adj[e][s] = c
    
# key = [float('inf') for _ in range(V)] 
# p = [-1 for _ in range(V)]
# mst = [False for _ in range(V)]

# # 시작점: 0정점
# key[0] = 0
# cnt = 0
# result = 0
# while cnt < V:
#     # 아직 mst가 아니고 key가 최소인 정점 선택: u
#     min = 999999
#     u = -1
#     for i in range(V):
#         if not mst[i] and key[i] < min:
#             min = key[i]
#             u = i
#     #u를 mst로 선택
#     mst[u] = True
#     result += min
#     #key값을 갱신
#     #u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
#     for w in range(V):
#         if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
#             key[w] = adj[u][w]
#             p[w] = u
#     cnt += 1
# print(key)
# print(p)
# print(result) # 175
import heapq

V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s,e,c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])
    
INF = float('inf')
key = [INF] * V
mst = [False] * V
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
print(result)