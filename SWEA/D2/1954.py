# 달팽이 숫자

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 달팽이 숫자 리스트 초기화
    S = [[0]*N for _ in range(N)]

    dr = [0, +1, 0, -1]
    dc = [+1, 0, -1, 0]
    i = 0

    # 초기값
    r = c = 0
    S[r][c] += 1
    
    # 달팽이 모양으로 수 키우기
    for x in range(2, N**2+1):
        r += dr[i]
        c += dc[i]
        S[r][c] += x

        # 직진을 계속 할 수 있는 경우
        if 0 <= r + dr[i] < N and 0 <= c + dc[i] < N and S[r+dr[i]][c+dc[i]] == 0:
            i = i
        
        # 직진이 막힌 경우
        # i값이 3인 경우 => i값은 다시 0으로 돌아가야함
        elif i == 3:
            i = 0
        # i값이 3이 아닌 경우 => i+1 값으로 가야함
        else:
            i += 1

    print(f'#{TC}')
    for s in S:
        print(*s)