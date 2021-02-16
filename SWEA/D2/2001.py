# 파리 퇴치
T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    Flies = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    # 사각형의 가장 앞 꼭짓점 탐색
    for r in range(N-M+1):
        for c in range(N-M+1):

            sumF = 0
            # 사각형의 좌표값 탐색
            for i in range(M):
                for j in range(M):
                    sumF += Flies[r+i][c+j]

            if maxV < sumF:
                maxV = sumF

    print('#{} {}'.format(TC, maxV))