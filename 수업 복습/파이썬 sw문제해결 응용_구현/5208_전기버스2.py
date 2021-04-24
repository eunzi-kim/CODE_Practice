def bfs(now, count):
    global minV

    if now >= N:
        if minV > count:
            minV = count
        return

    if count > minV:
        return

    for i in range(now+M[now], now, -1):
        bfs(i, count+1)

T = int(input())
for TC in range(1, T+1):
    M = list(map(int, input().split()))
    N = M[0]
    minV = N
    bfs(1, 0)
    print("#{} {}".format(TC, minV-1))