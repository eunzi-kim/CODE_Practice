# 별 찍기 - 1

T = int(input())

for t in range(1, T+1):
    result = ''
    for x in range(t):
        result += '*'

    print(result)