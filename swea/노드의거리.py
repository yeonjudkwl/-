def bfs():
    result = 0
    while queue:
        #현재 노드
        v = queue.pop(0)

        #인접 노드
        for w in range(V+1):
            if graph[v][w] == 1 and visited[w] == 0 and w != 1:
                queue.append(w)
                #거리 계산
                visited[w] = visited[v] + 1
                #도착지면 거리 저장
                if w == G:
                    result = visited[w]
                    break
    return result

import sys
sys.stdin = open("노드의거리.txt")

for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    queue =[]

    #인접 행렬
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    #시작점, 도착점
    S, G = map(int, input().split())
    queue.append(S)
    result = bfs()

    print("#{} {}".format(tc+1, result))