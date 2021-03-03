# 소득 불균형

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Money = list(map(int, input().split()))
    # 평균 구하기
    sum = 0
    for x in Money:
        sum += x
    avg = sum / N
    # 평균 이하의 소득 카운트
    count = 0
    for x in Money:
        if x <= avg:
            count += 1
    print("#{} {}".format(TC, count))