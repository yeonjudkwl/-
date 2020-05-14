def play(player1, player2):
    for i in range(6):
        # 카운트 세기
        player1_cnt[player1[i]] +=1
        player2_cnt[player2[i]] +=1
        # 베이비진 확인
        for j in range(10):
            if j < 8 and (player1_cnt[j] >= 1 and player1_cnt[j+1] >= 1 and player1_cnt[j+2] >= 1):
                return 1
            if player1_cnt[j] >= 3:
                return 1
        for j in range(10):
            if j < 8 and (player2_cnt[j] >= 1 and player2_cnt[j+1] >= 1 and player2_cnt[j+2] >= 1):
                return 2
            if player2_cnt[j] >= 3:
                return 2
    return 0

import sys
sys.stdin = open("babygin.txt")

for tc in range(int(input())):
    arr = list(map(int, input().split()))
    player1 = [arr[i] for i in range(len(arr)) if not i&1]
    player2 = [arr[i] for i in range(len(arr)) if i&1]
    player1_cnt = [0 for _ in range(10)]
    player2_cnt = [0 for _ in range(10)]

    print("#{} {}".format(tc+1, play(player1, player2)))