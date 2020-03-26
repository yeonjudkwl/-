def dfs(x, y, k, num):
    if k == 6:
        rst.add(num)
        return
    else:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<5 and 0<=ny<5:
                #num+pan[nx][ny]가 아니라 num+pan[x][y] 붙이기
                dfs(nx, ny, k+1, num+pan[x][y])

pan = [[0 for _ in range(5)] for _ in range(5)]
rst = set()
for i in range(5):
    #문자열로 받기
    pan[i] = list(input().split())
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, '')

print(len(rst))