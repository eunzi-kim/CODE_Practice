# 회문1

import sys
sys.stdin = open("input.txt", "r")

for TC in range(1, 11):
    N = int(input())
    Board = [list(input()) for _ in range(8)]
    count = 0
    # 가로 회문 확인
    for i in range(8):
        for j in range(9-N):
            String = ""
            for k in range(N//2):
                if Board[i][j+k] == Board[i][j+N-1-k]:
                    String += Board[i][j+k]
            if len(String) == N//2:
                count += 1
    # 세로 회문 확인
    for i in range(8):
        for j in range(9-N):
            String = ""
            for k in range(N // 2):
                if Board[j+k][i] == Board[j+N-1-k][i]:
                    String += Board[i][j + k]
            if len(String) == N // 2:
                count += 1
    print("#{} {}".format(TC, count))