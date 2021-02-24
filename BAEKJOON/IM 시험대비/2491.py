# 수열

N = int(input())
Arr = list(map(int, input().split()))

count = 1
countR = 1
maxV = 0
for i in range(N-1):
    # 정방향
    if Arr[i] <= Arr[i+1]:
        count += 1
        if maxV < count:
            maxV = count
    else:
        count = 1
    # 역방향
    if Arr[i] >= Arr[i+1]:
        countR += 1
        if maxV < countR:
            maxV = countR
    else:
        countR = 1

print(maxV)