# 빙고

Bingo = [list(map(int, input().split())) for _ in range(5)]
Number = []
for n in range(5):
    Number += input().split()

# 사회자가 부르는 수를 차례로 지우기
x = 0
while x < 25:
    for i in range(5):
        for j in range(5):
            if int(Number[x]) == Bingo[i][j]:
                Bingo[i][j] = 0
    x += 1

    # 빙고 찾기
    # 가로줄
    countC = 0
    for i in range(5):
        sumC = 0
        for j in range(5):
            sumC += Bingo[i][j]
        if sumC == 0:
            countC += 1

    # 세로줄
    countR = 0
    for j in range(5):
        sumR = 0
        for i in range(5):
            sumR += Bingo[i][j]
        if sumR == 0:
            countR += 1

    # 대각선
    sumL1 = sumL2 = 0
    countL1 = countL2 = 0
    for i in range(5):
        sumL1 += Bingo[i][i]
        sumL2 += Bingo[i][4-i]
    if sumL1 == 0:
        countL1 += 1
    if sumL2 == 0:
        countL2 += 1

    # 빙고가 나타나면 멈추기
    if countC + countR + countL1 + countL2 >= 3:
        result = x
        break

print(result)