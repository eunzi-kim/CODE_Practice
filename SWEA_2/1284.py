T = int(input())

for test_case in range(1, T+1):
    p, q, r, s, w = map(int, input().split())

    a = p * w
    if w > r:
        b = q + (w - r) * s
    else:
        b = q

    if a > b:
        result = b
    else:
        result = a

    print(f'#{test_case} {result}')
