T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    number_list = list(map(int, input().split()))
    numbers = sorted(number_list)

    result = ""
    for x in numbers:
        result += str(x) + " "
    print(f'#{test_case} {result}')