def partition(a, l, r):
    #가장 왼쪽 요소를 피봇으로
    pivot = a[l]
    i = l
    j = r

    while i < j:
        #피봇보다 큰 요소 찾기
        while a[i] <= pivot:
            i += 1
            #빼먹으면 안 됨
            if(i == r): break
        #피봇보다 작은 요소 찾기
        while a[j] >= pivot :
            j -= 1
            #빼먹으면 안 됨
            if(j == l): break
        #찾은 큰 요소와 작은 요소 자리바꾸기
        if i < j :
            a[i], a[j] = a[j], a[i]
    #피봇과 j요소 바꾸기(피봇기준으로 왼쪽은 작은 요소들이, 오른쪽은 큰 요소들이 위치하게 됨)
    arr[l], arr[j] = arr[j], arr[l]
    #j자리에 위치한 피봇 반환
    return j

def quicksort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quicksort(a, low, pivot-1)
        quicksort(a, pivot+1, high)


import sys
sys.stdin = open("quick_sort.txt")

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 원본 수정
    quicksort(arr, 0, len(arr)-1)
    print("#{} {}".format(tc+1, arr[N//2]))