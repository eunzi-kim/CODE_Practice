# 자리배정

C, R = map(int, input().split())
K = int(input())

# 좌석 초기화
Seat = [[0]*C for _ in range(R)]

# 이동 변수
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

i = 0
r = c = 0
x = 1
while x <= C * R:
    Seat[r][c] = x
    r += dr[i]
    c += dc[i]
    x += 1
    if 0 <= r+dr[i] < R and 0 <= c+dc[i] < C and Seat[r+dr[i]][c+dc[i]] == 0:
        i = i
    elif i == 3:
        i = 0
    else:
        i += 1

if K > C * R:
    print(0)
else:
    for c in range(C):
        for r in range(R):
            if Seat[r][c] == K:
                print(c+1, r+1)