# 창고 다각형

N = int(input())
lstL = [0] * N
lstH = [0] * N
for n in range(N):
    L, H = map(int, input().split())

    lstL[n] = L
    lstH[n] = H

# 위치순으로 lstL, lstH 정렬
for i in range(N-1):
    for j in range(i, N):
        if lstL[i] > lstL[j]:
            lstL[i], lstL[j] = lstL[j], lstL[i]
            lstH[i], lstH[j] = lstH[j], lstH[i]

# 가장 긴 막대 구하기
maxH = maxI1 = maxI2 = 0
for h in range(N):
    if lstH[h] > maxH:
        maxH = lstH[h]
        maxI1 = h
    if lstH[h] >= maxH:
        maxH = lstH[h]
        maxI2 = h

# 막대 길이 비교하며 넓이 구하기
result = 0
# 가장 긴 막대를 기준으로 왼쪽부터 넓이 구하기
k = pos1 = 0
x = y = 0
while k+pos1 <= maxI1:
    if lstH[k] < lstH[k+pos1]:
        x = lstL[k+pos1] - lstL[k]
        y = lstH[k]
        k += pos1
        pos1 += 1
        result += x * y
    else:
        pos1 += 1
# 가장 긴 막대를 기준으로 오른쪽부터 넓이 구하기
l = N-1
pos2 = x = y = 0
while l-pos2 >= maxI2:
    if lstH[l] < lstH[l-pos2]:
        x = lstL[l] - lstL[l-pos2]
        y = lstH[l]
        l -= pos2
        pos2 += 1
        result += x * y
    else:
        pos2 += 1

# 가징 긴 막대의 넓이 구하기
s = lstL[maxI2] - lstL[maxI1] + 1
result += s * maxH

print(result)