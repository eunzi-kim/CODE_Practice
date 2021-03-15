# 퍼펙트 셔플

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    String = list(input().split())
    result = ""
    if N % 2:
        for x in range(N//2+1):
            if x < N//2:
                result += String[x] + " " + String[N//2+1+x] + " "
            else:
                result += String[x]
    else:
        for x in range(N//2):
            result += String[x] + " " + String[N//2+x] + " "
    print("#{} {}".format(TC, result))