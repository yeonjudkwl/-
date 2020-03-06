import sys
sys.stdin = open("가능한시험점수.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    rst = set([0])

    for x in score:
        num = set()
        for y in rst:
            num.add(x+y)
        rst = set(list(rst)+list(num))
    print("#{} {}".format(tc+1, len(rst)))