# 백만 장자 프로젝트

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Val = list(map(int, input().split()))
    # 자신의 최대이익 리스트 초기화 => 구매일 기준
    lstM = [0] * N
    # 자신의 이익 탐색
    for i in range(N-1, 0, -1):
        for j in range(i-1, -1, -1):
            if Val[i] <= Val[j]:
                break
            elif Val[i] > Val[j]:
                P = Val[i] - Val[j]
                # 최대 이익 탐색
                if lstM[j] < P:
                    lstM[j] = P
    # 최대 이익들 합하기
    result = 0
    for x in lstM:
        result += x
    print("#{} {}".format(TC, result))