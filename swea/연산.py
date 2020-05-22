from collections import deque

def bfs(n):
    cnt = 0
    queue = deque()
    # 연산 했던 num 체크 할 list
    lists = []
    queue.append((n, cnt))
    while queue:
        num, count = queue.popleft()
        # 연산 했었으면 continue
        if num in lists: continue
        # num이 음수면 continue
        if int(num) < 0: continue
        # 연산 할 num을 lists에 추가
        lists.append(num)

        for w in ['+1', '-1', '*2', '-10']:
            # 각 연산 시행
            rst = eval(str(num)+w)
            if rst != int(M):
                queue.append((rst, count+1))
            else:
                return count+1

import sys
sys.stdin = open("연산.txt")

for tc in range(int(input())):
    N, M = input().split()

    print("#{} {}".format(tc+1, bfs(N)))