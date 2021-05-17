# 부분 수열의 합

T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    # 부분 수열의 합이 K가 되는 경우의 수 초기화
    count = 0
    # 목표 : 부분 집합을 이용하여 부분 수열 구하기!
    for i in range(1 << N):
        # 부분 수열의 각각의 합
        sumV = 0
        for j in range(N):
            if i & (1 << j):
                sumV += Arr[j]
        # 부분 수열의 합이 K가 되는 경우
        if sumV == K:
            count += 1
    print("#{} {}".format(TC, count))