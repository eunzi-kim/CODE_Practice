T = int(input())
for TC in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 리스트 초기화
    GL = [[] for _ in range(V+1)]
    for e in range(E):
        s, f = map(int, input().split())
        # 인접 리스트 채우기
        GL[s].append(f)
    S, G = map(int, input().split())
    # 방문기록과 스택 초기화
    Visited = [False] * (V+1)
    Stack = []
    # 방문기록, 스택 초기값 삽입
    Stack.append(S)
    Visited[S] = True
    # 스택에 데이터가 존재하면 계속 진행
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