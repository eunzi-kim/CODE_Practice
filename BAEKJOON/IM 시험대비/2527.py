# 직사각형

for tc in range(4):
    A = list(map(int, input().split()))
    # 최대값 구하기
    maxV = 0
    for a in A:
        if maxV < a:
            maxV = a
    # 격자공간 초기화
    Space = [[0] * (maxV + 1) for _ in range(maxV + 1)]
    # 격자공간에 사각형 그리기
    for i in range(A[0], A[2]+1):
        for j in range(A[1], A[3]+1):
            Space[i][j] += 1
    count = 0
    for k in range(A[4], A[6]+1):
        for l in range(A[5], A[7]+1):
            Space[k][l] += 1
            if Space[k][l] == 2:
                count += 1
    # 공통부분이 없음
    if count == 0:
        result = 'd'
    else:
        # 점
        if count == 1:
            result = 'c'
        # 선분
        elif A[0] == A[6]:
            result = 'b'
        elif A[4] == A[2]:
            result = 'b'
        elif A[1] == A[7]:
            result = 'b'
        elif A[5] == A[3]:
            result = 'b'
        # 직사각형
        else:
            result = 'a'
    print(result)