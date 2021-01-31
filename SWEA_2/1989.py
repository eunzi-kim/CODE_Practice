T = int(input())

count = 0
for test_case in range(1, T+1):
    test_case = input()
    count += 1

    reverse = ''
    for idx in range(len(test_case)-1, -1, -1):
        reverse += test_case[idx]

    if reverse == test_case:
        result = 1

    else:
        result = 0

    print(f'#{count} {result}')