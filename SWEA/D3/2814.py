# 최장 경로
# 경로 탐색
def search(x, count):
    global result

    if count > result:
        result = count

    Visited[x] = 1
    for w in G[x]:
        if Visited[w] == 0:
            search(w, count+1)
    # 다음 반복을 위한 초기화
    Visited[x] = 0

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    # 인접 그래프
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    Visited = [0]*(N+1)
    result = 0
    for i in range(N):
        search(i, 1)
    print("#{} {}".format(TC, result))