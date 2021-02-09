T = int(input())

# N이 5일 경우,
# 1 – 2 + 3 – 4 + 5 = 3

# N이 6일 경우,
# 1 – 2 + 3 – 4 + 5 – 6 = -3

for test_case in range(1, T + 1):
    test_case = int(input())

    result = 0
    for number in range(1, test_case+1):
        result += (-1) ** (number+1) * number

    print(f'#{test_case} {result}') 