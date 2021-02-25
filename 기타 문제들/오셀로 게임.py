T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())

    # 보드 초기화
    Board = [[0]*(N+2) for _ in range(N+2)]
    Board[N//2][N//2] = 2
    Board[N//2+1][N//2+1] = 2
    Board[N//2+1][N//2] = 1
    Board[N//2][N//2+1] = 1

    # 흑돌 : 1, 백돌 : 2
    for m in range(M):
        x, y, color = map(int, input().split())

        # 돌 놓기
        Board[y][x] = color

        # 주변 살펴보며 상대방의 돌 찾기
        Enemy = []
        for i in range(-1, 2): # -1 0 1
            for j in range(-1, 2): # -1 0 1
                if Board[y+i][x+j] != 0 and Board[y+i][x+j] != color:
                    Enemy.append((i, j))


        # 상대방의 방향으로 탐색하며 나의 돌 찾기
        # => 나의 돌을 찾고, 그 곳까지 나로 변경하기
        for position in Enemy:
            r = y + position[0]
            c = x + position[1]
            Stack = []
            while Board[r][c] != 0:
                # 상대방의 돌이 나오는 경우
                # 상대방 돌의 좌표 스택에 push
                if Board[r][c] != color:
                    Stack.append((r, c))
                    r += position[0]
                    c += position[1]
                # 나의 돌이 나오는 경우
                # 스택에 있는 상대방의 돌의 좌표 이용하여
                # 자신 돌의 색으로 변경하기
                else:
                    for S in Stack:
                        Board[S[0]][S[1]] = color
                    break

    # 돌의 색 카운트
    Black = White = 0
    for i in range(N+1):
        for j in range(N+1):
            if Board[i][j] == 1:
                Black += 1
            elif Board[i][j] == 2:
                White += 1

    print("#{} {} {}".format(TC, Black, White))