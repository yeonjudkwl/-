for tc in range(int(input())):
    N, M, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    stack = [] 
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        row, col = map(int, input().split())
        field[row][col] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                stack.append((i, j))
                field[i][j] = 0
                visited[i][j] = 1
                cnt += 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0<=nx<N and 0<=ny<M and field[nx][ny]==1 and visited[nx][ny]==0:
                            stack.append((nx,ny))
                            visited[nx][ny] = 1
                            field[nx][ny] = 0
    print(cnt)