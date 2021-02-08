# 별 찍기 - 2

T = int(input())

for t in range(1, T+1):

    result = ''
    for x in range(1, t+1):
        result += ' ' * (T - x) + '*' * x + "\n"

print(result)