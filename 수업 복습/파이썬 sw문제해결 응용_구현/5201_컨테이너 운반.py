T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    i = 0
    result = 0
    for t in T:
        while i < len(W):
            if t >= W[i]:
                result += W[i]
                i += 1
                break
            i += 1
    print("#{} {}".format(TC, result))
