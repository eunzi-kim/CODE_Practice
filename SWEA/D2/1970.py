T = int(input())

for test_case in range(1, T+1):
    x = int(input())
    result = ''
    count = 0
    while count <= 7:
        if count == 0:
            if x // 50000 == 0:
                result += '0' + ' '
            else:
                result += str(x // 50000) + ' '
                x = x % 50000
            count += 1
        elif count == 1:
            if x // 10000 == 0:
                result += '0' + ' '
            else:
                result += str(x // 10000) + ' '
                x = x % 10000
            count += 1
        elif count == 2:
            if x // 5000 == 0:
                result += '0' + ' '
            else:
                result += str(x // 5000) + ' '
                x = x % 5000
            count += 1
        elif count == 3:
            if x // 1000 == 0:
                result += '0' + ' '
            else:
                result += str(x // 1000) + ' '
                x = x % 1000
            count += 1
        elif count == 4:
            if x // 500 == 0:
                result += '0' + ' '
            else:
                result += str(x // 500) + ' '
                x = x % 500
            count += 1
        elif count == 5:
            if x // 100 == 0:
                result += '0' + ' '
            else:
                result += str(x // 100) + ' '
                x = x % 100
            count += 1
        elif count == 6:
            if x // 50 == 0:
                result += '0' + ' '
            else:
                result += str(x // 50) + ' '
                x = x % 50
            count += 1
        elif count == 7:
            if x < 10:
                result += '0'
            else:
                result += str(x // 10) + ' '
                x = x % 10
            count += 1
            
    print(f'#{test_case}\n{result}')