def chk(j, X):
    # triplet 확인
    if X[j] == 3:
        return 't'
    # run 확인
    if j < 8 and X[j] and X[j+1] and X[j+2]:
        return 'r1'
    if 0 < j < 9 and X[j-1] and X[j] and X[j+1]:
        return 'r2'
    if 1 < j and X[j-2] and X[j-1] and X[j]:
        return 'r3'

T = int(input())
for TC in range(1, T+1):
    Card = list(map(int, input().split()))
    # 카드 카운트
    A = [0] * 10
    B = [0] * 10
    # 결과 초기화
    result = 0
    # 하나씩 번갈아가며 카드 나누어주기
    for i in range(12):
        if i % 2 == 0:
            A[Card[i]] += 1
        else:
            B[Card[i]] += 1
        # triplet과 run 확인
        # 둘 중 한 명이라도 나오면 게임 끝
        if chk(Card[i], A):
            result = 1
            break
        if chk(Card[i], B):
            result = 2
            break
    print("#{} {}".format(TC, result))