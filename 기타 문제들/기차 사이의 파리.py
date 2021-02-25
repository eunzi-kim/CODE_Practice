T = int(input())
for TC in range(1, T+1):
    D, A, B, F = map(int, input().split())
    result = D / (A + B) * F
    print("#{} {}".format(TC, result))