def f(n, sum, d, m, m3):
    global minV
    if n>12:
        if sum < minV:
            minV = sum
    elif minV <= sum:
        return
    else:
        #한 달 이용권 끊은 경우
        #min(table[n]*d, m) => table[n]*d: 1일권과 m: 한 달권중 저렴한 거 선택
        f(n+1, sum+min(table[n]*d, m), d, m, m3)
        #세 달 이용권 끊은 경우
        f(n+3, sum+m3, d, m, m3)

import sys
sys.stdin = open("수영장.txt")

T = int(input())
for tc in range(T):
    d, m, m3, y = map(int, input().split())
    #index와 월을 맞추기위해 0번index에 0추가
    table = [0] + list(map(int, input().split()))
    #1년이용권을 최소값으로 초기화
    minV = y
    f(1,0,d,m,m3)
    print('#{} {}'.format(tc+1, minV))