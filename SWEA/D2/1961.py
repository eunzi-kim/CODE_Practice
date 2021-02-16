# 숫자 배열 회전
T = int(input())
for TC in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    # 결과 리스트 초기화
    result = [['']*N for _  in range(N)]

    # 90도 회전
    for r in range(N-1, -1, -1):
        for c in range(N):
            result[c][0] += str(numbers[r][c])

    # 180도 회전
    for c in range(N-1, -1, -1):
        for r in range(N-1, -1, -1):
            result[N-r-1][1] += str(numbers[r][c])

    # 270도 회전
    for r in range(N):
        for c in range(N-1, -1, -1):
            result[N-c-1][2] += str(numbers[r][c])

    # 결과 리스트 str으로 변경
    num = ''
    for x_lst in result:
        num += '\n'
        for n in x_lst:
            num += n + " "

    print('#{} {}'.format(TC, num))
