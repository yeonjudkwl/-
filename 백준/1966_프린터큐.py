for tc in range(int(input())):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    pos = M
    cnt = 0
    maxP = max(priority)

    while 1:
        if priority[0] < maxP:
            value = priority.pop(0)
            priority.append(value)
            if pos == 0:
                pos = len(priority)-1
            else:
                pos -= 1
        elif priority[0] == maxP:
            #원하는 문서 출력
            if pos == 0:
                cnt += 1
                break
            else:
                pos -= 1
                priority.pop(0)
                maxP = max(priority)
                cnt += 1
         
    print(cnt)