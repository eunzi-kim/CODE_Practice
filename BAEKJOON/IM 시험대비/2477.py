# 참외밭

N = int(input())

D = [0] * 12
L = [0] * 12

# 가장 큰 사각형의 가로, 세로값 초기화
w = h = 0

for a in range(6):
    d, l = map(int, input().split())
    D[a] = d
    D[a+6] = d
    L[a] = l
    L[a+6] = l

    # 가장 큰 사각형 넓이
    if d >= 3 and w < l:
        w = l
    if d < 3 and h < l:
        h = l
    maxA = w * h

# 떼어 내야할 사각형의 넓이
for b in range(1, 10):
    if D[b] == D[b+2] and D[b-1] == D[b+1]:
        maxS = L[b] * L[b+1]

# 진짜 참외밭의 넓이
S = maxA - maxS

# 참외의 개수
result = S * N

print(result)