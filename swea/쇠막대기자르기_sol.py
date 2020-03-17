import sys
sys.stdin = open("쇠막대기자르기.txt")

for tc in range(int(input())):
    pal = list(input())
    cnt = 0
    stick = 0

    for i in range(len(pal)):
        if pal[i] == '(':
            stick += 1
        elif pal[i] == ')' and pal[i-1]=='(':
            stick -= 1
            cnt += stick
        else:
            stick -= 1
            cnt += 1
    print("#{} {}".format(tc+1, cnt))
