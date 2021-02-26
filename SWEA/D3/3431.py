# 준환이의 운동관리
T = int(input())
for TC in range(1, T+1):
    L, U, X = map(int, input().split())
    # 운동 시간 초과
    if X > U:
        result = -1
    # 운동 시간 적정
    elif L <= X and X <= U:
        result = 0
    # 운동 시간 부족
    else:
        result = L - X
    print("#{} {}".format(TC, result))