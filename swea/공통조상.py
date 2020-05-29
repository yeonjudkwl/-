import sys
sys.stdin = open("공통조상.txt")

for tc in range(int(input())):
    V, E, v1, v2 = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    # 조상 노드들
    tmp = list()
    cnt = 0

    for i in range(E):
        parent, child = edges[i*2], edges[i*2+1]
        if tree[parent][0]:
            tree[parent][1] = child
        else:
            tree[parent][0] = child
        tree[child][2] = parent
    
    v1_parents = find_parent(v1)
    v2_parents = find_parent(v2)

    # 공통 조상 노드
    num = -1
    for i in range(len(tmp)):
        if tmp.count(tmp[i]) == 2:
            num = tmp[i]
            break

    print("#{} {} {}".format(tc+1, num, preorder(num)))

def find_parent(node):
    tmp.append(node)
    if node != 0:
        find_parent(tree[node][2])
    return tmp

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
    return cnt