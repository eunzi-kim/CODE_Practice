# 영준이와 신비한 뿔의 숲

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    twin = N - M
    uni = M - twin
    print("#{} {} {}".format(TC, uni, twin))