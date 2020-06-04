def BFS():
    q = deque()
    dist[0][0] = roadMap[0][0]
    check[0][0] = 1
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            cx, cy = x + dx, y + dy
            if 0 <= cx < N and 0 <= cy < N:
                if not check[cx][cy] or dist[cx][cy] > dist[x][y] + roadMap[cx][cy]:
                    check[cx][cy] = 1
                    dist[cx][cy] = dist[x][y] + roadMap[cx][cy]
                    q.append((cx, cy))
 
from collections import deque
import sys
sys.stdin = open("보급로.txt")

for tc in range(int(input())):
    N = int(input())
    roadMap = [list(map(int, input())) for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]
    check = [[0 for _ in range(N)] for _ in range(N)]
    BFS()
    print("#{} {}".format(tc+1, dist[N-1][N-1]))