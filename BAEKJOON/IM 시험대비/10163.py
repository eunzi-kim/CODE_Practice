# 색종이

# 평면 초기화
BG = [[0]*101 for _ in range(101)]

N = int(input())
for a in range(1, N+1):
    x, y, w, h = map(int, input().split())

    # 색종이 올리기
    for c in range(x, x+w):
        for r in range(y, y+h):
            BG[r][c] = a

# 색종이의 각각 보이는 면적값 구하기
for b in range(1, N+1):
    # 면적값 초기화
    Area = 0
    for i in range(101):
        for j in range(101):
            if BG[i][j] == b:
                Area += 1

    print(Area)