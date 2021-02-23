# 0223 복습

T = int(input())
for TC in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 리스트 초기화
    GL = [[] for _ in range(V+1)]
    # 인접 리스트 입력
    for a in range(E):
        s, e = map(int, input().split())
        GL[s].append(e)

    S, G = map(int, input().split())

    # 스택과 방문기록 초기화
    Stack = []
    Visited = [False] * (V + 1)
    # 스택과 방문기록 초기값 입력
    Stack.append(S)
    Visited[S] = True

    while Stack:
        v = Stack.pop(-1)
        Visited[v] = True

        if v == G:
            result = 1
            break

        for x in GL[v]:
            if not Visited[x]:
                Stack.append(x)

        result = 0
        
    print("#{} {}".format(TC, result))