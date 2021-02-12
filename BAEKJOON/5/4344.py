# 평균은 넘겠지

T = int(input())
for tc in range(T):
    scores = list(map(int, input().split()))

    sums = 0
    for i in range(1, scores[0]+1):
        sums += scores[i]

    avg = sums / scores[0]

    u_avg = 0
    for j in range(1, scores[0]+1):
        if scores[j] > avg:
            u_avg += 1

    result = round((u_avg / scores[0]) * 100, 3)
    
    # 주의! 소수점 아래 '0'도 출력하기! 
    print('{:.3f}%'.format(result, 3))