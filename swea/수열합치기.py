import sys
sys.stdin = open("수열합치기.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    numbers = [[0 for _ in range(N)] for _ in range(M)]
    new = []

    for i in range(M): 
        numbers[i] = list(map(int, input().split()))

    new = numbers[0]
    
    #추가할 수열 idx
    pos = 1
    while pos < N:
        for j in range(len(new)):
            # 추가할 수열 첫 번째 값보다 큰 값 찾기
            if numbers[pos][0] < new[j]:
                # 그 값 앞에 수열 전체 넣기
                # for문과 insert로 하나하나 넣으면 런타임에러!
                new[j:0] = numbers[pos]
                break
        # 큰 값 없으면 마지막에 넣기
        else:
            new.extend(numbers[pos])
        pos += 1

    print("#{}".format(tc+1), end=' ')
    for i in range(-1, -11, -1):
        print(new[i], end=' ')
    print()