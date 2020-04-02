import sys
sys.stdin = open("피자굽기.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    queue = []
    for i in range(N):
        queue.append([pizza[i], i])

    pos = 0
    while len(queue) != 1:
        queue[0][0] //= 2

        if queue[0][0] == 0:
            if N + pos < M:
                queue.pop(0)
                queue.append([pizza[N+pos], N+pos])
                pos += 1
            elif N+pos >= M:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

    print("#{} {}".format(tc+1, queue[0][1]+1))