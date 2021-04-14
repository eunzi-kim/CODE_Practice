# 최대 상금

T = int(input())
for TC in range(1, T+1):
    number, N = map(int, input().split())
    M = len(str(number)) # 숫자판의 길이
    Num = [str(number)]
    # N번 반복하며 모든 숫자판의 경우 탐색
    for _  in range(N):
        # 현재 숫자판
        Pan = Num
        # N번째의 모든 숫자판 넣기
        Num = []
        for X in Pan:
            # 모든 자리 변경
            for i in range(M-1):
                for j in range(i+1, M):
                    # i와 j의 자리 변경
                    money = X[:i] + X[j] + X[i+1:j] + X[i] + X[j+1:]
                    if money not in Num:
                        Num.append(money)
        # Num 중에서 가장 큰 상금 탐색
        result = 0
        for x in Num:
            if result < int(x):
                result = int(x)
    print("#{} {}".format(TC, result))