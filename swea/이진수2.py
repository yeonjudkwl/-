import sys
sys.stdin = open("이진수2.txt")

for tc in range(int(input())):
    N = float(input())
    rst = ''
    while N != 0.0:
        val = N * 2
        N = val % 1
        rst += str(int(val))
    if len(rst) >= 13:
        rst = 'overflow'
    print("#{} {}".format(tc+1, rst))