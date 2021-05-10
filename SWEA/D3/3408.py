# 세가지 합 구하기

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    # 양의 정수 중에서 작은 순서대로 N개의 합
    S1 = ((N+1)*N) // 2
    # 양의 정수 중 홀수인 것들 중에서 작은 순서대로 N개의 합
    S2 = N ** 2
    # 양의 정수 중 짝수인 것들 중에서 작은 순서대로 N개의 합
    S3 = (N+1)*N
    print("#{} {} {} {}".format(TC, S1, S2, S3))