T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   

for test_case in range(1, T + 1):
    result = 0
    a, b, c, d, e, f, g, h, i, j = map(int, input().split())
    for x in a, b, c, d, e, f, g, h, i, j:
        if x % 2 != 0:
            result += x
    print(f'#{test_case} {result}')
