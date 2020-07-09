N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
flooding = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
#비가 안 올 때의 경우 추가하기!!!!!!
height = [0]
stack = []
cnt = 0
max_cnt = 0

for i in range(N):
    height.extend(field[i])
# 비의 양 후보
h = set(height)

for k in h:
    for i in range(N):
        for j in range(N):
            if field[i][j] <= k:
                #침수 된 지역
                flooding[i][j] = 1
    # for l in flooding:
    #     print(l)
    # print(k)

    pre_cnt = cnt   
    for i in range(N):
        for j in range(N):
            if flooding[i][j] == 0:
                stack.append((i, j))
                visited[i][j] = 1
                cnt += 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0<=nx<N and 0<=ny<N and flooding[nx][ny] == 0 and visited[nx][ny] == 0:
                            stack.append((nx, ny))
                            visited[nx][ny] = 1
                            flooding[nx][ny] = 1
                           
    flooding = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    current_cnt = cnt - pre_cnt
    if current_cnt > max_cnt:
        max_cnt = current_cnt
print(max_cnt)
            