import sys
sys.stdin = open("가능한시험점수.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    total = sum(score)
    s = [0 for _ in range(total+1)]
    s[0] = 1

    for x in score:
        for i in range(total-x, -1, -1):
            if s[i] == 1:
                s[i+x] = 1
    print("#{} {}".format(tc+1, sum(s)))