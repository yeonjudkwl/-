import sys
sys.stdin = open("올림픽종목투표.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    sports = list(map(int, input().split()))
    score = list(map(int, input().split()))
    vote = [0 for _ in range(N)]

    for j in range(M):
        for i in range(N):
            if score[j] >= sports[i]:
                vote[i] += 1
                break
    print("#{} {}".format(tc+1, vote.index(max(vote))+1))