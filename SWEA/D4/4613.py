# 러시아 국기 같은 깃발

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    Flag = [list(input()) for _ in range(N)]
    # 깃발 변경 개수 초기화
    change = M * N
    # 하얀색 깃발 변경 탐색
    white = 0
    for w in range(N-2):
        for i in range(M):
            if Flag[w][i] != 'W':
                white += 1
        # 파란색 깃발 변경 탐색
        blue = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if Flag[b][j] != 'B':
                    blue += 1
            # 빨간색 깃발 변경 탐색
            red = 0
            for r in range(b+1, N):
                for k in range(M):
                    if Flag[r][k] != 'R':
                        red += 1
            # 깃발 변경 탐색
            count = white + blue + red
            # 최소 깃발 변경 탐색
            if count < change:
                change = count
    print("#{} {}".format(TC, change))