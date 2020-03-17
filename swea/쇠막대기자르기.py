import sys
sys.stdin = open("쇠막대기자르기.txt")

for tc in range(int(input())):
    pal = list(input())
    cnt = 0
    stick = 0
    pos = 0

    while pos <= len(pal)-1:
        if pal[pos] == '(':
            stick += 1
        else:
            stick -= 1
            #레이저인 경우
            if pal[pos-1] == '(':
                cnt += stick
            #쇠막대 끝인 경우
            else:
                cnt += 1
        pos += 1
    print("#{} {}".format(tc+1, cnt))
