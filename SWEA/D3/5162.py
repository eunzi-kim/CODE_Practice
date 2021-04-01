# 두가지 빵의 딜레마

T = int(input())
for TC in range(1, T+1):
    A, B, C = map(int, input().split())
    if A <= B:
        select = A
    else:
        select = B
    count = 0
    while C >= select:
        C -= select
        count += 1
    print("#{} {}".format(TC, count))