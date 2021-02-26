# 창고 다각형

N = int(input())
lstL = []
lstH = []
for n in range(N):
    L, H = map(int, input().split())
    lstL.append(L)
    lstH.append(H)
# 리스트들 번호순으로 정렬
maxV = 0
for i in range(N-1):
    for j in range(i+1, N):
        if lstL[i] > lstL[j]:
            lstL[i], lstL[j] = lstL[j], lstL[i]
            lstH[i], lstH[j] = lstH[j], lstH[i]
# 가장 높은 건물의 높이 구하기
maxH = maxHI = 0
maxEH = maxEHI = 0
for i in range(N):
    if lstH[i] > maxH:
        maxH = lstH[i] # 가장 높은 첫 건물의 높이
        maxHI = i # 가장 높은 첫 건물의 인덱스
    if lstH[i] >= maxH:
        maxEHI = i  # 가장 높은 마지막 건물의 인덱스
# 넓이 초기화
Area = 0
# 왼쪽에서부터 넓이 구하기
w = 0
h = lstH[0]
for j in range(maxHI):
    w = lstL[j+1] - lstL[j]
    Area += w * h
    if h < lstH[j+1]:
        h = lstH[j+1]
# 오른쪽에서부터 넓이 구하기
w = 0
h = lstH[N-1]
for j in range(N-1, maxEHI, -1):
    w = lstL[j] - lstL[j-1]
    Area += w * h
    if h < lstH[j-1]:
        h = lstH[j-1]
# 가장 큰 높이의 빌딩들 넓이 구하기
w = lstL[maxEHI] - lstL[maxHI]
Area += h * (w + 1)
print(Area)