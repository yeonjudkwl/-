import sys
sys.stdin = open("노드의합.txt")

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    data = [0 for _ in range(N+1)]
    minI = 999

    #리프노드의 값 저장
    for _ in range(M):
        idx, val = map(int, input().split())
        data[idx] = val
        if idx < minI:
            minI = idx
    
    #pos: 리프노드가 아닌 노드 중 가작 마지막 노드
    pos = minI-1
    while pos != 0:
        if pos*2+1 >= len(data):
            data[pos] = data[pos*2]
        else:
            #왼쪽 자식 노드와 오른쪽 자식 노드의 합을 저장 
            data[pos] = data[pos*2] + data[pos*2+1]
        #다음 노드
        pos -= 1
    print("#{} {}".format(tc+1, data[L]))