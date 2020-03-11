import sys
sys.stdin = open("최솟값으로이동하기.txt")

for tc in range(int(input())):
    W, H, N = map(int, input().split())

    x, y = map(int, input().split())

    ans = 0
    for _ in range(N-1):
        tx, ty = map(int, input().split())

        #수직 이동
        if x == tx: 
            ans += abs(y - ty)
        #수평 이동
        elif y == ty: 
            ans += abs(x - tx)
        #왼쪽 위에서 오른쪽 아래 대각선 이동
        elif (x < tx and y > ty) or (x > tx and y < ty):
            #문제에서 '대각선 길'이 없으므로 (수직+수평)과 동일
            ans += abs(x - tx) + abs(y - ty)
        #오른쪽 위에서 왼쪽 아래 대각선 이동
        else:
            ans += max(abs(x - tx), abs(y - ty))
        #다음 좌표로 이동
        x, y = tx, ty
        
    print("#{} {}".format(tc+1, ans))