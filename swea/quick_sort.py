def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = list(), list()
    pivot = arr[0]

    for i in range(1, len(arr)):
        if pivot > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

import sys
sys.stdin = open("quick_sort.txt")

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 사본 반환
    sorted_arr = quick_sort(arr)
    print("#{} {}".format(tc+1, sorted_arr[N//2]))