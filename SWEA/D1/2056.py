#  ”YYYY/MM/DD”형식으로 출력하고,

# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

T = int(input())

count = 0
for test_case in range(1, T+1):
    test_case = input()

    y, m, d = test_case[:4], test_case[4:6], test_case[6:]

    m_31 = [1, 3, 5, 7, 8, 10, 12]
    m_30 = [4, 6, 9, 11]
    m_28 = [2]

    count += 1

    if int(m) in m_31:
        if 0 <= int(d) <= 31:
            result = f'{y}/{m}/{d}'
        else:
            result = -1
    elif int(m) in m_30:
        if 0 <= int(d) <= 30:
            result = f'{y}/{m}/{d}'
        else:
            result = -1
    elif int(m) in m_28:
        if 0 <= int(d) <= 28:
            result = f'{y}/{m}/{d}'
        else:
            result = -1
    else:
        result = -1

    print(f'#{count} {result}')