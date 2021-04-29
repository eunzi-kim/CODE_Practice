# 파도반 수열

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 수열 배열 리스트 초기화
    Arr = [1, 1, 1]
    # 배열 안에 3개의 숫자가 들어있으므로 N-3까지 반복
    # Arr에 수열 추가
    for i in range(N-3):
        newN = Arr[i] + Arr[i+1]
        Arr.append(newN)
    # N번째 배열의 값이 결과
    result = Arr[N-1]
    print("#{} {}".format(TC, result))
