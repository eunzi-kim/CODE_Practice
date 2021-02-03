# 500원, 100원, 50원, 10원으로 
# 내어줄 수 있는 거스름돈의 최소 개수

def money(N):
    result = 0
    while N >= 10:
        if N // 500 > 0:
            result += N // 500
            N = N % 500
        elif N // 100 > 0:
            result += N //100
            N = N % 100
        elif N // 50 > 0:
            result += N // 50
            N = N % 50
        else:
            result += N // 10
            N = N % 10
    return result

print(money(1260))