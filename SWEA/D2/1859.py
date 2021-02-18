# 백만 장자 프로젝트
T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Money = list(map(int, input().split()))

    for i in range(1 << N): # i = 0 1 2 3 4 5 6 7
        sumM = 0
        for j in range(N): # j = 0 1 2
            if i & (j << N):
                print(j)