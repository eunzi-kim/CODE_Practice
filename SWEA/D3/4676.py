# 늘어지는 소리 만들기

T = int(input())
for TC in range(1, T+1):
    String = list(input())
    h = int(input())
    Position = list(map(int, input().split()))
    P = [0] * (len(String) + 1)
    for i in Position:
        P[i] += 1
    result = ''
    for j in range(len(String)):
        if P[j]:
            result += '-' * P[j]
        result += String[j]
    if P[len(String)]:
        result += '-' * P[len(String)]
    print("#{} {}".format(TC, result))