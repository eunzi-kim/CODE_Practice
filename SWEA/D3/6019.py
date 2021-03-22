# 기차 사이의 파리

T = int(input())
for TC in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # h : 충돌까지의 시간
    h = D / (A + B)
    # (시간) * (파리의 속력) = (파리가 이동한 거리)
    print("#{} {}".format(TC, h*F))


