# 나머지

number = [0] * 42
for tc in range(10):
    x = int(input())
    number[x % 42] += 1

count = 0
for y in number:
    if y >= 1:
        count += 1

print(count)