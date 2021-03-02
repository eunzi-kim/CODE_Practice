import sys
sys.stdin = open("4875_input.txt", "r")

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    # 시작 위치 탐색
    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                start = i, j
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 스택과 방문기록 초기화
    Stack = []
    Visited = [[False]*N for _ in range(N)]
    # 스택 초기값
    Stack.append(start)
    i = 0
    # 길찾기 시작
    while Stack:
        # 현재 위치
        v = Stack.pop(-1)
        r = v[0]
        c = v[1]
        # 현재 위치 방문 기록
        Visited[r][c] = True
        # 결승점 탐색 성공
        if Maze[r][c] == 3:
            result = 1
            break
        # 현재 위치에서 상, 하, 좌, 우 살펴보며 미로 찾기
        for i in range(4):
            if 0 <= r + dr[i] < N and 0 <= c + dc[i] < N and not Visited[r+dr[i]][c+dc[i]] and Maze[r+dr[i]][c+dc[i]] != 1:
                Stack.append((r+dr[i], c+dc[i]))
        # 결승점 탐색 실패
        result = 0
    print("#{} {}".format(TC, result))