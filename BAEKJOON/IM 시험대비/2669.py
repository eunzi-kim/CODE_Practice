# 직사각형 네개의 합집합의 면적 구하기

# 그래프 초기화
G = [[0]*100 for _ in range(100)]

for TC in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 직사각형 넓이 = 1로 표현
    for i in range(x1, x2):
        for j in range(y1, y2):
            if G[j][i] == 0:
                G[j][i] += 1

# 1의 개수 구하기
# = 직사각형이 차지하는 면적
val = 0
for g in G:
    for x in g:
        if x == 1:
            val += 1

print(val)