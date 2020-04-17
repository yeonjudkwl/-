import sys
sys.stdin = open("별자리.txt")

for tc in range(int(input())):
    mymap = [[0 for _ in range(10)]for _ in range(10)]
    visited = [[0 for _ in range(10)]for _ in range(10)]
    stack = []
    cnt = 0 
    for i in range(10):
        mymap[i] = list(map(int, input().split()))

    for i in range(10):
        for j in range(10):
            if mymap[i][j] == 1 and visited[i][j] == 0:
                stack.append((i, j))
                visited[i][j] = 1
                cnt += 1
                
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0<=nx<10 and 0<=ny<10 and mymap[nx][ny]==1 and visited[nx][ny]==0:
                            stack.append((nx, ny))
                            visited[nx][ny] = 1

    print("#{} {}".format(tc+1, cnt))