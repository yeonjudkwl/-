def swap(Numbers, cnt):
    global max_change, l, arr
    if cnt == max_change:
        return
    now = 0
    while now < l-1:
        for i in range(now+1,l):
            Numbers[now], Numbers[i] = Numbers[i], Numbers[now]
            if Numbers not in arr[cnt]:
                add = Numbers[:]
                arr[cnt].append(add)
                swap(Numbers, cnt+1)
            Numbers[i], Numbers[now] = Numbers[now], Numbers[i]
        now += 1
 
import sys
sys.stdin = open("최대상금.txt")
 
for tc in range(int(input())):
    numbers, max_change = map(int,input().split())
    Numbers = list(str(numbers))
    l = len(Numbers)
    arr = [[] for _ in range(max_change)]
    swap(Numbers, 0)
    max_num = 0
    for i in arr[max_change-1]:
        max_num = max(max_num, int(''.join(i)))
 
    print('#{} {}'.format(tc+1, max_num))