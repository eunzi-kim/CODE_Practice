# 삼성시의 버스 노선

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 버스 노선 정보
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    P = int(input())
    # 버스 정류장 초기화
    Stop = [0] * 5000
    # 버스 정류장 정보 담기
    for j in range(N):
        for k in range(A[j]-1, B[j]):
            Stop[k] += 1
    # 결과값 초기화
    result = ""
    for _ in range(P):
        C = int(input())
        result += str(Stop[C-1]) + " "
    print("#{} {}".format(TC, result))