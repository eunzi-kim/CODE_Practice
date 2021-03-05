# 러시아 국기 같은 깃발

import sys
sys.stdin = open("4613_input.txt", "r")

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    Flag = [list(input()) for _ in range(N)]
    # 변경 최소값은 모든 칸의 수보다는 작으므로
    # 최소값의 초기화를 모든 칸의 수로
    minV = N*M
    # 하얀색으로 변경
    W_chg = 0
    for w in range(N-2):
        for i in range(M):
            if Flag[w][i] != "W":
                W_chg += 1
        # 파란색으로 변경
        B_chg = 0
        for b in range(w+1, N-1):
            for i in range(M):
                if Flag[b][i] != "B":
                    B_chg += 1
            # 빨간색으로 변경
            R_chg = 0
            for r in range(b+1, N):
                for i in range(M):
                    if Flag[r][i] != "R":
                        R_chg += 1
            # 최소값 구하기
            if minV > W_chg + B_chg + R_chg:
                minV = W_chg + B_chg + R_chg
    print("#{} {}".format(TC, minV))