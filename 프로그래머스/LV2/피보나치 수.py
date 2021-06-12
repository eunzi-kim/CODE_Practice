def solution(n):
    answer = 0
    a = b = 0
    for x in range(n+1):
        if x == 0:
            continue
        elif x == 1:
            b = 1
        else:
            c = a + b
            a = b
            b = c
        answer = b % 1234567
    return answer