# A + B - 5

a = b = 1
result = ''
while a != 0 or b != 0:
    a, b = map(int, input().split())
    if a + b != 0:
        result += str(a + b) + "\n"
    else:
        result += ''

print(result)
