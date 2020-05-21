# 각 하나의 집합 만들기
def make_set(x):
    p[x] = x

# 대표자 찾기
def find_set(x):
    if p[x] == x : return x
    else: return find_set(p[x])

# 두 집합 합치기(여기서 대표자는 x)
def union(x,y):
    p[find_set(y)] = find_set(x)

N = 6
p = [0] * (N+1)
for i in range(1,N+1):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)

print(p)
print(find_set(6))