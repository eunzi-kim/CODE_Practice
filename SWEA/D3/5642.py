# 합

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Arr = list(map(int, input().split()))
    # 최대값 초기화
    maxV = -1000000
    # 합 초기화
    sumV = 0
    # 시작 인덱스 탐색
    for i in range(N):
        # 처음부터 더하기
        sumV += Arr[i]
        # 최대값 갱신
        if sumV > maxV:
            maxV = sumV
        # 현재까지의 합이 음수이면 버리기
        if sumV < 0:
            sumV = 0
    print("#{} {}".format(TC, maxV))