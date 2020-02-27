import sys
sys.stdin = open("행렬찾기.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    temp = []
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                x, y = i, j
                while data[x][j] != 0:
                    x += 1
                while data[i][y] != 0:
                    y += 1
                temp.append((x-i, y-j))

                for ii in range(i, x+1):
                    for jj in range(j, y+1):
                        data[ii][jj] = 0
                cnt += 1

    for i in range(0, len(temp)-1):
        min = i		
        for j in range(i+1, len(temp)):
            if temp[j][0]*temp[j][1] < temp[min][0]*temp[min][1]:
                min = j
        temp[i], temp[min] = temp[min], temp[i]

    print("#{} {}".format(tc+1, cnt), end=" ")
    for t in temp:
        print(*t, end=' ')
    print()