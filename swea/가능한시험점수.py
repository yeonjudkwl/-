def powerset(n, k, sum):
    if n == k:
        #set이므로 add(append 아님)
        rst.add(sum)
    else:
        # check[k] = 0
        powerset(n, k+1, sum)
        # check[k] = 1
        powerset(n, k+1, sum+score[k])

import sys
sys.stdin = open("가능한시험점수.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    # check = [0 for _ in range(N)]
    rst = set()

    powerset(N, 0, 0)
    print("#{} {}".format(tc+1, len(rst)))