# 진기의 최고급 붕어빵

T = int(input())
for TC in range(1, T+1):
    N, M, K = map(int, input().split())
    G = list(map(int, input().split()))
    # 손님 순서대로 정렬
    G.sort()
    # 판매한 붕어빵 초기화
    Sold = 0
    # 붕어빵 판매 확인 리스트 초기화
    Check = [False] * N
    for i in range(N):
        # 손님이 왔을 때, 붕어빵이 있는지 확인
        # 만든 붕어빵 개수
        fishM = (G[i] // M) * K
        # 현재 붕어빵의 개수
        fish = fishM - Sold
        # 붕어빵 존재
        if fish >= 1:
            Sold += 1
            Check[i] = True
        # 붕어빵 없음
        else:
            Check[i] = False
            break
    # 결과 초기화
    result = 'Possible'
    # 붕어빵 판매 확인
    for j in range(N):
        if Check[j] == False:
            result = 'Impossible'
            break
    print("#{} {}".format(TC, result))