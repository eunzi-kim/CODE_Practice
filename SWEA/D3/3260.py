# 두 수의 덧셈

T = int(input())
for TC in range(1, T+1):
    A, B = map(int, input().split())
    print("#{} {}".format(TC, A+B))