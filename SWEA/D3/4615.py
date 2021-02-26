# 재미있는 오셀로 게임

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    # 보드판 초기화
    Board = [[0]*(N+2) for _ in range(N+2)]
    Board[N//2][N//2] = 2
    Board[N//2+1][N//2+1] = 2
    Board[N//2+1][N//2] = 1
    Board[N//2][N//2+1] = 1
    for m in range(M):
        x, y, color = map(int, input().split())
        # 돌 놓기
        Board[y][x] = color
        # 놓은 돌의 주변 탐색하며 상대방의 돌 찾기
        # 상대방의 돌로 가는 방향 모으기
        enemyD = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if Board[y+i][x+j] != 0 and Board[y+i][x+j] != color:
                    enemyD.append((i, j))
        # 상대방의 돌로 가는 방향으로 직진하며 좌표 스택에 추가
        # 나의 돌을 발견했을때 중지하고 사이에 있던 상대방의 돌 내 돌로 변경
        for position in enemyD:
            r = y + position[0]
            c = x + position[1]
            Stack = []
            while Board[r][c] != 0:
                # 상대방의 돌이 나왔을 때,
                if Board[r][c] != color:
                    Stack.append((r, c))
                    r += position[0]
                    c += position[1]
                # 내 돌이 나왔을 때,
                else:
                    for S in Stack:
                        Board[S[0]][S[1]] = color
                    break
    # 돌의 색 구분하기
    black = white = 0
    for i in range(N+2):
        for j in range(N+2):
            if Board[i][j] == 1:
                black += 1
            elif Board[i][j] == 2:
                white += 1
    print("#{} {} {}".format(TC, black, white))