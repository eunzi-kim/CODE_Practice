T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    q = a // b
    r = a % b
    print(f'#{test_case} {q} {r}')

