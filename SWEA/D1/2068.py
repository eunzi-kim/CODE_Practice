T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #
    a, b, c, d, e, f, g, h, i, j = map(int, input().split())
    max_val = 0
    for x in a, b, c, d, e, f, g, h, i, j:
        if x > max_val:
            max_val = x
    print(f'#{test_case} {max_val}')