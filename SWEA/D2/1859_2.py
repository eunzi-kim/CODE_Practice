# 백만 장자 프로젝트 복습
T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Val = list(map(int, input().split()))
    # 최대 이익 리스트 => 구입시기 기준
    Profit = [0]*N
    # 가장 비싼 가격
    maxV = Val[-1]
    for i in range(N-1, 0, -1): # 2 1 0 / 2 1 0 / 4 3 2 1 0
        if maxV < Val[i-1]:
            maxV = Val[i-1]
        if maxV > Val[i-1]:
            Profit[i-1] = maxV - Val[i-1]
    # 이익 합계
    result = 0
    for v in Profit:
        result += v
    print("#{} {}".format(TC, result))