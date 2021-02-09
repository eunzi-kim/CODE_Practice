T = int(input())

for test_case in range(1, T+1):
    a, b, c, d = map(int, input().split())

    h = a + c
    m = b + d

    if  m > 60:
        h += 1
        m -= 60

    if h > 12:
        h -= 12

    result = str(h) + ' ' + str(m)
    
    print(f'#{test_case} {result}')