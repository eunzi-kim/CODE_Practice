# 순열함수
def perm(idx):
    global result

    if idx == N:
        sumV = 0
        for i in range(N):
            sumV += Map[Arr[i-1]][Arr[i]]
        if result > sumV:
            result = sumV
    else:
        for i in range(N):
            if Visited[i] == 0:
                Visited[i] = 1
                Arr[idx] = i
                perm(idx+1)
                Visited[i] = 0

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    Visited = [0] * N
    Visited[0] = 1
    Arr = [x for x in range(N)]
    # 최소합
    result = 1000000000000
    perm(1)
    print("#{} {}".format(TC, result))