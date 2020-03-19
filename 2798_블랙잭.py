'''
5 21
5 6 7 8 9
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
rst = 0

for i in range(N):
    for j in range(i+1, N):
        my_sum = 0
        for k in range(j+1, N):
            my_sum = arr[i] + arr[j] + arr[k]
            if my_sum <= M:
                rst = max(rst, my_sum)
print(rst)
