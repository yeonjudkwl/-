# 전위 순회
def preorder(pos, cnt):
    global rst
    # 자식 노드가 있을 경우
    if pos != 0:
        rst = cnt
        preorder(data_list[pos][0], rst+1)
        preorder(data_list[pos][1], rst+1)
        return rst

import sys 
sys.stdin = open("subtree.txt")

for tc in range(int(input())):
    E, N = map(int, input().split())
    pair = list(map(int, input().split()))
    # E+1+1: 노드의 개수(간선의 개수 + 1) + 1
    data_list = [[0 for _ in range(2)] for _ in range(E+1+1)]

    # 노드 저장
    for i in range(0, E*2, 2):
        if data_list[pair[i]][0] == 0:
            data_list[pair[i]][0] = pair[i+1]
        else:
            data_list[pair[i]][1] = pair[i+1]

    # 전위 순회 시작
    rst = preorder(N, 1)
    
    print('#{} {}'.format(tc+1, rst))