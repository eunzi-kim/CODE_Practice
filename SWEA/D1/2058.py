T = int(input())

result = 0
while T > 0:
    result += T % 10
    T = T // 10

print(result)