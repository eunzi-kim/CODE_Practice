# 현주의 상자 바꾸기

T = int(input())
for TC in range(1, T+1):
    N, Q = map(int, input().split())
    # 상자 숫자 리스트 초기화
    Arr = [0] * N
    # 상자 숫자 바꾸기
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            Arr[j] = i
    # 상자 숫자 리스트 스트링화 하기
    result = ""
    for x in Arr:
        result += str(x) + " "
    print("#{} {}".format(TC, result))
