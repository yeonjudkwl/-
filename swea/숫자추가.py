## python으로 구현
# import sys
# sys.stdin = open("숫자추가.txt")

# for tc in range(int(input())):
#     N, M, L = map(int, input().split())
#     number = list(map(int, input().split()))
#     for _ in range(M):
#         idx, val = map(int, input().split())
#         number.insert(idx, val)
#     print("#{} {}".format(tc+1, number[L]))


# LinkedList로 구현
class Node:
    def __init__(self, d=0):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    #뒤에 추가
    def add(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
        else:
            node = self.head
            #마지막 노드 찾기
            while node.next:
                node = node.next
            #새로운 노드 추가
            node.next = Node(data)
            self.size += 1
    
    #해당 idx노드 출력
    def node_print(self, idx):
        node = self.head
        for _ in range(idx):
            node= node.next
        return node.data
    
    #해당 idx 위치에 새 노드 추가
    def insert(self, idx, data):
        node = self.head
        new_node = Node(data)
        #삽입할 위치의 바로 이전 노드 찾기
        for _ in range(idx-1):
            node= node.next
        #새 노드는 삽입할 위치의 바로 이전 노드가 가리키고 있던 노드 가리키기
        new_node.next = node.next
        #삽입할 위치의 바로 이전 노드는 새 노드 가리키기
        node.next = new_node
        

import sys
sys.stdin = open("숫자추가.txt")

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    number = list(map(int, input().split()))

    mylist = LinkedList()

    #주어진 수열 노드에 추가
    for i in range(N):
        mylist.add(number[i])

    #해당 위치에 삽입
    for _ in range(M):
        idx, val = map(int, input().split())
        mylist.insert(idx, val)
    
    print("#{} {}".format(tc+1, mylist.node_print(L)))      