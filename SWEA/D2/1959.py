# 두 개의 숫자열
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # N = len(Ai) / M = len(Bj)
    
    # Ai의 개수가 Bj의 개수보다 작거나 같은 상황
    if N <= M:
        sum_v = [0] * (M-N+1)        
        for j in range(M-N+1):
            sums = 0
            for i in range(N):
                sums += Ai[i] * Bj[i+j]
            sum_v[j] += sums

    # Ai의 개수가 Bj의 개수보다 큰 상황
    else:
        sum_v = [0] * (N-M+1)
        for i in range(N-M+1):
            sums = 0
            for j in range(M):
                sums += Ai[i+j] * Bj[j]
            sum_v[i] += sums

    max_v = 0
    for a in sum_v:
        if max_v < a:
            max_v = a
    print(f'#{tc} {max_v}')