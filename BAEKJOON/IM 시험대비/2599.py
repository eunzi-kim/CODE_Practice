# 수열
# 두 포인터 사용하기!!
N, K = map(int, input().split())
Temp = list(map(int, input().split()))

# 체온들의 K만큼 모든 합 구하기

i = 0
sumT = sum(Temp[i:K+i])
# 가장 높은 체온값 초기화
maxT = sumT
while i + K < N:
    sumT = sumT - Temp[i] + Temp[K+i]
    i += 1

    # 가장 높은 체온 구하기
    if maxT < sumT:
        maxT = sumT

print(maxT)