import copy

N = int(input())
data = [list(input()) for _ in range(N)]
data2 = copy.deepcopy(data)
visited = [[0 for _ in range(N)] for _ in range(N)]
stack = []

#적록색약 아닌 사람
group1 = 0
#적록색약인 사람
group2 = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            color = data[i][j]
            group1 += 1
        if data[i][j] == color:
            stack.append((i, j, color))
        while stack:
            x, y, c = stack.pop()
            visited[x][y] = 1
            data[x][y] = 0
            for k in range(4):
                next_i = x + di[k]
                next_j = y + dj[k]
                if 0<=next_i<N and 0<=next_j<N and data[next_i][next_j]==c and visited[next_i][next_j] == 0:
                    stack.append((next_i, next_j, c))
            

for i in range(N):
    for j in range(N):
        if data2[i][j] == 'G':
            data2[i][j] = 'R'
data = data2 
visited = [[0 for _ in range(N)] for _ in range(N)]
stack = []

for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            color = data[i][j]
            group2 += 1
        if data[i][j] == color:
            stack.append((i, j, color))
        while stack:
            x, y, c = stack.pop()
            visited[x][y] = 1
            data[x][y] = 0
            for k in range(4):
                next_i = x + di[k]
                next_j = y + dj[k]
                if 0<=next_i<N and 0<=next_j<N and data[next_i][next_j]==c and visited[next_i][next_j] == 0:
                    stack.append((next_i, next_j, c))

print("{} {}".format(group1, group2))