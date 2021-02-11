# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

number = A * B * C
r_list = [0] * 10
for n in str(number):
    r_list[int(n)] += 1

for x in r_list:
    print(x)