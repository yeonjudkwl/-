import sys
sys.stdin = open("컨테이너운반.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    total = 0 

    # 화물 무게 및 적재용량 큰 순으로 정렬
    w.sort(reverse=True)
    t.sort(reverse=True)

    for i in range(N):
        for j in range(M):
            # 화물 무게보다 적재용량이 크면 실을 수 있음
            if w[i] <= t[j]:
                total += w[i]
                t[j] = 0
                break

    print("#{} {}".format(tc+1, total))