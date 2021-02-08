# x보다 작은 수

n, x = map(int, input().split())

temp_n = list(map(int, input().split()))
result = ''
for number in temp_n:
    if number < x:
        result += str(number) + " "

print(result)