def make_set(x):
    p[x] = x
    
def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] =  find_set(p[x])
        return p[x]
 
def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1
        
import sys
sys.stdin = open("Kruskal.txt")

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(E)]

edges.sort(key=lambda x:x[2])

#make_set
p = [0] * V
rank = [0] * V
for i in range(V):
    make_set(i)
    
#모든 간선에 대해서 반복 => V-1개의 간선이 선택될때까지
cnt = 0
result = 0
mst = []
for i in range(E):
    s,e,c = edges[i][0], edges[i][1],edges[i][2]
    #사이클이면 스킵 : 간선의 두 정점이 서로 같은 집합이면 => find_set
    if find_set(s) == find_set(e): continue
    #간선 선택
    result += c
    mst.append(edges[i])
    union(s,e)
    cnt += 1
    if cnt == V-1: break
    
print(result)
print(mst)