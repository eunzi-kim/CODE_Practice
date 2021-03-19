# 의석이의 세로로 말해요

T = int(input())
for TC in range(1, T+1):
    # 문자열 리스트
    String = [list(input()) for _ in range(5)]
    # 가장 긴 문자열 탐색
    N = 0
    for i in range(5):
        if len(String[i]) > N:
            N = len(String[i])
    # 가장 긴 문자열을 기준으로 칠판 글자 리스트 작성
    # 빈 공간은 문자가 될 수 없는 '10'으로 작성
    Board = [['10']*N for _ in range(N)]
    for i in range(5):
        for j in range(N):
            if len(String[i]) > j:
                Board[i][j] = String[i][j]
    # '10'이 아닌 문자들 세로로 말하기
    result = ''
    for c in range(N):
        for r in range(5):
            if Board[r][c] != '10':
                result += Board[r][c]
    print("#{} {}".format(TC, result))