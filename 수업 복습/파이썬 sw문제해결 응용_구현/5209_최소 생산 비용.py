def perm(idx, money):
    global minV

    if idx == N:
        if minV > money:
            minV = money
        return
    if minV < money:
        return
    else:
        for i in range(N):
            if Visited[i] == 0:
                Visited[i] = 1
                perm(idx+1, money+Map[idx][i])
                Visited[i] = 0

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    Arr = [x for x in range(N)]
    Visited = [0] * N
    minV = 100000000000000
    perm(0, 0)
    print("#{} {}".format(TC, minV))