# 색종이

T = int(input())

# 도화지 초기화
Paper = [[0]*100 for _ in range(100)]

for TC in range(1, T+1):
    x, y = map(int, input().split())

    # 도화지에 색종이 올리기
    for j in range(x, x+10):
        for i in range(y, y+10):
            Paper[i][j] = 1

# 색종이 넓이 구하기
result = 0
for a in range(100):
    for b in range(100):
        if Paper[a][b]:
            result += 1

print(result)