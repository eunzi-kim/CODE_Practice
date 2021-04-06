# 문자열 교집합

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    A = set(input().split())
    B = set(input().split())
    # & : 교집합
    result = len(A & B)
    print("#{} {}".format(TC, result))