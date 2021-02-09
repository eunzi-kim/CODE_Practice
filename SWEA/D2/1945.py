T = int(input())

count = 0
for test_case in range(1, T+1):
    test_case = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
     
    result = ''
    count += 1
    while test_case > 1:
        if test_case % 2 == 0:
            test_case = test_case // 2
            a += 1
        elif test_case % 3 == 0:
            test_case = test_case // 3
            b += 1
        elif test_case % 5 == 0:
            test_case = test_case // 5
            c += 1
        elif test_case % 7 == 0:
            test_case = test_case // 7
            d += 1
        elif test_case % 11 == 0:
            test_case = test_case // 11
            e += 1

    result = str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(e)

    print(f'#{count} {result}')