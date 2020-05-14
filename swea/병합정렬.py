def split(arr):
    global cnt

    if len(arr)<= 1:
        return arr
    
    m = len(arr)//2
    left = split(arr[:m])
    right = split(arr[m:])

    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)

#left, right 배열을 인자로 넘김
def merge(left, right):
    merged = list()
    left_point = right_point = 0
    
    #left배열, right배열 남아있을 때
    while len(left) > left_point or len(right) > right_point:
        if len(left) > left_point and len(right) > right_point:
            if left[left_point] > right[right_point]:
                merged.append(right[right_point])
                right_point += 1
            else:
                merged.append(left[left_point])
                left_point += 1
            
        #left배열 남아있을 때        
        elif len(left) > left_point:
            merged.append(left[left_point])
            left_point += 1
            
        #right배열 남아있을 때
        else:
            merged.append(right[right_point])
            right_point += 1
        
    return merged

import sys
sys.stdin = open("병합정렬.txt")

for tc in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0

    merged = split(L)
    print("#{} {} {}".format(tc+1, merged[N//2], cnt))