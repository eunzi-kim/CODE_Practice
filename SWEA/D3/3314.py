# 보충학습과 평균

T = int(input())
for TC in range(1, T+1):
    Score = list(map(int, input().split()))
    sumS = 0
    for x in Score:
        if x >= 40:
            sumS += x
        else:
            sumS += 40
    print("#{} {}".format(TC, sumS//5))