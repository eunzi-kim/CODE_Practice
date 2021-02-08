# 윤년

T = int(input())

if T % 4 == 0 and T % 100 != 0:
    result = 1
elif T % 400 == 0:
    result = 1
else:
    result = 0

print(result)