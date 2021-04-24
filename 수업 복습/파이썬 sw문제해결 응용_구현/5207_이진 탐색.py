def binary(x, l, r):
    global past

    m = (l+r)//2
    if x == A[m]:
        return 1
    elif A[m] < x:
        if past == 'right':
            return 0
        else:
            past = 'right'
            return binary(x, m + 1, r)
    else:
        if past == 'left':
            return 0
        else:
            past = 'left'
            return binary(x, l, m - 1)


T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    count = 0
    for b in B:
        past = ''
        if binary(b, 0, N-1):
            count += 1
    print("#{} {}".format(TC, count))