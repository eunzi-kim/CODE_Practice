# 햄버거 다이어트
T = int(input())
for TC in range(1, T+1):
    N, L = map(int, input().split())
    T = []
    K = []
    result = 0
    for n in range(N):
        Ti, Ki = map(int, input().split())
        T.append(Ti)
        K.append(Ki)
    for i in range(1 << N):
        sumK = sumT = 0
        for j in range(N):
            if i & (1 << j):
                sumK += K[j]
                sumT += T[j]
        if sumK <= L:
            if sumT > result:
                result = sumT
    print("#{} {}".format(TC, result))

'''
Powerset 다시 생각해보기!!
'''