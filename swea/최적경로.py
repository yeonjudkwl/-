def path(n, dis):
    global min_dis
 
    if n == N:
        new_dis = dis + (abs(p[N-1][0]-home[0])+abs(p[N-1][1]-home[1]))
        if new_dis < min_dis:
            min_dis = new_dis
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                p[n] = users[i]
                if n == 0:
                    new_dis = dis + (abs(company[0]-users[i][0])+abs(company[1]-users[i][1]))
                else:
                    new_dis = dis + (abs(p[n - 1][0] - p[n][0]) + abs(p[n - 1][1] - p[n][1]))
                if new_dis < min_dis:
                    path(n+1, new_dis)
                visited[i] = 0

import sys 
sys.stdin = open("최적경로.txt")

for tc in range(int(input())):
    N = int(input())
    location = list(map(int, input().split()))
    company = (location[0], location[1])
    home = (location[2], location[3])
    users = []
    visited = [0] * N
    p = [0] * N
    min_dis = 999999

    for i in range(4, len(location), 2):
        x = location[i]
        y = location[i+1]
        users.append((x, y))
    
    path(0, 0)
    print('#{} {}'.format(tc+1, min_dis))