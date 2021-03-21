# 세제곱근을 찾아라

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    x = round(N ** (1 / 3), 2)
    result = -1
    if int(x) == x:
        result = int(x)
    print("#{} {}".format(TC, result))