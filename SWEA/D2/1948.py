# 날짜 계산기

T = int(input())
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())

    d_31 = [1, 3, 5, 7, 8, 10, 12]
    d_30 = [4, 6, 9, 11]
    d_28 = [2]

    result = 0
    if a != c:
        while a < c:
            c -= 1
            if c in d_31:
                d += 31
            elif c in d_30:
                d += 30
            else:
                d += 28

    result = d - b + 1

    print(f'#{tc} {result}')


    