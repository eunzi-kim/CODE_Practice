# 농작물 수확하기

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Crop = [list(map(int, input())) for _ in range(N)]
    # 가운데 ~ 처음
    result = 0
    for r in range(0, N//2+1):
        for c in range(N//2-r, N//2+r+1):
            result += Crop[r][c]
    # 가운데 밑부터 마지막까지
    for r in range(N-1, N//2, -1):
        for c in range(N//2-(N-r-1), N//2+(N-r)):
            result += Crop[r][c]
    print("#{} {}".format(TC, result))