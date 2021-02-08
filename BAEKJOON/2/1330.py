# 두 수 비교하기

a, b = map(int, input().split())

if a > b:
    result = ">"
elif a < b:
    result = "<"
else:
    result = "=="

print(result)