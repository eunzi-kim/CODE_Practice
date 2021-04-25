# 동철이의 일 분배
# 순열함수 이용
def perm(idx, p):
    global maxV

    if idx == N:
        if p > maxV:
            maxV = p
        return
    # 백트래킹
    if p * (100 ** (N-idx)) <= maxV:
        return
    else:
        for i in range(N):
            if Visited[i] == 0:
                Visited[i] = 1
                perm(idx+1, p*Map[idx][i])
                Visited[i] = 0

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    Visited = [0] * N
    maxV = 0
    perm(0, 1)
    result = round(maxV * (0.01) ** (N-1), 6)
    print("#{} {:6f}".format(TC, result))