# 구구단 1

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 한 자리수 약수 탐색
    M = []
    for x in range(1, N+1):
        if x >= 10:
            break
        if not N % x:
            M.append(x)
    # 결과값 초기화
    result = "No"
    # 한 자리수들의 곱인 경우
    for m in M:
        if 0 < (N // m) < 10:
            result = "Yes"
    print("#{} {}".format(TC, result))