import sys
sys.stdin = open("암호.txt")

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    pw = list(map(int, input().split()))

    i = 0
    for _ in range(K):
        # M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터
        if i+M >= len(pw):
            diff = (len(pw)-1) - (i)
            i = M-diff-1
            # 첫 번째 칸이면 마지막 칸에 추가
            if i == 0:
                pw.insert(len(pw), pw[i-1]+pw[i])
                i = len(pw)-1
            # 아니면 그 해당 칸에 추가
            else:
                pw.insert(i, pw[i-1]+pw[i])
        # M칸 뒤에 추가 
        else:
            i += M
            pw.insert(i, pw[i-1]+pw[i])
    # 역순으로 변환 후 10자리만 출력
    result = ' '.join(map(str, pw[::-1][:10]))
    print("#{} {}".format(tc+1, result))