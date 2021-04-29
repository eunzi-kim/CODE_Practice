# 평범한 숫자

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    # 카운트 초기화
    count = 0
    # 2 <= i <= N-1 탐색
    for i in range(1, N-1):
        minV = 1000000000
        maxV = 0
        # 3개의 숫자 중 최소값, 최대값 탐색
        for j in range(i-1, i+2):
            if minV > P[j]:
                minV = P[j]
            if maxV < P[j]:
                maxV = P[j]
        if P[i] != maxV and P[i] != minV:
            count += 1
    print("#{} {}".format(TC, count))