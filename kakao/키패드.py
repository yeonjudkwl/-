def solution(numbers, hand):
    rst = ''
    # 키패드 좌표
    phone = {1:(0, 0), 2: (0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2), 0:(3, 1)}
    # 초기 왼손 좌표
    l_pos = (3, 0)
    # 초기 오른손 좌표
    r_pos = (3, 2)

    for num in numbers:
        # 왼손
        if num % 3 == 1:
            rst += 'L'
            # 왼손 좌표 바꾸기
            l_pos = phone[num]
        # 오른손
        elif num % 3 == 0 and num != 0:
            rst += 'R'
            # 오른손 좌표 바꾸기
            r_pos = phone[num]
        # 2,5,8,0일 경우
        else:
            # 눌러야 할 번호의 좌표
            pos = phone[num]
            # 왼손이 가까울 경우
            if abs(l_pos[0] - pos[0]) + abs(l_pos[1] - pos[1]) < abs(r_pos[0] - pos[0]) + abs(r_pos[1] - pos[1]):
                rst += 'L'
                l_pos = pos
            # 오른손이 가까울 경우
            elif abs(l_pos[0] - pos[0]) + abs(l_pos[1] - pos[1]) > abs(r_pos[0] - pos[0]) + abs(r_pos[1] - pos[1]):
                rst += 'R'
                r_pos = pos
            # 거리가 같을 경우
            else:
                if hand == 'right':
                    rst += 'R'
                    r_pos = pos
                else:
                    rst += 'L'
                    l_pos = pos
    return rst