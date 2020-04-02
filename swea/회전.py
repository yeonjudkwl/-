import sys
sys.stdin = open("회전.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(M):
        poped = queue.pop(0)
        queue.append(poped)
    
    print("#{} {}".format(tc+1, queue.pop(0)))