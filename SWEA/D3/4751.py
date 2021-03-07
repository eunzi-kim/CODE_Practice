# 다솔이의 다이아몬드 장식

T = int(input())
for TC in range(1, T+1):
    String = list(input())
    N = len(String)
    # 다이아몬드 초기화
    Dia = [['.']*(4 * N + 1) for _ in range(5)]
    # 0행, 4행
    for c in range(2, 4 * N + 1, 4):
        Dia[0][c] = "#"
        Dia[4][c] = "#"
        # 중앙 행 문자열 넣기
        v = String.pop(0)
        Dia[2][c] = v
    # 1행, 3행
    for c in range(1, 4 * N + 1, 2):
        Dia[1][c] = "#"
        Dia[3][c] = "#"
    # 중앙 행
    for c in range(0, 4 * N + 1, 4):
        Dia[2][c] = "#"
    # 리스트를 문자형으로 변환
    result = ""
    for i in range(5):
        for j in range(4 * N + 1):
            result += Dia[i][j]
        if i < 4:
            result += "\n"
    print(result)