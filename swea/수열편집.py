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
        #해당 idx 노드가 없을 경우
        if self.size < idx:
            return -1
        for _ in range(idx):
            node= node.next
        return node.data
    
    #해당 idx 위치에 새 노드 추가
    def insert(self, idx, data):
        node = self.head
        new_node = Node(data)
        #삽입할 위치의 바로 이전 노드 찾기
        for _ in range(idx-1):
            node = node.next
        #새 노드는 삽입할 위치의 바로 이전 노드가 가리키고 있던 노드 가리키기
        new_node.next = node.next
        #삽입할 위치의 바로 이전 노드는 새 노드 가리키기
        node.next = new_node
        #size 증가
        self.size += 1

    #해당 idx 노드 삭제
    def delete(self, idx):
        node = self.head
        #삭제할 위치의 바로 이전 노드 찾기
        for _ in range(idx-1):
            node = node.next
        #삭제할 위치의 바로 이전 노드는 다음 노드 가리키기
        node.next = node.next.next
        #size 감소
        self.size -= 1

    #해당 idx 노드 값 바꾸기
    def change(self, idx, data):
        node = self.head
        #해당 idx 노드 찾기
        for _ in range(idx):
            node = node.next
        node.data = data
        
import sys
sys.stdin = open("수열편집.txt")

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    number = list(map(int, input().split()))

    mylist = LinkedList()

    #주어진 수열 노드에 추가
    for i in range(N):
        mylist.add(number[i])

    #해당 작업
    for _ in range(M):
        # mode, idx, val
        work_list = list(input().split())

        if work_list[0] == 'I':
            mylist.insert(int(work_list[1]), int(work_list[2]))
        elif work_list[0] == 'D':
            mylist.delete(int(work_list[1]))
        elif work_list[0] == 'C':
            mylist.change(int(work_list[1]), int(work_list[2]))
    
    result = mylist.node_print(L)
    print("#{} {}".format(tc+1, result))      