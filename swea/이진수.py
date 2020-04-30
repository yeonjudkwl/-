import sys
sys.stdin = open('이진수.txt')

for tc in range(int(input())):
    n, hex_num = input().split()
    rst = ''
    for num in hex_num:
        if num.isdecimal():
            num = int(num)
            # 10진수를 이진수로 변환 후 빈 자리 채우기
            rst += bin(num)[2:].rjust(4, '0')
        else:
            # 16진수를 10진수로 변환
            digit = int(num, 16)
            # 10진수를 2진수로 변환 후 빈 자리 채우기
            rst += bin(digit)[2:].rjust(4, '0')
    print("#{} {}".format(tc+1, rst))