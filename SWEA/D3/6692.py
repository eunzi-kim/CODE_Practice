# 다솔이의 월급 상자

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    sumA = 0
    for _ in range(N):
        pi, xi = map(float, input().split())
        sumA += pi * xi
    print("#{} {}".format(TC, sumA))