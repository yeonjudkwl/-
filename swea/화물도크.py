import sys
sys.stdin = open("화물도크.txt")

for tc in range(int(input())):
    N = int(input())
    schedule = []
    check = 0
    cnt = 1

    for i in range(N):
        s, e = map(int, input().split())
        schedule.append((s, e))

    # 입력된 스케줄 끝나는 순으로 정렬
    schedule.sort(key=lambda x:x[1])

    # 가장 빨리 끝나는 스케줄
    check = schedule.pop(0)

    # 끝나는 스케줄 보다 늦게 시작하는 스케줄 cnt
    for i in range(len(schedule)):
        if check[1] <= schedule[i][0]:
            cnt += 1
            check = schedule[i]
            
    print("#{} {}".format(tc+1, cnt))