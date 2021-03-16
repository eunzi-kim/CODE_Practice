# 건초더미

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 건초더미 리스트 초기화
    Hay = [0] * N
    Sum = 0
    for n in range(N):
        x = int(input())
        Hay[n] = x
        Sum += x
    # 건초더미 원래 높이 구하기
    org = Sum // N
    # 건초더미 원상 복구
    count = 0
    for h in Hay:
        # 원래 건초더미보다 낮은 건초더미에게
        # 건초더미 올려주기
        if h < org:
            count += org - h
    print("#{} {}".format(TC, count))