# 수열

N = int(input())
numbers = list(map(int, input().split()))

maxC = 0
for i in range(N-1):
    count = 1
    for j in range(i, N-1):
        if numbers[j] <= numbers[j+1]:
            count += 1
        else:
            count = 0
        # print(count)
        if count > maxC:
            maxC = count
print(maxC)