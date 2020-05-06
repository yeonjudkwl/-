# def find(x, y, my_sum):
#     if x == N-1 and y == N-1:
#         sum_rst.append(my_sum) 
#     else:
#         for dx, dy in [(0, 1), (1, 0)]:
#             nx = x + dx
#             ny = y + dy
#             if 0<=nx<N and 0<=ny<N:
#                 find(nx, ny, my_sum+data[nx][ny])

# import sys
# sys.stdin = open("최소합.txt")

# for tc in range(int(input())):
#     N = int(input())
#     data = [[0 for _ in range(N)] for _ in range(N)]
#     sum_rst = []
#     for i in range(N):
#         data[i] = list(map(int, input().split()))
    
#     find(0, 0, data[0][0])
#     print("#{} {}".format(tc+1, min(sum_rst)))

def find(x, y, my_sum):
    global min_sum
    if x == N-1 and y == N-1:
        if my_sum < min_sum:
            min_sum = my_sum
    # 가지치기
    elif my_sum > min_sum:
        return
    else:
        for dx, dy in [(0, 1), (1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                find(nx, ny, my_sum+data[nx][ny])

import sys
sys.stdin = open("최소합.txt")

for tc in range(int(input())):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    min_sum = 999999
    
    find(0, 0, data[0][0])
    print("#{} {}".format(tc+1, min_sum))