# 유클리드 호제법
def find_gcd(w, h):
    a = w if w > h else h
    b = w if w < h else h
    n = a % b 

    while n != 0:
        a = b 
        b = n
        n = a % b
        
    return b
    

def solution(w,h):
    total_cnt = w * h
    incomplete_cnt = 0

    # 최대공약수
    gcd = find_gcd(w, h)

    # (w//gcd + h//gcd - 1): "한 패턴"에서의 incomplete_cnt
    incomplete_cnt = (w//gcd + h//gcd - 1) * gcd

    return total_cnt - incomplete_cnt

print(solution(8, 12))