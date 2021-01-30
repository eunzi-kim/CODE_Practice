T = int(input())

# N이 5일 경우,
# 1 – 2 + 3 – 4 + 5 = 3

# N이 6일 경우,
# 1 – 2 + 3 – 4 + 5 – 6 = -3

a = map(int, input().split())

result = 0
for number in range(1, a+1):
    result += (-1 ** (number + 1)) * number

print(result) 