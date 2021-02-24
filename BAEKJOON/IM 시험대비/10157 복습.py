# 자리배정
C, R = map(int, input().split())
K = int(input())

# 좌석 초기화
Seat = [[0]*C for _ in range(R)]

# 이동 변수
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

x = 1
r = c = 0
i = 0
while x <= C*R:
    Seat[r][c] = x
    r += dr[i]
    c += dc[i]
    x += 1
    if 0 <= r+dr[i] < R and 0 <= c+dc[i] < C and Seat[r+dr[i]][c+dc[i]] == 0:
        r = r
        c = c
    elif i == 3:
        i = 0
    else:
        i += 1

if K > C*R:
    print(0)
else:
    for j in range(R):
        for i in range(C):
            if Seat[j][i] == K:
                I = i + 1
                J = j + 1
    print(I, J)