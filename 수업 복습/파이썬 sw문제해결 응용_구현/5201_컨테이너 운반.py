T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    # 결과값 초기화
    result = 0
    # 무게 인덱스 초기화
    i = 0
    # 가장 무거운 트럭부터 화물을 싣는다.
    for t in T:
        while i < len(W):
            if t >= W[i]:
                result += W[i]
                i += 1
                break
            i += 1
    print("#{} {}".format(TC, result))