import sys
sys.stdin = open("자기방으로돌아가기.txt")

for tc in range(int(input())):
    N = int(input())

    #복도
    cnt = [0 for _ in range(201)]

    for _ in range(N):
        #a방에서 b방으로 이동
        a, b = map(int, input().split())

        #a방 앞의 복도 번호
        a = (a+1)//2
        #b방 앞의 복도 번호
        b = (b+1)//2

        if a > b: a, b = b, a
        #a방에서 b방까지의 복도에 이동해야 한다고 체크
        for i in range(a, b+1):
            cnt[i] += 1
        #동선이 겹치면 안되므로 max값만큼 시간이 필요
        rst = max(cnt)
    print("#{} {}".format(tc+1, rst))