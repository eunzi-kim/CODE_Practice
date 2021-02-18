# 0218 복습
# 회문2

# import sys
# sys.stdin = open("input.txt", "r")

def chk(M):
    for i in range(100):
        # 시작점 탐색
        for j in range(101 - M):

            # 가로 방향 기준 탐색
            pos = 0
            # 문자열의 시작점과 끝점이 가운데로 모이면서 회문 탐색
            while pos < M // 2 and P[i][j + pos] == P[i][j + M - 1 - pos]:
                pos += 1
            if pos == M // 2:
                return 1

            # 세로 방향 기준 탐색
            pos = 0
            # 문자열의 시작점과 끝점이 가운데로 모이면서 회문 탐색
            while pos < M // 2 and P[j + pos][i] == P[j + M - 1 - pos][i]:
                pos += 1
            if pos == N // 2:
                return 1

    # 회문이 안 되는 경우
    return 0


for TC in range(10):
    T = int(input())
    P = [[x for x in input()] for _ in range(100)]


    # 문자열의 길이 100부터 줄여가면서 회문 찾기 => 찾으면 break!
    result = 0
    for N in range(100, 0, -1):
        if chk(N):
            result = N
            break
    print('#{} {}'.format(T, result))

