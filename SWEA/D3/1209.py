# Sum

for TC in range(1, 11):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(100)]
    # 최대값 초기화
    maxV = 0
    # 행/열의 합 탐색
    for i in range(100):
        subS1 = subS2 = 0
        for j in range(100):
            subS1 += Arr[i][j]
            subS2 += Arr[j][i]
        if subS1 > maxV:
            maxV = subS1
        if subS2 > maxV:
            maxV = subS2
    # 대각선의 합 탐색
    subS3 = subS4 = 0
    for i in range(100):
        subS3 += Arr[i][i]
        subS4 += Arr[i][99-i]
    if subS3 > maxV:
        maxV = subS3
    if subS4 > maxV:
        maxV = subS4
    print("#{} {}".format(TC, maxV))

    print(maxV)