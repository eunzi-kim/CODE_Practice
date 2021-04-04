# 전봇대

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Pole = [list(map(int, input().split())) for _ in range(N)]
    # 개수 초기화
    count = 0
    # 전선 교차하는 개수 구하기
    for i in range(N):
        for j in range(N):
            if Pole[i][0] > Pole[j][0] and Pole[i][1] < Pole[j][1]:
                count += 1
            elif Pole[i][0] < Pole[j][0] and Pole[i][1] > Pole[j][1]:
                count += 1
    # 중복되는 전선수 제외하기 위해 2로 나누기
    print("#{} {}".format(TC, count//2))