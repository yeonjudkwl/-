from collections import deque

def bfs(n):
    cnt = 0
    queue = deque()
    lists = []
    queue.append((n, cnt))
    while queue:
        num, count = queue.popleft()
        if num in lists: continue
        if int(num) < 0: continue
        # print(num)
        lists.append(num)

        for w in ['+1', '-1', '*2', '-10']:
            rst = eval(str(num)+w)
            if rst != int(M):
                queue.append((rst, count+1))
            else:
                return count+1

import sys
sys.stdin = open("연산.txt")

for tc in range(int(input())):
    N, M = input().split()
    visited = [0 for _ in range(4)]

    print("#{} {}".format(tc+1, bfs(N)))