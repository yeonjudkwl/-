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
sys.stdin = open("MST_최소신장트리.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(E)]

    edges.sort(key=lambda x:x[2])

    p = [0] * (V+1)
    rank = [0] * (V+1)
    for i in range((V+1)):
        make_set(i)

    mst = []
    result = 0
    cnt = 0
    for i in range(E):
        s, e, c = edges[i][0], edges[i][1], edges[i][2]
        #사이클이 생길 경우
        if find_set(s) == find_set(e): continue

        # mst
        mst.append(edges[i])
        result += c
        cnt += 1
        union(s, e)

        if cnt == V: break
        
    print("#{} {}".format(tc+1, result))