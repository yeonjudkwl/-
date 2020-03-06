import sys
sys.stdin = open("가능한시험점수.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    s = sum(d)
    rd = [0]
    nd = [1] + [0]*(s)
    for i in d:
        temp = rd[:]
        for j in temp:
            if not nd[i+j]:
                nd[i+j] = 1
                rd.append(i+j)
 
    print(f'#{tc} {sum(nd)}')