# View
for TC in range(1, 11):
    N = int(input())
    lstB = list(map(int, input().split()))

    # 목표 : 각각의 빌딩의 주변에(2) 자신보다 더 큰 빌딩이 없음을 탐색

    # 결과값 초기화
    result = 0
    for i in range(2, N-2):
        # 자신을 기준으로 2만큼 거리에 자신보다 큰 건물이 없는 경우
        if lstB[i-1] < lstB[i] and lstB[i+1] < lstB[i] and lstB[i-2] < lstB[i] and lstB[i+2] < lstB[i]:
            # 자신의 2만큼 떨어진 거리에 있는 건물중 가장 큰 건물의 길이 초기화 (자신제외)
            submaxV = 0
            for j in range(i-2, i):
                if lstB[j] > submaxV:
                    submaxV = lstB[j]
            for j in range(i+1, i+3):
                if lstB[j] > submaxV:
                    submaxV = lstB[j]
            result += lstB[i] - submaxV

    print("#{} {}".format(TC, result))