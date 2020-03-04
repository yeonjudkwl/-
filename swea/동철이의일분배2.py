def dfs(row, temp_result=1):
    global result
    if temp_result <= result:
        return
    if row == N:
        if temp_result > result:
            result = temp_result
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(row+1, temp_result * P[row][i] * 0.01)
            visited[i] = 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    for i in range(N):
        visited[i] = 1
        dfs(1, P[0][i])
        visited[i] = 0
    print('#{0} {1:.6f}'.format(tc, result))