# 평균

T = int(input())
scores = list(map(int, input().split()))

M = 0
for score in scores:
    if score > M:
        M = score

sum = 0
for score in scores:
    sum += score / M * 100
    
result = sum / T

print(result)