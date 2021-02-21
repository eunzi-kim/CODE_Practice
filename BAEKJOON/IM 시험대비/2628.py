# 종이 자르기

C, R = map(int, input().split()) # 가로, 세로 길이
N = int(input()) # 잘라야하는 점선의 개수

# 컷팅 리스트 초기화
lstC = [0] * N + [C]
lstR = [0] * N + [R]

for n in range(N):
    # 가로 컷팅 : 0, 세로 컷팅 : 1 => V
    V, M = map(int, input().split()) # M : 컷팅 점선 번호

    # 컷팅 리스트
    if V:
        lstC[n] = M
    else:
        lstR[n] = M

# 컷팅 리스트 크기순으로 정렬
for i in range(N-1):
    for j in range(i+1, N):
        if lstC[i] > lstC[j]:
            lstC[i], lstC[j] = lstC[j], lstC[i]
        if lstR[i] > lstR[j]:
            lstR[i], lstR[j] = lstR[j], lstR[i]

# 부분 넓이 구하기
c1 = c2 = 0
maxA = 0
for c in lstC:
    r1 = r2 = 0
    Area = 0
    if c:
        for r in lstR:
            if r:
                r2 = r
                c2 = c
                Area = (c2-c1)*(r2-r1)
                if maxA < Area:
                    maxA = Area
                r1 = r2
        c1 = c2
print(maxA)