M, N, K = map(int, input().split())
data = [[1 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            data[i][j] = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
stack = []
area = []
for j in range(0, N):
    for i in range(M-1, -1, -1):
        cnt = 0
        if data[i][j] == 1:
            stack.append((i, j))
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    next_i = x + di[k]
                    next_j = y + dj[k]
                    if 0 <= next_i < M and 0 <= next_j < N and data[next_i][next_j]==1:
                        cnt += 1
                        stack.append((next_i, next_j))
                        data[next_i][next_j] = 0  
            if cnt == 0:
                area.append(1)
            else:     
                area.append(cnt)
print(len(area))
for i in area:
    print(i, end=' ')