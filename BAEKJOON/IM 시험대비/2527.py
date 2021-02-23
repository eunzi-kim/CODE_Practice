# 직사각형

for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    maxV = max(x1, y1, p1, q1, x2, y2, p2, q2)
    # 격자공간 초기화
    Space = [[0] * (maxV + 1) for _ in range(maxV+1)]

    # 격자공간에 사각형 그리기
    for i in range(x1, p1+1):
        for j in range(y1, q1+1):
            Space[i][j] += 1
    count = 0
    for k in range(x2, p2+1):
        for l in range(y2, q2+1):
            Space[k][l] += 1
            if Space[k][l] == 2:
                count += 1

    # count = 0
    # for a in range(maxV+1):
    #     for b in range(len(maxV+1):
    #         if Space[a][b] == 2:
    #             count += 1

    if count > 0:
        # 점
        if count == 1:
            result = 'c'
        # 선분
        elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
            result = 'b'
        # 직사각형
        else:
            result = 'a'
    else:
        # 공통부분이 없음
        result = 'd'

    print(result)