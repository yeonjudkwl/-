def check(temp, col):
    row = len(temp)
    for queen_row in range(row):
        queen_col = temp[queen_row]
        # 수직 체크 or 대각선 체크
        if ( queen_col == col) or (abs(queen_col-col) == row - queen_row):
            return False
    return True
            
def DFS(N, row, temp):
    if row == N:
        rst.append(temp[:])
        return
    
    for col in range(N):
        if check(temp, col):
            temp.append(col)
            DFS(N, row + 1, temp)
            #가지치기(현재 temp에서 dfs다 돌았을 때 불가능하면 pop하기)
            temp.pop()

import sys
sys.stdin = open("NQueen.txt")

for tc in range(int(input())):
    N = int(input())
    rst = []
    DFS(N, 0, [])

    print("#{} {}".format(tc+1, len(rst)))

