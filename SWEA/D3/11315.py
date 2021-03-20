# 오목판정

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Board = [list(input()) for _ in range(N)]
    # Stack에 바둑알 좌표 넣기
    Stack = []
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 'o':
                Stack.append((i, j))
    # 결과값 초기화
    result = 'NO'
    while Stack:
        v = Stack.pop(0)
        r = v[0]
        c = v[1]
        cntR = cntC = cnt1 = cnt2 = 0
        for i in range(5):
            # 세로 판별
            if 0 <= r+i < N and Board[r+i][c] == 'o':
                cntC += 1
            # 가로 판별
            if 0 <= c+i < N and Board[r][c+i] == 'o':
                cntR += 1
            # 대각선 판별
            if 0 <= r+i < N and 0 <= c+i < N and Board[r+i][c+i] == 'o':
                cnt1 += 1
            if 0 <= r+i < N and 0 <= c-i < N and Board[r+i][c-i] == 'o':
                cnt2 += 1
        if cntR == 5 or cntC == 5 or cnt1 == 5 or cnt2 == 5:
            result = 'YES'
            break
    print("#{} {}".format(TC, result))