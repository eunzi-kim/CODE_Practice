# 가장 빠른 문자열 타이핑

T = int(input())
for TC in range(1, T+1):
    A, B = input().split()

    N = len(A)
    M = len(B)

    i = 0
    count = 0
    while N > i:
        if i + M <= N:
            strA = ''
            for j in range(i, i+M):
                strA += A[j]
            # A의 문자 중 길이가 M인 문자열과 B가 같은 경우
            if strA == B:
                i += M
                count += 1
        # A의 문자 중 길이가 M인 문자열과 B가 다른 경우
            else:
                i += 1
        else:
            i += 1

    # A의 길이에서 사용된 B의 개수 더하고,
    # 그 개수만큼의 길이 M 빼기
    result = N + (1 - M) * count

    print('#{} {}'.format(TC, result))