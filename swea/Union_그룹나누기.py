# 각 하나의 집합 만들기
def make_set(x):
    p[x] = x

# 대표자 찾기
def find_set(x):
    if p[x] == x : return x
    else: return find_set(p[x])

# 두 집합 합치기(여기서 대표자는 x)
def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

import sys
sys.stdin = open("Union_그룹나누기.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())
    group = list(map(int, input().split()))
    p = [0 for _ in range(N+1)]
    rank = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        make_set(i)

    for i in range(M):
        x, y = group[2*i], group[2*i+1]
        union(x, y)
    # print(p)
    
    print("#{} {}".format(tc+1, len(set(p))-1))