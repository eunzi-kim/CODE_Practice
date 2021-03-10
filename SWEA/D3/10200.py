# 구독자 전쟁

T = int(input())
for TC in range(1, T+1):
    N, A, B = map(int, input().split())
    maxV = min(A, B)
    sumV = A + B
    if sumV <= N:
        minV = 0
    else:
        minV = sumV -  N
    print("#{} {} {}".format(TC, maxV, minV))