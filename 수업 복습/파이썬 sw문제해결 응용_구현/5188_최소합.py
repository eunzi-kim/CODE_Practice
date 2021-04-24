T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    # BFS 이용!!
    start = (0, 0)
    # Queue 초기화
    Queue = [start]
    # 시작점부터 최소 합계 리스트
    Dis = [[1000000000]*N for _ in range(N)]
    Dis[0][0] = Map[0][0]
    # 하 우
    dr = [1, 0]
    dc = [0, 1]
    while Queue:
        v = Queue.pop(0)
        r = v[0]
        c = v[1]
        # 현재 위치의 최소 합
        x = Dis[r][c]
        for i in range(2):
            newR = r+dr[i]
            newC = c+dc[i]
            if 0 <= newR < N and 0 <= newC < N and Dis[newR][newC] > x + Map[newR][newC]:
                Dis[newR][newC] = x + Map[newR][newC]
                Queue.append((newR, newC))
    # 도착 최소 합
    result = Dis[N-1][N-1]
    print("#{} {}".format(TC, result))