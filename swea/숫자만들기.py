def f(n, k, r, op1, op2, op3, op4):
    global minV, maxV

    if n==k:
        if r>maxV:
            maxV = r
        if r<minV:
            minV = r
    else:
        if op1>0:
            f(n+1, k, r+num[n], op1-1, op2, op3, op4)
        if op2>0:
            f(n+1, k, r-num[n], op1, op2-1, op3, op4)
        if op3>0:
            f(n+1, k, r*num[n], op1, op2, op3-1, op4)
        if op4>0:
            #r//num[n]하지 않도록 주의(음수일 경우 //은 내림, int(/)는 소수점아래 버림)
            f(n+1, k, int(r/num[n]), op1, op2, op3, op4-1)

import sys
sys.stdin=open("숫자만들기.txt")

T=int(input())
for tc in range(T):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    num = list(map(int, input().split()))
    minV = 10000000000
    maxV = -10000000000

    #1부터 N깊이까지 재귀
    f(1, N, num[0], op1, op2, op3, op4)
    print("#{} {}".format(tc+1, maxV-minV))