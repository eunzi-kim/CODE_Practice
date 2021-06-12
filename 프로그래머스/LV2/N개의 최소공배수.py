# a, y의 최소공배수 구하는 함수
def lcm(a, y):
    minV = min(a, y)
    maxV = max(a, y)
    # 최대공약수 초기화
    n = 0
    for i in range(1, minV+1):
        if minV % i == 0 and maxV % i == 0:
            # 최대공약수
            n = i
    # 최소공배수
    return (a // n) * (y // n) * n

def solution(arr):
    answer = 1
    for x in arr:
        answer = lcm(answer, x)
    return answer